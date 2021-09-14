1. introduction
    - what is internet?
        - nut and bolts 관점(구성품의 관점, 전지적 관점)
            - computing devices
                - 각 장치.
                - a.k.a. `host`
                - a.k.a. `end systems`

            - communication links
                - 각 장치를 연결.
                - transmission rate: bandwidth(대역폭)

            - packet switches
                - 패킷을 전송
                - router and switches
                    - 최근에는 기술에 발전에 의해 차이가 모호해져서 둘이 거의 같은 개념으로 사용.

            - 그냥 network가 아니라 inter(연결) network로, 여러 네트워크를 연결한다는 뜻에서 `network of networks` 라고 함.
            - 네트워크를 연결해주는 사업들이 있음. 이들이 인터넷 서비스를 제공해준다고 볼 수 있는데, 이들을 ISP(Internet Service Provider) 라고 부름
            - protocols
                - 메세지의 송수신을 control 하는 방식을 말함.
                - tcp, ssh, http 등이 있음.
            - internet standards
                - 통신에 표준이 필요함.
                - IETF : 인터넷 프로토콜을 표준화한 단체.
                - RFC : IETF에서 제정한 표준 문서.
        - service 관점(host 관점)
            - 어플리케이션을 서비스하기 위한, 데이터를 주고 받기위한 infra structure. 즉, 인터넷을 사용하기 위한 하부 구조로써 매우 기초적이고 눈에 보이지 않는 구조다.
    - What is protocol?
        - network entity 사이에 주고 받는 message의 format, order, action을 정의하는 것.
            - format: 형식
            - order: 순서
            - action: 행동
    - network edge (네트워크 가장자리)
        - nework 그룹은 크게 세 그룹으로 나누어 볼 수 있음
            - network edge
                - 작은 network에서 router를 제외한 hosts가 이에 해당됨.
                - end systems(hosts), access networks, links 가 존재할 수 있음.
                - server, client가 있고, server는 대부분 data center에 들어있음.
            - access network
                - network edge에 해당하는 여러 host들이 외부 network 연결을 위해 가장 먼저 접근하는 network의 router들이 이에 해당됨.
                - 일반적으로 우리가 생각하는 작은 단위의 네트워크와 같다고 생각하면 될듯.
                - edge router
                    - network edge에서 end system이 통신을 위해 만나는 첫번째 라우터를 말함.
                - keep in mind
                    - bandwidth(속도): (bps: bits per second)
                    - shard network or dedicated network?
            - network core
                - 네트워크에 걸쳐있는 router를 포함한 모든 네트워크 간 연결부를 말함.
    - access network 역사
        - dial-up modem(전화망)
            ![image](https://user-images.githubusercontent.com/44149738/132981901-80b1cc86-d610-4898-8f7d-0fe62de8083b.png)
            - 집에서 central office까지 연결하는데에 이 전화망을 사용함.
                - 집에서 dial-up modem을 사용하여 central office에 도달하고, 이후 인터넷에 접속하는 방식.
            - 56Kbps
            - can't surf and phone at same time. (여러 통신이 동시에 불가.)
            - not always on
        - Digital subscriber line(DSL)
            ![image](https://user-images.githubusercontent.com/44149738/132982032-1f2b4786-c51a-4c83-b2bb-7c7702d087d9.png)
            - 기존 전화망을 사용하되, central office 까지 도달하는 부분이 변경.
            - DSL modem이라는 장치를 통해 속도가 빨라짐.
            - upstream 2.5Mbps
            - downstream 24Mbps
            - 인터넷과 전화서비스를 동시에 지원할 수 있었음.
        - cable network(= cable modem)
            ![image](https://user-images.githubusercontent.com/44149738/132982047-f5bc71b5-da38-4b60-af35-0ec6ecde0ea9.png)
            - 동축선(두꺼움)을 이용.
            - 선으로 통신되는 부분을 채널별로 쪼개서 여러 종류의 데이터를 보낼 수 있도록 구성.
                - 채널을 쪼개는 방식은 다음과 같음
                    - FDM (Frequency Division Multiplexing)
                    - TDM (Time Division Multiplexing)
            - 각 가정이 shared cable(공유되는 케이블)을 이용
                - 집 안에서는 동축선(coax)
                - 각 가정이 공유하는 선은 광섬유(fiber)
                - 이렇게 두 종류의 선을 혼합하는 것을 HFC(Hybrid Fiber Coax)라고 함.
            - asymmetric
                - 데이터 송수신 방식이 비대칭적인 것을 말함.
                - 데이터를 올리는 것보다 다운 받는 경우가 많기 때문.
            - upstream 2Mbps
            - downstream 30Mbps
            - 여러명이 동시에 케이블을 사용할 수 있는 share access network임.
        - FTTH(Fiber To The Home)
            ![image](https://user-images.githubusercontent.com/44149738/132982254-cabfba1c-58f9-4da6-a79b-3bb581110899.png)
            - 제일 중요.
            - 광섬유가 central office에서 집까지 연결되는 방식.
                - 정확히는 OLT 에서 ONU까지
            - 가정에서 가장 많이 사용하는 방식.
            - 속도가 가장 좋다. 1Gbps.
        