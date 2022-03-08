1. 정보보안과 네트워크 보안
    - 정보보안의 3요소와 추가요소
        - 기밀성(Confidentiality)
            - 대표적 공격 : 스니핑
            - 일반적 방어 : 암호화
        - 무결성(Integrity)
            - 대표적 공격 : MITM, 악성코드
            - 일반적 방어 : 암호화
        - 가용성(Availability)
            - 대표적 공격 : DoS
        - 서버 인증(Server Authentication)
            - 클라이언트가 올바른 서버로 접속하는가?
            - 대표적 공격 : DNS 스푸핑, 서버파밍
            - 일반적 방어 : SSL, 사용자에게 경고 후 선택
        - 클라이언트 인증(Client Authentication)
            - 올바른 클라이언트가 접속을 시도하는가?
            - 대표적 공격 : 스푸핑, 세션 하이재킹, 피싱 등
            - 대표적 방어 : 아이디/패스워드
2. 정보보호란?
    - 정보보호의 특성
        - 100%는 없다
        - 사용자 편의성을 제한한다.
        - 가시적인 이익을 얻을 수 없다.
        - 다단계의 복합 대책 구현 시 위험이 크게 감소한다.
            - 방화벽이나 암호화 적용 등과 같은 특정 솔루션에 의존하기 보다는 포괄적으로 커버될 수 있는 정책 마련 필요
    - 정보보호 필요성
        - 새로운 기술은 항상 등장한다.
        - 취약성은 계속 생겨날 것.
    - 공격
        - 악성코드
        - DDoS
        - Homepage Defacement
        - Phishing
            - 보이스피싱, 메신저피싱, 스미싱
        - Ransomware
        - APT
        - 스피어피싱 : 특정인을 겨냥하여 악성코드 유포 -> 파일 실행 시 정보유출
        - 파밍 : 불특정 다수를 대상으로 악성코드 유포 -> 금융정보 갈취

3. 프로토콜
    - 프로토콜의 요소
        - 구문(syntax) : 데이터 구조와 포맷
        - 의미(semantics) : 데이터 각 부분이 어떤 의미를 가지는지.(오류제어, 동기제어, 흐름제어 포함)
        - 순서(timing) : 어떤 데이터를 얼마나 빠르게 보낼건지
    - 프로토콜의 기능
        - 캡슐화(encapsulation)
            - 데이터에 제어 정보를 덧붙이는 것
        - 연결제어(connection control)
            - 연결 설정, 데이터 전송, 연결 해제에 대한 통제 수행
        - 흐름제어(flow control)
            - 데이터 양이나 속도를 조절하는 기능
        - 오류제어(error control)
            - SDU : Service Data Unit : 페이로드(실제 데이터가 담긴 부분)
            - PCI : Protocol Control Unit : 헤더
            - SDU나 PCI가 잘못되었을 경우 이를 발견하는 기법
            - 순서 검사 및 timeout 발생 시 재전송 요구
        - 동기화(synchronization)
            - 타이머나 윈도우 크기 등을 통해 동시에 정의된 인자값을 공유.
        - 다중화(multiplexing)
            - 통신 선로 하나에서 여러 시스템을 동시에 통신할 수 있는 기법
        - 전송 서비스
            - 우선순위 결정, 서비스 등급과 보안 요구 등을 제어하는 서비스
        - 주소설정(addressing)
            - 두 개체가 통신을 하는 경우 필요
        - 순서제어(sequence control)
            - 프로토콜 데이터 단위를 전송할 때 순서를 명시.
            - 연결지향형(connection-oriented)에만 사용
        - 단편화 및 재조합(fragmentation & reassembly)
            -  대용량 파일은 전송 효율이 높은 작은 단위로 나누어 전송한 뒤 재조합을 함.

4. 네트워크 계층 구조
    - osi 7 layer
        - ![image](https://user-images.githubusercontent.com/44149738/133914913-e6dd8de9-ce5d-4740-a3a0-8cb6acef58ce.png)
        - `물 데 네 전 세 표 응`
        - 물리계층(1계층)
            - 전기적, 무리적 세부 사항을 정의
            - ex) 허브, 리피터
        - 데이터링크 계층(2계층)
            - P2P 사이의 신뢰성있는 전송을 보장하기 위한 계층
            - CRC 기반 오류제어와 흐름제어가 필요
            - ex) 이더넷
        - 네트워크 계층(3계층)
            - 여러 노드를 거칠 때 마다 경로를 찾아주는 역할
            - 라우팅, 흐름제어, 단편화(segmentation/desegmentation), 오류제어 등을 수행
            - ex) L3 스위치
        - 전송계층(4계층)
            - 양 끝단 사용자들이 신뢰성 있는 데이터를 주고받을 수 있게 하여 상위 계층이 데이터 전달의 유효성이나 효율성을 고려하지 않아도 되게 해줌.
            - 전송계층 프로토콜 중 하나인 TCP는 연결지향(connection-oriented) 프로토콜
        - 세션게층(5계층)
            - 양 끝단 응용 프로세스가 통신을 관리하기 위한 방법 제공
            - 동시 송수진 방식(duplex), 반이중 방식(half-duplex), 전이중 방식(full-duplex) 통신과 함께 체크 포인팅과 유휴, 종료, 재시작 과정 등을 수행
            - TCP/IP 세션을 만들고 없애는 책임을 짐.
        - 표현계층(6계층)
            - 시스템에서 사용되는 코드 간 번역을 담당
            - 데이터 압축과 암호화 기능 수행
        - 응용계층(7계층)
            - 사용자나 응용 프로그램 사이에 데이터 교환을 가능하게 하는 계층
            - ex) http, ftp, ssh, telnet 등
    - TCP/IP 4계층
        - ![image](https://user-images.githubusercontent.com/44149738/133914943-ccc73f1a-66e1-418d-a2a5-b7c38870cf02.png)

5. 물리계층
    - 1계층 물리계층 Physical layer
    - 시스템 간 연결선 (흔히 LAN을 뜻함)
    - 전화선은 CAT 1 사용하고, 랜 케이블은 요즘 보통 CAT 5,6 정도를 사용
    - ![image](https://user-images.githubusercontent.com/44149738/133914993-7fba2461-4a7d-426d-b7da-7e690d12a09b.png)
    - 일반적인 랜 케이블은 UTP 사용
        - UTP, FTP, STP 등이 있는데 가성비가 제일 좋은 UTP를 주로 사용
    - 커넥터
        - ![image](https://user-images.githubusercontent.com/44149738/133915069-dc500216-7780-42e7-9336-c316cb378981.png)
        - 랜 케이블은 UTP 케이블 중 CAT 5, 6에 해당하는 `10/100/1000 BASE-T(IEEE 802.3)` 선과 `RJ-45` 커넥터를 많이 씀.
        - RJ-11 은 전화선에서 많이 씀.
    - 리피터
        - 네트워크를 연장하기 위한 장비
        - 신호 증폭.
        - 최근에는 모든 네트워크 장비에 리피터가 공통으로 들어감.
    - 허브
        - 요즘 쓰이는 스위치의 예전 형태
        - 스위치랑 다른점은 패킷을 모든 곳에 똑같이 복사해서 보낸다는 것이 다름.(스위치는 목적지에만 전송)

6. 데이터링크 계층
    - 2계층 데이터링크 계층 Data Link Layer
    - 하드웨어 주소(MAC 주소)만으로 통신하는 계층
    - `ipconfig /all` 명령으로 확인 가능
    - MAC 주소
        - 12개의 16진수로 구성
        - 앞 6개는 벤더사(OUI)를 뜻하고, 뒤쪽은 호스트 식별자이다.
        - 같은 MAC 주소는 존재하지 않음.
    - 프로토콜
        - X.25 : 1980부터 규격화된 프로토콜
        - 프레임 릴레이 : X.25보다 10배 고속 전송 가능
        - ATM(Asynchronous Transfer Mode) : 실시간 영상 전송과 같은 고속 전송
        - 이더넷
            - 64 ~ 1518KBytes 의 패킷 길이를 가지고 있음. 
    - 브리지
        - 랜과 랜을 연결하는 초기 네트워크 장치
        - 데이터 프레임을 복사하는 역할
    - 스위치
        - 예전에 쓰이던 더미 허브는 연결된 시스템이 늘어날 수록 패킷 충돌이 발생하는 문제가 있었음
        - 이러한 더미 허브의 문제점을 해결하는 획기적인 방안으로 L2 스위치를 사용
    - 스위칭 방식
        - 패킷 전송 방식에 따른 구분
            - 컷스루(cut through) 방식
                - 목적지 주소의 포트로 프레임을 즉시 전송하여 지연시간 최소화
            - 저장 후 전송(store & forward)
                - 전체 프레임을 수신해서 버퍼에 보관 후 오류를 확인하여 전송
                - 패킷 길이에 비례해 전송 지연지 발생하지만 브리지나 라우터보다 신속
                - 속도가 서로 다른 포트를 연결할 경우에 반드시 사용해야함.
                - 최근에는 비용 감소의 효과를 위해 컷스루와 동시에 지원하는게 일반적임
            - 인텔리전트
                - 보통 컷스루로 작동하다가 오류가 발생하면 저장 후 전송 모드로 자동 전환하여 오류 프레임 전송을 중지.
                - 오류율이 0가 되면 다시 컷스루로 전환
        - 제공하는 경로의 대역폭에 따른 구분
            - 반이중
                - 양방향이지만 한번에 하나(수신/송신)만 가능
            - 전이중
                - 송/수신 포트를 분리해서 성능이 두배로 뛰어남
                - 충돌이 없어서 거리 제한을 늘릴 수 있음
                - 기술적으로 스위치에서만 전이중 방식을 지원할 수 있음.
    - 스위치 테이블
        - 각 포트에 연결된 MAC 주소 데이터

7. 네트워크 계층
    - LAN을 벗어난 통신을 위해 IP 주소를 사용
    - ARP(Address Resolution Protocol)
        - 데이터를 전달하려는 IP 주소와 통신에 필요한 물리적인 주소(MAC)을 알아내는 프로토콜
        - 선택된 매체에 브로드캐스트를 통해 특정 IP 주소를 사용하는 호스트가 응답하도록 요구하는 방식을 사용
    - RARP(Reverse ARP)
        - 호스트가 IP 주소를 서버로부터 확인하는 프로토콜
    - IP
        - 가장 대표적인 네트워크 계층 프로토콜
        - 노드 간 데이터 전송 경로를 확립해주는 역할.(단말 장치 간 패킷 전송 서비스)
        - IP는 32자리 2진수로 8자리마다 점을 찍어 구분 
        - ![image](https://user-images.githubusercontent.com/44149738/133917510-568835b0-34a3-4606-81a6-1d99a34a558f.png)
    - ICMP(Internet Control Message Protocol)
        - 메시지를 제어하고 오류를 알려주는 프로토콜
        - ping 이 대표적인 툴
        - ICMP echo request/reply 메세지
            - 송신측의 패킷이 목적지에 도착했는지를 확인하는데 사용
        - ICMP destination unreachable 메세지
            - 도달하지 못했을 때으 메세지
        - ICMP redirect
            - 라우터가 송신측 노드에 적합하지 않은 경로로 설정되어 있을 경우 최적화된 경로를 다시 지정해주는 메세지
        - ICMP time exceeded 메세지
            - TTL이 0이 되면 보내는 메세지
        - ICMP source quench 메세지
            - WAN 쪽에 집중이 발생해서 송신 불능 상태가 되면 보내는 메세지
            - 송신측은 이 메세지를 통해 패킷의 양을 제어
    - IGMP(Internet Group Management Protocol)
        - 멀티캐스트에 관여하는 프로토콜로 멀티캐스트 그룹을 관리하는 역할
        - 유니캐스트(unicast)
            - 한 호스트에서 다른 호스트로 전송
        - 브로드캐스트(broadcast)
            - 호스트에서 네트워크에 있는 전체 호스트로 전송
        - 멀티캐스트(multicast)
            - 유니-브로드 중간형태
            - 멀티캐스트 그룹에 속한 모든 호스트에 전달
    - 라우터
        - 게이트웨이라고도 함.
        - "논리적"으로 분리된 둘 이상의 네트워크를 연결.
        - 도착지까지 패킷의 최적 경로를 찾기 위한 라우팅 테이블 구성
        - `route PRINT` 명령으로 라우팅 테이블 확인
        - `tracert` 명령으로 icmp 패킷 보내서 네트워크 경로를 확인
    - 라우팅
        - 정적 라우팅
            - 보안이 중요한 경우 선호
            - 초기에 관리자가 라우팅 정보를 분석한 최적의 경로를 설정 가능
            - 정해진대로 최적 경로로 가기 때문에 처리 부하 감소
            - 그러나 네트워크 환경 변화에 대한 능동적 대처가 어려움.
            - 네트워크가 쉽게 변하지 않고, 보안성이 중요한 스카다 시스템 같은 곳에서 사용하기 적합함.
        - 동적 라우팅
            - 라우터가 네트워크 연결상태 스스로 파악해서 최적 경로 선택해 전송
            - 네트워크 연결 형태가 변경되어도 자동으로 문제 해결
            - 네트워크 환경 변화에 따라 능동적 대처가 가능하고, 관리가 쉬움.
            - 그러나 라우팅 정보 송수신으로 인한 대역폭 낭비
            - 네트워크 환경 변화 시 라우터의 처리 부하 증가로 지연 발생
            - 네트워크가 수시로 변하는 환경에 적합
        - 정적/동적 비교
            - ![image](https://user-images.githubusercontent.com/44149738/133918096-4241c93e-1903-4d78-b3be-060daad9a86a.png)

8. 전송계층
    - 대표적으로 TCP가 있음
    - TCP가 가진 주소를 포트(port)라고 하며, 0~65535번까지 존재
    - 0 ~ 1023 : well known port
    - TCP
        - 연결 지향형 프로토콜
        - IP와 함께 통신을 하는데 반드시 필요한 가장 기본적인 프로토콜
        - TCP 특징
            - 높은 신뢰성
            - 가상 회선 연결 방식(규모적인 부분에서 이점)
            - 연결의 설정과 해제
            - 데이터 체크섬
            - 시간 초과와 재전송
            - 데이터 흐름 제어
        - TCP 패킷 구조
            - ![image](https://user-images.githubusercontent.com/44149738/133951443-e7e9c730-c00b-41ac-9662-08e6611cc7d9.png)

        - 연결 설정 과정(three-way handshaking)
            - tcp가 연결 전에 가상 경로를 설정
            1. C ----- SYN -----> S
            2. C <-- SYN + ACK -- S
            3. C ----- ACK -----> S
        
        - 연결 해제 과정
            1. C ---- FIN ---> S
            2. C <--- ACK ---- S
            3. C <--- FIN ---- S
            4. C ---- ACK ---> S
    
    - UDP
        - 비연결 지향형 프로토콜
        - 응답 확인과정이 없어서 네트워크 부하를 주지 않음
        - 그러나 확인 과정이 없어서 신뢰성도 없음.(무결성 보장 못함)
        - UDP 특징
            - 비연결 지향형
            - 네트워크 부하 감소
            - 비신뢰성
            - 전송된 데이터의 일부가 손실됨
        - UDP 패킷 구조
            - ![image](https://user-images.githubusercontent.com/44149738/133952433-6c91aaff-eed7-4a0c-81e1-ea09f83b7d2a.png)

9. 응용계층
    - 관련 응용 프로그램이 별도 존재하며, 여러가지 프로토콜에 대하여 사용자 인터페이스를 제공
    - 프로토콜
        - FTP(file transfer protocol, 20, 21)
            - 파일 전송을 위한 가장 기본적 프로토콜
            - C와 S가 대화형으로 통신 가능
        - Telnet(23)
            - 원격에 로그인하도록 tcp 연결을 설정.
        - SMTP(simple mail transfer protocol, 25)
            - 메일 서비스
        - DNS(domain name system, 53)
            - 도메인 이름 주소를 통해 IP 주소를 확인할 수 있는 프로토콜
        - TFTP(trivial file transfer protocol, 69)
            - 파일을 전송하는 프로토콜
            - UDP 패킷을 사용하고, 인증 기능을 제공하지 않음
            - 임베디드 시스템에서 주로 사용
        - HTTP(hypertext transfer protocol, 80)
            - 인터넷을 위해 사용하는 기본적인 프로토콜
        - POP3 & IMAP
            - POP3(110) : 메일 서버로 전송된 메일을 "확인"할 때 사용
            - IMAP(143) : POP3와 기본적으로 같으나, 메일이 서버에 남음
        - RPC(remote procedure call, 111)
            - sun의 remote procedure call을 나타냄
        - NetBIOS(network basic input/output system, 138)
            - 기본적인 사무기기와 window 시스템 간 파일 공유를 위한 것
            - NBT(NetBIOS over tcp) 프로토콜을 사용해 원격의 인터넷으로 전달 가능
        - SNMP(simple network management protocol, 161)
            - 네트워크 관리와 모니터링을 위한 프로토콜

10. whois
    - 도메인 확인, 도메인과 관련된 사람 및 인터넷 자원을 찾아보기 위한 프로토콜
    - 처음에는 와일드카드 검색이 가능했으나, 인터넷 상업화와 스팸메일 증가로 해당 기능 삭제
    - 얻을 수 있는 정보
        - 도메인 등록 및 관련 기관 정보
        - 도메인 이름과 관련된 인터넷 자원 정보
        - 등록자, 관리자, 기술관리자의 이름, 연락처, 이메일
        - 레코드의 생성시기와 갱신 시기
        - 주 DNS 서버와 보조 DNS 서버
        - IP 주소의 할당 지역 위치
    - 서버 목록
        - 전체 : whois.internic.net
        - 아시아 : www.arin.net, www.apnic.net
        - 한국 : whois.krnic.net 
        - 해커 애용 : whois.greektoos.com
        - 검색서비스
            - https://후이즈검색.한국/kor/whois/whois.jsp

11. Hosts
    - DNS가 존재하기 전에 사용. 지금도 목적에 따라 많이 사용.
    - 경로
        - 윈도우 : {시스템 경로}/system32/drivers/etc/hosts
        - 리눅스 : /etc/hosts
    - 파일 구조
        - 보통 hosts 파일은 비어있음
        - DNS 서버가 작동하지 않을 때, 별도의 네트워크를 구성하여 임의로 사용할 때, 다른 IP 주소를 가진 여러 대의 서버가 같은 도메인으로 클러스터링되어 운영되는 상태에서 특정 서버에 접속하고자 할 때 유용
    - 윈도우10에서는 디펜더가 변조를 방지함.

12. DNS
    - IP를 도메인 이름으로 상호 매칭시켜주는 시스템
    - DNS 계층구조
        - ![image](https://user-images.githubusercontent.com/44149738/134617063-7a6095db-a5c6-4f6d-9765-08c8393f2164.png)
        - 가장 상위 개체는 root(.)
        - FQDN(Fully Qualified Domain Name) : 완성된 주소
            - ex) www.g0pher.kr
    - OS별 DNS 등록 및 확인
        - 리눅스
            - /etc/resolv.conf
            - - `ifconfig`
        - 윈도우
            - 인터넷 프로토콜 등록 정보에서 추가
            - `ipconfig /all` 으로 확인
    - `ipconfig /displaydns` : 캐싱된 dns 확인
    - `ipconfig /flushdns` : 캐시 flush
    - DNS 서버의 구분
        - 주 DNS : 중심 서버
        - 부 DNS : 백업 서버
        - 캐시 DNS : 임시 DNS 서버
    - DNS 레코드의 종류
        - ![image](https://user-images.githubusercontent.com/44149738/134632265-9b3acd33-ee0e-46d2-a8e3-ed5e23ed1122.png)
        - ns : 네임서버
        - mx : 메일서버
        - soa : 도메인에 권한있는 서버
        - all : 모두


13. IP 추적
    - 메일 서비스
        - 메일에서 원본보기 기능을 이용하면 메일을 raw 하게 확인할 수 있음.
        - 수많은 헤더 중에 Received를 확인하면 수신자의 IP를 확인할 수 있다.
        - Received-SPF : 주요 메일 서버와 IP를 등록해두고, 메일이 전소오딘 서버의 IP와 메일 주소를 확인하여 스팸 메일 여부를 검사한 결과를 표시
            - ![image](https://user-images.githubusercontent.com/44149738/135768118-a0898912-97f6-498a-82b8-b15edd2dea02.png)
        - G suite 도구상자 messageheader 기능을 이용하면 메일 원본을 해석해준다.
    - P2P 서비스
        - 중간에 서버가 끼는 경우 영장과 같은 방법으로 확인할 수 있음
        - 대용량 같은 경우 서버에서 IP만 제공받고, 직접 통신
            - 여기서 IP가 드러나서 위험할 수 있음
    - 웹 서비스
        - 웹 접근에 대한 로그가 남음.
            - `IIS 관리자` - `로깅` 에서 관련 설정 확인할 수 있음.
            - 저장되는 기본 폴더는 `\inetpub\logs\LogFiles` 에 있음.
    - traceroute
        - TTL을 설정해서 경로 탐색
        - 윈도우에서는 tracert를 사용 
        - Open Visual Traceroute 라는 프로그램이 있음. trace route 과정을 비주얼하게 볼 수 있음.
        - 오래되긴 했지만 sam spade 툴로 여러 ip 관련 분석을 진행해볼 수 있음. 


14. 풋프린팅(footprinting)
    - 발자국을 살펴보는 일
    - 공격 대상의 정보를 모으는 방법 중 하나
    - 사회 공학 기업(social engineering)
        - 약한패스워드, 패스워드를 적어놓거나 공개된 곳에 공유하는 등의 원초적인 취약점
    - 해킹에 필요한 정보
        - 침투하고자 하는 계정
            - id, pw, 이메일 등
        - 게시판 이용
        - 협력사나 계열사 보안조치 확인
        - 직접 접속하는 것 보다 유틸리티로 웹 사이트를 다운로드한 뒤 검색하는 것이 좋음.

15. 스캔
    - 서버 및 서비스가 살아있는지 확인하는 과정
    - 전통적으로 ping과 같은 방법으로 ICMP 스캔이 있음
        - ICMP를 통해 활성화 여부를 확인하는 방법
            - ![image](https://user-images.githubusercontent.com/44149738/136903696-39012dea-3f9c-4c5f-a464-ff06bff9ba17.png)
        - Echo Request가 막혔을 때 이용할 수 있는 방법
            1. timestamp request 패킷 이용.
            2. information request 패킷 이용.
            3. address mask request와 reply 패킷 이용
            - ![image](https://user-images.githubusercontent.com/44149738/136904368-8d08d0b3-131e-4f8f-b778-b74bfd37173d.png)
    - 공격에 사용되는 스캔들
        - TCP
            - TCP Open 스캔
                - tcp를 이용한 가장 기본적인 스캔
                - ![image](https://user-images.githubusercontent.com/44149738/136904503-0e684bce-afaf-459e-a719-d0eca2585a0a.png)
                - 3way handshake 여부를 이용. SYN 전송시 `RST + ACK`가 오거나 안오면 죽은것.
                - reverse ident : 서버의 데몬을 실행하고 있는 프로세스의 소유권자를 확인하기 위한 것
                    - 보통 113번 포트를 사용자 인증에 사용하는데, 보통 중지되어있음.
            - 스텔스(Stealth) 스캔
                - 로그를 남기지 않고, 자신의 위치를 숨기는 스캔 모두를 통칭
                - ![image](https://user-images.githubusercontent.com/44149738/136905284-24373408-77e3-4e8b-acbe-244b5735c371.png)
                - 살아있을 때 rst를 보내버려서 연결이 맺어지지 않아서 기록이 남지 않음.
                - 대표적으로 TCP Half Open 스캔이 있음
                - FIN(Fisish 스캔)
                    - 포트가 열린 경우 응답이 없고, 닫힌 경우 rst 패킷이 돌아옴
                - NULL 스캔
                    - 플래그 값을 설정하지 않고 보낸 패킷
                - XMAS 스캔
                    - ACK, FIN, RST, SYN, URG 플래그 모두를 설정하여 보낸 패킷
                - ![image](https://user-images.githubusercontent.com/44149738/136905598-a3a0e946-77d7-4057-ae94-99ed85a87c01.png)
            - ACK 패킷을 이용한 스캔
                - RST 패킷을 받아 분석
                - 열린 경우 : TTL 64 이하인 RST 패킷, 윈도우가 0이 아닌 임의 값을 가진 RST 패킷
                - 닫힌 경우 : TTL값이 일정하게 큼, 윈도우 크기가 0인 RST 패킷
            - TCP 패킷을 이용한 스캔
                - 모든 시스템에 동일하게 적용되지는 않고, 많이 알려져서 거의 적용되지 않음.
                - SYN 패킷을 이용한 스캔 방법은 세션을 성립하기 위한 정당한 패킷과 구별할 수 없어서 아직도 유효하며, 아주 효과적임
            - TCP 단편화
                - 크기가 20바이트인 TCP 헤더를 패킷 두 개로 나누어서 보냄
                    - 첫 번째 패킷은 출발지와 도착지 IP주소
                    - 두 번째 패킷은 스캔하려는 포트 번호
                - 첫 번째 패킷은 포트정보가 없어서 방화벽을 통과하고, 두 번째 패킷은 IP주소가 없어 방화벽을 지날 수 있음
            - 시간차를 이용한 스캔
                - 짧은시간동안 많은 패킷을 보내는 방법
                    - 방화벽과 IDS 처리 용량의 한계를 넘김
                - 아주 긴 시간동안 패킷을 보내는 방법
                    - 더미 패킷을 던짐
                - 시간차에 의한 공격의 구분
                    - ![image](https://user-images.githubusercontent.com/44149738/136906955-b75e5b31-a02e-4b50-891b-e107d545b54f.png)
            - FTP 바운스 스캔
                - 취약한 FTP 서버에서 PORT 명령을 사용하여 다른 시스템의 포트 활성화 여부를 확인.
                - 대부분 통제하기 때문에 큰 의미는 없으나, 알아두면 좋음
        - UDP 스캔
            - 포트가 닫힌경우에만 ICMP Unreachable 패킷이 옴.
            - 신뢰성이 떨어짐. 파급력있지는 않음.
    - 실습
        - fping
            - `-q` : icmp req와 reply를 숨김
            - `-a` : 활성화되어있는 시스템을 보여줌.
            - `-s` : 스캔이 끝난 후 결과를 정리해서 보여줌.
        - nmap
            - 강력한 스캐닝 툴임
            - `-sT` : TCP Open 스캔
            - `-sS` : SYN 스텔스 스캔
            - `-sF` : 특정 포트 스캔. `-p` 옵션이랑 함께 사용.
            - `-f -sS` : 방화벽을 통과하기 위해 패킷을 쪼갬.
            - 기타
                - ![image](https://user-images.githubusercontent.com/44149738/136911305-b5d059ea-1ed5-4e7e-9317-498cab154909.png)

16. 운영체제 탐지
    - 배너 그래빙(banner grabbing)
        - 원격지 시스템에 로그인을 하면 뜨는 안내문과 비슷한 배너를 확인하는 기술
    - TCP/IP 반응 살펴보기
        - FIN 스캔 이용
            - 윈도우, BSD, CISCO, IRIS 등이 해당
            - 세션 연결 시 TCP 패킷의 시퀀스 넘버 생성 관찰
                - 윈도우 : 시간에 따른 시퀀스 넘버 생성
                - 리눅스 : 완전한 랜덤
                - FreeBSD, Digital-Unix, IRIX, 솔라리스 : 시간에 따른 랜덤한 증분
    - netcraft 이용하기
        - https://sitereport.netcraft.com/?url=http://www.naver.com


17. 방화벽
    - 1차 방어선
    - 접속 허용/차단 결정
    - IDS : 방화벽이 막을 수 없거나, 차단에 실패한 공격을 탐지하여 관리자에게 알려주는 역할
    - firewalk(파이어워크)
        - 방화벽의 ACL을 알아내는 방법
        - 방화벽까지의 TTL보다 1만큼 큰 TTL을 생성해서 전송
        - 패킷 차단 시, 아무 패킷도 돌아오지 않음
        - 패킷을 그대로 보낼 시, 다음 라우터에서 traceroute 처럼 ICMP Time Exceeded 메세지(type11)를 보냄

18. SNMP(Simple Network Management Protocol)
    - 중앙 집중적인 관리 툴의 표준 프로토콜
    - ICMP 만으로 네트워크를 관리하기에는 너무 복잡해졌기 때문에 UDP를 이용한 관리방법 등장
    - 관리 시스템과 관리대상(AGENT)로 나뉨.
    - Agent의 구성
        - SNMP(simple network management protocol) : 전송 프로토콜
        - MIB(management information base) : 관리할 개체의 집합
        - SMI(structure fo management information) : 관리 방법
    - 관리시스템과 agent 통신의 최소 일치 사항
        - 버전, 커뮤니티, pdu 타입
    - 관리시스템과 agent 통신
        - ![image](https://user-images.githubusercontent.com/44149738/136928278-ac5c115e-d2b5-4ed2-a294-022eaa16e687.png)
        - get request: 관리시스템이 특정 변수 값을 읽음.
        - get next request: 관리 시스템이 이미 요청한 변수 다음 변수 값을 요청
        - set request: 관리 시스템이 특정 변수 값의 변경을 요청
        - get response: 에이전트가 관리 시스템에 해당 변수값을 전송
        - trap: 에이전트의 특정 상황을 관리 시스템에 알림.
    - MIB
        - 관리자가 조회하거나 설정할 수 있는 개체들의 데이터베이스
        - 개체별로 트리 형식 구조를 이룸 (RFC 1213)
        - 네트워크 관리자는 MIB의 특정 값을 가져와서 agent의 상태를 보고 관리함.
    - SMI
        - 표준에 적합한 MIB를 생성하고 관리하는 기준(관리 정보 기준)
    - OID
        - MIB를 생성하려면 OID를 지정받아야 함. (IP 주소와 유사한 표기법 사용)
        - 각 제조업체나 기관은 특정 번호를 할당받고 이 번호를 생산한 장비에 부여
        - OID 구조
            - ![image](https://user-images.githubusercontent.com/44149738/136928936-a5c5a366-49c7-48f6-baa9-76dce74c97c7.png)
    - SNMP의 취약점
        - 기본적으로 누구라도 SNMP의 MIB 정보를 볼 수 있음
        - 패킷이 UDP로 전송되어 연결의 신뢰도가 낮음
        - 데이터가 암호화되지 않은 평문으로 전송되어 스니핑 가능.
    - 실습
        ```bash
        sudo apt install snmp # install client snmp
        sudo nmap -sU -p 161 <server-ip> # check server snmp service is opened
        sudo nmap -sU -p 161 --script=snmp-brute 192.168.171.129 # snmp community string crack : "public"
        snmpwalk -v 1 -c public 192.168.171.129 1.3.6.1.2.1.1 # view system info by OID
        ```
    - 보안 대책
        - SNMP가 불필요하다면 SNMP 사용을 막음
        - 커뮤니티를 패스워드처럼 복잡하게 설정하여 쉽게 노출되지 않도록 관리
        - 패킷을 주고받을 호스트를 설정하여 SNMP를 사용할 시스템의 IP를 등록
    
19. 스니핑(sniffing)
    - 전형적인 공격 수단.
    - 행위 자체는 매우 불공평하고 비도덕적이나, 효과는 공격의 효과도는 상당히 크다
    - 네트워크 패킷을 유심히 관찰. 모니터링하고자 하는 타겟이 명확할 때 필터링을 통해 집중적으로 관찰. 특정 타겟의 ID와 PW와 같은 개인정보를 탈취하는것이 목적
    - 수동적(passive)인 공격 : 공격 시 어떠한 적극적인 행위를 하지 않아도 충분함.
    - 개념
        - 전화선이나 UTP에 탭핑(tapping)해서 전기 신호를 분석하여 정보를 찾아냄
        - 전기신호(emanation)을 템페스트(tempest) 장비를 이용해 분석하는 일
        - 위 두개는 사실상 실현가능성이 좀 낮음. 이 개념이 네트워크에 올라왔다고 보면 됨.
    - 모드
        - 프러미스큐어스 모드(promiscuous mode)
            - mac, ip와 상관없이 모든 패킷을 스니퍼에게 넘겨주는 모드.
            - 리눅스 유닉스는 랜카드에 대해 모드 설정이 가능
            - 윈도우에서는 스니핑을 위한 드라이버를 따로 설치해야함
            - 스니핑을 하려면 좋은 랜 카드가 필요
        - 바이패스 모드(bypass mode)
            - 패킷 분석까지 HW로 구현되어있는 랜카드
            - 기가바이트 단위의 백본 망에서 스니핑을 하기 위한 장비로, 고가임.
    - 프러미스큐어스 모드 설정하기
        - ifconfig
        - sudo ifconfig ens33 promisc
        - 바꾸고 나면 ifconfig 내용이 다음과 같이 바뀜
            - before : `ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>`
            - after : `ens33: flags=4419<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>`
    - 툴
        - tcp dump
            - 리눅스에서 기본이 되는, 하지만 강력한 스니핑 툴
            - 네트워크 관리를 위해 개발되었기 때문에 관리자 느낌이 강함.
            - TCP dump로 획득한 증거 자료는 법적 효력이 있음.
                - 포렌식 관점에서 tcp dump의 신뢰성이 높다는 뜻.
            - 설치 : `sudo apt install tcpdump`
            - 실행 : `sudo tcpdump -i ens33 -xX host 192.168.0.2`
        - fragrouter(프래그라우터)
            - 스니핑 보조 툴.
            - 받은 패킷을 전달하는 역할
            - 세션을 가로채는 경우 패킷을 정상적으로 전달해야 은닉할 수 있음. 패킷 릴레이가 반드시 필요함.
            - 설치 : `sudo apt install fragrouter`
        - DSniff(디스니프)
            - 스니핑을 위한 다양한 툴이 패키지처럼 만들어진 것
            - 한국계 미국인 미국 미시건 대학교의 송덕준 교수가 개발
            - 알트보어(altvore)와 함께 대표적인 스니핑 툴
                - 알트보어 : FBI에 맞서기 위해 해커가 만듬
            - 암호화된 계정과 패스워드까지 읽을 수 있음.
            - 내포된 툴
                - ![image](https://user-images.githubusercontent.com/44149738/137814624-952ff4bd-2994-44ec-9cdc-36a67775d286.png)
            - 설치 : `sudo apt install dsniff`
        - urlsnarf
            - 웹 세션 스니핑
            - kali에 기본적으로 깔려있음
            - 웹로그처럼 생김
    - 스위칭 환경과 스니핑
        - 스위치는 각 장비의 MAC 주소를 확인하여 포트에 할당
        - 자신에게 향하지 않은 패킷 외에는 애초에 받을 수 없어 스니핑 방지가 됨.
            - 스니핑 방지를 위해 만들어진건 아닌데 하다보니 막아진 경우
        - ARP 리다이렉트
            - 공격자가 본인이 라우터라고 속이는 공격기법
            - 기본적으로 2계층 공격.
            - 라우터의 MAC주소로 위조된 ARP 패킷으로 속임
            - ARP 스푸핑은 HOST TO HOST 공격이고, ARP 리다이렉트는 ALL HOST TO ROUTER 구조임.
            - 실습
                - sudo fragrouter -B1 # 패킷 릴레이
                - sudo arpspoof -i eth0 -t 192.168.171.128 192.168.171.2
                - 피해자의 pc에서 arp table이 바뀐 것을 볼 수 있음.
        - ICMP 리다이렉트
            - ARP 공격과 비슷하지만 정교한 공격이 가능
            - 라우터가 두개 이상으로, 로드벨런싱이 적용된 네트워크에서 사용
            - 라우터가 경로에 없어도 되는 경우 요청자에게 icmp 리다이렉트를 응답하여 다음부터 빠르게 경로를 찾아가도록 하는 기능이 있음.
            - 2계층이 아닌 3계층에서 운영됨.
            - 최근 운영체제에서는 기본적으로 ICMP 리다이렉트를 차단함.
        - 스위치 재밍(Switch jamming)
            - 스위치를 직접 공격
            - mac 테이블을 위한 캐시 공간에 버퍼 오버플로우 공격을 실시
                - 과부하걸려서 오작동함
            - 일부 고가 스위치는 mac 테이블 캐시와 연산장치 캐시가 독립적으로 나누어져 있어서 통하지 않음.
            - 실습
                - `macof` dsniff 설치 시 자동 설치됨.
        - SPAN(Switch Port Analyzer)
            - 포트 미러링을 이용한 것. 주로 IDS를 설치할 때 많이 사용.
                - 네트워크 속도적인 측면에서 피해를 주지 않기 위함.
            - 시스코에서 사용하는 용어이며, 다른 벤더엥서는 port roving 이라고 부르기도 함.
        - 태핑
            - 복사의 개념이라서 네트워크가 느려질 수 있음.
            - 허브와 같이 포트를 모니터링하기 위한 장비.
            - splitter 라고 부르기도 함.
    - 대응책
        - 능동적 대응책 - 스니퍼 탐지
            - ping을 이용한 탐지
                - 이상한 mac 주소로 위장해서 보냈는데 ICMP Echo Reply를 받으면 스니핑을 하고 있는 것
            - arp를 이용한 탐지
                - 위조된 arp request를 스니퍼임을 확인하고자 하는 시스템에 보냄
                - 대상 시스템이 응답으로 ARP Response 를 보내면 이를 통해 프러미스큐어스 모드로 동작중인 스니퍼임을 확인
            - dns를 이용한 탐지
                - 테스트 대상 네트워크로 ping sweep을 보내고 들어오는 inverse-dns lookup을 감시
            - 유인을 이용한 탐지
                - 가짜 계정과 패스워드를 뿌려 공격자가 이 정보로 접속을 시도하면 접속을 시도한 시스템을 탐지 
                - decoy 또는 honeypot이라고 불림.
                - high tech 임.
            - arp watch를 이용한 타밎
                - map 주소와 ip 매칭 데이터를 저장하고, arp 모니터링을 통해 변조 패킷이 발생되면 관리자에게 알림
        - 수동적인 대응책 - 암호화
            - ssl
                - 암호화된 웹 서핑을 가능하게 함
                - 40비트, 128비트 암호화키가 존재
            - PGP, PEM, S/MIME
                - 이메일 전송시 사용하는 암호화 방법
                - PGP: 내용 암호화. 기본적으로 web of trust 개념 사용
                - PEM : 공개키 암호화 표준 따름. CA에서 키 관리
                - S/MIME : MIME 형식에 암호화 서비스만을 추가한 것
            - SSH
            - VPN

20. arp 스푸핑
    - mac 주소를 속이는 것.
    - 2계층에서 작동하기 때문에 공격 대상이 같은 랜에 있어야 함.
    - 실습
        - 환경
            - kali / 192.168.171.133 / 00:0c:29:d4:2a:09
            - ubuntu desktop / 192.168.171.131 / 00:0c:29:68:29:3d
            - ubuntu server / 192.168.171.132 / 00:0c:29:6f:bf:81
        - 설치
            - `apt install fake` in kali
        - arp table 채우기
            - `fping -a -g 192.168.171.1/24`
            - 이후 `arp -a` 명령으로 네트워크 탐색
        - 스푸핑
            - `sudo fragrouter -B1` 명령으로 패킷 릴레이
            - `sudo tcpdump -xX` 명령으로 패킷 스니핑
            - `sudo send_arp 192.168.171.131 00:0c:29:d4:2a:09 192.168.171.131 00:0c:29:68:29:3d`
                - client에게 서버의 MAC 주소를 Kali의 MAC으로 속임
            - client에서 server로 telnet 접속을 하면 잘 된다.
            - 그러나 kali의 wireshark에는 telnet 정보가 뜸.
    - 보안 대책
        - `arp -s <IP> <MAC>` 형태로 STATIC 하게 ARP table을 관리
            - 스푸핑 공격이 들어와도 변하지 않음
            - 그러나 자산이 너무 많으면 관리가 어려움.
            - 자동화 해주는 솔루션들이 있음.
- trust(트러스트)
    - ip로만 접근 인가하는 방식.
    - 편리하지만 사용이 위험함.
    - 이제는 안씀.
    - SSE(Single Sign On) : 트러스트 약점이 알려지면서 개발됨.
        - 대표적인 예로는 커버로스(kerberos)를 사용하는 윈도우의 액티브 디렉토리, 썬 마이크로시스템즈의 NIS+ 등이 있음.
    - 설정과 역할
        - `./etc/hosts.equiv` : 시스템 전체에 영향을 미침
        - `.$HOME/rhost` : 사용자 한 사람에 귀속하는 파일

21. IP 스푸핑
    - trust 같은 환경에서 사용.
    - 그러나 trust 자체를 요즘은 잘 사용 안함.
    - 심지어 보안때문에 패스워드 검사는 함.
    - 또한, ssh 권고하기 때문에 쓸일도 없음
    - 상용화된 솔루션도 많음.
    - 보안대책
        - trust를 사용하지 않는 것
        - mac 주소를 static으로 지정

22. DNS 스푸핑
    - 웹 스푸핑과 비슷
    - ARP 스푸핑과 같은 선행작업이 필요
    - DNS 응답 쿼리가 도달하기 전에 먼저 위조된 DNS 응답 패킷을 보냄.
        - 나중에 도착한 응답은 무시.
    - 실습
        - arpspoof, fragrouter, dnsspoof, ettercap
        - 환경
            - win7 / 171.128 / 2b:96:79
            - kali / 171.133 / d4:2a:09
        - 공격
            - `vi /etc/ettercap/etter.dns`
                - `*.google.*    A    192.168.171.133` 추가
            - ettercap 실행
                - 체크표시 클릭 -> 스니핑 시작
                - [메뉴 - hosts - scan for hosts] -> host 스캐닝
                - [메뉴 - hosts - hosts list] -> 스캐닝 결과 보기
                - 라우터(.2)를 target1로, victim(.128)을 target2로 설정
                - [지구본 - ARP poisoning] -> ARP 스푸핑
                - [메뉴 - plugin - manage plugins] 에서 dns_spoof 더블클릭 -> dns 스푸핑
                    - 여기서 조금 기다려야 함.
            - 피해자 pc에서 google.com에 http로 접속하면 해커의 웹서버로 이동.
    - 보안대책
        - 중요한 사이트는 hosts 파일에 적어두어서 스푸핑 당하지 않도록 설정.
        - dns 서버에 대한 dns 스푸핑 공격도 존재.
            - 이는 bind를 최신 버전으로 바꿔서 해결
                - bind : ptr 레코드 뿐만 아니라 ptr 레코드에 의한 a 레코드 정보까지 확인
                    - ptr : ip에 대한 도메인 이름 해석
                    - a : forward zone에서 도메인 이름에 대한 ip 주소를 해석 

23. E-MAIL 스푸핑
    - 실습
        - hmailserver, sendmail
    - 보안대책
        - 보안이 강화된 샵(#) 메일을 사용.
            - 국내에서 만들어진 전자우편 서비스. 보안이 중요한 분야에서 사용하기 위해 만들어짐.
        - 상용 스펨메일 탐지 솔루션을 사용.





24. 터널링
    - 터널링과 VPN
        - 터널링
            - 인터넷을 사적이고 안전한 네트워크의 일부로 사용하게 하는 기술
        - 캡슐화
            - 터널 장비를 지날 때, 2계층 이상의 정보를 벗겨내지 않고 캡슐화
            - ![image](https://user-images.githubusercontent.com/44149738/141281078-ff14d70c-5b83-408f-a7e0-915351771d8a.png)
            - 대표적으로 VPN
        - VPN (Virtual Private Network)
            - 터널링의 대표적인 보안 장비
        - Internal Network (or IntraNet)
            - 기업 내부 데이터 통신용 네트워크
            - 인터넷과 구분된 별도의 임대회선(leased line) 사용
            - 가격이 고가임
                - 임대 회선과 비슷한 수준의 기밀성을 제공하려면 vpn 사용 및 암호화 필요
                - vpn 암호화 프로토콜에는 PPTP, L2TF, IPSec, SSL 등이 있음
        - 실습 - vpn
            - 환경: ubuntu 14
            - apt install openvpn easy-rsa
            - sudo vi /etc/openvpn/server.conf 
                - 다음과 같이 설정
                - ![image](https://user-images.githubusercontent.com/44149738/141300789-8aaac699-5a84-4b67-9e6f-31b23cb432ab.png)
            - sudo vi /etc/sysctl.conf
                - 다음과 같이 설정
                    - ![image](https://user-images.githubusercontent.com/44149738/141300865-997f51fb-f396-4898-a38e-9edc048c85ba.png)
            - cp -r /usr/share/easy-rsa/ /etc/openvpn
            - mkdir /etc/openvpn/easy-rsa/keys # 키 저장공간 생성
            - sudo vi /etc/openvpn/easy-rsa/vars
                - 다음과 같이 본인 설정에 맞게 자유롭게 변경
                - ![image](https://user-images.githubusercontent.com/44149738/141301785-68e94c59-84e8-4e28-af10-3ee9aa5eb0aa.png)
            - openssl dhparam -out /etc/openvpn/dh2048.pem 2048 # 인증서에 사용할 디피헬만키 생성
            - cd /etc/openvpn/easy-rsa
            - source ./vars
            - ./clean-all
            - ./build-ca # ca 인증서 생성
            - ./build-key-server server # 서버의 인증서와 키 생성
            - ls /etc/openvpn/easy-rsa/keys
                - 여기에 ca.pem, crt, key 그리고 server.crt, csr, key 이렇게 다 있는지 확인
                - 이거를 openvpn에 넣어주면 됨
            - cp /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn
            - cp /etc/openvpn/easy-rsa/keys/server.crt /etc/openvpn
            - cp /etc/openvpn/easy-rsa/keys/server.key /etc/openvpn
            - 이제 시작
            - service openvpn start
            - service openvpn status
            - 클라이언트 인증서와 키 생성
            - cd /etc/openvpn/easy-rsa
            - ./build-key client01
            - 클라이언트(windows)에서도 openvpn 설치.
                - 이것도 예전버전으로. 2.3.11
                - 실행 시 관리자권한으로.
            - 프로그램이 설치된 폴더에서 config/client.ovpn 파일 열어서 수정
                - 아래 부분도 수정
                - ![image](https://user-images.githubusercontent.com/44149738/141307801-291acc22-64ff-4f16-9e1f-4f7d9fc89c4f.png)
                - remote 부분의 ip를 서버의 ip로  잘 설정해주어야 함. 포트는 1194
            - ubuntu 에서 ca.crt랑, client01.cr, client01.key 3개 파일을 윈도우로 가져옴.
                - config 폴더에 넣음
            - openvpn을 실행해서 트레이 우클릭 후 connect!
            - ping(win -> ubuntu) 과정을 ubuntu에서 wireshark로 캡쳐해보기
                - openvpn으로 암호화 됨
        - 실습2 - ssh 터널링
            - win7, ubuntu 14 환경.
            - apt install openssh-server # ssh 설치
            - vi /etc/ssh/sshd-config 파일의 내용 아래와 같이 수정.
                - 없으면 생성.
                - ![image](https://user-images.githubusercontent.com/44149738/141615516-c81a21ee-093c-46d9-a811-b1e184f166d0.png)
            - /etc/init.d/ssh restart # ssh 재시작
            - windows에서 putty로 접속 
            - 인터넷도 옵션에서 프록시 5000 포트로 설정하면 터널링된 상태로 통신
    - 은닉채널
        - 은닉 메세지를 전송하기 위해 기본 통신 채널에 기생하는 채널
        - ackcmd 툴
            - ack 패킷만 이용해서 세션을 성립시키지 않음.
            - ack 패킷 안에 숨겨진 데이터를 주고받음.
            - 세션이 맺어지지 않아서 방화벽에 탐지도 안됨.
            - 그러나 너무 많으면 탐지할 수도 있으니 live 여부정도나 간단한 커맨드 정도로 사용
            - 공격 후 백도어로 데이터 송수신에 사용할 수도 있을 듯
        - 어떻게 방어할 수 있을까? 어떻게 방어를 우회할 수 있을까?
            - 요즘 머신러닝을 이용해서 탐지.
        - dns2tcp 툴
            - ubuntu 14, ubuntu server 16 환경
            - 서버에서 dns2tcp 세팅
                - apt install dns2tcp
                - vi ./dns2tcpd_config
                    - ![image](https://user-images.githubusercontent.com/44149738/141644633-4230ea7b-94a9-45ec-8eba-3d40f63c45f6.png)
                - dns2tcpd -d 3 -f ./dns2tcpd_config
                    - 만약 충돌나면 udp 53 포트 사용중인 것.
                    - 프로세스에서 kill 해야함.
            - 클라이언트에서 dns2tcp 세팅
                - apt install dns2tcp
                - vi ./dns2tcpc_config
                    - ![image](https://user-images.githubusercontent.com/44149738/141644694-4927db0a-7e8c-46ef-b329-610df6077a46.png)
                - dns2tcpc -f ./dns2tcpc_config
            - udp를 이용해서 ssh 접속이 가능해짐. dns를 이용해 은닉하는 방법
25. 세션 하이재킹
    - 세션을 가로채는 공격
    - active 한 공격
    - TCP 세션 하이재킹
        - 크게 두가지 종류
            - Non-Blind Attack(로컬 세션 하이재킹 공격)
                - 클라이언트와 서버가 통신할 때, 시퀀스 넘버를 이용하여 공격
            - Blind Attack(원격 세션 하이재킹)
                - 공격 대상을 탐지할 수 없으며, 시퀀스 넘버를 알아낼 수 없음
                - 사실상 시퀀스 경우의 수가 많아서 현실성은 없음.
        - TCP 시퀀스 넘버 교환
            - ![image](https://user-images.githubusercontent.com/44149738/141683462-1910d983-8a90-4b6c-9f4d-bf5edada34c6.png)
        - 동기화 상태 (3way handshaking)
            - ![image](https://user-images.githubusercontent.com/44149738/141683534-8d86ea68-6ef8-41ab-946b-429c6dfb6dcf.png)
        - 비동기 상태
            - 동기화가 이루어지지 못한 상태. 이 상태에서 하이재킹이 발생
            1. 데이터가 아예 전송되기 전은 안정적인 상태
            2. 데이터가 전송되었으나, 클라이언트에 전달되지 않았을 때.
            3. 패킷 수신이 불가능한 상태.
        - 비동기 상태로 만드는 방법
            - 서버에서 초기 설정 단계의 접속을 끊고 다른 시퀀스 넘버로 새로운 접속 생성.
            - 대량의 null 데이터(의미없는)를 보내는 방법 -> 결과가 어떨지 몰라서 의도한 대로 공격을 이끌어가기 어려움.
        - TCP 세션 하이재킹 시 TCP 세션의 변경 과정
            - ![image](https://user-images.githubusercontent.com/44149738/141683936-fee7c0af-bbf2-465b-9089-a3e11a07c02c.png)
        - ACK Strom
            - 만약 실제 client와 hacker가 서버로 ack를 보내게 된다면 동일 아이피에서 이상현상이 지속적으로 발생하게 되고, 연결을 위해 두 클라이언트는 끊임없이 경쟁하면서 ack를 보내게 됨. 서버는 이상한 현상을 해결하기 위해 재요청하고, 이러한 과정이 무한이 반복되는 경우를 뜻함.
            - 이러한 부자연스러운 상황으로인해 공격이 탐지될 수 있음
            - 이 현상을 막기 위해 ARP 스푸핑을 해두고 공격을 실시
        - 실습
            - arpspoof, shijack 툴 필요
            - 공격 순서
                1. 클라이언트가 서버로 telnet 접속
                2. 공격자가 arp 스푸핑으로 패킷의 흐름을 제어
                3. 클라이언트와 서버의 통신 끊고, 해당 세션 탈취
            - kali에 shijack 설치
                - https://packetstormsecurity.com/files/24657/shijack.tgz.html
                - 위 링크에서 다운로드
                - tar xvzf shijack.tgz 명령으로 압축 해제
                - 디렉토리에 들어가서 shijack-lnx 실행
            - ubuntu desktop에서 ubuntu server로 telnet 접속
            - kali가 패킷 릴레이 및 스푸핑
                - fragrouter -B1 # 패킷릴레이 
                - arpspoof -t 192.168.0.2 192.168.0.200 # 텔넷 서버에 대한 arp 공격
                - arpspoof -t 192.168.0.200 192.168.0.2 # 클라이언트에 대한 arp 공격
            - kali에서 tcpdump를 통해 스니핑 할 수 있음
                - telnet 통신중인 상호 ip, port 확인
            - 위 내용으로 세션 하이재킹 수행
                - shijack-lnx eth0 192.168.0.200 37426 192.168.0.2 23
                - 이후 mkdir 명령으로 디렉토리 만들면 잘 만들어짐.
        - 보안대책
            - ssh와 같이 암호화된 연결 지향 
                - 그러나 불가능한것까지는 아님. 하지만 티가 날 수 있음
            - 시퀀스 넘버를 주기적으로 체크하여 비동기화 상태에 빠지는지 탐지
            - ACK Storm 탐지
                - 잠깐 발생하는 상황이지만 발견할 수 있다면 탐지할 수 있음
            - 패킷의 유실과 재전송 증가를 탐지
            - 예상치 못한 접속의 리셋 탐지
                - 리셋 패킷은 여러 이유에 의해서 발생됨
26. MITM
    - 중간자공격
    - arp 리다이렉트, icmp 리다이렉트, apr 스푸핑 등이 이해 해당되기는 함.
    - 정확하게는 암호화된 채널을 사용하면서 위 공격들이 막혀서 생긴 공격
    - 위 세가지와 큰 차이점은, 위 세가지 공격은 패킷의 내용을 바꾸지는 않음. 그러나 mitm은 바꿈.
    - 실습
        - 윈도우 서버에 `C:\inetpub\wwwroot` 에 아무 이미지나 업로드
        - kali에서는 etterfilter 설정
            - filter.txt를 만듬
            - sudo etterfilter -o filter.ef filter.txt # 필터 파일로 생성(컴파일)
            - ettercap 실행
                - target 설정. (client)
                - filter 설정. load filter --> filter.ef 선택
        - client에서 iis 접속
        - 이미지가 replace되는 것을 확인
    - SSH MITM
        - SSH 암호화 기법
            1. 서버로부터 SSH 접속용 공개키 받음
            2. 개인키로 데이터를 암호화하고, 이를 다시 서버의 공개키로 암호화 하여 서버로 전송
            3. 서버는 개인키로 복호화한 후 클라이언트의 공개키로 복호화해서 데이터를 읽음
        - SSH 초기 연결 시 MITM으로 공격
    - SSL MITM
        - SSH 스니핑
            - SSH와 동일한 방식
        - 실습
            - SSL 통신 확인하기
                - daum.net과 같이 ssl 사용하는 아무 사이트나 접속
                - https 확인
            - DNS 스푸핑 공격 준비
                - `vi ./dnsspoof.hosts`
                - `192.168.0.201 *.daum.net` 추가
            - ARP 스푸핑 공격 수행 및 패킷 릴레이
            - 패킷 복호화
            - ssldump로 패킷을 복호화
                - ssldump -a -d -r wireshark.pcap -k webmitm.crt > wireshark_dec.txt
        - 실제로는 SSL 2.0으로 넘어가서 잘 안되기도 하고, 리소스도 생각보다 큼. 이론적으로만 알아두면 될듯.
        - SSH 스트립
            - https를 유지해주는게 아니라 클라이언트한테는 http로 통신
        - 실습
            - ssltrip 툴을 사용해야하는데, 공홈 안됨 ㅠ.
            - 이것도 이론만,,,
            - bettercap(?) 이라는 툴을 사용하기도 하나봄
    - MITM 대책
        - 기본적인 대응책은 ARP스푸핑과 DNS스푸핑의 경우와 같음
            - static 한 정보를 체크해야함
        - SSH MITM의 경우 SSH2.0을 사용하면 막을 수 있음
    - SSL Strip 대책
        - HTTP가 SSL로 잘 접속되고 있는지 확인
     
27. 무선 랜
    - IEEE 802.11
        - 무선랜 표준 (유선은 802.3)
        - 현재는 `.11n`이 많이 쓰임. 그 이상은 고가의 장비.
    - 통신범위
        - 지향성 / 무지향성
            - 무선은 대부분 무지향성.
            - 많은 사람이 접속할 수 있도록 하기 위함.
    - AP 정보 수집 실습
        - Kali에서 Kisnrnet 프로그램 사용
        - wardriving : 신호 기반으로 무선랜 위치를 수집
        - `sudo kismet`
            - 최신버전은 web으로 띄워줌. 2501 포트.
    - 암호화 프로토콜
        - WEP(Wired Equivalent Privacy)
            - RC4를 사용
            - WEB KEY 크랙 실습
                - `ifconfig wlan0 down` 일단 랜 죽임
                - `airmon-ng start wlan0`
                - 모니터링 모드 설정
                    - `sudo iwconfig`
                - 공격 대상 ap 설정
                    - `airodump-ng wlan0mon`
                - IV 수집하기
                    - `airodump-ng --ivs -c 1 -w WEP_DUMP --bssid {MAC} wlan0mon`
                - `aircrack-ng -b {MAC} WEB_DUMP-01.ivs`
                    - 안될 수도 있음. -> 강제로 패킷 생성해야됨
                - `airplay-ng -1 -0 -a {MAC} -H {MAC} wlan0mon`
        - WPA-PSK
            -  WEP 보완
            - 딕셔너리만 잘 구성되어있고, 약한 비밀번호 설정 시 공격 가능
            - 보안설정
                - AP 수신거리 조정
                - DHCP 중지
                - MAC 필터링
                    - 허용 MAC 관리
                - 요즘에는 AP에 WIPS(Wireless IPS)와 F/W이 합쳐진 상태로 나오기도 하기 때문에 이를 통해 관리할 수 있음.
            - 세션 하이재킹 실습
                - Ettercap 사용
                - WiFi 비밀번호 설정
                - 타겟 스캔
                - 타겟 설정
                - MITM
                - Wireshark로 분석
        - EAP
            - 중앙집중화된 무선랜 인증방식
            - RADIUS 서버와 클라이언트가 상호인증
            - 순서
                - ![image](https://user-images.githubusercontent.com/44149738/143725568-c383a755-1044-4bca-8021-0c1d55107079.png)
                - ![image](https://user-images.githubusercontent.com/44149738/143725577-0cd5a7c4-6976-4e9a-8730-6a98532546e2.png)
        
28. DoS/DDoS
    - DoS (Denial of Service)
        - 네트워크 용량을 초과시켜 정상동작하지 못하도록 하는 공격
        - 특징
            - 파괴,,,는 불가능한건 아니긴 함.
            - 시스템 자원고갈
            - 네트워크 자원고갈(대역폭)
        - Ping of Death 공격
            - ping을 이용하여 ICMP 패킷의 크기를 정상보다 아주 크게 만듦.
            - 크게 만들어진 패킷은 네트워크를 통해 라우팅되어 아주 작은 조각으로 쪼개짐
            - 공격 대상은 조각화된 패킷을 모두 처리해야해서 부하가 많이 걸림.
            - 실습
                - hping3 사용
                    - 패킷생성 툴인데, 공격용으로도 활용가능.
                    - 3계층 이상의 다양한 테스트가 가능.
                - `apt install hping3`
                - `hping3 --icmp --rand-source 192.168.0.134 -d 65000`
            - 보안대책
                - 반복적으로 들어오는 일정 수 이상의 ICMP 패킷은 무시하도록 설정
        - SYN Flooding
            - 최대 동접자수를 가득 채워서 다른 사용자가 서비스를 제공받지 못하게 하는 공격
            - 원리
                - ![image](https://user-images.githubusercontent.com/44149738/143726290-1d5f1487-19be-4747-8499-ab80c234a4ad.png)
                1. 수많은 SYN 보냄
                2. 서버는 SYN/ACK로 응답
                3. 공격자는 ACK 응답을 하지 않아서 timeout 시간동안 트래픽 점유
            - 실습
                - 마찬가지로 hping3 사용
                - `-S` 옵션을 붙여서 SYN만 보냄
                - `--flood` 옵션을 붙이면 그대로 서버가 뻗음
            - 대책
                - 시스템 패치 설치
                - IDS/IPS 설치
                - 공격패턴 확립. 짧은 시간에 똑같은 형태의 패킷.
                - Syn_Cookie 이용해서 보완
                    - ![image](https://user-images.githubusercontent.com/44149738/143726500-551a47be-c79e-492f-9765-d57554f2f589.png)
        - Boink, Bonk, Teardrop
            - 시퀀스 넘버를 조작해서 시스템 패킷 재전송과 재조합에 과부하가 걸리도록 시퀀스 넘버를 속임.
            - Bonk : 모두 1번 시퀀스로 조작해서 보냄
            - Boink : 정상적으로 보내다가 중간부터 일정한 시퀀스넘버를 보냄
            - Teardrop : 중첩과 빈 공간을 만들어 시퀀스 넘버가 좀 더 복잡해지도록 섞음.
                - Teardrop 실습
                    - hping3 이용
                    - `--seqnum` 이용해서 조작가능
        - Land
            - 도착하다. 출발지와 목적지를 둘 다 공격지 IP로 설정.
            - 실습
                - `-a` 옵션으로 ip 설정
                - `--icmp`, `--flood` 공격 가능
        - Smurf 공격
            - 웜이 네트워크를 공격할 때 많이 사용하는 것으로 ICMP 패킷 이용
            - 라우터는 기본적으로 브로드캐스트를 지원하지 않아 다른 네트워크에 브로드캐스트를 할 때는 다이렉트 브로드캐스트를 하게 됨.
            - 라우터 내부 에이전트에게 브로드캐스트를 때리고, 에이전트는 그 ICMP 응답을 공격대상에게 보낸다.
            - 실습
                - `agent ip 설정`
                - `-a 공격대상ip`
                - `--icmp --flood`
        - 7계층 DoS 공격
            - 웹 어플리케이션을 대상으로 공격방향을 전환
            - 주요 프로토콜
                - http, smtp, ftp, VoIP 등
            - http
                - http get flooding
                    - get 계속 보내는것
                - http cc 공격
                    - 캐시를 사용하지 않기 때문에 서버 부하 증가
                - 동적 http request flooding
                    - 요청 페이지를 변경하면서 웹 페이지를 지속적 요청
                - slow http header DoS(Slowloris) 공격
                    - header를 비정상적으로 조작.
                    - header를 완전히 수신할 때까지 연결을 유지.
                    - 요청이 끝나지 않은 것으로 인식해서 웹로그도 남지 않음.
                    - 실습
                        - switchblade 라는 프로그램 사용
                        - 라인피드 부분에서 총 2bytes중 1bytes만 보내서 대기시킴.
                        - 공격이 끝나면 최대 연결 가능 수를 확인할 수 있음
                - slow http post
                    - ![image](https://user-images.githubusercontent.com/44149738/143729050-87e4e8d4-88f7-4bbf-bb65-3c95fdc7f931.png)
                    - content-length 헤더를 설정하면 "어느정도" 대응 가능
                    - 실습
                        - content-length 값을 엄청 크게 하고, 실제 데이터는 1byte를 전송
            - mail bomb
                - 스팸 메일 종류
                - 메일이 폭주해서 디스크 공간을 가득 채우면 정작 필요한 메일을 받지 못함.
    - DDoS
        - 피해 양상이 상당히 심각하지만 확실한 대책이 없음
        - 발원지 파악이 어려움.
        - 공격 특성상 대부분 DDoS공격은 자동화된 툴 이용
        - 공격을 이루는 기본 구성
            - ![image](https://user-images.githubusercontent.com/44149738/143729580-58e24124-dc45-4f7a-b1d9-03744471c630.png)
            - Attacker : 해커 PC
            - Master : 명령 받는 시스템. 여러 agent 관리
            - Handler : 마스터 시스템 역할을 수행하는 프로그램
            - Agent : 실제 공격 시스템
            - Daemon : 에이전트 시스템 역할을 수행하는 프로그램
        - DDoS 공격 툴 종류
            - Trinoo(트리누)
                - UDP가 기본공격.
                - statd, cmsd, ttdbserverd 데몬이 주된 공격 대상
                - 마스터의 주요 명령
                    - ![image](https://user-images.githubusercontent.com/44149738/143729669-94007f73-6dbc-4ee5-9f9b-50ba3e3319c3.png)
                - 에이전트 명령
                    - ![image](https://user-images.githubusercontent.com/44149738/143729679-b8f0b21f-3192-465d-80ee-15c69c148e0c.png)
            - TFN(Tribed Flood Network)
                - Trinoo가 발전된 형태
                - ICMP Echo Request 패킷 사용
                - 연결이 맺어지지 않아서 모니터링이 쉽지 않음.
            - TFN 2K
                - TFN의 발전된 형태
                - 암호화 되어있음
                - 포트도 임의로 결정할 수 있음
                - 다양한 공격을 사용
                - 모든 명령은 CAST-256 알고리즘으로 암호화됨.
                - TCP 포트에 백도어 기능
                - 데몬 설치 시 정상 프로세스 이름과 비슷하게 설정해서 프로세스 모니터링을 회피
            - Stacheldraht(슈타첼드라트)
                - TFN을 발전시킨 형태
                - 공격자 - 마스터 - 에이전트 - 데몬 간 통신에 암호화 기능 추가
                - 마스터에 에이전트가 자동으로 갱신됨
        - 악성코드를 이용한 DDoS 공격
            - 공격자가 악성코드를 이용해서 에이전트들을 만듬
            - c&c로 에이전트를 통제해서 공격대상을 공격
            - 여기서 핵심은 내/외부에 있음
                - 외부 공격으로 진행하면 결국에 다른 형태랑 비슷하고, fw에서 막힐 수 있음.
                - 내부자를 감염시킬 수만 있다면 방화벽을 우회할 수 있음
            - 사례
                - 7.7 인터넷 대란
                - 부트섹터를 날려 마감하도록 설계됨
            - 대책
                - 내부 네트워크와 외부 네트워크의 경계선에 우선 설치
                - 방화벽이 차단할 수 있는 침입은 실제로 30%정도
                - 최소한의 포트만 열고 나머지는 닫음.
                - Trust 금지
                - 인증없이 접속할 수 있는 사용자를 허용하지 않음.
                - IPS/IDS
                - UTM (IPS + IDS)
                - 차세대 장비 : UTM + F/W + Snort rule 
                    - 오픈소스로도 있음
                - 서비스 별 대역폭 제한
                    - 공격자가 공격에 필요한 최소 대역폭을 얻을 수 없어짐.

29. 방화벽
    - 싸게는 백단위, 비싸게는 억단위
    - 근데 방화벽의 원리나 구조 자체는 굉장히 단순함.
        - 애초에 복잡하면 안되는 장비.
        - 최근에는 다양한 기술들이 적절하게 추가되면서 기능이 다양해짐.
    - 공유기는 방화벽이 고도화된 기술을 제공하지는 않음.
    - 굥유기 목적
        1. NAT 기능
        2. WIPS 무선 침입을 어느정도 방지
        3. 간단한 Access Control(AC)
            - 보통 디폴트로 꺼져있음.
    - 방화벽 기능
        - 접근제어(AC)
        - 로깅(Logging)과 감사추적(Audit Trail)
        - 인증(Authentication)
            - 메시지 인증
            - 사용자 인증
            - 클라이언트 인증
        - 데이터 암호화
            - 방화벽끼리 전송되는 데이터를 암호화해서 보냄
    - 방화벽의 한계
        - 바이러스 차단 불가
        - 내부 공격 차단 불가
            - 외 -> 내 (탐지)
            - 내 -> 외 (탐지)
            - 내 -> 내 (탐지 불가)
                - 이런건 백신단에서 엔드포인트를 검사하는 형태로 해야함.
        - 장비를 통하지 않은 통신에 대한 제어 불가
        - 새로운 형태의 공격 차단 불가
            - Zeroday Attack
    - 베스천 호스트(Bastion Host)
        - 독일어로 성곽의 모서리 둥근 부분을 지칭
        - 네트워크에서 철저한 방어 정책이 구현되어있고, 외부 접속에 대한 일차적인 연결을 받아들이는 시스템을 뜻함.
        - 일부 방화벽으로 동일하게 보는 사람들이 있으나, 동일한 것은 아님
            - 베스천 호스트 중 한 곳에 방화벽이 놓일 뿐.
            - 예를 들면 F/W 앞단에 DDoS 방어장비가 놓이게 되면 배스천 호스트는 DDoS 방어장비가 되게 됨.
    - 스크리닝 라우터
        - 3,4 계층에서 실행
        - IP 주소와 PORT 에 대한 접근 제어만 가능
        - 단점 : 디테일한 규칙을 적용하기 어렵고, 규칙 많아지면 부하가 걸림
        - 장점 : 저렴함
    - 단일 홈 게이트웨이
        - single-homed Gateway
        - 스크리닝 라우터의 발전된 형태
        - 일반적으로 베스천 호스트라고 부르기도 함.
        - 점근제어, 프록시, 인증, 로깅 등 방화벽의 가장 기본이 되는 기능을 수행
        - OS가 있는 시스템에 설치해서 운용하기 때문에 선행작업 필요
        - 비교적 강력한 보안 정책을 실행할 수 있으나, 손상되면 무조건적인 접속을 허용.
        - 방화벽으로의 접속 정보가 노출되어서 원격접속이 가능해지면 내부 네트워크를 보호할 수 없음.
        - 단일로는 잘 구성하지는 않음
    - 이중 홈 게이트웨이
        - Dual-homed gateway
        - NAC를 둘 이상 갖춘 방화벽
        - 사설 네트워크를 여러개 나눌 수 있음.
        - 사용 용도에 맞게 나누면 보안성 향상
        - 이런 형태를 많이 사용함.
    - 스크린된 호스트 게이트웨이
        - Screened Host Gateway
        - 라우터와 방화벽을 구분하여 운영
        -  2단계 방어를 실행하므로 안전함.
        - 가장 많이 이용하는 구조!!!
        - 단점
            - 융통성은 좋은데, 해커가 스크리닝 라우터를 해킹하면 베스천 호스트를 거치지 않고 내부 네트워크에 직접 접근할 수 있음.
            - 비용도 많이 듬
        - 이중 홈 게이트웨이와 함께 사용할 수도 있음.
    - 스크린된 서브넷 게이트웨이
        - Screened Subnet Gateway
        - 외부/내부 네트워크 사이에 완충지대를 두는 것
        - 장점
            - 다른 방화벽의 장점을 모두 살리고 융통성도 있음.
        - 단점
            - 설치와 완리가 어려움
            - 비용이 비쌈
    - 실습
        - IPCop는 오래돼서 IPFire로 설치
            - 같은 계열이라고 보면 됨.
        - IPFire는 두 가지 인터페이스로 나뉨
            - Red interface
                - 공인쪽 interface
                    - 공인이 아니어도 아무튼 외부 네트워크 interface
            - Green interface
                - 사설쪽 interface
        - 방화벽 red, green 맞게 설치
        - green쪽 client에서 http://방화벽IP:444 접속하면 방화벽 웹콘솔에 접근가능
    - 보안의 기본 원칙
        - fail safe
            - 오류가 발생해서 시스템이 정상적으로 작동하지 않을 때, 사용자나 시스템에 피해를 입히지 않는 상태로 남아있어야 함.
            - 방화벽은 일반적으로 fail safe 원칙이 적용.
            - "명백히 허용하지 않은 서비스에 대한 거부"를 기본 원칙으로 함.
        - safe failure
            - 실패가 일어난 경우에도 안전해야함을 의미.
            - 시스템에 오류가 생겨도 네트워크가 마비되지 않도록 허브로 작동
    - fail safe를 적용하는 과정
        1. 허용할 서비스 확인(화이트리스트)
        2. 보안문제가 없는지, 허용이 타당한지 검토
        3. 서비스가 이루어지는 형태를 확인, 어떤 규칙을 적용할지 구체적으로 결정
        4. 실제로 방화벽에 적용을 한 뒤 적용된 규칙을 검사
    - 패킷 필터링에 대한 이해
        - 가장 최상단 룰은 통신을 위한 규칙을 명시(allow)
        - 가장 마지막 룰은 명시된 룰을 제외한 모든 패킷은 차단하도록 명시(deny)
    - 실습
        - 통신을 위해 dhcp 설정
            - network - dhcp configuration 메뉴
                - green interface 선택
                - start, end adress 설정
                - primary dns는 green interface 주소로 설정
                    - 앞으로 green 영역의 client ip 주소 설정 시 게이트웨이를 green interface 주소로 설정
        - status - external 또는 internal 메뉴
            - 내/외부 트래픽을 확인할 수 있음.
        - firewall - rule 메뉴
            - 룰 설정 후 add -> apply changes
            - http , https , icmp 설정
    - NAT( Network Address Translation)
        - Normal NAT
            - 기본적인 개념
        - Reverse NAT
            - 내부에 서버가 존재하는 경우에 설저
            - Static Mapping 이라고도 함.
            - 외부 클라이언트의 IP를 유지해줌.
        - Redirect NAT
            - 목적지 주소를 재지정
        - Exclude NAT
            - Normal NAT를 적용받지 않고 방화벽을 지나도록 설정
            - 특정 목적지에 대해서 설정 적용 가능
    - 실습
        - 똑같이 rule 설정 메뉴
        - 외부에서 내부로 들어오는 룰 추가
    - 프록시
        - 방화벽의 한 구성 요소로 동작하면서 패킷 필터링에 대한 보조적인 도구 또는 독립적으로 운영
        - 보안상 또는 회사 정책상 부합하지 않는 부분에 대한 규제가 가능하며, 로그 정보 역시 효과적으로 관리 가능
    - 프록시 종류
        - 회로 계층 프록시
            - circuit level proxy
            - socks처럼 하나의 회로를 만들 뿐 실제적인 프로토콜 분석 불가능
        - 응용 계층 프록시
            - application level proxy
            - http, ftp 등 하나의 서비스에 대한 프록시가 개별적으로 존재
    - 실습
        - network - web proxy 메뉴
        - enable green, transparent green, supress version information 활성화 후 save
        - 방화벽 룰 추가. http 기반 통신 막음
        - 클라이언트에서 인터넷 옵션에 들어가서 프록시를 켜고 방화벽 ip로 설정
        - web 들어가면 안됨. -> s 계열 통신 때문.
        - 기능 정도는 디폴트로 제공한다! 정도만 알것. 실제로는 클라이언트에 인증서관리하는 프로그램 필요
    
30. NAC
    - Network Access Control
    - 가상환경으로 구성하기에는 한계가 있음.
    - ACL : Access Control List
        - OS에서 객체에 대한 접근 제어를 담당하는 테이블
        - 방화벽의 룰셋과 비슷한 역할
        - 규칙인 단순해서 높은 대역폭에서도 효과적으로 작동하나, 방화벽에 비해 기능이 제한적임.
        - 종류
            - 숫자로 구분하는 Numbered, 임의 이름을 부여하는 Named로 구분
            - Numbered는 standard와 extended로 구분
            - Standard
                - 1~99번
                - 출발지 주소만 검사하여 제어
                - ex) R1(config)# access-list 1 deny 192.168.1.0 0.0.0.255
                - in/outbound 설정
                    - ex)
                        ```
                        R1(config)# interface serial 0/0
                        R1(config)# ip access-group 1 in
                        R1(config)# ip access-group 2 out
                        ```
            - Extended
                - 100~199번
                    - ex)
                        ```
                        R1(config)# access-list 101 deny ip 192.168.1.0 0.0.0.255 210.1.6.0 0.0.0.255
                        R1(config)# access-list 110 accept tcp[ 192.168.1.0 0.0.0.255 172.16.1.0 0.0.0.255 eq 80
                        ```
        - ACL 적용 규칙
            - 입력 순서대로 수행 : ACL 허용의 경우, 좁은 범위의 설정을 먼저 작성하고 넓은 범위를 순서대로 작성
            - 마지막에 DENY ANY 생략 : ACL 조건이 없는 모든 경우는 deny가 됨.
            - 중간에 수정 불가 : Numbered ACL은 순서대로 입력되므로 중간에 삽입하거나 삭제가 불가
        - Extended ACL 원리
            - ![image](https://user-images.githubusercontent.com/44149738/146768320-7af080aa-c040-4450-b03f-e0eaac577ffb.png)

31. VLAN
    - Virtual LAN
    - 네트워크 분할 기능 제공
    - 네트워크 관리자는 네트워크를 작은 네트워크로 임의로 나눈 뒤 나누어진 것에 여러개로 구별되는 브로드캐스트 패킷을 제한하는 기능을 갖게 함.
    - 목적별로 네트워크를 분리하여 네트워크 보안 수준을 높일 수 있음.
    - 스위치의 VLAN 통신
        - Trunc 포트를 이용해서 통신.
        - VLAN 표시를 client에게 전달할 때는 떼고 보냄

32. NAC
    - 네트워크 접근 통제 시스템
    - 지금의 NAC은 많은 기능이 있음
        - 자원관리
        - 비인가 장비 탐지
    - 종트래픽만 가능
    - 기능
        - 접근 제어/인증
            - 역할 기반 내부 직원 접근 제어
            - 네트워크의 모든 ip 기반 장치로의 접근 제어
        - pc 및 네트워크 장치 통제(무결성 체크)
            - 백신 관리
            - 패치 관리
            - 자산 관리(비인가 시스템 자동 검출)
        - 해킹, 웜, 유해 트래픽의 탐지 및 차단
            - 유해 트래픽의 탐지 및 차단
            - 해킹 행위 차단
            - 완벽한 증거 수집 능력
    - 방식
        - in-line 방식
            - 게이트웨이 형태로 일부 물리적 네트워크에 NAC 추가
            - 기존 네트워크의 변경을 최소화하여 적용할 수 있음.
            - 네트워크를 가로막는 방식
        - 802.1x 방식
            - RADIUS 서버와 802.1x를 지원하는 스위치 필요
            - 스위치 포트를 차단하여 우회가능성을 거의 없앤, 매우 효과적인 네트워크 차단방식
            - 구축이 어렵고, 스위치가 모두 이 방식을 지원해야함.
            - 무선환경에서 많이 사용
        - VLAN 방식
            - 비인가는 통신 불가 VLAN에, 인가 사용자는 통신 가능한 VLAN 망에 할당
            - 보안이 뛰어나며, 우회가 어려움
            - 네트워크의 모든 장비가 VLAN을 지원해야함
        - ARP 방식
            - 차단하려는 단말에게 ARP 스푸핑 패킷을 보내 네트워크의 정상적인 접근을 막는 것
            - 장비의 제약을 받지 않음
            - 단순한 구조라 빠르게 적용 가능
        - 에이전트 설치 방식
            - 클라이언트에 에이전트를 설치하는 방식
            - 종/횡 모두 판단 가능
            - 에이전트를 통해 네트워크를 차단
            - 격리 수준이 높음
    - 실습
        - PacketFense 프로그램 사용
        - Zero effort NAC 탭 선택 후 download 클랙 -> sourceforge 연결 -> 파일 다운로드
        - 압축 풀면 ova 파일 나옴. VM 프로그램에서 로드
        - 계정 : root / p@ck3tf3nc3
        - 클라이언트에서 nac의 1443 웹 페이지 접속
        - interface 별 NAC 설정.

33. IDS/IPS
    - IDS 목적
        - 경찰과 비슷한 역할 == 탐지
        - 데이터 수집(raw data collection)
            - HIDS (Host-based IDS)
                - OS에 부가적으로 설치되어 운용.
                - 전체 네트워크에 대한 침입 탐지 불가능(스스로가 공격 대상이 될 때만 침입 탐지 가능)
                - OS 취약점으로 인해 HIDS가 손상될 수 있으며, 다른 IDS에 비해 많은 비용 필요
            - NIDS (Network-based IDS)
                - 네트워크에서 하나의 독립된 시스템으로 운용(TCP Dump도 NIDS)
                - 감사와 로깅 시 자원손실 및 데이터 변조 없음
                - 네트워크 전반에 대한 감시 가능
                - IP 주소를 소유하지 않아서 해커의 직접적인 공격은 거의 완벽하게 방어 가능.
                    - IP를 가지고는 있는데 다른 네트워크에서 봄
                - 공격당한 시스템에 대한 결과를 알 수 없고, 암호화된 내용을 검사할 수 없음.
                - 스위칭 환경에서 NIDS를 설치하려면 부가 장비 필요
                - 1Gbps 이상의 네트워크에서는 정상 작동 어려움.
            - HIDS, NIDS를 상호 보완적으로 사용
        - 데이터 필터링과 축약
            - 효과적인 필터링을 위해서 데이터 수집에 대한 규칙을 설정하는 작업이 필요
            - 클리핑 레벨(Clipping Level) : 일정 수 이상 잘못된 패스워드로 접속을 요구하면 로그를 남김.
        - 침입탐지
            - 오용탐지(Misuse Detection)
                - 탐지 오판 확률이 낮고 비교적 효율적
                - 제로데이 공격은 방어가 어려움.
            - 이상탐지(Anomaly Detection)
                - 급격한 변화가 생기거나, 확률이 낮은 일이 발생할 경우 침입 탐지로 여겨서 알리는 것
                - 인공지능과 같은 기술을 사용.
                - 정확도는 좀 떨어질 수 있음. 이상적인 수치나 편의성은 좀 떨어짐.
        - 책임 추적성과 대응
            - 공격을 발견하면 알리는 수준이었던 과거와 달리 최근에는 공격을 역추적하는 등 능동적 기능들이 추가되고 있음
        - IDS가 실행할 수 있는 능동적 기능
            - 공격자에게 TCP Reset 패킷을 보내 연결을 끊음.
            - 공격자의 ip주소나 사이트를 확인하여 라우터나 방화벽으로 차단
            - 공격 포트를 ㅗ학인하여 라우터와 방화벽을 설정
            - 심각한 사태에 이르렀을때는 네트워크 구조 자체를 임시로 바꿈.(현실적으로는 좀 어려움. 잘 못함)
    - IPS
        - IDS에 차단 기능을 부가한 시스템
        - 보통 방화벽 뒷단에 설치
        - 설치가 간편
        - 최근에는 방화벽 없이 IPS만 설치하기도 함(방화벽이 합해진 UTM)
34. 허니팟
    - 해커의 정보를 얻거나 잡으려고 설치
    - 허니넷
        - 허니팟을 포함한 네트워크로 경각심, 정보, 연구를 목적으로 함.
    - 허니팟의 요건
        - 해커에게 쉽게 노출된다.
        - 쉽게 해킹이 가능한 것처럼 취약해 보인다.
        - 시스템의 모든 구성 요소를 갖추고 있다.
        - 시스템을 통과하는 모든 패킷을 감시한다.
        - 시스템에 접속하는 모든 사람에 대해 관리자에게 알려준다.
    - 허니넷의 구성(허니넷 GEN-I)
        - 분당 다섯 개 정도의 연결만 허용
        - 자동화된 툴의 공격과, 웜 공격에 대한 정보 수집에 좋은 성능을 보이며, DoS나 무차별적 스캐닝 공격을 막을 수 있음
        - 보통 방화벽으로 iptables를 사용하고 IDS는 Snort를 사용
    - 허니넷의 구성(허니넷 GEN-II)
        - 호그와시라는 2계층 IDS 게이트웨이 추가
        - 공격으로 탐지되는 패킷을 2계층에서 차단
35. 통합 보안 관리 시스템(Enterprise Security Management, ESM)
    - 다양한 보안 솔루션을 통합해 관리하는 솔루션
    - 제대로 쓰려면 굉장한 보안 지식이 필요함.
        - 제대로 못쓰면 개별적으로쓰는거나 다름없음. 돈낭비.
        - ex) splunk (자유도 높은 ESM. 차단은 못함.)
    - Agentless 방식이 난이도가 더 높음
    - 구성
        - 관리 콘솔 : 정책 설정, 침해사고 모니터링, 분석, 경보, 보고서 생성 등
        - 매니저 : 관리 콘솔에서 설정한 정책 적용, 데이터를 취합 및 저장, 분석
        - 에이전트 : 방화벽, 침입탐지시스템, 침입차단시스템, 일반 서버에 설치. 과련 로그 수집 뒤 매니저에게 전송.
    - 특징
        - 보안 정책의 일관성 유지.
            - 일관성이 장점으로 작용하려면 섬세한 정책 제작이 필요함
            - 제대로 못쓰면 이 일관성 때문에 탐지를 못하는 경우 발생
        - 통합 보안 관리 인프라 구축 
        - 효과적인 침해사고 대응
            - 솔직히 대부분 ESM이 제대로 활용 못되고 놀고있음.
            - 그냥 로그 보관용으로 사용하는 사례가 많음.
            - 이걸 효과적으로 사용하는 것이야 말로 훌륭한 관제사라고 볼 수 있음
        

    - IPS

































# 2주차 과제
1. 프로토콜의 3가지 요소가 아닌 것은 무엇인가?  
    답) 2. 통제

2. 프로토콜의 기능이 아닌 것은 무엇인가?  
    답) 4. 비동기화

3. 다음 중 B 클래스에 속하는 IP 주소는 무엇인가?  
    답) 2. 168.126.63.1

4. OSI 7계층 중 라우팅, 흐름 제어, 단편화, 오류 제어 등을 수행하는 계층은 무엇인가?  
    답) 3. 네트워크 계층

5. OSI 7계층 중 점대점(point-to-point) 연결에 신뢰성 있고 투명한 데이터 전송을 보장하기 위한 계층으로, 이를 위해 양단 간에 오류 제어와 통신량 제어 그리고 다중화를 제공하는 계층  
    답) 2. 전송계층

6. 다음 중 2계층에서 동작하는 네트워크 장비는 무엇인가?  
    답) 2. 스위치

7. 수신되는 프레임의 목적지 주소를 확인하고 목적지 주소의 포트로 프레임을 즉시 전송하는 스위칭 방식은 무엇인가?  
    답) 컷스루 방식

8. 비연결 지향형 프로토콜로, 상대방이 보낸 응답을 확인하지 않으며 송신 시스템이 전송하는 데이터에 대한 목적지 시스템의 확인 절차를 생략하여 네트워크에 부하를 주지 않는 것이 장점인 프로토콜은 무엇인가?  
    답) 3. UDP

9. 호스트 서버와 인터넷 게이트웨이 사이에서 메시지를 제어하고 오류를 알려주는 프로토콜로 ping에 사용되는 것은 무엇인가?  
    답) 3. ICMP

10. 244.0.0.1 ~ 239.255.255.255 IP를 사용하여 한 호스트에 특정한 호스트를 묶어서 전송하는 식으로 특정 그룹에 패킷을 전송하는 형태는 무엇인가?  
    답) 3. 멀티캐스트

11. 다음 중 연결 지향형으로 동작하는 전송계층 프로토콜은 무엇인가?  
    답) 3. TCP

12. 다음 중 서비스와 포트 번호가 잘못 연결된 것은 무엇인가?  
    답) 3. SMTP, 53. *25번 포트

13. 프로토콜의 기능 중 캡슐화에 대해 설명하시오  
    답) 패킷 송수신을 위해 계층별로 사용하는 프로토콜이 있습니다. 수신을 위해 각 프로토콜은 필요한 정보를 패킷의 앞단 또는 뒷단에 붙입니다. 이 과정을 encapsulation 이라 하며, 송신측에서는 반대로 encapsulation 되어있는 패킷을 하위 계층 구조부터 참조하여 어떤 상위 계층 구조를 참조할 것인지 파악하며 최종적으로 내부 data를 읽을 수 있게 됩니다. 이는 decapsulation 이라고 합니다. 이렇듯 해킷을 en/decapsulation 하는 로직을 가지고있는 수신측 OS 또는 네트워크 장비의 펌웨어가 존재할 것이기 때문에, 구조에 맞지 않는 악의적인 패킷이나 필드값이 조작된 패킷을 송신하여 en/decapsulation 과정을 이용한 공격이 가능할 것 같습니다.


14. ARP와 RARP에 대해 설명하시오  
    답) LAN 단위의 네트워크에서는 IP 주소와 함께 MAC주소를 이용하여 통신합니다. 따라서 IP와 MAC주소를 알아내기 위한 프로토콜이 존재하는데, 이것이 ARP와 RARP입니다. ARP는 IP를 통해 MAC 주소를 획득하기 위한 브로드캐스팅 질의과정이며, RARP는 MAC주소를 통해 IP를 획득하기 위한 브로드캐스팅 질의과정입니다. 그러나 이는 브로드캐스팅에 응답한 장치의 신뢰성을 따지지 않기 때문에 취약성이 존재할 수 있습니다. 대체로 동적 ARP 테이블을 이용하는데, 해커가 ARP 응답패킷을 보내게 되면 ARP 테이블에 해커의 주소가 등록되어 이후 해커와 통신하게 되는 arp spoofing과 같은 공격이 발생할 수 있습니다.


15. 동적 라우팅과 정적 라우팅의 특성 세 가지씩 간단히 기술하시오.  
    - 라우팅 테이블 관리  
        정적 라우팅에서는 라우팅 테이블을 네트워크 구조를 잘 알고있는 관리자가 직접 수동으로 관리해야합니다. 라우팅 알고리즘을 거치지 않는다는 점에서 빠르다는 장점이 있지만 구조가 복잡하거나 변동이 잦은 네트워크에서는 변화를 자동으로 파악하지 않기 때문에 사용하기 적합하지 않습니다. 이 경우에는 동적 라우팅을 사용하는데, 라우팅 테이블이 자동으로 관리되기 때문에 네트워크 변화에 민감하지 않습니다.

    -  처리 부하  
        동적 라우팅을 위해서는 패킷의 송수신 경로를 설정하기 위해 라우터에서 라우팅 알고리즘을 이용하여 최적의 경로를 탐색합니다. 또한 네트워크 변화에 유동적으로 대응하기 위해 주기적으로 패킷을 보내 라우팅 테이블을 업데이트합니다. 따라서 동적 라우팅을 운영하기 위해서는 자동화를 위해 CPU와 메모리에 부하가 발생할 수 있습니다. 반면에 정적 라우팅은 네트워크 구조를 이미 알고있고, 미리 설정해둔 테이블을 참조하여 라우팅을 진행하기 때문에 라우팅 테이블을 갱신하기 위한 CPU와 메모리 부하가 발생하지 않습니다. 그러나 정적 라우팅의 단점을 해결하기 위해 실시간 관리 차원에서 NMS를 운영하게 되면, 그 과정에서 부하가 발생할 수 있습니다.

    - 백업 및 복구  
        어떤 라우터에서 장애가 발생할지는 모르기 때문에 정적/동적 라우팅이 대응하는 과정에서도 차이가 있습니다. 동적 라우팅의 경우 라우팅 테이블 업데이트를 주기적으로 진행하기 때문에 장애 발생 시 수 초 내로 다른 라우팅 경로로 통신할 수 있게 구성됩니다. 따라서 장애가 발생해도 통신할 수 있는 백업 회선 및 장비를 구축하기만 하면 장애에 대응할 수 있어서 편리합니다. 반면에 정적 라우팅의 경우 따로 해당 라우터에 대한 백업 회선을 구축해두지 않는다면 장애 시 대응이 어렵습니다.

16. TCP 프로토콜에 대해 간단히 설명하시오  
    답) TCP 프로토콜은 연결 지향형 프로토콜입니다. 논리적인 "연결" 상태를 유지하기 위해서 3 way handshake 라는 연결과정과 4 way handshake 라는 연결 해제 과정을 진행하게 되는데, 이 과정에서 송신자와 패킷 내 송신자와의 일치 여부를 고려하지 않기 때문에 DoS 공격에 악용될 수 있습니다.


