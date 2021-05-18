# 1주 1장
- 운영체제 기본 개념 소개
    - Process / Scheduling / Concurrency
    - Virtual memory / File system / IO system, ...
- 주요 기능에 대한 내부 동작 원리 이해
    - 각 구성 요소에 대한 이론적 지식 습득
    - Nachos를 이용한 운영체제 구현
- Prerequisites
    - C/Java programming skills
    - 자료구조 관련 기본 지식


# 1주 2장
- 운영체제에 대한 정의
- 운영체제가 하는 작업

운영체제 역할
- 하드웨어 관리(resource allocatior) - 스케쥴링
- application 실행 환경 제공(control program) - 잘못된 메모리 접근 막아줌

## pc가 켜지는 순서
파워 on
-> bootstrap(=firmware)이 hw 검사
-> kernel 로딩.(각종 초기화 작업)
-> 로그인 화면 출력

## Computer system
- processing Unit
- storage structure
- io structure

## Processing Unit
마우스나 키보드 등을 누르면 interrupt가 발생함
os에서 대부분 이 interrupt를 이용해서 처리
발생 시 interrupt service 루틴으로 넘어감

interrupt vector table이 존재해서
여기서 참조해서 해당하는 interrupt service를 실행
거기서 최종 처리

interrupt 처리 방식 2가지
- polling - 주기적으로 디바이스들을 체크
- vectored interrupt system - 발생 시 테이블에서 찾아서 실행

## storage structure
- 프로그램 메모리에 적재
- 기계어 코드 읽음
- 이걸 decode
- 연산을 위한 데이터를 읽어옴
- 연산
- 결과를 저장


## IO Structure
IO와 CPU는 개별적으로 실행될 수 있다.
모든 장치는 해당 장치를 위한 device controller가 존재
device controller를 제어하는 것이 os안의 device driver임.

cpu가 io장치에 직접 값을 쓰는것이 아니라 controller 안에 버퍼가 존재함
거기에 쓰고, controller가 io장치에 직접 쓰는것임

## DMA (direct memory access)
1M마다 interrupt발생한다고 가정하면
10M를 보내려면 10번 발생.
이를 해결하기 위한 방안이 DMA 
원래는 interrupt를 통해서 cpu가 중간에 메모리와 io를 중계함.
DMA는 device controller가 cpu의 중재 없이 직접 io장치하고 데이터 송수신

## symmetric multiprocessing architecture
여러개의 cpu가 존재하고, 각각 독립적으로 reg, cache 등을 가지고 있음.
모든 cpu가 메모리에 system bus를 통해 접근.
bus에서 겹치는 문제 발생할 수 있음(교착).

## dual-core design
하나의 single chip 안에 두 개의 core가 존재
전력소모도 작고, 교착문제 감소

# 1주 3장
## multiprogramming(batch system)
single user 상황에서는 cpu와 io를 바쁘게 만들 수 없음.
그래서 이걸 설계함.
이거는 여러개의 프로그램을 메모리에 올리는 방식임.
프로세스가 io를 할때 다른애를 cpu 사용하게 해서
cpu와 io를 쉴틈없이 바쁘게 만들 수 있음.

## timesharing(multitasking)
여러개의 프로그램을 메모리에 올리는건 같다.
time을 설정해서 작업을 못끝내면 강제 회수
마치 대화형 컴퓨팅인것처럼 생각할 수 있다.
interactive 하다! 유리하다!

어떤 job을 메모리에 올릴 것인가?
-> job Scheduling

메모리의 어떤 프로세스에게 자원을 제공해서 실행시킬것인가?
-> cpu Scheduling

메모리가 부족해서 덩치가 큰 프로세스를 실행하기 어려우면
-> swapping -> 다른걸 메모리에 저장하고 큰 놈을 가져온다

아예 큰놈을 쪼개서 실행하는건 어떨까?
-> virtual memory

## os operations
H/W interrupt : hw작업이 끝났을 때
S/W interrupt : system call을 요청할 때, 보호, 무한루프 등에 사용됨

무한루프(cpu독점)이나 인가되지 않은 메모리에 접근하는 것을 막아야하는것이
os의 역할임.

이를 위해 도입되는 방법이 dual-mode execution과 timer
dual-mode execution : kernel, user mode를 가지고 실행 보호
timer : 일정시간내에 job을 끝내지 않으면 자원 회수.

## dual-mode execution
user mode / kernel mode
hw의 mode bit와 기계어의 모드를 비교.
같으면 실행.
<명령어 비교>
- timer 설정 명령(kernel)
- clock 읽는 명령(user)
- interrupt off (kernel)
- io access(kernel)
- trap instruction (user) 중요!!!

## os 작업들
프로그램 실행 환경을 구성하기 위해 하는 작업들
- process 관리
- memory 관리
- storage 관리
- 보안 관리

## process 관리
- program : 디스크에 있는거
- process : 메모리에 올라간 프로그램(active하다!)
    - cpu, memeory, io, files 같은 리소스가 제공됨.
- single-threaded : program counter 한개
- multi-threaded : 각 스레드별 program counter가 존재

### process 관리 activities
- 프로세스 생성 및 제거
- 프로세스 재실행
- 프로세스 동기화
- 프로세스 커뮤니케이션
- 프로세스 데드락 제어

## memory 관리
- 어려 프로그램을 메모리에 올리기 위해 필요한 작업이 있음
- 필요에 따라서 데이터 일부를 swapping하기도 함
- 메모리 할당

## storage 관리
- file 기본단위.
    - low level에서는 disk block으로 볼 수 있고,
    - high level에서는 연속된 공간으로 볼 수 있음.

## protection & security
- 남이만든걸 함부로 접근하고 그러면 안됨.

## 정리
- os
    HW를 관리하고, 응용프로그램 실행환경을 제공하는 소프트웨어
- os 동작
    - 기본적으로 interrupt로 동작
        - hw / sw(trap)
    - dual-mode operation & timer
- multiprogramming & timesharing
    - 항상 cpu와 io를 바쁘게 만듬!
    - 운영방법에 차이
        - multiprogramming : io로 전환될 때 다른 job에 cpu 넘김
        - timesharing : time을 정해두고 관리 대화형 시스템에 적합

# 1주 4장
- os를 구성하는 컴포넌트
- system call
- 아키텍처

## 운영체제의 서비스
- 사용자를 위한 시스템 서비스
    - GUI, io operations 등등
- 효율을 위한 서비스
    - 자원 allocation, accounting, protection&security
이 두개로 나누어볼 수 있음

## system call
- os에서 제공되는 서비스를 호출하기 위한 프로그래밍 인터페이스
- 대부분 high level lang로 만들어져있음(c/c++)
    - asm으로 짜기 어려우니!
- 각 시스템콜은 번호가 할당되어있음. 관련된 테이블을 관리해주어야함.

## api, system call상관관계
open을 할 경우 이건 api. api가 systemcall을 이용하도록 구현되어있음.
결국엔 systemcall 구현에 대해 생각 안해도 api를 사용하면 됨.

## systemcall 파라미터 전달
- register로 전달
- memory block을 전달
- stack을 이용

## 시스템콜 만드는법
- 시스템 콜 함수 정의
    - `/linux/include/linux/syscalls.h`에 정의
- 시스템 콜 번호 할당
    - `/linux/include/asm-i386/unistd.h`에서 번호 define
- 시스템 콜 함수 등록
    - `/linux/arch/i386/kernel/vsyscall-sysenter.S` 어셈파일에 등록
- kernel rebuild & test


# 2주 1장

## simple structure - ms dos
- 모듈이라는 개념이 없고, 필요에 따라 컴포넌트 생성
- 메모리 접근이 자유로워서 위험함

## non simple structure - unix
- systems programs 파트(사용자)와 kernel 파트로 나누어져있음.
- 주먹구구식 코드가 많음

## layered approach
레이어를 기준으로 시스템을 관리. 깰-꼼
각 레이어는 인접한 상/하위 레이어로부터 api를 제공받아 처리
코드 관리 및 디버깅이 용이.

문제는 덩치가 엄청 큰 os 프로그램을 layer 형태로 짜기가 어렵다!

## microkernel system structure
기존의 커널의 기능을 user 영역으로 걷어내서 최대한 compact하게 만듬.
message passing을 이용해서 다른 기능을 사용하는 방식
다양한 아키텍처에 포팅하기 쉬워진다는 장점이 있다.
== 확장성이 좋다
그러나 기존 kernel 기능을 사용하기 위해서는 항상 message passing을 이용해서
다른 user space에 접근해서 사용해야하기 때문에 오버헤드 발생해서 느림.

## Modules
그다음으로 나온게 모듈임.
동적으로 커널 모듈을 넣고 뺄 수 있도록 함.
커널이 모듈로 구성되어있기 때문에 절차에 맞게끔 개발하면 모듈 만들 수 있음.
layered approach에서 발생하는 오버헤드가 발생하지 않음.
마이크로커널처럼 컴팩트하게 관리할 수 있음.
심지어 api를 직접 호출하기 때문에 마이크로커널보다 빠름

## 정리
system call
-> 사용자가 원하는 low한 작업.(위험한 작업)
-> os가 제공하는 서비스를 사용하기 위해 호출하는 방법.


# 2주 2장
- 프로세스 기본 개념
- 다중 프로세스에서 커뮤니케이션 방법

## 프로세스 개념
- 프로세스란?
    실행중에 있는 프로그램.
    메모리에 올라간 프로그램
- 프로세스 상태
    - new : 새로 생김
    - running : cpu를 할당 받아서 실행중
    - waiting : io 작업을 기다리는 상태
    - ready : cpu를 할당받을 준비가 된 상태
    - terminated : 프로세스가 종료된 상태
- 프로세스 상태전이
    - admitted : new -> ready
    - interrupt : ready -> running
    - dispatch : running -> ready
    - exit : running -> terminated

## PCB (Process Control Block)
프로세스와 관련된 모든 정보가 PCB에 저장됨.
- proecess state
- program counter
- cpu register
- cpu Scheduling info
- memory management info
- io status info

## process scheduling
여러가지 종류의 q를 만들어서 관리
- job queue : 메모리에 올라갈 준비가 되어있는 작업 큐
- ready queue : cpu를 할당할 준비가 되어있는 작업 큐
- device queues : 각 디바이스마다 엑세스하고자 하는 프로세스 큐

## scheduler
- short term scheduler(CPU scheduler)
    - 무척 빠르게 동작해야함.
    - 빈번하게 일어남.(밀리세컨)
    - c
- long term scheduler(job scheduler) 
    - 누구를 ready q에 올릴것인가?
    - 상대적으로 빈번하게 일어나지 않기 때문에(세컨, 미닛) 비교적 long term임
    - multiprogramming의 정도를 얘가 결정함
- long term 중요한 역할
    - io bound process - 이것만 하면 cpu가 논다.
    - cpu bound process - 이것만 하면 io가 논다.
    이 둘을 적절하게 잘 관리해주어야 함.
    이거를 long term scheduler가 해야함.
- midium term scheduler
    - 메모리가 충분하지 않을 때 swapping.
- context switch
    - 프로세스간 switch가 일어난다.
    - PCB 정보에 의해서 수행된다.
    - context switch time은 짧으면 짧을수록 좋다.
        - cpu가 실제 일하는 시간을 늘릴 수 있다.
    - arm 프로세서는 context switch를 hw상에서 구현된 것임.

## process 관련 operations
- process create
    - 각 프로세스는 pid를 가지고 있음. 부모 자식 프로세스 관련 관리가 필요함.
    - 예를 들면 부모의 종료시점과 자식종료시점이라든지, 공유 데이터 영역이라든지.
    - 이거는 개발하는 사람에 따라 다르다.
    - fork : 동일한 자식 프로세스 생성
    - exec : 완전히 다른 프로세스 생성
- process termination
    - exit : 현재 프로세스 종료
    - wait : 자식 프로세스가 끝날때까지 대기
    - abort : 자식 프로세스 종료
    - 부모가 종료되면 자식까지 모두 종료되는 경우도 존재.
        - 이를 cascaded termination 이라고 함.
        
- get/set priority
- get id
- get PCB


# 2주 3장
웹서버 같은 복잡한 프로그램의 경우 프로세스 하나로 문제 해결이 어려울 수 있음.
사용자 request 받아들이는 용도, work 용도 등등 

다중프로세스로 작업하게되면 당연히 속도가 빨라짐.
웹서버처럼 기능별로 나누면 모듈러하게 개발이 가능하기도 함.

각 프로세스별로 데이터를 주고받는 방법도 필요함. 이게 IPC

## IPC 모델
    - producer -consumer problem
        producer과 consumer가 데이터를 주고받아야하는 버퍼는 필수적이다
    - Message passing
        - 메세지 패싱을 이용해서 프로세스를 경유
        - 개발 방식에 따라 다양한 구현이 가능함.
            - 두 프로세스간 링크는 언제 만들것인가?
            - 링크에 한번에 보낼 수 있는 데이터 크기는 얼만큼인가?
            - 가변크기 메시지도 가능한가?
            - 하나의 링크가 송/수신 둘다 가능한지 따로 가능한지.
        - 구현방법 두 가지
            - direct communication
                - 데이터 송수신 방식을 명시적으로 지시.
            - indirect communication
                - 직접 보내는게 아니라 매개체를 이용해서 송수신.
                - 그 매개체가 mailboxes
                - mailbox에 붙는 수만큼 서로 데이터를 주고 받을 수 있음
                - mailbox 생성하고 붙는 operation이 있어야함.
        - synchronization
            - blocking : 계속 기다림
            - non-blocking : 안되면 그냥 넘김
        - buffering
            - p가 q에 넣는 속도가 c가 q에서 읽는 속도보다 빠르면 q가 점점 찬다.
            - 큐에 얼마나 데이터를 넣을 수 있는지에 따라 구현 방법이 다름.
                - zero capacity : 큐가 비워지지 않으면 삽입 불가
                - bounded capacity : n개의 한계가 있음
                - unbounded capacity : 무한대로 넣을 수 있음
        
    - shared memory
        - 공유메모리를 통해서 데이터 송수신
        - 이거는 동시접근에서 심각한 문제가 발생할 수 있음

## IPC 구현 방법
- socket
    - ip와 port를 통해 접근. bytes 스트림 송수신.
    - 로우하게 접근 가능하지만 구현이 귀찮음
- remote procedure call(rpc)
    - 데이터를 주고받을 때, 함수를 CALL하는것처럼 주고받자!
    - 함수를 호출하면 원격지의 함수가 호출되어서 데이터를 주고받음.
    - 실제로 중간에 이를 중계하는 PROXY가 있음.
    - 다른 체계의 시스템에서 데이터를 송수신 할 때, client쪽에서 marshalls를 해야한다.
    - 두 체계 사이에서 data의 표현 방식을 맞춰주는 것임.
    - 서버쪽에서도 이걸 고려해야하는데 MIDL이라는걸 통해서 진행한다.
    - (XML같은거임)
- pipes
    - byte 스트림을 보내는 도구.
    - ordinary pipes
        - unidirectional한 성격을 띔 : 송/수신 파이프가 따로있음
        - 송수신이 끝나면 파이프도 사라짐.
    - named pipes
        - 송수신이 끝나도 관리하기 위한 파이프

- pipe와 message passing의 차이점
    - `bit stream`을 보내느냐 `structured message`를 보내느냐의 차이


# 2주 4장
- thread가 무엇인지
- multithreading models

## thread
- 프로세스보다 작은 cpu 활용 단위
- 멀티 스레드로 만들면 멀티 프로세스보다 경제적인 측면이 유리해짐
    - 메모리 공간적인 이득이 있음
    - 레지스터와 스택은 개별적으로 존재하지만
    - 코드, 데이터, 파일 등은 공유
- 장점
    - 훨씬 빠른 문제 해결
    - 리소스적인 측면에서 이득(코드영역, 파일 등)
    - 경제적 (스레드가 프로세스 메모리를 공유하기 때문에 경제적)
    - 확장성(scalability) : 스레드를 여러개 코어로 구성하면 코어별로 돌기 때문에 좋음


# 3주 1장
(복습)

# 3주 2장

## multicore programming
cpu 안에 여러개의 core로 구성되어있음.
병렬 처리가 가능함!
- parallelism : 물리적으로 동시에 실행
    - data parallelism : 데이터를 나눠서 동시처리
    - task parallelism : 데이터를 가져와서 각 task가 처리
    이 두개는 교양으로만 알아두길.
- concurrency : 마치 동시에 실행하듯 실행

## multithreading models
- user thread
    - 유저영역 라이브러리로 관리됨
- kernel thread
- models
    - 스레드간 매핑이 필요
        - many to one model
            - 여러개의 유저 스레드가 커널 스레드 하나에 매핑.
            - 문제점
                - 하나의 유저 스레드가 커널스레드로 blocking 요청
                - 이렇게되면 다른 유저 스레드가 커널스레드 사용불가
        - one to one model
            - 하나 유저 - 하나 커널
            - 유저스레드만큼 커널스레드가 필요해서 리소스가 많아짐
            - 하지만 blocking 문제 발생하지 않음
        - many to many model
            - 여러 유저 - 여러 커널로 매핑
            - 1대1 매핑이 아니기 때문에 유휴 커널 스레드를 찾아 이용
            - 그래도 일반적으로 커널 스레드보다 유저 스레드가 많기 때문에
            - 스레드를 많이 사용하게되면 blocking되는 스레드 발생 가능 
        - two -level model
            - many to many랑 one to one을 같이 사용.
            - 중요한 것들은 one to one으로 따로 뺌

## thread library
스레드 라이브러리로 개발을 하게 될것임
ex1. pthread. 표준화된 api이기 때문에 모든 시스템에서 사용 가능.
ex2. java에서는 jvm에서 제공해주는 스레드로 관리됨

## threading issues
- semantics of fork() & exec() system call
    - 프로세스를 fork할 때 스레드를 모두 복제할건지 등등 고려해야함.
- signal handling
    - process는 default 시그널 핸들러를 가지고 있는데
    - user-defined 시그널 핸들러를 통해서 시그널이 들어왔을 때,
    - 스레드를 모두 처리(ex 죽인다든지)할건지 한개만 할건지 등등 고려해야함.
- thread cancellation
    - 종료할 때, 어떻게 종료할 것인지.
- thread-local storage
    - 스레드별로 각자 저장공간을 주자!
- scheduler activation
    - 유저 스레드와 커널 스레드 스케쥴링을 어떻게 해줄 것인지.
    - 유저 스레드를 LWP라는 애가 스케쥴링함.
    - LWP는 커널 스레드와 1:1 연결되어있음.
    - 커널 스레드가 BLOCKING 되었을 때, LWP가 연결된 유저 스레드에 UPCALL함
    - 이를 통해 유저스레드로 필요한 정보를 전달해준다.


# 4주 1장
cpu 스케쥴링에 대해서 소개함.
cpu의 효율은 최대화 시키는 것이 좋음.
multiprogramming, multitasking이 그 역할을 함..
cpu burst : cpu를 사용하는 구간
io burst : io를 사용하는 구간

cpu 스케쥴러는 ready q에 존재하는 여러 프로세스 중
어떤 녀석을 cpu할당을 해줄지 결정하는 방법이 cpu 스케쥴러

cpu를 프로세스가 자발적으로 반납하는것 : nonpreemptive(비선점)
cpu를 강제로 회수하는 것 : preemptive(선점)

## dispatcher
context-switch를 하는 주요 모듈
dispatch latency : context-switch time

## 스케쥴링 기준
- cpu utilization : cpu 효율
- throughput : 주어진 시간내에 얼마나 많은 프로세스를 처리하는가
- turnaround time : job를 시작한 시각부터 최종적으로 끝날때까지 시간
- waiting time : waiting q에 들어가있는 시간
- response time : 시작시점으로부터 첫 응답 시간

## 스케쥴링 알고리즘
- FCFS (first come first served)
    - nonpreemptive로 동작함.
        - 강제 회수 안됨.
    - convoy effect 문제가 발생함.
        - cpu burst가 아주 큰 프로세스가 발생해서 전체 대기시간이 길어짐
- SJF (shortest-job-first)
    - nonpreemptive
        - cpu burst가 가장 짧은 job을 먼저 실행
        - 이보다 짧은 대기시간을 가지는 알고리즘은 없음.
        - 그러나 실제 cpu burst를 알기 어려움.
        - 다양한 테크닉을 통해 예측해서 유사하게 접근할 수 있다.
        - Starvation 발생 가능
    - preemptive
        - shortest-remaining-time first scheduling이라고 함.
- Priority Scheduling
    - 우선순위를 기반으로 스케쥴링
    - preemptive/nonpreemptive 둘다 동작
    - starvation (=indefinite blocking)
        - 우선순위가 낮은 프로세스가 실행되지 않는 문제
        - aging  기법을 사용해서 해결가능
            - 우선순위를 시간이 지남에 따라 조금씩 올려주는 방법
- Round-Robin
    - 대표적인 알고리즘
    - response time이 짧아진다는 이점.
    - time quantum을 정의하여 이 기간 내에 job을 해결하지 못하면 회수하므로 공정한 스케쥴링임.
    - preemptive 형식
    - n개의 프로세스가 cpu의 1/n을 사용하는것과 같음
    - 1/n컴퓨터를 혼자 사용하는것 같은 효과를 냄.
    - time quantum이 너무 크면 FCFS랑 같음
    - time quantum이 너무 작으면 context-switch에 시간을 다 써서 job 수행불가
    - time quantum은 전체 프로세스의 80%의 cpu burst보다 큰 값으로 정하는게 적당
- multilevel queue scheduling
    - 여러개 큐를 가지고 있고 각 큐는 각각의 알고리즘을 가지고 있을 수 있음
    - 프로세스의 특성에 따라 특성에 맞는 큐에 들어감
    - 큐 간에 스케쥴링도 필요함.
        - fixed priority scheduling
            - 우선순위가 높은 큐가 모두 끝나야만 하위 큐 실행
            - starvation 문제 발생
        - time slice
            - 각 큐에 일정비율로 cpu 할당
- multilevel feedback queue scheduling
    - 큐가 여러개 있는건 같음
    - 다른점은 프로세스가 특정 큐에 들어가는게 아니라
    - 여러 큐를 옮김

## thread scheduling
- user 스레드는 바로 cpu가 할당되는게 아니라 kernel 스레드와 중간에 있는 LWP가 스케쥴링

## multi processor scheduling
    - asymmetric : 프로세스 하나가 나머지 프로세스를 정함.
    - symmetric : 모든 프로세스가 동일하게 동작

    - processor affinity
        - 프로세스와 프로세서의 유사도 검사(물리적 위치라든지).
        - 비슷한 프로세스에 프로세서 할당
        - 가능하면 가까운 영역에 접근하는게 속도가 빠르기 때문에
        - 유사도가 높을수록 효율이 좋음.

    - load balancing : 모든 프로세서들이 바쁘게 만들어주는 방법
    - push migration : job이 많으면 다른 프로세서에게 넘김
    - pull migration : job이 없으면 다른 프로세서에서 가져옴

## multicore processors
    - 전력과 속도측면에서 이득
    - 물리적으로 동시에 실행됨


# 4주 2장

## real-time cpu 스케쥴링
- 실시간 운영체제 : 이벤트가 발생하면 그걸 처리하기까지 데드라인이 정해져있음
- hard real time system : 반드시 그 기간에 끝내야함
- soft real time system : 얼추 그 근처에 끝내면 됨

- 마감기한을 지키는 것(성능)에 영향을 미치는 두가지 latency 
    - interrupt latency : 인터럽트 발생 시 switch를 끝내기까지의 시간
    - dispatch latency : contet-switch에 들어가는 시간

- 스케쥴링 알고리즘
    - priority-based scheduling(우선순위 기반으로 동작해야함. 데드라인 맞춰야하니까)
    - preemptive 일수밖에 없음.
    - periodic하다! 주기적으로 프로세스가 요청한다
    - 0 < t(processing time) < d(deadline) < p(period)
    - `rate monotonic 스케쥴링`
        - priority = 1/period임
        - period가 작으면(자주 요청되면) : 우선순위가 높음
        - period가 크면(가끔 요청되면) : 우선순위가 낮음
        - DEADLINE을 못맞추는 문제가 발생할 수 있다.
    - `Earliest deadline first(EDF) 스케쥴링`
        - 위 문제를 해결하기 위해 deadline을 기준으로 우선순위를 할당





# 5주 1장
- process synchronization
    - critical section problem
    - semaphore
    - monitor

## backgorund
- machine instruction
    - 0과 1로 이루어진 기계어
- asm
    - 기계어와 1대 1로 매칭되어있는 언어
- high level languages
    - high level 하나가 1:다 의 형태로 매칭됨.
    - 이 부분이 문제의 시작.
    - shared data를 여러 프로세스가 동시에 접근하게 되면 문제가 됨.
    - 이걸 race condition이라고 함.
    - race condition이 발생하는 공유데이터 공간을 critical section이라고 함.

## critical section problem solution 조건
- mutual exclusion
    - 한 순간에 하나의 프로세스만 접근한다
- progress
    - 준비가 된 프로세스들을 대상으로 어떤 프로세스가 다음에 들어갈것인지 판단.
    - 무한정 기다리게끔 하지 않아야 한다.
- bounded waiting
    - 프로세스가 준비가 되었다면 일정 시간이 지나면 반드시 critical section에 들어가야한다.
    - 만약 프로세스하나가 계속 쓸 수 있다? 그럼 bounded waiting이 만족이 안되는거
    - 프로세스간 context-switch 시점을 정의하면 안된다

## solution
- peterson's solution
    - 이론적인 솔루션이라 실제 사용은 안함.
    - 두 개의 프로세스 대상으로만 동작
    - load/store 연산에 한해서 인터럽트가 발생하지 않는다는 가정 존재.
- semaphore
    - atompic한 특정 함수로만 접근가능한 정수형 변수(wait / signal)
    - 0/1 만 표현되는 binary semaphore
    - 0~N 값을 가지는 counting semaphore
    - 두 문제를 해결할 수 있음
        - critical section 문제
        - process synchronization 문제

## semaphore
구현 방법 두가지
- busy waiting
    - while문으로 기다림
    - 리소스 너무 많이 발생
    - critical section 코드 실행 시간이 아주 짧으면 오히려 좋음
- block & wakeup
    - 쓸데없이 cpu 낭비하는 문제 해결법
    - block : waiting q에 집어넣는 동작
    - wakeup : waiting q에서 ready q로 전환
```
typedef struct {
    int value;
    struct process *list;
} semaphore;

wait (semaphore *S) {
    S->value--;
    if(S->value >= 0) {
        // add this process to S->list;
        block();
    }
}

signal (semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // remove a process P from S->list;
        wakeup(p)
    }
}
```


## semaphore 문제
잘못사용하게 되면 문제 발생
- deadlock & starvation
    - 잘못사용 -> deadlock
    - 잘못구현 -> starvation
        - LIFO로 구현하면 문제 야기
        - 오히려 FIFO가 낫다

- priority inversion
    - 우선순위 역전현상.
    - 우선순위가 낮은 프로세스가 semaphore를 가지고 있는데, 우선순위 높은 녀석이 자꾸 들어오면
    - 우선순위 낮은 프로세스가 semaphore를 반환할 수 없기 때문에 모두 사용불가
    - 해결법 : 우선순위 계승
        - 특정 프로세스가 높은 우선순위 프로세스에서 요구하는 자원을 가지고 있다면
        - 높은 우선순위로 일시적으로 높여주는 기법.
- semaphore 문제는 전적으로 프로그래머에게 달려있음.
- 근본적으로 이러한 문제를 줄일 수 없을까? -> 모듈 -> Monitor

## monitor
- java에서는 synchronize기능이 있음.
- 여러개의 프로세스가 동시에 함수를 호출해도 한번에 하나씩 호출해준다.
    - 기본적으로 critical section 문제를 해결해줌
- 그러나 프로세스간 실행 순서를 제어해주지는 않음
    - 프로세스동기화 문제는 해주지 않음
    - 그래서 이걸 해결해주기 위해 condition 변수를 사용할 수 있음.
    - x.wait() : 무조건 suspended 되어서 q에 들어감
    - x.signal() : wait 시켜준 프로세스 중 하나를 wakeup시켜서 실행시킬 수 있음.
    - 주의! p1,p2가 동시에 f1에 접근한 후, p1이 wait하고 p2가 signal하면 critical section 문제 발생.
    - 참고. semaphore의 wait/signal과는 다른거임. 우연히 이름이 같은거임.

## condition 변수 선택
- siganl and wait scheme
    - x.signal시 자신을 q에 넣는 방법
```
wait(mutex)
//...
if(next_count > 0)
    signal(next)
else
    signal(mutex)
```
```
semaphore x_sem
int x_count = 0

// x.wait()
// 본인을 멈춤

x_count ++
if (next_count > 0)
    signal(next)
else
    signal(mutex)
wait(x_sem)
x_count --

// x.signal()
// wait상태인 프로세스 wakeup
if(x_count > 0) {
    next_count ++
    signal(x_sem)
    wait(next)
    next_count--
}
```
- x.signal시 다른 누구를 먼저 실행시켜야하나?
    - 가장 간단한 방법은 FCFS. 항상 정답은 아님.
    - conditional-wait를 사용할 수도 있음. condition 변수로 우선순위 설정

# 6주 2장
semaphore로 해결할 수 있는 문제
- bounded buffer problem
- readers-writers problem
- dining-philosophers problem

## bounded buffer problem
producer와 consumer가 공유데이터에 접근할 때 문제 해결
- mutex
    - binary semaphore
    - 한개만 접근허용
    - init -> 1
- full
    - counting semaphore
    - 차있는 버퍼수
    - init -> 0
- empty
    - counting semaphore
    - 비어있는 버퍼수
    - init -> N
``` c
// producer
do {
    wait(empty)
    wait(mutex)
    // do
    signal(mutex)
    signal(full)
}

// consumer
do {
    wait(full)
    wait(mutex)
    // do
    signal(mutex)
    signal(empty)
}
```


## readers-writers problem
file에 reader, writer가 접근.
- read_count
    - read하는 프로세스가 몇개인지
- mutex
    - read_count 보호용도
    - init -> 1
- rw_mutex
    - write가 있을 때는 reader 접근못함.
    - init -> 1

``` C
// writer
do {
    wait(rw_mutex)
    // do
    signal(rw_mutex)
}

// reader
do {
    wait(mutex)
    read_count++
    if (read_count == 1)
        wait(rw_mutext)
    signal(mutex)
    // do
    wait(mutex)
    read_count--
    if (read_count == 0)
        signal(rw_mutex)
    signal(mutex)
}
```

## dining-philosophers problems
젓가락 나눠서 밥먹기



## deadlock 조건
- mutual exclusion : 하나 프로세스만 접근
- hold and wait : 자원보유 상태에서 추가 요청
- no preemption : 중간에 강제회수 불가
- circular wait : 원형으로 요청


(8주차)
1. Deadlock
    - 프로세스들이 어떠한 이벤트를 기다리고 있어서 결국엔 어떠한 동작도 하지 못함.
    - 다음과 같은 4가지 조건을 만족해야 deadlock 발생.
        - mutual exclusion
            - 임의의 순간에 한 프로세스만 자원을 사용해야한다.
        - hold and wait
            - 프로세스가 자원을 소유하고 있는 상황에서 다른 자원을 요청해야한다.
        - no preemption
            - 프로세스가 반납하지 않으면 자원을 뺏어갈 수 없다.
        - circular wait
            - 위 상태가 원형을 이루어야 한다.
            - 이 성질이 존재하냐 안하냐는 굉장히 중요한 요소임.
                - 만약 리소스에 하나의 instance가 있으면 -> deadlock
                - 만약 리소스에 여러개의 instance가 있으면 -> deadlock이 아님.

2. deadlock을 어떻게 처리할 것인가.
    1) os가 deadlock이 발생하지 않게끔 관리해주는 방법.
        (1) deadlock prevention
            - 조건 4가지 중 하나라도 만족시키지 못하게 만들어서 데드락을 피함
                - mutual exclusion 회피
                    - 사실 이걸 만족시키지 못하게 하는건 방법이 없음.
                    - 애초에 시스템 성격임.
                - hold and wait 회피
                    - 방법1. 프로세스가 필요한 자원이 있으면 모두 할당받아 동작.
                    - 방법2. 프로세스가 필요한 자원이 있으면 소유중인 자원이 모두 없을 때만 허용
                    - 리소스 효율이 떨어지고 + starvation 문제가 발생할 수 있음.
                - no preemption 회피
                    - 프로세스가 요청한 자원을 바로 사용할 수 없을 때, 가지고 있는 자원 release.
                - circular wait 회피
                    - total ordering을 만족하는 함수를 하나 정의해야한다.
                        - total ordering을 만족한다 == 집합 내 모든 원소의 대소관계가 명확.
                        - A = (a, b, 100, 400)  => total ordering 만족하지 않음.
                        - B = {1, 57, 2, 100}   => total ordering 만족.
                        
                        - resource types가 input이 된다.
                            - ex -> f(printer) = 10
                                    f(disk)    = 20
                                    f(scanner) = 30
                        - f(Rj) > f(Ri)
                            - f(x)값이 현재 소유하고 있는 자원의 f(x)값보다 작으면 할당받을 수 없다.
                            - 만약 disk를 할당받은 상태라면, scanner는 할당요청할 수 있지만, printer는 안된다. printer를 할당 받으려면 기존 자원을 release 해야함.

        (2) deadlock avoidance
            - 부가적인 정보를 이용해서 특정 자원을 할당 할 때, 미래에 시스템이 deadlock에 빠질 가능성을 예상하여 할당여부를 결정.
            - 부가적인 정보
                - 현재 이용 가능한 자원
                - 각 프로세스에 할당되어있는 자원
                - 각 프로세스가 앞으로 추가적으로 요청하고 release 할지에 대한 정보
                    - process lifetime동안 몇 개의 정보를 요청하는가?
            - 위 세가지 부가정보로 "어떻게" 미래 deadlock을 판단하는가?
                - safe state임을 유지(!!매우 중요)
                    - safe state가 되면 deadlock이 발생하지 않는다.
                    - sequence : 프로세스에게 자원을 할당해주는 "순서"
                    - sequence가 특정 조건을 만족하면 safe sequence가 됨.
                        - 조건
                            - P2, P1, P0가 있다고 가정.
                            - P2 -> [현재 이용 가능한 자원] 을 요청
                            - P1 -> [현재 이용 가능한 자원 + P2의 자원] 을 요청
                            - P0 -> [현재 이용 가능한 자원 + P2의 자원 + P1의 자원] 을 요청
                    - 한개라도 safe sequence가 존재한다면 safe state라고 본다.
            - safe state가 아니면 자원을 안해주는 방식.
            - resource type별로 instance가 한개인 경우
                - resource allocation graph에서 graph가 있는지 없는지만 판단하면 됨
            - resource type별로 instance가 여러개인 경우
                - resource allocation graph에서 circle이 존재해도 deadlock이 발생이 안되는 경우도 있음. 그래서 다른 알고리즘을 사용해야함.
                - claim edge
                    - 프로세스가 자원을 요청할 수 도 있다. 라는 뜻
                    - 실제 요청 시, claim edge가 request edge로 바뀜.
                    - 할당이 되면, assignment edge로 바뀜.
                    - release 되면 다시 claim edge로 바뀜.
                - banker's algorithm
                    - 구조
                        - n : 프로세스 개수
                        - m : 리소스 타입의 개수
                        - available : 리소스 타입 별 현재 이용가능한 자원 수
                        - max : 프로세스 별 리소스 타입 몇개를 요청하는지.
                        - allocation : 각 프로세스 대상 리소스 타입 별로 몇 개의 리소스가 할당되어 있는지
                        - need : 각 프로세스 별로 몇개의 리소스 타입 별로 몇 개의 리소스를 요청할 것인지.

                        - need[i, j] = max[i, j] - allocation[i, j]
                    - safety algorithm
                        - safe sequence가 있는지 없는지 알아내는 것이 이 알고리즘임.
                        - 로직
                            - work[m], finish[n] 선언
                            - work = available
                            - need[i] < work
                            - work = work + allocation[i]
        (9주차)
        (3) deadlock detection
            - 리소스별 인스턴스 한개인 경우
                - wait-for graph 사용
                    - resource allocation graph를 간략화(리소스 부분 제거) 한 것임.
            - 리소스별 인스턴스 여러개인 경우
                - banker's algorithm을 변형하여 사용
                    - 구조
                        - available : 이용 가능한 자원
                        - allocation : 프로세스에게 리소스 타입별로 할당된 수
                        - request : 각 프로세스가 리소스 타입별로 얼만큼의 자원을 요청하는가
                    - 알고리즘
                        - banker's algorithm과 같이 work와 finish를 사용함.
                        - "hold and reuqest" 조건을 만족해야하기 때문에 allocation이 0이면 finish를 true로 설정하고 나머지는 false로 설정한다.
                        - 이 외는 banker's algorithm과 같다.
            - deadlock이 발생했을 때 대처방법.
                - 모든 프로세스를 다 종료시키는 방법.
                    - 어떤 프로세스를 먼저 종료시킬 것인가? 
                - deadlock에 걸린 프로세스의 자원을 뺏는 방법
                - rollback하는 방법
                - starvation 문제가 발생할 수 있다.
                    - 계속 deadlock발생해서 종료되는 경우
    2) 시스템이 deadlock에 빠졌는지 주기적으로 확인해서 고치는 방법.
    3) 이런거 다 무시하고 그냥 발생하면 재부팅 하든가 하는 방법.

    - 실제로는 3번을 많이 씀.
    - os가 이걸 고려하려면 너무 많은 리소스가 발생함.

3. 메모리 관리
    - background
        - 프로그램이 실행되기 위해서는 메모리에 프로그램이 올라가야함.
        - cpu가 직접 접근할 수 있는 공간은 main memory와 레지스터임.
        - memory unit은 address, read, write, data만 볼 수 있다.
        - one cpu clock 내에서 레지스터가 접근할 수 있다.
        - 메모리는 cpu 외부에 있기 때문에 데이터를 읽을 때, 여러개의 clock cycle 을 지나야 해서 기다리는 현상이 발생할 수 있음. 이릉 stall이라고 함.
        - 메모리와 cpu의 속도차를 개선하기 위해 cache를 사용함.
        - os는 메모리를 보호해야함. 프로세스별 공간도 보호해주어야함.
        - base register, limit register을 가지고 범위를 제한할 수 있음. PCB에 저장.
        - Address binding
            - 기본적으로 모듈 기준으로 상대적인 위치에 배치된다.
            - linker와 loader가 로드되면 물리 주소를 사용하게 된다.
            - 명령어와 데이터들이 실제 물리주소로 언제 바뀌는가? == address binding
                - compile time
                    - ex) ms-dos
                    - 컴파일 하게되면 변수가 물리적 주소로 매칭된다.
                        - x = 1   -->   mov 0x001258, 1
                - load time
                - execution time(runtime)
                    - ex) linux, window
        - address
            - logical address : cpu에 의해 계산되는 주소(= virtual address)
            - physical address : 실제 주소
            - execution time에 address binding이 발생하는 시스템에서는 logical address와 physical address가 다르다. MMU라는 하드웨어에 의해 주소가 변환된다.
        - MMU
            - 가상 주소를 물리주소로 바꾸어주는 하드웨어 장치
        - dynamic linking
            - static linking : 라이브러리 코드 등 모두 바이너리에 때려박는 것.
                - 크기가 엄청 커짐.
            - 공유 라이브러리를 사용하는 것.
        - swapping
            - 메모리가 부족한 상태에서 프로그램을 더 실행하기 위해 사용하는 방법
            - 메모리에 있던 프로세스를 디스크에 저장(swap out)
            - 디스크의 프로그램을 메모리로 적재(swap in)
    - 연속된 공간에 메모리를 할당하는 방법
        - first-fit : 가장 앞의 메모리 영역 할당
        - best-fit : 가장 작은 메모리 영역 할당. 메모리 전체 free 공간을 다 탐색해야함.
        - worst-fit : 가장 큰 메모리 영역 할당. 메모리 전체 free 공간을 다 탐색해야함.
        - 문제점
            - external fragmentation 외부 단편화
                - hole보다 할당하려는 메모리가 큰 경우 할당할 수 없음.
                - 전체 hole의 크기는 크지만, 연속된 영역이 없어서 할당할 수 없는 문제 발생.
            - internal fragmentation 내부 단편화
                - 보통 할당은 byte단위가 아니라 block 단위(4k)로 할당함.
                - 5k 프로세스를 올리려면 8k를 할당해야함.
                - 3k의 손해 발생.
        - 해결법
            - compaction
                - execution time때 address binding 되는 시스템에서만 가능.
                - external fragmentation해결을 위한 방안.
                - 분산되어있는 영역들을 앞으로 모아 정렬.
                - 한계
                    - io중인 프로세스는 옮길 수 없음. 
            - paging & segmentation
                - 연속되지 않은 공간에 프로세스를 할당. 
            - paging
                - external fragmentation문제는 해결되지만 여전히 internal fragmentation 문제가 남아있음.
    - paging
        - 물리 메모리(physical memory)는 frame으로 구성되어있고, 이들의 집합이다.
        - 논리 메모리(logical memory)는 page로 구성되어있고, 이들의 집합이다. 
        - page table
            - logical memory frame 들이 physical memory의 어떤 frame에 저장되어있는지 저장.
            - 프로세스별로 존재
            - 시작주소는 PTBR(Page Table Base Register), 길이는 PTLR(Page Table Length Register)
        - internal fragmentation 문제 발생
        - paging을 사용하게 되면 runtime 때 address binding이 일어나야함.
        - paging 에서 주소체계
            1) page number (p) : page table의 참조할 index
            2) page offset (d) : page 내에서의 offset
        - 메모리에 두 번 접근해서 속도가 느림. page table 한 번, 실제 메모리 한 번.
        - TLB(Translation Look-aside Buffers)
            - 속도문제를 개선하기 위해 캐시같은 역할인 TLB를 사용
            - page table의 일부를 TLB에 저장
            - TLB를 모든 프로세스에서 공유하게 된다면 Process 넘버정보를 포함하는 ASID 를 사용해야함.
            - EAT(Effective Access Time)
                - 알파(a) = 80%, TLB search time : 20ns, memroy access time : 100ns
                - TLB hit  : 20 + 100 : 120
                - TLB miss : 20 + 100 + 100 : 220
                - EAT = 0.8 * 120 + 0.2 * 220
        - pageing protection
            - page table의 valid-invalid bit라는 특수한 bit을 이용해 접근을 제어.
        - 공유 pages
            - 코드를 공유하는것이 용이함. 자주 사용되는 코드는 
        - page table 구성방법 3가지
            - hierarchical page tables
                - page table 자체를 한번 더 pageing (2-level page table)
                - 2-level paging 은 3번 메모리를 access 하게 된다.
                - 3-level paging은 더 크다. 4번. access에 사용되는 오버헤드가 크기 때문에 깊게는 안한다.
                - address가 32bit보다 크게되면 잘 사용하지 않음.
            - hashed page tables
                - hierarchical 방식이 32bit보다 큰 시스템에서 오버헤드때문에 사용하지 않는다는 단점 보완.
            - inverted page tables
                - 앞서 설명한 테이블들은 프로세스마다 테이블이 존재한다.
                - inverted는 공유 테이블이다. 그러므로 어떤 프로세스의 페이지인지도 명시되어있다.
    - segmentation
        - pageing과 기본개념은 같음.
        - pageing은 고정된 크기의 메모리를 할당해주지만, segmentation은 segment라는 단위로 variable한 공간을 할당한다.
        - segment : 프로그램을 구성하는 논리적 단위. code segment, global segment, ...
        - segment table이 필요.
            - 2개의 요소 필요.
                1) STBR(Segment-table base register) : 세그먼트의 시작주소
                2) STLR(Segment-table length register) : 세그먼트의 크기
            



                        




    