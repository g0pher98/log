1. bitcoin
    - what is bitcoin?
        - 전자화폐 시스템(분산화된, 탈중앙화된 시스템)의 기반이 되는 개념과 기술들이 모여서 만든 플랫폼
        - 참여자들은 기존 화폐처럼 활용할 수 있음
            - 물건 구매/판매
            - 송금, 교환, 환전
        - 가상화폐/암호화폐
            - 암호화폐라는 말을 선호함. 가상화폐라는 말은 기존에 있던 포인트, 마일리지와 같은 개념이기 때문에 비트코인은 정확히는 암호화폐로써 차별화된 기술이라는 점이 중요.
            - 물리적/전자적 coin 개념은 사실 없음. 그래서 정확히 몇 비트코인이 있다! 이런 식의 개념이 없음.
                - 거래소에서 뜨는건?
                    - 정확히는 transaction(거래, tx)이 있고, 그 안에 함축적으로 표현되는 것임.
            - bitcoin의 소유권은 cryptographic key가 증명함.
            - bitcoin을 소비하기 위해서는 key를 이용한 전자서명을 생성해야 함.
            - key는 보통 wallet(지갑)에 저장해서 사용.
        - distributed, peer-to-peer(p2p) 시스템으로 구성되어있음.
            - 완전히 분산되어 별도의 중앙서버가 존재하지 않음.
                - 중앙서버의 상태에 따라 전체 생태계가 크게 영향받는다는 점을 해소
            - 신규 bitcoin은 mining이라 불리는 합의과정 중에 생성됨
                - 누구나 mining 과정에 참가할 수 있음
            - 모든 transaction은 blockchain을 통해 저장됨
        - 신규 bitcoin 발행
            - 중앙 서버가 없는데 누가 보상을 주나?
                - mining에 성공한 채굴자가 보상으로 새로 발행된 bitcoin을 획득.
            - 대략적으로 10분마다 하나씩 발행할 수 있도록 난이도 조절이 됨.
                - 노드가 적으면 적을 수록 쉬운 문제,
                - 많으면 많을수록 어려운 문제
            - 보상 규모는 대략 4년 주기로 보상이 반으로 줄어드는 반감기를 거침.
                - 점점 반으로 줄어드니 나중에는 보상이 거의 없어짐.
                    - 새로운 코인이 거의 발행되지 않기 때문에 안정적으로 운용됨.
                    - 2020년 보상 규모는, 채굴당 6.25 bitcoin
    - bitcoin 구성요소
        - bitcoin protocol
            - 여러 노드들이 분산된 p2p 네트워크를 구성해서 통신이 가능하도록 하는 프로토콜이 필요
        - blockchain
            - 공적인 거래장부(원장)
            - 누구나 열람할 수 있음
        - consensus rules
            - 트랜젝션이 올바른지, 올바르게 소유하고 있는지 검증하는 룰
        - proof-of-work (PoW)
            - 사용자들이 거래내역이 맞는지 일종의 합의를 끌어내기 위해 사용하는 알고리즘
    - 비트코인 이전의 가상화폐
        - 가상화폐가 되려면
            - 진짜인가? 위조인가? 발행하지 않았는데 가짜로 만든게 아닌가? 이를 검증할 수 있어야 함.
            - 물리적 화폐로는 불가능하지만, 논리적인 화폐는 동시간대에 결제를 하는 double spending 문제를 해결할 수 있어야 함.
            - 소유자가 A가 맞는지 검증할 수 있어야 함.
        - 기존 가상화폐
            - 중앙집중형 방식이었음
            - 중앙서버가 공격자의 주요 타겟이 되고 SPoF(single point of failure) 문제 발생
    - 캐릭터
        ![image](https://user-images.githubusercontent.com/44149738/132997872-acfd2692-feac-4d5c-badb-f3b1073a043a.png)
    - 지갑
        - 비트코인을 사용할 수 있도록 정보들을 저장하는 공간
        - 플랫폼에 따른 분류
            - desktop wallet
            - mobile wallet
            - web wallet
            - hardware wallet
            - paper wallet
        - 역할과 동작방식에 따른 분류
            - full-node client
                - 모든 transaction을 저장하고 검증하는 역할.
                - 적극적으로 비트코인 운영에 관여함.
                - full-node가 많아지면 비트코인이 더욱 견고해지지만, 상당한 리소스때문에 일반 사용자는 full-node가 되기 어려움.
            - lightweight client(SPV client)
                - transaction 정보를 얻기 위해서는 full-node에 연결해야함.
                - 지갑 사용자에 관련된 transaction 처리만 담당. 가벼움.
            - third-party API client
                - 직접적으로 연결하지 않고, third-party 시스템을 이용해 bitcoin에 연결
        - bitcoin core
            - bitcoin에 참여하는 노드가 되기 위한 방법.
            - 가장 대표적인 reference implementation
        - quick start
            - 지갑이 개인키/공개키를 생성하고, 공개키를 바탕으로 address 생성.
            - address는 다른 사람들과 공유
            - address가 생성되었다고 바로 비트코인에 등록되는 개념은 아니고 실제로 거래가 이루어져서 트랜젝션이 발생하면 그때 bitcoin system에 기록됨
        - bitcoin 획득 방법
            - 기존 사용자로부터 구매
            - 물건/서비스 판매를 통한 획득
            - ATM 기기를 이용한 구매
            - 거래소를 통한 구매
        - 송금
            1. 특정 address에 대해 btc 전달 요청
            2. wallet은 이 요청을 기반으로 transaction 생성 후 wallet 내 개인키를 통해 signing
            3. bitcoin network에 transaction 전파( < 1sec)
            4. 수신자는 몇초 후에 확인 가능
            - 그러나 이는 unconfirmed 상태임. (블록체인 네트워크에 기록되진 않았음.)
            - 10분마다 mining이 수행이 될 때, 트렌젝션이 블록에 추가가 되면 confirmed 상태가 됨.
            - 이제서야 수신자는 해당 비트코인에 대해 정상적인 소유자가 됨.

2. transactions
    - 구조
        - double-entry bookkeeping 과 비슷한 방식. 
        - input을 output의 형태로 가치를 변화시키는 것.
        - transaction 안에는 inputs(수입) 와 outputs(지출)에 대한 내용과 그 합계가 있다.
        - (outputs 합) - (inputs 합) = 수수료
        - input의 신뢰성을 판단하는 방법
            - 이전 트랜젝션에서 받은 output을 기반으로 input 형성
        - 잔돈은 잔돈이라고 명시하지는 않지만 다시 보내는 output을 형성함으로써 구현
            - 일반적으로 익명성을 위해 같은곳으로 잔돈을 받지 않음.
    - 올바른 input 구성하기
        - 주소를 이용한 검색으로 해당 주소에 output으로 들어온 트랜젝션을 탐색
        - output에 있지만 이후 input으로 사용된 트랜젝션은 이미 소진된 거래이기 때문에 제외.
        - full-node client
            - 모든 노드를 탐색
        - lightweight client
            - 모든 트랜젝션을 저장할수는 없으니 본인이 관심이 있는 항목에 대해서만 모아서 저장.
            - 만약 정보가 누락되거나 부족할 경우, 주변의 full node client에게 정보 요청
    - output 구성하기
        - 실제로는 스트립트를 만들어서 output 구성
        - 누군가 output을 사용하려고 할 때, 스크립트에 대한 솔루션을 제시해야지만 사용할 수 있음.
        
        
        
        

