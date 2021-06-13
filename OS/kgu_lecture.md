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
:9주차
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
:10주차
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
        - 모든 page를 frame에 할당하고 시작하는 방식. 즉, 앞서 공부한 방식을 pure paging이라고 한다.
    - segmentation
        - pageing과 기본개념은 같음.
        - pageing은 고정된 크기의 메모리를 할당해주지만, segmentation은 segment라는 단위로 variable한 공간을 할당한다.
        - segment : 프로그램을 구성하는 논리적 단위. code segment, global segment, ...
        - segment table이 필요.
            - 2개의 요소 필요.
                1) STBR(Segment-table base register) : 세그먼트의 시작주소
                2) STLR(Segment-table length register) : 세그먼트의 크기
:12주차-1
- Vitual Memory Management Strategy
    - Demand paging
        - pure paging과는 다르게 모든 메모리를 다 할당해놓고 시작하는게 아니라 일부만 할당해놓고 시작
    - page replacement schemes
        - 페이지가 필요한 부분을 할당하려고 했을 때, 메모리에 공간이 없을 때, 사용중인 메모리 일부를 걷어내서 그곳을 사용하는 방식

    - background
        - 프로그램을 실행하기 위해서는 메모리에 적재해야함.
        - 프로그램 전체를 굳이 올리지 않아도 필요한 부분 일부만 메모리에 올린다는 아이이어. -> 가상메모리의 기본 개념
            - 프로세스 일부만 메모리 할당받는 방식의 장점
                - 필요한 부분만 올리기 때문에 물리메모리 양에 구애받지 않을 수 있다.
                - 위 장점에 의해 동시 실행가능한 프로세스 수가 늘어난다.
                - 첫번째 장점에 의해 IO 양도 줄어든다(= 속도가 빨라진다) 
    
    - virtual address space
        - 사실상 space가 무한대라고 볼 수 있다
            - 전체를 다 할당받을 필요없고, 상황에 따라 필요한 부분만 할당하기 때문에 virtual space에서 제한은 없다.
        - 당연히 MMU에서는 address translation이 일어나야한다.
    
- Demand Paging
    - 프로세스가 100개의 page를 필요로 한다면, pure paging은 모두 할당하지만 demand paging에서는 필요한 부분. 예를 들면 30개정도만 할당받는다.
        - IO가 줄어들고
        - 메모리 필요 공간도 줄어들고
        - IO가 줄었으니 당연히 response time도 빨라짐
        - 필요 메모리 공간이 줄어드니 더 많은 사용자 프로세스를 올릴 수 있음.
    - Lazy swapper (or pager) 라고 불림.
    - 어떤 page가 올라가있고, 어떤 page가 디스크에 있는지 파악해야함.
        - valid-invalid bit를 이용.
        - valid : 메모리에 올라가있고, access해도 됨.
        - invalid : access 하면 안됨. 또는 access는 해도 되지만 메모리에 올라가있지 않으니 메모리 할당을 먼저 하라는 것을 뜻함.
:12주차-2
    - Page Fault
        - invalid page에 접근하는 것을 page fault가 발생.
        - page fault가 발생하면 판단을 해야하는데, access가 아예 안되는 page인지, access는 되는데 할당이 안된건지 파악해야한다.
        - 후자인 경우에는 empty(free) frame를 받아온다. 그리고 그곳에 page를 로드하고, valid로 변경한다.
        - free frame이 없는 경우, 기존에 올라가있는 page를 swap하여 공간을 만들어냄.
        - 이후 page fault가 발생한 코드를 재실행.
    
    - Aspect of demand paging
        - Extreme case (최악의 경우)
            - 프로세스가 처음 시작할 때 부터 아무 page도 적재하지 않은 상태로 실행하는 경우.
            - 이것을 pure demand paging 이라고 함.
        - 여러개 page를 동시에 접근하면 page fault가 동시에 발생할 수 있다. 이런 경우에는 page를 메모리에 올릴 때 하나만 올리는게 아니라 유사한 주소의 page를 동시에 올려서 locality를 형성해서 page fault를 줄일 수 있다.
        - 하드웨어 지원
            - page table에 valid/invalid bit가 있어야 함
            - swap sapce가 존재해야하고
            - instruction restart를 지원해야함.

    - instruction restart
        - 명령을 재실행 할 때 overhead가 발생.
        - 상황에 따라 이전 수행 내용을 다시 복원해야하는 경우가 생길 수 있음. 이 부분에서 오버헤드 발생.
        - 이러한 문제는 사전에 page fault가 발생하는지에 대한 검사를 하는것과 같은 방식으로 해결할 수 있다. 

- Performance of Demand Paging
    - Worse case인 Demand paging 과정
        1. memory access
        2. 메모리에 안올라가있으면 page fault 발생
        3. os가 trap 발생
        4. 현재 프로세스 상태(레지스터 등)를 저장해야함
        5. trap이 page fault에 의한 trap인지 체크
        6. access 해도 되는 page인지 체크
        7. access가 가능하나 메모리에 적재되지 않아서 발생한 것이라면 메모리에 적재할 page 주소를 가져옴.
        8. 사용하지 않는 frame에 page를 저장하기 위해 Disk I/O 시작
        9. Disk I/O가 수행되는 동안 CPU를 다른 프로세스에게 넘김.
        10. I/O 인터럽트를 받으면 disk로부터 발생한 것인지 확인.
        11. page table 업데이트
        12. CPU를 받을 때 까지 Wait
        13. 프로세스 상태를 복원
    - Tree major activities
        - interrupt를 처리하는데 소요되는 시간
        - page를 read하는 시간
        - process를 restart하는 시간
    - Effective Access Tiem(EAT)
        - p : page fault rate. 0~1 범위의 값.
            - p=0 : page fault가 없음.
            - p=1 : 모든 주소에서 fault 발생.
        - Memory Access Time : page fault가 발생하지 않을 때 소요되는 메모리 access 시간.
        - Page Fault Time : page fault가 발생할 때 소요되는 메모리 access 시간.
        - 식
            ```
            EAT = (1-p) * Memory Access Time
                    + p * Page Fault Time
            ```

        - page fault overhead :  page fault에 사용되는 오버헤드. 앞서 설명한 interrupt 처리시간, page 읽는 시간, process를 restart하는 시간이 모두 포함됨.
        - swap page out : page replacement가 발생했을 때, swap out 하는 시간. 발생하지 않을 수 있음. 즉, 옵션.
        - swap page in : page를 frame에 저장하는 시간
        - restart overhead : 명령어를 restart하는 오버헤드
        - 식
            ```
            Page Fault Time = 
                    page fault overhead
                    + swap page out
                    + swap page in
                    + restart overhead
            ```
    
    - EAT 예시
        - 상식
            - 1 milliseconds = 10^3 microseconds = 10^6 nanoseconds
            - 즉, 1 milliseconds = 1,000,000 nanoseconds
        - 문제
            - Memory Access Time = 200 nanoseconds
            - 평균 page fault service time = 8 milliseconds
        
        - 풀이
            ```
            EAT = (1-p) * 200 + p * 8,000,000
                = 200 + p * 7,999,800
            ```
            - if one access out of 1,000 causes a page fault
                - p = 1/1000 = 0.001 이므로
                - EAT = 8199.8 nanoseconds
                      = 8.1998 microseconds
                      = 약 8.2 microseconds
                - 평소 메모리 접근에 200 nanoseconds 가 소요됨.
                - page fault가 발생하면 8199.8 nanoseconds 가 소요됨.
                - page fault가 발생하면 메모리 접근이 약 41배 느려짐
        
        - 속도를 10% 감소시키기 위한 방법,,,?????????
            - 220 > 200 + 7,999,800 * p
            - 20 > 7,999,800 * p
            - p < .0000025
            - < 400,000번의 메모리 접근에 한번의 page fault 발생

    - copy-on-write
        - paging이나 segmentation을 사용하게 될 경우 공용 코드인경우 프로세스간 공유가 쉽게 일어난다. 한번만 적재되고, 해당 페이지를 각 프로세스의 page table에 기록하여 공유가 가능해진다.
        - 공유중인 page에 어떠한 프로세스가 변경을 가할 때, 그때 copy가 된다.

- page replacement
    - free frame이 없을 때, 적재되어있는 page를 disk에 저장하고 그 공간을 사용하는 것을 말함.
    - 그러나 page replace를 하려고 할 때, 어떤 page를 swap하느냐에 따라서 추가 page fault가 더 발생할 수 있다.
    - 이런 문제를 해결하기 위해서 page replacement algorithms가 존재.
    - 당연한 이야기지만, 이러한 알고리즘들은 replace 이후 발생할 page fault를 최소화 하는 것을 목적으로 한다.
    - modify (dirty) bit
        - 이 비트가 1이라면 한번이라도 수정된 적이 있음을 뜻하고, 0이면 한번도 수정되지 않은 page라는 뜻.
        - dirty bit이 0이라면 disk에 있는 것과 같으므로 swap out을 해줄 필요가 없기때문에 disk I/O가 줄어서 처리가 더 빨라짐.
    - 기본 동작
        1. 어떤 page를 메모리에 적재해야하는지 탐색.
        2. free frame 탐색
        3. 없으면 page replace algorithm을 돌려서 바꿀 victim frame을 찾음.
        4. victime frame을 디스크에 write함.
            (dirty bit가 1일 때만. == 수정된 page인 경우에만)
        5. page를 free frame에 저장하고, page table을 업데이트함.
        6. instruction restart

:12주차-3
- Page and Frame Replacement Algorithm
    - Frame-allocation algorithm
        - 각 프로세스에게 얼만큼 많은 FRAME을 할당해 줄 것인가?
    - Page-replacement algorithm
        - victim frame을 어떤 것으로 설정할 것인가?
        - page-fault rate를 최소화하는 것이 목적.
        - 평가 방법
            - page에 접근하는 순서를 page에 해당하는 숫자들의 나열로 이루어진 예시(reference string)가 주어지고, 몇번 page fault가 발생하는지를 살펴봄.
        
        - "page fault 횟수"와 "프로세스당 할당하는 Frames 개수"와의 상관관계
            - 프로세스당 할당하는 Frames 개수가 많으면 많을 수록 page fault 횟수는 줄어든다.

- Page replacement algorithms
    - FIFO Algorithm
        - 가장 오래 access된 frame을 victim frame으로 설정
        - Belady's abnomaly 문제가 발생.
            - frame이 더 많음에도 불구하고, 더 많은 page fault를 야기할 수 있음.
    - Optimal Algorithm
        - 가장 오래동안 사용되지 않은 page를 replace
        - 현재를 기준으로 미래의 reference string을 찾아서 오래동안 사용되지 않을 page를 찾아서 변경.
        - 최상의 알고리즘이지만, 미래의 내용을 확인해야하기 때문에, 미래를 파악할 수 없어서 이론상으로만 가능한 알고리즘.
    - Least Recently Used (LRU) Algorithm
        - optimal과는 다르게 과거를 보고 가장 예전에 사용되었던 page를 선택. 즉, 오래동안 접근이 없었던 page를 변경.
        - FIFO보다 좋지만 당연히 OPT보다는 좋지 않음.
        - 자주 사용되는 알고리즘. 다른 분야에서도! 알아두면 좋음
        - 구현방법
            - counter를 사용한 구현방법
                - page마다 counter를 둔다.
                - page가 언제 access되었는지 counter에 저장.
                - counter 값을 이용하여 가장 오래된 page를 탐색.
            - stack을 사용한 구현방법
                - 가장 최근에 사용한 page가 위쪽에 있게 되고, 가장 과거의 page는 아래쪽에 존재하게 됨.
                - 가장 아래쪽 page를 replace.
                - 중간에 access되면 해당 page를 스택 맨 위로 올림
    - LRU Approximation Algorithm
        - LRU 알고리즘은 특별한 하드웨어가 필요하고 여전히 느리다는 단점이 있다.
        - page table에 reference bit을 사용하는 것으로 LRU 알고리즘을 흉내낼 수 있다.
            - access가 안되면 0, 되는 순간 1
            - 1이 여러개면 순서를 알 수 없다는 단점이 있다.
        - 이를 활용한 알고리즘
            - Additional-Reference-bit algorithm
                - 위 단점해결을 위한 방안.
                - 8bit 사용.
                - 주기적(일정한 time interval)으로 비트값을 오른쪽으로 1bit씩 shift한다.
                - access가 발생하면 가장 좌측 bit를 설정.
                - bit의 값이 크면 클수록 가장 최근에 접근했다고 판단.
                - 어느정도의 오류는 허용.
                - bit수가 많아질수록 더욱 정교한 판단이 가능.
            - Second-Chance algorithm
                - 기본적으로 FIFO와 똑같이 동작. 그러나 reference bit가 1인 page에는 기회를 한번 더 줌.
                - 탐색 시 reference bit가 1이면 0으로 바꾸기만 하고 넘어감.
                - 탐색 시 reference bit가 0이면 replace.
                - 그러나, 모든 page의 bit가 1로 설정되어있으면 FIFO와 완전 동일하게 동작함. Belady's abnomaly 문제 발생
            - Enhanced Second-Chance Algorithm
                - reference bit + modify bit 두 개의 비트를 활용

                - reference bit(0) + modify bit(0)
                    - 최근에 access 되거나 modify된적 없음.
                    - replace를 위한 최적조건.
                - reference bit(0) + modify bit(1)
                    - 최근에 access 되진 않았지만, 과거에 access가 되어서 modify 된적 있다.
                    - 무조건 swap out이 발생
                - reference bit(1) + modify bit(0)
                    - 최근에 access 하긴 했지만, modify되진 않음.
                - reference bit(1) + modify bit(1)
                    - 최근에 access 했고, modify됨.
                
                - [0,1], [1,0] 두 상황에 대해서는 우열을 가릴 수 없다. 정답이 없다.
                - [0,0]인 page를 찾는것이 목표.
                - 두 비트가 모두 0인 page를 찾기 위해 page table을 모두 탐색해야한다.

    - counting-based algorithm
        - 각 page가 가지고있는 counter 값에 의해 결정되는 알고리즘.

        - LFU(Least Frequently Used)
            - count가 가장 작은 page를 선택
        - MFU(Most Frequently Used)
            - count가 가장 큰 page를 선택
        
        - 어떤 방식이 더 좋다고 말할 수 없음. 프로세스의 성격에 따라 case by case임.

:13주차-1
- page replacement examples(예시) - 계산문제임.
    - 알고리즘 별(LRU, FIFO, Optimal) page fault가 얼만큼 발생하는가에 대한 문제

- frame 할당
    - 각 프로세스의 최소 frame할당 개수는 CPU에 따라 다름.
    - 프로세스 시작 시 얼만큼의 frame을 할당하는가에 따라 할당 방법이 다름.
        - fixed allocation
        - priority allocation
    - frame replacement가 발생할 때, 교체할 victim frame을 어디서 찾는지에 따라 다름.
        - global allocation
        - local allocation

- fixed allocation
    - equal allocation
        - 모든 프로세스가 동일한 크기의 frame을 갖는다.
        - 예를 들면 100개 frame이 있고, 5개 프로세스가 있으면, 20(100/5)frame 씩 할당 
    - proportional allocation
        - 프로세스 크기의 비율에 따라 차등.
        ```
        m = 전체 frame 개수
        p = 프로세스.
        s = p의 크기.
        S = 전체 s의 합.
        a = p에 할당될 frame 수. = (s / S) * m
        ```

- priority allocation
    - 크기가 아닌 우선순위에 따라 할당.

- global allocation VS. local allocation
    - page fault 발생 시, victim frame을 어디서 선택하는가?
    - global allocation
        - p1에서 page fault가 발생했지만, p2나 p3 등 다른 p에서 victim frame을 가져옴. 
        - 장점 : 모든 프로세스가 target이 되기 때문에 throughput(처리량)이 나아진다.
        - 단점 : 반대로 다른 프로세스가 메모리를 뺏어갈 수 있으므로 process execution time을 예측하기가 어려워짐.
    - local allocation
        - p1에서 발생했으면 반드시 p1에서 victim frame을 찾음.
        - 장점 : 다른 프로세스가 메모리를 뺏어가지 않기 때문에 퍼포먼스가 일관된 형태로 나타난다.
        - 단점 : 메모리 효율이 떨어진다

- 여기까지가 demand paging에 대한 기본 개념.
- thrashing
    - demand paging의 가장 큰 문제점.
    - 모든 메모리를 할당하는게 아니라 일부만 할당한다. 따라서 각 프로세스가 충분히 많은 frame을 할당받지 못하면 page-fault가 자주 일어날 수 밖에 없다. 결국, i/o에 시간을 많이 사용할 수밖에 없다. 즉, cpu 효율이 떨어진다.
    - page fault가 자주 발생해서 swap in/out에 모든 시간을 쏟는 현상을 thrashing이라고 한다.
    - 이를 해결하기 위해서는 각 프로세스에게 가능한한 많은 메모리를 할당해주면 된다.
    - 그렇다면 프로세스가 필요로 하는 양을 어떻게 알 것인가?
        - 이에 대해 가장 많은 정보를 주는것이 locality이다.
        - locality란, 현재 프로세스가 active하게 사용하고있는 메모리 영역.
        - 현재 locality를 담을 수 있는 메모리 공간보다, 실제로 할당된 메모리 공간이 더 작기 때문에 thrashing이 발생한다.
        - 즉, 현재 locality를 담을 수 있을 만큼의 충분한 메모리 공간을 할당해주면 page fault는 발생하지 않는다.
    - 그러나 locality는 미래 사실이기 때문에 정확히 예측할 수 없다.
    - 그렇다면 어떻게 이를 알 수 있는가?
        - working set
            - 과거의 메모리 access 패턴을 이용해서 locality를 찾아냄.

- working-set model (계산)
    - locality를 기반으로 함.
    - working-set window : 현재로부터 고정된 수의 메모리 reference.
        - 현재로부터 과거 n개의 메모리 access 패턴을 본다는 것.
    - WS : Working Set
        - 프로세스 p의 working-set window에 포함되어있는 page reference들.
    - WSS : WS의 크기.
        - working set window를 너무 작게 만드는 경우
            - 현재 locality를 못담을 수도 있음.
        - working set window를 너무 크게 만드는 경우
            - active 하지 않은 locality도 담게됨.
        - working set window가 무한대가 되면
            - 지금까지 access한 전체 영역에 해당.
    - D : 전체 WSS의 합
        - 전체 프로세스가 필요로 하는 FRAME의 양.
        - if (D > m ) : thrashing 발생.
    
    - 실제로 어떻게 working set을 측정하는가?
        - reference bit와 interval timer를 이용한다.
        - interval timer에 의해 reference bit이 rshift 되고, reference bit이 하나라도 1이 존재하면 working set window 내에서 접근이 있었던 것.
        - reference bit이 크면 클수록 정교해짐.

- working-set과 page fault
    - working-set에서는 각 프로세스의 locality를 예측할 수 없다. 왜냐? 미래의 사실이기 때문에.
        - 예측을 해도 완전히 다른 locality가 발생할 수도 있는 것.
    - working set 모델에서의 page fault 패턴은 아주 비슷한 형태의 그래프를 그린다.
        - 초반에는 working set이 locality를 담고있지 않기 때문에 page fault가 발생하면서 working set에 locality가 담겨지기 시작한다. 당연하게 page fault 횟수가 증가하게 된다. (상승그래프)
        - 어느정도 working set이 현재 locality를 담게 되면 이에 맞게 memory가 점점 할당되면서 page falut는 줄어든다 (하강그래프)
        - 충분한 memory가 할당되고 나서부터는 패턴이 바뀌기 전까지는 아주 낮은 page fault를 보인다.

- page fault frequency(PFF)
    - working-set 모델 외 방법.
    - 프로세스마다 어느정도의 page fault는 허용한다. 라는 임계값을 설정.
    - local replacement policy를 이용하여 처리
        - page fault가 낮게 측정되면 frame을 반납
        - page fault가 높게 측정되면 frame을 더 할당.


:13주차-2
- Memory-Mapped Files
    - disk block을 page에 로딩해서 사용.
    - 이는 disk i/o를 빠르게 할 수 있게 됨.
    - file이 처음에 읽혀지면 page 단위로 만듬. 이를 file system으로부터 physicla page로 만듦.
    - 이는 디스크 일부분이 메모리에 올라가있기 때문에 훨씬 빠르게 access가 가능.
    - 지난번에 page table을 설정하여 여러 프로세스가 동일 page에 접근할 수 있다는 것을 설명했었다. 이를 이용해서 여러 프로세스가 하나의 파일을 쉽게 공유할 수 있게됨.
    - 수정된 메모리의 내용을 언제 실제 디스크에 적용할 것인가? 가 이슈. 주기적으로 write할수도 있고, 수정할때마다 할수도 있다.

- 여기까지는 사용자(user) 영역에서의 메모리 할당에 관한 이야기.

- Kernel Memory Allocation
    - 어떤 프로세스가 호출될지 알 수 없고, 각 프로세스가 메모리를 어떻게 사용하는지도 알 수 없다.
    - kernel 메모리는 kernel만 사용하기 때문에, 메모리를 어떻게 사용하는지 잘 알 수 있음. 쉽게말해 kernel이라는 프로세스 하나가 계속 메모리를 사용하기 때문에 잘 알 수 있다는 것.
    - 커널이 메모리 할당 방식이 다른 이유
        - 특정메모리를 독점한다는 특징에 따라서 특화된 메모리 할당 방법을 이용. 
        - 연속적인 메모리 접근을 하게되면 paging과 같이 불연속 메모리 할당 방식에 비해서 확실히 속도가 빠름. kernel 역시 속도가 중요하기 때문에 연속적인 할당방식을 사용.
    - 대표적인 memory allocation 방식.
        - buddy system
        - slab allocation
    
- buddy system
    - if 프로세스가 24kb를 필요로 한다! 
        - 큰 메모리 256을 2로 계속 나누어간다.
        - 최종적으로 32kb가 나오면 이 부분을 할당.
    - 당연하게도 단편화가 발생.
        - 내부단편화, 외부단편화 모두 발생할 수 있다.

- slab allocation
    - slab : 하나 이상의 연속된 page들
    - cache : 여러개의 slab.
    - kernel이 어떤 크기의 object를 사용한다는 것을 알고 있다. 따라서, 커널이 필요로 하는 data structure에 부합되는 object들을 담을 수 있는 메모리 공간으로 나누어져 있다.
    - 연속된 메모리를 사용하기 때문에 빠르게 메모리 할당이 가능하다는 장점이 있다.
    - 또한, paging 기법을 사용하기 때문에 단편화 문제도 해결한다.

- paging 구현에서 발생할 수 있는 이슈.
    - prepaging
        - demand paging에서는 프로세스가 필요한 양만큼 메모리 할당을 받아서 사용.
        - 필요하는 page가 메모리에 없으면 page fault가 발생. 디스크에 있는 page를 메모리에 로드.
        - prepaging이란, 이처럼 디스크에 있는 page를 메모리에 로드할 때, 디스크에 있던 주변 page도 같이 메모리에 로드하는 것을 말함.
        - 지금은 access가 일어나지 않았지만, 앞으로도 일어날 것이라고 보는 것.
        - 사용하면 다행이지만 그렇지 않다면 오히려 메모리 낭비일 수 있다.
        - s개의 prepage 에서 alpha 비율 만큼만 사용된다. 라고 했을 때,
            ```
            감소된 page fault 비용 : s * alpha
            낭비된 비용 : s * (1-alpha)
            ```
            - 즉, alpha가 0에 가까울 수록 prepaging을 하면 안된다.
        - 아무튼 page fault를 미리 막아보자 하는 차원에서의 방법임.
    - page size에 따른 이슈
        - fragmentation (단편화)
            - page size가 클수록 내부단편화 발생 확률 높음.
        - table size
            - page size가 작을 수록 table size가 커짐. 관리해야하는 요소의 개수가 많아지기 때문.
        - I/O overhead
            - page szie가 클수록 I/O overhead는 감소. 한번에 많은 양을 보낼 수 있기 때문.
        - locality
            - page size가 클수록 너무 많은 locality가 한 page에 담길 수 있다.
            - page size가 작을수록 하나의 locality가 하나의 page에 담길 수 없고 여러개의 page에 흩어질 수 있다.
        - 최근 동향을 보면, page size는 점점 커져가고 있다.
    - TLB Reach
        - TLB를 통해서 access 할 수 있는 메모리의 크기를 말함.
            - TLB Reach = (TLB size) * (page size)
        - 메모리를 엑세스할 때, TLB에 있으면(TLB hit) memory access time을 줄일 수 있기 때문에 EAT(Effective Access Time)를 줄일 수 있음.
        - 가장 좋은 케이스는 현재의 working set. 즉, locality가 모두 TLB에 올라가 있으면 당연히 memory access time이 빨라지기 때문에 좋아짐.
        - TLB Reach를 키우기 위해서는 (TLB size)를 키우거나 (page size)를 키워야 함.
            - TLB size가 커지면 당연히 레지스터 개수가 늘어나야하기 때문에 H/W COST가 늘어날수밖에 없음.
            - page size가 커지면 단편화 문제가 발생한다.
            - 최근 추세는 page size가 하나로 고정되는게 아니라 multiple하게 여러개의 size를 가지게끔 os가 구현됨.
    - program structure
        - 프로그램 구조를 어떻게 제작하느냐에 따라서 page fault 횟수가 달라질 수 있음.
            - 예를 들면 128x128 배열이 있고, 각 행이 하나의 page에 저장된다고 할 때,
            - 행을 모두 채우고 다음 행으로 넘어가는 프로그램은 128번의 page fault가 발생.
            - 열을 모두 채우고 다음 열로 넘어가는 프로그램은 128*128=16384번의 page fault가 발생.
    - I/O Interlock
        - disk 데이터를 page 두 개에 걸쳐 메모리에 로드했다고 가정했을 때, 두 page가 replacement가 일어나면, 디스크는 이 사실을 모르기 때문에 replace된 상태의 page를 덮어버릴 수도 있다.
        - 이를 위해 Lock bit를 설정해서, 해당 page가 replace되면 안된다는 것을 명시.

:13주차-3
- file
    - 물리저장소 유닛.
    - file을 구현하는 것은 os마다 다르고 정답이라는 것은 없다.

    - 파일 내부 구조
        - disk block 단위로 할당됨. 연속적이지 않을 수 있고, 내부 단편화가 발생할 수 있음.


    - open file
        - file pointer : 파일의 어느 부분을 읽고 있는가?
        - file open counter : 몇개의 프로세스가 이 파일에 접근하고 있는가?
        - disk location : 실제 위치
        - access right : 접근 권한
        - lock
            - shared lock : reader lock
            - exclusive lock : writer lock
         
        - 리눅스에서 운영체제는 프로세스와 상관없이 global하게 유지, 관리해주는 데이터가 존재하고, 프로세스 마다 유지,관리해주는 데이터가 존재한다.
    
    - access method
        - sequential access. 순차적으로 byte단위로 읽기.
        - direct access. 읽을 지점을 지정해서 바로 읽기
        - 각 데이터의 위치정보를 indexing해서 빠르게 찾을 수 있음(like DB)

- directory
    - file을 담을 수 있는 공간
    - 리눅스에서는 directory도 file로 관리하기 때문에 file과 operation이 같다.
    - 디렉토리 관리하는 방법
        - single level directory
            - naming problem : 유니크한 파일 이름만 가능하기 때문에 문제.
            - grouping problem : 모든 파일이 하나의 디렉토리에 있기 때문에 그룹화도 어려움.
        - two level directory
            - user 별로 directory 생성.
            - path name 개념 추가.
            - 다른 user 밑에서는 같은 파일 명 존재 가능.
            - 여전히 grouping problem 발생. 사용자별로는 구분되지만, 동일 사용자 내에서 그룹화 불가.
        - tree-structured directory
            - 효율적인 탐색.
            - 그룹화 가능
            - 절대/상대주소 개념.
        - acyclic-graph directory
            - 같은 파일을 서로 다른 파일로 접근하는 것.
            - delete 할 때 문제가 발생.
        - general graph directory
            - cycle이 존재.
            - 무한 루프에 빠지는 문제 발생.
            - 링크가 있는 상태에서 delete할 때 문제 발생.

- file system mount
    - 외부 장치를 마치 하나의 file system처럼 논리적으로 붙이는 작업.
    - mount 되는 지점을 mount pointer 라고 함.

- file protection
    - file별로 접근에 대한 권한을 설정하기 위해 access control lists(ACLs)를 가지고 있음. 
    - 그러나 사용자별로 권한을 생성하면 너무 많아질 것임.
        - unix에서는 user, group, other로 나누어서 read, write, execute 권한을 설정.


:14주차-1
- file system을 구현하는 방법에 대해 알아본다.
- file system structure
    - 일반적으로 file system을 구현할 때, layer를 나눠서 구현한다. layer로 나눈다는 것 또한 방법론 중 하나이기 때문에, 사용하지 않아도, layer를 맘대로 나누어도 무관하다.
    - layer
        - application programs
        - logical file system
            - logical address를 기반으로 모든 file에 대한 meta-data를 관리한다.
            - FCB(File Control Block)을 관리.
                - name, ownership, permissions
                - reference cound, time stamps
                - ...
        - file-organization module
            - logical block과 physical block 간의 translation을 담당.
        - basic file system
            - 여러가지 버퍼관리.
            - I/O가 느리기 때문에, I/O에 직접 접근하는게 아니라, buffer를 통해서 접근.
        - I/O control
            - 물리적인 디바이스에 접근하기 위한 device drive가 필요함. 이거이 i/o control에 해당.
            - read, write를 실질적으로 수행하는 부분.
        - devices
    
- file system data structure
    - os 는 다양한 데이터 구조들을 처리할 수 있어야 한다.
    - 어디에 저장되느냐에 따라 크게 두 분류로 나눌 수 있다.
    - on-disk structures -> 비휘발성
        - boot control block (BCB)
            - 부팅 디스크의 0번째 블록(512bytes)에 저장된 내용.
        - volume control block
            - 현재 볼륨 안에 몇개의 블록이 있는지, 어떤게 사용중이고 사용중이 아닌지 등등의 정보를 담고 있음.
        - directory
        - per-file FCB
    - in-memory structures -> 휘발성
        - mount table
        - directory cache
        - global open-file table
        - per-process open-file table
        - 다양한 buffer들

- virtual file system
    - 각기 다른 file system 을 추상화.

- directory 구현
    - file로서 관리하기 때문에 결국엔 FCB를 이용.
    - 구현방법
        - linked list
            - 탐색이 느리다는 것이 단점
        - hash table
            - hash function이 같을 때, 충돌문제가 발생할 수 있음.
            - 빠르게 탐색할 수 있음.

:14주차-2
- allocation methods
    - continuous allocation
        - 연속된 disk block을 할당
        - 디렉토리에서 파일 관리할 때, 어디서 시작되고, 길이가 얼만큼인지에 대한 정보만 가지고 있으면 된다.
        - 원하는 위치에 바로 접근하기가 용이하다
        - 간단한 만큼 문제가 많다.
            - first-fit / best-fit / worst-fit 중에 어떤 것을 이용할지 선택해야함.
            - 외부단편화가 발생.
            - 할당 공간이 부족하면 아예 송두리채 복사해서 여유공간에 넣어야 하는 과정이 필요.
    - linked allocation
        - block들이 linked list로 구성.
        - 디렉토리는 최초 block과 마지막 block만 알고있으면 됨.
        - 단편화 없음.
        - access가 어려움. link를 타고 타고 가야함.
        - 노드별로 약간의 부분을 데이터가 아닌 다른 용도로 써야 함.(next link, ...) 이는 하나로 보면 작지만 모든 노드들을 모아보면 용량의 큰 소모가 발생.
    - file-allocation table(FAT)
        - table에 각 entry가 disk block을 가리킨다.
        - free block을 찾는것도 쉬움. 다음 index가 0인 것을 찾으면 됨.
    - indexed allocation
        - paging과 비슷한 관점에서 보면 됨.
        - index block안에 주소들을 index로 접근해서 얻을 수 있음
        - index block 크기는 제각각이므로 overhead가 발생할 수 있음.
        - 이러한 index block을 관리하는 방법이 여러개 있음
            - linked scheme
                - linked list를 이용.
            - multi-level scheme
                - outer index table을 가지고 index table을 관리.
                - 그러나 index table이 file에 따라서 낭비되는 경우가 있음.
                - 이를 해결하고자 나온것이 unix의 inode 시스템.
            - unix inode
                - 작은 파일은 direct block을 이용하여 관리.
                - 큰 파일은 크기에 따라 single indirect, double indirect, triple indirect 순으로 관리.

:14주차-3
- free space 를 관리하는 방법
    - bit vector
        - 1 : free, 0 : not free
        - 장점 : 간단하다. free block을 찾기 쉽다
        - 단점 : 메모리가 커질수록 bit가 차지하는 영역이 커짐.
    - linked list
        - free space를 link로 연결.
    - grouping
        - n개의 free block을 링크드리스트 형식으로 연결
    - counting
        - 첫번째 free block과 연속된 block들의 size를 저장

- 효율, 성능
    - page cache
        - i/o 는 buffer를 이용해 읽어들인다. 여기서 page cahce를 사용하게 될 경우, page cache에도 file 내용이, buffer에도 file 내용이 중복된다.
        - unified buffer cache
            - memory-mapped I/O에서 직접 buffer에 접근할 수 있도록 하면 중복문제를 해결할 수 있다.

- consistent checking
    - unix : fsck
    - windows : chkdsk

- log structured file system (or journaling)
    - file에 대한 작업을 모두 log로 남기는 것. filesystem이 깨지면 log를 이용해서 원상복구할 수 있도록 하는 것.

- network file system
    - 원격지에 있는 file system을 마지 local처럼 사용할 수 있도록 하는 것.
    - NFS Mounting
