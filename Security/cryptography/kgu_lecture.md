1. 캐릭터
    - 좋은 캐릭터
        - 엘리스
        - 밥
        - 찰리
    - 나쁜 캐릭터
        - 트루디
        - 이브

2. 보안의 핵심 개념 (CIA)
    - Confidentiality (기밀성) : 읽거나 볼 수 없다.
    - Integrity (무결성)       : 내용이 변경되지 않음.
    - Availability (가용성)    : 언제든지 접근할 수 있다. (= 정상 운용된다)

3. CIA 응용/심화
    - Authentication (인증) : 상대방이 맞는지 검증.
    - Authorization (인가)  : 인증이 된 다음에, 권한이 있는 행위만 할 수 있도록 제한.

4. Crypto
    - Cryptology : Cryptography, Cryptanalysis 를 아울러 이르는 말
    - Cryptography (암호학) : 암호를 만드는 것
    - Cryptanalysis : 공격자의 입장에서 암호를 푸는 것.
    - Crypto : 전체를 아울러 이르는 말

5. Kerckhoffs Principle
    - 암호 알고리즘을 숨기지 않아야 한다.
    - 알고리즘이 외부에 공개된 상태에서 분석을 진행해야 안전성을 검증 할 수 있다.

6. Simple subsitution
    - 알파벳과 매칭되는 mapping table이 있음.
    - 이를 이용하여 치환하는 형태의 암호방식.
    - 종류
        - Caesar's cipher                       # TODO : 프로그램 만들어야겠음
            - 단순히 고정된 시프트 문자 mapping table을 이용.
        - not-so-simple substitution            # TODO : 프로그램 만들어야겠음
            - 시프트 값을 key로 설정하여 생성된 mapping table을 이용.
        - even-less-simple subsitution          # TODO : 프로그램 만들어야겠음
            - 랜덤한 mapping table이 key로 사용됨.
            - keyspace가 크기 때문에 비교적 안전.
            - 그러나 frequency를 이용한 공격에 취약.

7. Double Transposition cipher
    - 알파벳 값을 변환하는게 아니라, 위치를 바꾸는 형태의 암호방식
    - plaintext를 행렬로 나열한 후에, 행과 열 순서를 뒤바꾸어 표현.

8. One-time Pad
    - 랜덤한 키를 생성하여 plaintext와 xor을 진행한다. 
    - ciphertext에 다시 키를 xor하면 plaintext를 구할 수 있다.
    - 전수조사가 의미가 없다. 그 이유는 xor 특성상 key에 따라 말이 되는 결과가 나올 수 있기 때문.
    - 오히려 무결성 문제가 생김.

9. codebook
    - 일종의 치환암호
    - 단어가 적힌 책을 이용하여 해독.

10. 공격 방식
    - Ciphertext only attack
        - 오직 암호문만 가지고 공격
    - Known plaintext attack
        - plaintext와 이에 대응하는 ciphertext 몇 개를 가지고 있는 상황
    - chosen plaintext attack
        - 원하는 plaintext의 ciphertext의 결과를 사전에 알고 있는 상황
    - adaptively chosen plaintext attack
        - 실시간으로 원하는 plaintext의 ciphertext를 구할 수 있는 상황

11. symmetric key(대칭키) 암호
    - 크게 두 가지로 나눌 수 있음
        - stream cipher
            - 지속적으로 들어오는 데이터를 실시간으로 암/복호화(영상 등)
            - 종류
                - A5/1
                    - 3개의 레지스터(X-19bit, Y-22bit, Z-23bit)로 이루어져있음.
                    - shift 방식을 이용. hw단에서 연산이 가능하기 때문(=빠름).
                - RC4
                    - 256개의 원소 중 key에 의해 값을 뽑아 key stream 형성
            - 블록사이퍼로 스트림 처럼 사용할 수 있게 되어 스트림 사이퍼는 잘 안쓰게 됨
            - 여전히 사용되고 있긴 함.
        - block cipher
            - 긴 plaintext를 암호하기 위해 block 단위로 잘라서 암호화.
            - feistel cipher
                - block cipher을 디자인하는 대표적인 방법.
                - 암호 알고리즘은 아니고, 디자인 틀이라고 보면 됨.
                - 여러 round로 이루어져 있음.
                - 각각의 round가 연결(이전 round결과가 다음 round에 영향을 미침)
                - 각 round마다 round function을 통해 결과를 도출함.
            - 종류
                - DES (Data Encryption Standard)
                    - feistel cipher 형태를 사용
                    - 64bit block length
                    - 56bit key length
                        - 64bit 중 8bit는 내부적으로 제거
                    - 16 rounds
                    - 48bit subkey
                    - 컴퓨팅 파워가 좋아지면서 전수조사가 가능해짐
                - Triple DES (= 3DES)
                    - 암호화 =>     C = E(D(E(P,K1),K2),K1)
                    - 복호화 =>     D = D(E(D(C,K1),K2),K1)
                - AES (Advanced Encryption Standard)
                    - fiestel 형태가 아님.
                    - DES의 한계를 느끼고 공모를 통해 만든 암호체계
                    - block size : 128bit
                    - key len : 128, 192, 256
                    - 10 to 14 round
                    - subbytes 연산이 des의 s-box처럼 nonlinear한 성질을 제공
                - IDEA
                - Blowfish
                - RC6
                - TEA
            - mode 연산
                - 종류
                    - ECB
                        - 좋지 않은 방법. 쓰지마!
                        - cut and paste 공격에 취약함.
                            - 복호화 하지 않아도 순서를 재배열 할 수 있음.
                        - 동일한 plaintext block이면 ciphertext block도 같다는 취약점이 있다.
                        - 이미지를 암호화하는 경우 실루엣이 그대로 남는다.'
                            - 같은 값이 동일한 값으로 암호화 되기 때문
                    - CBC
                        - block들이 상호연결(chain)되어있다.
                        - 평문 블록을 암호문 블록과 xor하여 안정성 높임
                    - CTR
                        - counter 이용.
                        - 스트림 암호를 대체할 수 있음.
            - MAC
                - confidentiality(기밀성)은 보장하지만
                - Integrity(무결설)을 보장하지 못하는 문제가 발생
                - 무결성을 체크해주는 방향으로 발전.
                - 그 역할을 하는것이 MAC
                - 사전에 MAC 용도의 KEY 공유.
                - 송신자는 KEY로 메시지를 CBC 연산.
                - 수신자는 KEY로 복호화된 메시지를 CBC 연산을 통해 체크.

12. Public key(공개키) 암호
    - public key(공개키)와 private key(개인키) 총 두 개의 key를 가짐.
    - trap door한 성지를 가지는 one way function을 기반으로 동작함.
        - one way function : 단방향으로만 연산 가능.
            - f(x)가 y인 것을 알기는 쉬우나, f(x)를 만족하는 x를 찾기는 어려움.
    - 종류
        - knapsack problem 기반
            - 일반적인 knapsack problem(GK)는 NP-problem임. (= 풀기 어려움)
            - superincreasing knapsack(SIK) 문제는 어렵지 않다. 쉽다.
                - 앞의 합보다 큰 다음수의 연속.
                - 큰수부터 넣으면 풀림.
            - public key : GK
                - modular 연산으로 생성
            - private key : SIK
                - modular inverse로 생성
            - trapdoor 특성
                - 일반적인 문제를 푸는 건 어려움. 그러나 특수조건(SIK)에서는 풀기 쉬움.
            - one-way 특성
                - 문제를 출제하는건 쉬움. 그러나 반대로 푸는건 어려움.
            - 한계
                - 메시지가 길어지면 키도 길어짐
                - 해독방법 연구에 성공함. -> 그러나 아주 취약한건 아님.
        - RSA
            - Rivest, Shamir, Adleman (MIT)
            - 큰 소수인 p, q 생성(1024bit)
            - p, q의 곱인 N 생성(2048bit)
            - phi = (p-1)(q-1)
            - phi와 서로소인 e 생성
            - ed = 1 mod phi 인 d 생성
                - ed = k(p-1)(q-1) + 1
            - public key : (N,e)
            - private key : d   -> (N,d)
            - M = C^d mod N
            - C = M^e mod N
            - e 는 너무 작으면 안됨.
                - 일반적으로 e^16 + 1 값을 사용. (= 65537)
            - RSA padding
                - 동일한 메시지는 동일한 결과가 나옴.
                - 이를 해결하기 위해 암호화 이전에 랜덤한 값을 추가.
                - OAEP 방식의 패딩을 사용.
        - Discrete Logarithm 기반
            - 이산대수 문제
            - RSA와 더불어 가장 많이 사용되는 알고리즘.
            - Diffie-Hellman 키교환, DSA에 많이 사용됨.
            - 오일러 정리.
                a^(phi(n)) = 1 (mod n)
                : a와 n이 서로소인 소수라고 할 때
                : 1 mod n 을 만족하는 a가 있다면 a의 phi(n)제곱도 모두 만족한다.
            - a^m  = 1 (mod n) 을 만족하는 m 생성
            - 여러개의 m이 존재할 수 있음. 가능한 작은 m의 값을 mod n상에서 a의 order라고 함.
            - if m이 phi와 같다면 primitive root라고 한다.
        - Diffie-Hellman
            - 최초의 공개키 형태
            - 단순히 키 교환을 위한 알고리즘. 암호화를 위한게 아님.
            - 중간자가 모르도록 키 교환하는것이 목적
            - Discrete Logarithm 문제에 기반.
                - g, p가 주어지고, g^k mod p가 주어질 때, k를 찾아라.
            - 과정
                - p, g는 사전에 서로 공유.
                - g^a mod p 값을 전송
                - g^b mod p 값을 전송
                - 서로 g^(ab) mod p 생성
            - 안전한가?
                - (g^a mod p)(g^b mod p)를 해도 g^(a+b) mod p 라서 못구함
                - (g^a mod p) 에서 a 를 추출할수도 없음. b도 마찬가지.
                - 스니핑으로는 알아내기 무척 어려움.
                - 그러나 MITM 공격에는 취약함. (= 많은 프로토콜이 취약하긴 함.)
                    - 어떤 방식으로든 인증 기능을 추가해야함.
        - Elliptic Curve Crypto (ECC:타원곡선암호)
            - 타원곡선을 기반으로 하는 암호
            - 성능이 좋다.
                - 동일한 안전성을 보장하면서 더 빠르게 연산할 수 있다.
        - 공개키 표기법
            - encrypt : with alice's public key  : {M}Alice
            - sign    : with alice's private key : [M]Alice
            - {[M]Alice}Alice = M
            - [{M}Alice]Alice = M

13. 공개키는 대칭키와 어떻게 다른가?
    - 대칭키는 confidentiality를 제공하고, mac을 통해 Integrity도 보장함.
    - 공개키는 confidentiality를 제공하고, sign을 통해 인증과 Integrity를 보장함.
    - 공개키는 대칭키와 다르게 전자서명이라는 것을 제공함.
        - 이는 부인방지(non-repudiation)를 제공함.
    - 공개키는 사전에 안전한 키를 공유할 필요가 없음.
    - 대신 대칭키는 속도가 무척 빠름.

14. confidentiality와 non-repudiation을 동시에 제공하기 위한 방법.
    - M에 선 서명, 후 암호화 ( {[M]Alice}Bob )
        - Alice의 서명이 되어있으므로, 마치 다른사람에게 보내려던것처럼 꾸밀 수 있음.(러브레터 빗겨치기)
        - {[M]Alice}Charlie
    - M에 선 암호화, 후 서명 ( [{M}Bob]Alice )
        - alice 서명을 수정 할 수 있으므로, 수신자(서명자)를 변조할 수 있음.(논문 가로채기)
        - [{M}Bob]Charlie
    - 둘 다 문제가 있음!
        - 그래도 일반적으로 선 서명 후 암호화.
        - 무엇이 더 좋다기 보다는 서명의 의미가 퇴색되지 않도록 하기 위함.

15. Certificate Authority (CA)
    - 인증서를 발급하는 제 3기관
    - trusted 3rd party (TTP) 기관이라고 불림.
    - CA가 공격자에게 넘어가면 문제가 생김. 그러므로 꼭 잘 관리되어야 한다.
    - 인증서 표준 : X.509
    
16. Public Key Infrastructure (PKI)
    - 공개키를 사용하기 위한 인프라
    - ROOT CA, CA 전자서명 공개키 관리
    - 폐기된 인증서 관리
        - CRLs (Certificate revocation)
            - CA에서 주기적으로 폐기된 인증서 알림.
        - OCSP
            - 온라인에서 실시간으로 폐기된 인증서인지 체크.
    - PKI 구조
        - Monopoly model
            - 가장 심플한 형태
            - 전 세계에 ca 하나만 존재. 모두가 ca 하나만 알고있음.
            - 그러나 독점 문제, 만일의 해킹공격 문제.
            - 위험부담이 큼
        - Oligarchy
            - 여러개의 ca를 둠. 국가별, 지역별 등
            - 브라우저에서도 여러개의 ca 인증서를 관리
            - ca가 많으면 다른 ca의 인증서를 가져오면 신뢰 불가능한 문제 발생
            - ca끼리 인증서 공유하기도 함.
        - Anarchy model
            - 별도의 ca가 없음
            - 각자가 ca가 됨.
            - 인증서가 사용자 서로서로 연결되어있음.
            - web of trust라고 불림. PGP에서 많이 사용한다고 함.

17. Hash function
    - 아무리 긴 input이 들어와도 고정된 길이의 output을 보장함.
    - 전자서명에 사용되기도 함.
        - 데이터를 해싱 후 이 해시값을 전자서명.
            - 데이터의 길이가 어떻든 전자서명은 짧음.
    - 성격
        - compression (압축)
            - 고정된 길이의 결과를 반환한다.
        - efficiency (효율)
            - 빠르게 계산 되어야 한다.
        - one-way
            - 단방향으로만 연산이 가능하다.
        - weak collision resistance
            - x와 h(x)가 주어질 때, h(y)=h(x)를 찾음
        - strong collision resistance
            - 아무 x, y에 대해서 h(x)=h(y)를 찾음.
            - 공격자 입장에서 가장 쉬운 방법.
            - 이것이 보장된다면 weak 보다 더 안전함.
    - 종류
        - md5
            - rivest가 발명
            - 128bit output
            - 최근에는 충돌이 잘 발견되어 사용되지 않음.
        - sha-1
            - 미국 정부 표쥰
            - 160bit output
            - 최근에는 취약성이 발견되어 잘 안씀.
        - sha-2
            - sha-256, sha-512를 주로 사용함.
            - 숫자는 output의 길이를 뜻함.
    - avalanche effect
        - 눈덩이 효과.
        - 좋은 hash 함수를 만들기 위한 방법
        - input의 1bit만 바뀌어도 결과가 많이 바뀌는 것.
        - 다 바뀌는건 오히려 좋은게 아님. 반정도가 적당

18. HMAC
    - Hashed MAC
    - 메세지의 Integrity를 보장하기 위함.
    - 일반적으로 사용하게되면 문제가 발생함. 이를 방지하기 위해 표준이 제정됨. RFC 2104
    - RFC 2104  =>  ipad(0x36 rep)와 opad(0x5C rep)를 이용하여 xor 연산 추가

19. hash 활용도
    - Authentication (hmac)
    - message Integrity (hmac)
    - message fingerprint
    - data 오류 검출
    - 효율적인 전자서명
    - 블록체인(mining)

------------------ 중간고사 끝 -------------------------
:8주차
1. 전자서명
    - 데이터 저장하거나 전송할 때 변조되지 않도록, MAC이나 HMAC을 통해 메세지에 대한 무결성을 증명.
    - 인증에 대한 내용이 들어가있다

2. 전자서명 알고리즘
    - DSA(Digital Signature Algorithm)
        - 이산대수문제를 기반으로 한다.
        - elgamal 스키마와 schnorr 스키마를 기반으로 한다
        - 전자서명 전용 알고리즘. 암호화나 키교환은 없음.
        - 개인키 =  0 < x < q
        - 공개키 = g^(x) mod p
        - k : 전자서명 생성할 때마다 생성되는 key
            - 0 < k < q
        - r = (공개키 mod q)
        - s = [k^(-1)(H(m) + xr)] mod q
        - signaure = (r,s)

3. secret sharing
    - 해적에게 쫒기고 있는 해적들. 몰빵하면 배신할 수도 있으니 보물지도를 쪼개서 흩어지고 나중에 만나자고 하는데, 한명이라도 안오면 보물지도를 복원하지 못하는 상황이 생김. 이러한 문제를 말함.
    - shamir's secret sharing
        - y축의 한 점(데이터)을 지나는 직선을 그었을 때, 그 직선상의 점들을 나누어 가짐. 한개만 가지고서는 가능한 직선이 무한대이므로 데이터를 찾을 수 없지만 한명이라도 모이면 가능.
    - key escrow에 사용되기도 함.
        - 신뢰할 수 있는 기관에 데이터를 넘기더라도 독점의 가능성이 있기에 이를 분할하는 것.

4. random numbers
    - 보안에서의 난수는 통계적인 난수 성격을 만족함과 동시에 예측불가(unpredictable)해야한다.
    - 난수에 문제가 있으면 아무리 좋은 보안시스템을 구축해도 거기서부터 주르륵 무너져내린다
    - 현실의 랜덤한 요소를 seed로 동작하는 방식도 있긴 하다.

5. information hiding
    - 크게 두개로 나뉨
    - watermark
        - 저작물, 배포 권한과 관련된 소유자 정보 기입
        - visiblie한 경우가 있음. ex) topsecret, stock image, ...
        - invisible
            - robust : 데이터가 변해도 잘 깨지지 않음.
            - fragile : 공격자가 한 비트라도 바뀌면 워터마크가 쉽게 깨짐
    - steganography
        - 메세지를 숨김

6. access control
    - authentication : 인증
        - 인증하는 방법 3가지 분류
            - knowledge factors : 알고있는 것(something you know)
                - 안전하다고 하기는 어렵다.
                - 그러나 다른 보안 체계에 비해 비용이 저렴함
                - 변경도 쉬움.
                - ex) password
            - ownership factors : 가지고 있는 것(something you have)
                - 신분증, 면허증, 운전면허증 등
            - inherence factors : 신체 일부(something you are)
                - 지문, 손모양, 얼굴, 홍채, 목소리 등
                - 직관적인 인증이 가능함.
                - password에 비해서 보안상 안전함.
                - 그러나 비용이 높음
                - 좋은 생체정보란?
                    - universal : 모든 사람이 공통으로 가지고 있는 생체정보
                    - distinguishing : 모든 사람이 다 다른 값을 가지고 있는 정보
                    - permanent : 오랜 시간이 지나도 잘 변하지 않는 정보
                    - collectable : 인증을 위해 생체정보를 수집할 때, 그 과정이 간단하고 거부감 없어야 함.
                - 생체 정보 과정
                    - enrollment phase : 등록과정. 생체정보를 수집해서 db에 올리는 것.
                        - 느려도 상관없고, 여러번 해도 상관없다.
                        - 최초에만 하기 때문.
                    - recognition phase : 인식과정. 인증을 위해 확인하는 과정
                - 좋은 인증 시스템?
                    - fraud rate : 그 사람이 아닌데 맞다고 인증
                    - insult rate : 그 사람이 맞는데 아니라고 거부
                    - 일반적으로 두 상황은 반비례함. 한쪽을 높이면 한쪽이 낮아짐.
                    - 매칭되는 기준점에 따라서 달라지는 건데, 생체인식의 경우 같은 사람도 인증할 때 마다 달라질 수 있기때문에 어느정도 기준점을 낮추긴 해야함.
                    - equal error rate : fraud, insult의 정확도 차이.
        - 2-factor auth
            - 서로 다른 두가지 인증 패턴을 함께 사용.
                - ex) 인증서. 인증서 파일(have) + 인증서 비번(know)
        - single sign-on(SSO)
            - 토큰을 이용해 하나의 인프라 내에서 한번의 로그인으로 다른 서비스도 함께 로그인없이 사용
        - OAuth
            - 인가를 위한 프로토콜이긴 함.
            - 한 서비스(구글 네이버 카톡 등)에 로그인 되어있으면 다른 서비스들에 회원가입없이 바로 서비스 이용 가능.
(11주차)
    - authorization : 인가
        - 인가 처리 방법
            - objects : 접근하려는 리소스. 파일, 프린터, 네트워크 등
            - subjects : object 들에 대해서 사용하고자 하는 주체
            - access control matrix : 각 object, subject에 대해 표를 만들어서 권한 관리(rwx)
            - access control matrix가 점점 커진다는 문제가 있음.
            1) ACL(access control lists)  
                - 위 문제에 대한 방안으로 등장한게 ACL.
                - matrix를 column단위로 자름.
                - 각 리소스(object)에 권한값을 저장해서 관리.
            2) Capabilities
                - matrix를 row단위로 자름.
                - 각 어플리케이션(subjects)에 대해 필요한 리소스(objects) 권한값을 저장해서 관리
            - confused deputy
                - a는 파일에 접근권한이 없지만 b를 실행할 수 있다.
                - b는 파일에 접근권한이 있다.
                - a는 b를 통해 파일에 접근할 수 있게되는 문제 발생
                - 권한 위임을 통해 해결 가능. a가 b를 실행할 때 b는 a의 권한을 위임받아 실행됨.
            - ACL vs Capabilities 선택
                - ACL
                    - object(리소스)가 시스템에 아주 많고, 변화가 심한 경우.
                    - subject 수가 적고 변동이 적은 경우.
                    - ex) 파일시스템
                - Capabilities
                    - 반대로 object가 적고, subject가 많고 변동이 심한 경우.
                    - ex) 안드로이드

7. covert Channel
    - 커뮤니케이션이 가능한 여러 채널이 있는데, 이를 비정상적으로 이용하는 것을 말함.
    - 생성 조건
        1. sender, receiver가 공유하고 있는 리소스가 있어야함
        2. sender는 이 리소스를 변경할 수 있고, receiver는 이 리소스를 관찰할 수 있어야함.
        3. 동기화가 잘 되어있어야 타이밍에 맞추어 공유할 수 있어야 함.
    - 방지하는 방법
        - 리소스 채널을 다 없앤다. ㅋ
        - 현실적으로 매우 어려움.
    
8. Inference control(추론 제어)
    - 데이터가 많아진다 == 위험도가 높아진다.
    1) 중요한 정보를 특정할 수 없도록 질의 쿼리에 대한 응답을 설정해야한다.
    2) N-respondent, k% dominance rule
        - 특별하게 튀는 값을 가진 데이터는 평균 데이터에 영향을 미침. 추론이 가능
        - 이러한 것들을 배제.
    3) randomization
        - 랜덤하게 노이즈를 섞어줌.

    - 완벽하게 Inference를 control하는게 어려움. 그래도 안하는것보다는 낫다.
        - 암호와는 상반됨. 암호는 약하면 안하는게 낫지만 inference는 조금이라도 하는게 낫다.


9. turing test
    - 사람이라고 판단하는 기준점.
    - captcha는 튜링테스트를 활용하는 방법.

10. CAPTCHA
    - 접근자가 사람인지 봇인지 구별용도.
    - 일종의 접근 제어(access control).
    - Completely Automated Public Turing test to tell Computers and Humans Apart의 약자
        - Automated : 자동으로 문제가 출제됨.
        - Public : 동작 방식은 공개됨.
        - Turing test : 튜링 테스트와 같은 맥락.
    
(12주차)
네트워크에서의 접근제어.

11. Firewalls
    - 내부 네트워크와 인터넷 사이에 DMZ라는 영역을 구성함.
    - 외부에서 내부로 접근하는 패킷에 대해서 조건을 만족하는 것만 통과시킴.
    - 종류
        - packet filter : network layer에서 돌아감
            - 장점 : 속도가 빠름
            - 단점 : 상위 레이어 데이터를 분석하지 않으므로 깊이있는 분석 어려움.
            - 기본적으로 모두 deny로 막고, 필요한것만 허용하는 whitelist 방식을 선호함. 예상치 못한 공격을 막을 수 있기 때문.
        - stateful packet filter : transport layer에서 돌아감
            - 장점 : packet filter에 비해 tcp 기반 깊은 분석이 가능하다
            - 단점 : packet filter에 비해 속도가 느림. 여전히 상위레이어 분석 불가
        - application proxy : application layer에서 돌아감.
            - 모든 layer 정보를 볼 수 있음.
            - 기존 패킷을 그대로 전달하는게 아니라, 검사 후 기존 패킷과 동일한 의미를 가지는 다른 패킷을 생성하여 보냄. 이 부분에서 proxy라는 의미를 가짐.
            - 장점 : 모든 layer를 검사할 수 있다. 풍부하게 여러 공격을 막을 수 있다.
            - 단점 : 성능. 느림.
        - personal firewall : 기기로 존재하는게 아니라 pc에 탑재되는 형태

12. TCP ACK Scan
    - 서버 포트 스캔 공격.
    - network layer에서 동작하는 packet filter의 단점이 드러나는 공격방식

13. Firewalk
    - 포트스캔 tool.

14. 네트워크 구조상 방화벽 설치
    - 인터넷에 물려있는 네트워크에는 packet filter를 두어서 속도 저하를 최소화.
    - 내부망에 물려있는 네트워크에는 application proxy를 두어서 조금 느리더라도 확실하게 검사.

15. IDS(Intrusion Detection Systems)
    - 네트워크를 가로막지 않고, 미러링을 통해 모니터링함.
    - 보안의 중요한 요점은 prevention(방어)다. 그러나 완벽할 수 없기 때문에 혹시모를 침임 시 빠른 조치가 가능하도록 이를 탐지할 수 있게 IDS를 사용.
    - 탐지방식에 따른 분류
        - signature based IDS
            - 유명한 공격의 특성. 예를 들면 패킷의 특정한 패턴을 탐지.
            - 그러나 공격자는 다양항 방법으로 우회할 수 있음.
            - 장점 : 많이 사용되는 방법. 간단함. 잘 알려진 공격 방어 용이.
            - 단점 : 시그니처 파일을 주기적으로 업데이트해주어야함. 새로운 패턴의 공격 탐지 어려움.
        - anomaly based IDS
            - 과거 행위 기반 비정상 행위 탐지 방식.
            - 정상/비정상 기준이 필요함.
            - 통계학적으로 접근하고 있으며, 인공지능도 접목되고 있음.
            - 장점 : 잘 알려져있지 않은 공격에 대해서도 탐지
            - 단점 : 아직까지는 신빙성이 높지 않음. 또한, 비정상행위가 어디가 문제인지 명시해주지 않아서 파악이 어려움
    - 구조상 분류
        - host based ids
            - 전체 네트워크가 아니라 내 pc와 같이 host의 프로세스와 리소스들을 감시.
        - network based ids
            - 관리하에 있는 네트워크를 감시

16. IPS(Intrusion Prevention Systems)
    - 네트워크 길목에 자리잡아서 차단을 하는 시스템

17. Protocol
    - 통신 규약.
    - 네트워크 프로토콜
        - HTTP, FTP, etc
    - 보안 프로토콜
        - SSL, IPSec, Kerberos, etc
    
    - 프로토콜은 민감해서 조금만 데이터가 바뀌어도 원래 의도와는 다르게 동작하기도 하고, 사용이 불가능할 수 있다.
    - 지금의 프로토콜들도 시간이 지남에 따라 취약성이 발견되고, 발전되어왔다.
    - 프로토콜에 문제가 없어도 구현방법에 따라 취약성이 발견될 수 있다.

    - 이상적인 보안 프로토콜의 조건
        - 연산이 적고 네트워크 자원을 적게 사용(효율)
        - 잘 깨지지 않는 프로토콜
        - 구현이 쉬울수록 좋음
        - 사실 이걸 모두 만족하기 어려움.
        - 특정한 환경, 제한사항에 맞춘 보안 프로토콜이 있다.
        - 내 환경에 맞추어서 적합한 프로토콜을 선택해야한다.
            - 한쪽만 인증하는것이 아닌 모두 인증해야하는 mutual authentication이 필요할 때가 생길수도 있다.
            - 익명을 보장해야하는 상황이 생길수도 있다.

    (13주차)

    - replay attack
        - 인증 프로토콜을 동작시킬 때 replay attack을 조심해야한다
        - 내용을 보지 못하더라도, 재사용을 통해 취약성 발생가능.
        - challenge-response 방식으로 예방할 수 있음.
            - 연결때마다 다른 문제를 내서 재사용 불가능하게 함.
            - challenge-response를 구현하는 대표적인 방식은 nonce값을 받아 hash에 포함시키는 형태도 가능.
    
    - 대칭키를 이용한 인증
        - Alice와 Bob은 K(AB)라는 키를 공유하고 있음.
        - 이 둘은 서로를 인증하고 싶다!
        - 서로만이 알고있는 K(AB)를 이용해서 인증할 수 있다.
        - 이러한 프로토콜에서는 서로를 인증하는 부분에 집중해야하지만서도, K(AB)가 3자에게 노출되었을 때, REPLAY ATTACK을 진행할 때를 고려해야한다.
        
        - 앞서 hash를 이용했던 자리에 Encrypt 과정이 들어가면 된다. 그러나 이 방식은 Alice가 bob에게 본인임을 인증하는 것이다. 반대로 bob도 alice에게 본인임을 인증해야한다. 이렇게 상호인증하는 것을 mutual authentication 이라고 한다.
    
    - 공개키를 이용한 인증
        - {M}Alice : Alice의 공개키로 암호화
    
    - 전자서명을 이용한 인증
        - [M]Alice : Alice의 개인키로 서명
    
    - 인증 프로토콜을 악용해서 의도치 않은 메세지의 암호화나 전자서명이 생성되는 문제가 있음. 추천하는 방법은 사용 용도에 맞춰서 공개키를 따로따로 사용하는 것.


    - session key
        - session : 두 client가 서로 통신하기 위해 connection을 맺는 수단.
        - 이러한 session 내에서 데이터의 기밀성이나 무결성을 보증하기 위해 사용되는 key
        - session key를 따로 쓰는 이유는 혹시나 key가 노출이 되는 경우에도 안전하기 위함.
        - 보통 대칭키의 형태로 만들어져 사용됨.
            - 일전에 언급했던 공개키와 대칭키를 합한 hybrid 방식. 보통 인증 과정에는 공개키, 인증 이후 실제 통신은 대칭키. 
            - 실제 세션 키 자체는 데이터를 송수신할 때 사용하니까 속도가 빠른 대칭키를 이용하는 것.
    
    - 인증이 끝나고 서로 안전하게 통신하는(세션키를 공유하는) 프로토콜을 생각해보자.
        - 생성된 session key가 노출되지 않도록 설계하는게 중요.
        - 공개키를 이용한 경우
            - 표준적으로 사용됨.
            - 세션 키를 포함해서 서로 인증함.
            - Alice(좌)가 누구인지는 인증이 가능하나, bob(우)에 대한 인증은 이루어지지 않음. (상호인증 안됨)
        - 전자서명을 이용한 경우
            - 서로가 서로임을 인증할 수 있음.
            - 3자가 쉽게 공개키로 복화할 수 있기 때문에 session key가 노출됨.

        - 상호인증(mutual authentication)과 안전한 session key 교환을 위해 공개키 암호와 전자서명을 함께 진행할 수 있음.
            - 선 서명 후 암호화
                - session key와 nonce 데이터를 전자서명을 하여 사용자를 보증하고, 이를 공개키로 암호화하여 세션 키 유출을 방지할 수 있다
                - 그러나 공개키와 전자서명 방식을 합친다고 해도 MITM공격이 가능하다.
            - 선 암호화 후 서명
                - MITM을 방지할 수 있음.
                - 쓸만한 좋은 프로토콜
            - 이처럼 암호화와 서명의 순서만으로도 프로토콜의 안정성이 달라짐. 민감하다고 표현할 수 있음.


    - timestamps
        - 기존의 nonce를 대체할 수 있음. 게다가 통신 횟수를 3에서 2번으로 줄일 수 있음. nonce가 아니라 timestamp이기 때문에 서로 알고있기 때문.
        - nonce의 기능뿐만 아니라 timestamp의 기능도 얻을 수 있음.
        - 그러나 두 객체의 싱크가 잘 맞아야 함.
            - 통신 지연시간도 존재하고, 처리속도도 존재해서 당연하게도 오차가 발생할 수밖에 없음.
            - 얼만큼의 오차를 허용할 것인지 설정하는게 중요함.
            - 오차 범위가 너무 작으면 일반 사용자도 통신이 안될 수 있고, 반대로 크면 공격을 막을 수 없음.
     
        - 구현
            - 공개키 암호화와 전자서명을 이용.
            - 선 서명 후 암호화
                - 무려 MITM 방지가 됨.
                - 쓸만한 좋은 프로토콜
            - 선 암호화 후 서명
                - 공격이 가능해짐. MITM으로 응답에 있는 key를 획득할 수 있음.
                    - 응답에서 key 데이터를 빼서 보완할 수 있음.(이미 최초에 k를 보내기 때문에 공유된 상태로 볼 수 있기 때문)
            - 다시한번 알 수 있는건 보안 프로토콜이 예민하다는 것!

    - Perfect Forward Secrecy (PFS)
        - 과거에는 key를 구하지 못해 해독이 불가능하지만 데이터를 모두 수집해놓았다고 하자.
        - 나중에 보안사고가 발생하거나 어떠한 이유로 복호화가 가능해진다면 결국에는 알 수 있다.
        - 이런 상황을 방지하기 위한것이 PFS.
        - key로 직접 암호화하지 않는다. 휘발성 Key를 사용하는데, 이를 session key를 사용한다.
        - 그러나 문제가 있음. 결국에 session key를 생성하는것도 결국에는 key를 이용해서 교환해야하는데, 그렇다면 나중에 session key 또한 알게되는 것 아닌가?
        - 이 문제를 어떻게 해결해야하는가?
            - Diffie-Hellman 키 교환을 이용해서 session key 교환을 할 수 있다.
                - g^a mod p, g^b mod p
            - diffie-hellman 특성상 인증 과정이 없어서 MITM에 취약하다. 그렇기 때문에 이 부분을 고려하면서 프로토콜을 짜야한다.
                - E(g^a mod p, Key_AB), E(g^b mod p, Key_AB), session key = g^(ab) mod p
        - 이렇게 diffie-hellman 방식을 이용하여 휘발성 키를 만드는 것을 ephemeral diffie-hellman 키 교환이라고 함.

    - 앞서 설명한 프로토콜을 다 합쳐보자
        - 기능
            - 상호인증(Mutual authentication) 가능하며
            - 인증 이후 통신을 위한 session key를 사용하며
            - PFS로 미래 키 유출에도 대비 가능한 프로토콜!
        - 로직
            - Alice  ->  ("I'm Alice", R_A)  ->   Bob
            - Alice  <-  R_B, [{R_A, g^b mod p}Alice]Bob   ->   Bob
            - Alice  ->  [{R_B, g^a mod p}Bob]Alice  ->  Bob
        - 실제로 이런 형태를 기본적으로 이용하는 프로토콜이 많음.

    - 인증 프로토콜로 TCP를 쓰자! 라는 주장.
        - TCP로 서로의 IP를 알 수 있고, 3 Way handshake로 신뢰성 있는 연결하기 때문! 이라는 주장.
        - 그러나 IP는 쉽게 변조가 가능해서 말이 안되는 소리.
        - 근데 실제로 IP로 인증하는 프로토콜이 옛날에 있긴 했다고 함.
            - 문제가 되어서 수정됨.
        - 즉, 상대방에 대한 인증을 수행할 때 IP로 하면 안되고, 앞에서 배웠던 대칭키, 공개키 패스워드 이런걸 기반으로하는 인증 프로토콜을 개발해야한다.

(14주차)

18. Zero Knowledge Proof (ZKP)
    - 본인이 기밀을 알고 있다는 것을 증명하려고 하는 상황. 그러나 기밀에 대한 정보는 드러내지 않고 싶은 상황.
    - Alice가 주장하는 것을 Bob이 내용을 모르는 상태에서 이를 확인하려면 어떻게 해야하는가?
    - 어려운 문제임
    - 확률적 접근으로 증명함. N%의 확률로 알고있다!
    - 두 노드간 대화를 통해 이를 증명함.
        - Interactive 한 증명 시스템.
        - 보안 프로토콜의 형태를 따른다.
        - 그래서 기술 증명으로 분류되기도 하고, 프로토콜로 분류되기도 함.
    -  Bob's Cave
        - alice가 주문을 알고있다면 bob이 왼쪽, 오른쪽으로 나와라! 라고하면 그냥 나오거나 주문으로 문을 열고 반대쪽으로 나오거나를 할 수 있을 것이다.
        - bob의 명령에 잘 따른다면 가지고 있을 확률이 높고, 잘 못따른다면 확률이 낮다는 의미이다.

    - ZKP에 관한 프로토콜
        - Fiat-Shamir Protocol
            - 제곱근을 활용. modulo N 상에서의 제곱근을 구하는 문제는 무척 어렵다.
            - N = p * q
            - Alice는 secret한 S를 가지고 있음
            - v = S^2 mod N
            - v는 public, S는 secret
            - 과정
                1. Alice는 random한 r 생성.
                2. x = r^2 mod N
                3. (commits) x를 bob에게 보냄
                4. (challenge) bob은 random한 e(0 또는 1)를 보냄. 이는 엘리스에게 명령한것과 같음.
                5. alice는 y 계산. y = r*S^e mod N
                6. (responds) y를 bob에게 전송.
                7. bob는 y를 통해 alice가 S를 알고있는게 맞는지 확인.
                    - e가 1인 경우
                        - y^2 = r^2 * S^(2e) = r^2 * (S^2)^e mod N
                        - v가 S^2 mod N 이고, x가  r^2 mod N 이므로 y^2 = x * v^e mod N
                        - bob은 처음에 alice로부터 x값을 받았기 때문에 알고있고, v는 공개키라서 알고있고, e는 bob이 직접 생성한 값이므로 알고있다. 따라서 x * v^e를 계산할 수 있음.
                    - e가 0인 경우
                        - y^2 = r^2 mod N = x mod N
            - 이러한 과정을 매번 새로운 r과 함께 여러번 반복.
            - 영지식 명지식 명제식,,,?
            - Trudy가 공격할 수 있는가?
                - e=0이라면 r값만 보내주면 되니까 공격할 수 있음!
                - e=1이라면 y값을 보내야함. 그러나 y^2은 알 수 있어도 S를 알지 못하는 한 y는 알 수 없음.
                    - 그러나 교묘하게 이를 통과할 수 있음.
                        - trudy가 애초에 bob에게 x를 보낼 때 x = r^2 * v^(-1) mod N 으로 계산함.
                        - bob은 검증할 때 x * v^e 식으로 검증하는데, 이 때 e는 1이기 때문에 v는 x에 있던 modular inverse에 의해 사라짐. 즉, y^2 = r^2 이 되는 것.
                        - trudy는 조작한 x를 보내고 y^2 값으로 r^2를 보내면 됨.
                - 그렇다면 e=0도 가능하고 e=1도 가능하기 때문에 bob이 어떤 e를 보내는지만 알면 통과할 수 있음!
                - 그러나 문제는 선후관계인데, x를 조작해서 보냈는데 e=0이 오거나, x를 그대로 보냈는데 e=1이 오면 맞추지 못하는 것이다.
                - 결국 trudy가 문제를 맞출 확률은 1/2 이며, 이를 반복하면 1/(2^n)이 된다.
                - 당연하게도 e가 생성되는 로직은 간파당하면 안된다. 즉, trudy는 e 값을 예측할 수 없다.
                - 또한 alice는 매번 새로운 random한 r 값을 생성해야한다.
                    - e=0 일때의 r mod N이나, e=1 일때의 r * S mon N 값이 노출이 된다면 r * S 에서 r을 나눠서 S를 얻을 수 있기 때문.
    - ZKP를 왜 쓰는가?
        - 예를 들면 인증서 기반으로 인증을 하게되면 내가 ALICE라는걸 잘 인증받을 수 있음
        - 그러나 인증을 하면 "내가 ALICE야!" 라는것을 알려주는 것임.
        - 여기서 익명성을 보장하고 싶다면 ZKP를 사용하는 것임.

19. SSH
    - secure tunnel 생성
    - 인증을 하는 부분이 꼭 필요함. 인증 방식은 여러가지가 있음
    - certificate(인증서)를 이용하는 SSH 방식에 대해서 알아보자.
        1. [Alice -> Bob] Alice, CP, R_A
            - CP : Alice가 사용할 수 있는 암호 알고리즘 리스트
        2. [Bob -> Alice] CS, R_B
            - CS : CP 중에서 Bob도 사용 가능한 암호 중 선택한 암호 알고리즘
        3. [Alice -> Bob] g^a mod p
            - 디피헬만 키교환
        4. [Bob -> Alice] g^b mod p, certificate_B, S_B
            - S_B : H에 전자서명을 한 [H]Bob 값.
            - H : Hash(Alice, Bob, CP, CS, R_A, R_B, g^a mod p, g^b mod p, g^(ab) mod p)
        5. [Alice -> Bob] E(Alice, certificate_A, S_A, K)
            - S_A : [H, Alice, certificate_A]Alice
            - K : g^ab mod p : key 생성
    
    - MITM에도 안전! H_A, H_B가 다른 값을 Hashing 하기 때문.

20. SSL & TLS
    - Socket layer
        - application layer와 transport layer 사이에 삽입해서 동작하는 layer.
        - 이러한 layer을 동작시키는 프로토콜은 SSL/TLS 라고 한다.
    
    - What is SSL?
        - 인터넷에서 많은 행위가 일어나니 도청만 해도 많은 정보를 알 수가 있었음.
        - 사용자들은 지금 접속한 홈페이지가 피싱사이트인지 알 필요가 있었음. 
        - 즉, 서버에 대한 인증에 초점이 맞추어져 있었음.
    
    - 간단한 SSL 비슷한 프로토콜
        1. [Alice -> Bob] Hi~
        2. [Bob -> Alice] certificate_B
        3. [Alice -> Bob] {K_AB}Bob
        - 위와 같은 형태라고 볼 수 있다. 다만 지금같은 경우는 bob이 최종적으로 잘 풀었는지에 대한 내용이 없기 때문에 bob을 인증할 수 없다. 실제로는 더 복잡한 형태로 동작.
    
    - Simplified SSL Protocol
        - S는 pre-master secret 데이터
        - K = h(S, R_A, R_B)

        1. [Alice -> Bob] Hi~, cipher list, R_A
        2. [Bob -> Alice] certificate, cipher, R_B
        3. [Alice -> Bob] {S}Bob, E(h(msgs, CLNT, K), K)
        4. [Bob -> Alice] h(msgs, CLNT, K)
        5. K에 의해 안전한 데이터 송수신.
            - 실제로는 K를 바로 쓰는게 아니라 6가지로 나누어서 사용한다.
                - 2 암호화 KEY
                - 2 무결설 KEY. ex, MAC
                - 2 send and receive KEY
        
        - 기존 방식은 서버의 인증서를 받아서 인증함. 반대로 클라이언트를 인증하기 위해서 인증서를 요구하는 방법을 사용하기도 하는데, 일반적으로 사용자가 이런인증서를 가지고있지 않아서 잘 쓰이지는 않음.
        - 그러나 서버가 클라이언트를 인증할 필요가 있긴 함. 이럴때는 웹상에서 로그인같은 기능을 사용하면 됨.

    - SSL은 MITM에 취약한가?
        - 안전함. 인증서가 활용되기 때문.
        - 단, 인증서가 올바른 경우에만 안전.

    - SSL session과 connection
        - 안전하게 K를 주고받으면 안전한 session이 생겼다고 볼 수 있다.
        - 문제가 있는데, HTTP의 경우 요청이 여러번 발생하는데, 매 요청(connection)마다 SSL session을 맺는것은 너무 리소스가 크다. (공개키 연산)
        - 이를 해결하기 위해 session과 connection이라는 개념을 확립함.
        - 하나의 session을 만들면 그 다음부터 connection이 이루어지면 기존 session을 이용.

    - TLS 기능 특징
        - 서버인증(때에 따라 상호인증), 데이터에 대한 기밀성, MAC을 이용한 무결성.
        - application layer와 transport layer 사이에서 동작한다. 이 말인 즉슨 transport까지는 os에서 동작시키지만 tls부터는 application단에서 사용할지 안할지 애플리케이션마다 다르게 설정할 수 있다.
            - 이 부분이 IPSec과의 큰 차이점임.

21. Kerberos
    - 어원은 그리스 신화에서 지옥문을 지키는 머리 세개 달린 개의 이름.
    - 실제 커베로스 프로토콜도 동작할 때 3가지의 entity가 유기적으로 동작함.
    - 대칭키를 이용해서 인증하는 시스템.
    - TTP(Trusted third party)가 존재한다고 가정하고 동작함. 남들이 다 신뢰할 수 있는 기관을 말함.
    - 왜 만들어졌는가? 대칭키를 이용해서 인증을 해보려고 했는데, 키 고유의 문제가 있어서 이를 해결하기 위해 만들어짐 
        - N명의 사용자를 서로 인증하는 상황에서는 N^2. 정확히는 (N(N-1))/2 수준의 키가 필요함. 확장성에 문제가 있음. 이를 N 수준으로 성능을 향상시키고자 함.
    - KDC (Key Distribution Center)
        - TTP의 역할을 함.
        - 전체 사용자가 신뢰할 수 있는 중앙서버
    - client는 서버 가기 전에 KDC에 가서 client가 alice임을 인증함. 그러면 KDC는 인증 TGT를 발급해주고 CLIENT는 이걸 들고 서버에 접근 가능.
    - Kerberos Tickets
        - KDC가 발급해주는 인증 결과. 티켓.
        - Ticket-granting ticket (TGT)도 발급.
        - ticket은 단일 접근 용도, TGT는 자유이용권.
        - TGT가 가지고 있는 정보
            - session key
            - user id
            - 만료시간
        - TGT는 K_KDC로 암호화 되어있음.
            - E("Alice" || Session_A, K_KDC)
            - TGT를 발급받아도 내용은 알 수 없음.
    - 과정
        - KDC 인증 과정
            - [Alice -> KDC] Request TGT
                - TGT를 요청.
            - [KDC -> Alice] E(S_A || TGT, K_A)
                - A의 KEY로 세션과 TGT데이터 암호화.
                - A는 세션과 TGT를 얻을 수 있음 
                - TGT = E("Alice" || S_A, K_KDC)
                - TGT 내부 정보는 알 수 없음.
        - 목표 NODE 접근과정
            - [Alice -> KDC] I want to talk to Bob!, REQUEST
                - bob에 대한 접근 필요함을 알림
                - REQUEST = (TGT, authenticator)
                - authenticator = E(timestamp, S_A)
            - [KDC -> Alice] Reply
                - E("Bob" || K_AB || ticket to Bob, S_A)
                - ticket to Bob = E("Alice" || K_AB, K_B)
            - [Alice -> Bob] ticket to Bob, authenticator
                - authenticator = E(timestamp, K_AB)
    - 특징
        - S_A라고 하는 Session key는 인증이 된 alice가 돌아다니면서 새로운 티켓을 발급받을 때 사용.
        - K_AB는 Alice와 Bob간에 실질적인 데이터 전송시에 사용.
        - Nonce가 아니라 timestamp 방식을 사용함. 그래서 인증에 소요되는 메세지 수를 줄일 수 있다는 장점이 있음. 또한 replay 공격을 어느정도 방어할 수 있음. 그러나 time 기반이기 때문에 오차 허용범위 내에서 문제가 발생할 수 있음. 
    
        - Alice가 Bob에 접근할 때, Bob의 입장에서 Alice임을 인증하는건 됨. 그러나 trudy가 지켜볼 때, 접근자가 alice인지 알 수 없음. 즉, alice의 익명성이 보장이 됨.

    - KDC에서 모든 SESSION KEY나 TGT를 가지고 있지 않는 이유.
        - stateless한 성격을 띄도록 하고싶기 때문. 즉, 서버가 잠시 다운되거나 그래도 모든 client로 다시 발급받는게 아니라, 기 발급된 것으로 계속 사용할 수 있도록 하는것!