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

2. access network
    - home network
        - 일반 가정집에서 사용하는 구조
        - NAT역할을 하는 공유기. 보통 유무선 공용임.
    - enterprise access networks(ethernet)
        - 회사나 대학과 같은 곳에서 주로 사용
        - ISP로부터 서비스받고, 이를 라우터로 시작해서 뿌리내리는 형태
        - 공유기와는 급이 다른 성능의 라우터를 사용. 10Gbps까지도 낼 수 있음
    - wireless access networks
        - 무선 통신. 활발히 사용되고 있음
        - 독점이 아닌 공유(shared) 형태의 통신임.
            - 전송속도가 사용자가 많아지면 느려짐.
        - wifi, 4G, 5G와 같은 통신을 통해 access point나 base station(기지국)과 같은 end system에 접근함.
        - 크게 두 가지로 나누어볼 수 있음
            - wireless lan
                - 무선랜, bluetooth
                - 30미터 미만의 빌딩 안과 같은 공간에서 사용
                - WiFi는 802.11b/g/n/a/ac 이라는 표준이 있음 : 11, 54, 450
                    - IEEE 라고 하는 표준화 "단체"
                        - 802 로 시작하는 표준화 "그룹"
                            - 인터넷 네트워크 프로토콜을 표준화 함.
                - 블루투스는 IEEE 802.15.1 WG(working group)에서 표준화 함.
            - wide-area wireless access
                - 3G, 4G:LTE, 5G

3. physical media (물리 매체)
    - physical link
        - 물리적인 통신 경로
        - 두 개로 나누어 볼 수 있음
            - guided media
                - 실제 물리적 통로
                - ex) 구리선 광섬유 동축선
            - unguided media
                - 물리적 통로 없이 전파
                - ex) 라디오

    - guided media 종류
        - twisted pair (TP)
            - guided media 케이블 중 하나
            - 랜선이 이 방식임.
            - 절연구리선을 꼬아놓음
                - 전자기장 간섭을 최소화하기 위함.

        - coaxial cable (동축선)
            - 두 개의 선이 있고, 양방향으로 주고받을 수 있음
            - 여러개의 채널을 하나의 케이블에 담아서 보낼 수 있을 때 사용
            - HFC(Hybrid Fiber and Coax) 방법으로 사용할 수도 있음
            
        - fiber optic cable (광섬유)
            - 유리섬유에 빛으로 비트를 표현
            - 오류가 거의 없음. -> 전자기장에 대한 간섭이 거의 없어서.
                - 즉, 높은 속도로 만들어도 괜찮음! -> 속도가 빠름!
            - 광섬유 특성상 급격히 꺾거나 나누기 어려움. point to point 특성을 가지고 있음.
                - 다른 곳으로 쪼개기 위해서는 splitter와 같은 장비를 이용해서 나눠야함.

    - unguided media 종류
        - radio
            - 전기신호를 흘림에 따라 자기장이 생성됨.
            - 이후 전기장과 자기장의 상호작용을 통해 마치 파동(wave)처럼 퍼져나가게 됨.
            - 선 연결이 필요 없다는 장점
            - 양방향 통신이 가능
            - 벽이나 장애물이 있으면 있으면 회절 및 굴절이 됨.
                - 벽 뒤의 수신자도 통신이 가능
                - 주파수가 올라갈수록 회절이 잘 안됨.
                    - 5G가 직선구간에서만 잘되는 이유도 이것에 해당
            - 종류
                - LAN(WiFi)
                    - AP
                    - 54, 300, 450Mbps
                - wide-area
                    - base station
                    - 4G : ~ 10Mbps
                - terrestrial microwave
                    - base station
                    - DMB 생각하면 됨. 그냥 이런게 있음.
                - satellite
                    - 지구 -> 위성 -> 다른지역 전송
                    - 거리가 멀어서 속도는 떨어짐
                        - end-end 딜레이가 많이 발생
                    - 돈이 많이 들게 됨.
                        - 여러명이 나눠서 써야함.
                            - bandwidth를 줄이고 그만큼 여러개를 만들어야함
                                - 100Mbps 10개 x
                                - 10Mbps 100개 o
                    - 위성의 종류
                        - geosynchronous
                            - 고정위성.
                            - 지구 자전과 같이 돌아서 정지해 있는 것처럼 보임
                            - 매우 높이 있어서 딜레이 큼
                        - low altitude
                            - 유동위성
                            - 비교적 높이가 낮아서 딜레이가 상대적으로 작음
                            - 지구 자전때문에 움직이는것 처럼 보임.
                                - 실제로 사람 입장에서는 움직이는게 맞음

4. network core
    - ![image](https://user-images.githubusercontent.com/44149738/135022931-2d028e40-f777-4723-afc1-657ff82f6b03.png)
    - network core에는 기본적으로 라우터가 그물망처럼 서로 연결되어있음
    - circuit switching 또는 packet-switching 방식을 이용할 수 있음
        - circuit switching
            - 전화선 같은 존재. 하나의 연결마다 독립적인 하나의 회선 제공
        - packet-switching
            - 패킷단위로 쪼갠 다음, end system에 전송
            - link의 전체 용량(capacity)을 모두 사용할 수 있다는 장점이 있음.
                - 자세한건 뒤에서 다룸
    - alternative core: circuit switching
        - 스위치간 통신에서 어떤 회선을 사용할 것인지 선택해서 독점.
        - circuit-like 성능
            - circuit과 거의 같은 성능. 즉, link를 독점하기 때문에 전체를 나혼자 사용하는것과 같은 효과
        - 회선 사용을 예약 했는데 사용하지 않으면 다른 사람이 사용하지 못해서 낭비가 됨.
        - 회선을 쪼개서 사용할 수도 있음
        - 쪼개는 방식은 크게 두 가지가 있음.
            - ![image](https://user-images.githubusercontent.com/44149738/135025490-b669b503-d547-4e56-b4e9-94c61bd16713.png)
            - FDM (Frequency, 주파수)
                - 주파수를 기준으로 분할
            - TDM (Time, 시간)
                - 시간을 기준으로 분할

    - packet switching: queueing delay, loss
        - 먼저 요청된 패킷을 먼저 처리.
        - 예약 시스템의 낭비 문제를 해결할 수 있음
        - 버퍼를 관리하는 과정(queueing)에서 대기로 인한 딜레이가 발생할 수 있음
        - 버퍼가 가득 차면 패킷이 버려짐.(loss)
    
    - circuit switching VS packet switching
        - 동시 사용 : packet switching은 많아도 가능
            - 1Mbps 회선이 있다고 가정하자
            - 100Kbps 데이터를 보낸다고 하면
            - circuit switching
                - 10%를 독점하기 때문에 10명만 사용 가능
            - packet switching
                - 10명 동시사용까지는 원할하게 사용 가능하나, 그 이상부터는 대기시간이 길거나 유실되는 상황 발생 가능
                - 35명이 사용한다고 가정하면, 10명이 동시에 사용할 확률은 `.0004`임. 즉, 35명은 충분히 사용 가능하다고 볼 수 있음.
        - 그렇다면 packet switching이 절대적으로 좋은가?
            - packet switching은 폭발적인 통신이 발생하는 특성을 가진 네트워크에서 효율이 좋다.
            - 여기서 폭발적이란, 지속적인 통신이 아닌, 필요할 때 발생하고 그 외에 사용하지 않을때는 고요한 그런 특성을 말함.
            - 효율적으로 관리한다는 장점이 있지만, 혼잡한 순간이 발생할 수 있다는 단점도 존재한다.
                - 프로토콜을 이용해서 신뢰성을 높이고 혼잡제어 기능이 필요하다.
            - 실시간 서비스는 지속적인 데이터기 때문에 circuit like한 네트워크가 적합해보이지만 사실 아직 이런 기술이 개발되지 않음.

5. 인터넷 구조
    - network of networks. end system이 access ISP 들을 통해서 연결되어있음.
    - 점진적으로 덧붙혀지면서 인터넷이 확대되어오다보니 복잡한 구조를 띔.
        - 복잡한 구조가 된 이유는 경제적, 국가 정책적 이유
    - access net을 서로 연결하면 회선이 너무 많아져서 확장이 어려움.
    - 이를 해결하고자 global ISP가 서로 연결되고, customer가 제공받는 형태로 구성
    - global ISP가 여러개인 경우 서로 연결됨
        - peering 또는 IXP를 통해 연결
    - ![image](https://user-images.githubusercontent.com/44149738/136493591-40946eda-789e-4c8a-8415-a3001007a33e.png)

6. 딜레이
    - ![image](https://user-images.githubusercontent.com/44149738/136501210-ea9f25d3-cce1-4de2-ae89-8a2c75384e75.png)
    - process delay
        - 패킷에 오류검출, 결정 관련 처리 등 패킷을 처리할 때 드는 비용
    - queueing delay
        - 버퍼에서 앞의 패킷이 모두 빠질 때 까지 대기하는 시간
        - 가변적임
    - transmission delay
        - 패킷 전송을 위해 대역폭에 맞게 쪼개서 올리는 시간
        - delay = (Packet Length)/(Link bandwidth) = L/R
    - propagation delay
        - 실제 회선을 타고 출발지부터 목적지까지 이동하는 시간
        - delay = (물리적 회선의 길이) / (전송속도) = d/s
        - transmission delay와는 전혀 관계가 없다.
    - 실제 delay는 얼마나 발생하는가?
        - traceroute 프로그램을 사용하면 됨.

7. 패킷 loss
    - 버퍼가 가득 차면 패킷을 버린다(drop). 이를 loss라고 함.

8. thuroughput (수율)
    - 얼마나 빠르게 보낼 수 있는가를 나타냄
    - instantaneous : 특정 시간에 특정 지점에서
    - average : 긴 시간동안의 평균
    - 가장 대역폭이 작은 link를 `bottleneck link`라고 함.
        - 이 link가 곧 전체의 전송속도를 결정지음.

9. protocol "layers(계층)"
    - protocol stack
        - application
        - transport
        - network
        - link
        - physical
    - OSI 7 Layer
        - ISO에서 제작
        - presentation과 session 계층이 추가됨.
    - encapsulation
        - 계층별 패킷 명칭  
            - application : messasge
            - transport : segment
            - network : datagram
            - link : frame 
