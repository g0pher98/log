# Tutorial 4
이번 장에서는 ROS의 노드 개념에 대해 알아본다.  
[원문](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)  


우선 실습을 위해 다음과 같은 명령으로 튜토리얼 시뮬레이터(*i.e. lightweight simualtor*)를 설치해야한다.
``` bash
sudo apt-get install ros-<distro>-ros-tutorials
```
`<distro>` 위치에 본인의 ROS 배포명(*e.g. indigo, jade, kinetic*)을 기입하면 된다.

> *이전에 한 번 설치를 했었던 내용이라 이미 깔려있다면 설치하지 않아도 된다.*  

## 개요
빠른 이해를 위해 각 용어들과 개념들을 간단하게 나열하면 다음과 같다.
- **Nodes** (i.e. 노드)  
    ROS를 사용해서 다른 노드와 통신할 수 있는 실행파일. 정말 단순히 실행하는 주체에 지나지 않는다. 실행하면서 필요한 데이터나, 생산해내는 데이터는 topic을 통해 송/수신 한다.
- **Messages**  
    `topic`을 `subscribing` 또는 `publishing`할 때 사용할 데이터 타입을 말한다. ROS는 구독과 출판이라는 개념이 있는데, 말그대로 특정 `주제`에 대해서 어떠한 노드가 데이터를 `구독`해서 주기적으로 받아볼 수 있고, 또다른 노드는 그러한 데이터를 주기적으로 `출판`할 수 있다.
- **Topics**  
    각 노드는 topic에 데이터를 출판하거나 구독할 수 있다.
- **Master**  
    ROS의 이름 서비스. 각 노드가 서로를 찾는데 사용됨.
- **rosout**  
    ROS의 stdout/stderr
- **roscore**  
    Master + rosout + parameter server(추후 소개)

이렇게 다소 새로운 구조를 띄는 것은 다양한 플랫폼을 띄울 수 있다는 장점을 가지고 있다. 예를 들면 python으로 짜여진 코드와 c++이 짜여진 코드가 있다면 물론 이를 합치는 것은 원래 가능하나, 그것이 수없이 많아지면 무척 귀찮은 작업이 된다. 그러나 ros에서는 각각 따로 실행(*i.e. 노드*)하고 topic을 통해 연결해주면 간단하게 다양한 언어를 연결할 수 있게된다.

## roscore 명령어
roscore는 ROS를 사용하기 위해 가장 먼저 실행해야하는 명령어다.
``` bash
$ roscore

...

setting /run_id to 9cf88ce4-b14d-11df-8a75-00251148e8cf
process[rosout-1]: started with pid [13067]
started core service [/rosout]
```
위와 같은 결과를 얻었다면 `roscore`가 정상적으로 실행된 것이다. 만약 여기서 permission 관련 오류가 발생하면 sudo로 실행하면 안된다. 관리자 환경에 ros를 세팅하는 것이라 앞으로 모든 작업을 sudo로만 해야되게 될 수 있기 때문이다.
``` bash
sudo chown -R <사용자 이름> ~/.ros
```
위와 같이 소유자를 본인 계정으로 변경하자. `.ros`파일의 소유자가 최고관리자이기 때문에 발생하는 오류인데, 관리자권한으로 ros를 설치하게되면 이러한 문제가 발생한다. `.ros`의 소유자를 최고관리자가 아닌 본인의 계정으로 바꿔주어 해결할 수 있다.  

## rosnode 명령어
`roscore`가 실행된 터미널은 종료하지 않고 그대로 놔둔 상태에서 작업을 진행한다. 새로운 터미널을 열고 다음과 같은 명령을 입력해보자.
``` bash
$ rosnode list
/rosout
```
현재 `/rosout`이라는 하나의 노드가 존재한다는 것을 알 수 있다. 해당 노드에 대해 자세하게 살펴보기 위해 다음과 같은 명령을 입력할 수 있다.
``` bash
$ rosnode info /rosout
--------------------------------------------------------------------------------
Node [/rosout]
Publications: 
 * /rosout_agg [rosgraph_msgs/Log]

Subscriptions: 
 * /rosout [unknown type]

Services: 
 * /rosout/get_loggers
 * /rosout/set_logger_level


contacting node http://localhost:38539/ ...
Pid: 13214
```
아직은 정확하게 어떠한 정보가 담겨있는지는 모르겠다. 눈치껏 `publishing`과 `subscribe`에 대한 내용, 해당 노드를 이용하는것은 `http://localhost:38539`에 연결해서 사용한다 정도인 것 같다. 일단은 `rosnode info` 명령을 통해 원하는 노드의 정보를 열람할 수 있다는 정도만 알아두면 좋을 것 같다.

## rosrun 명령어
`rosrun` 명령을 사용하면 원하는 패키지 내에서 원하는 노드를 실제 경로를 알지 못해도 이름만 가지고 직접 실행시킬 수 있다. 기본적인 사용법은 아래와 같다.
``` bash
rosrun [패키지_이름] [노드_이름]
```
예시로 **꼬북이**를 실행시켜보자.
``` bash
$ rosrun turtlesim turtlesim_node
```
![꼬북이](/.resource/210320_1219.PNG)  
*....? 이 거북이 진심이다.*  

ROS 튜토리얼에 나온 작고 아담한 거북이와는 다르다. 진심펀치를 날릴 것만 같은 이두/삼두근이 경이롭다. 아마 등껍질을 떼어내면 미친광배근이 드러나겠지.

> 거북이는 사진과 다르게 나올 수 있다. 실행할 때마다 거북이 모습이 랜덤하게 바뀌는데, ROS 개발자의 이스터에그라고 보면 된다.

자, 이제 `turtlesim`이라는 패키지의 `turtlesim_node`라는 노드를 실행시켰으니, 노드 리스트에 새롭게 추가되었을 것이다. turtlesim을 종료하지 않은 상태에서 새 터미널을 열어 확인해보자.
``` bash
$ rosnode list
/rosout
/turtlesim
```

``` bash
$ rosnode info /turtlesim
-------------------------------------
Node [/turtlesim]
Publications: 
 * /rosout [rosgraph_msgs/Log]
 * /turtle1/color_sensor [turtlesim/Color]
 * /turtle1/pose [turtlesim/Pose]

Subscriptions: 
 * /turtle1/cmd_vel [unknown type]

Services: 
 * /clear
 * /kill
 * /reset
 * /spawn
 * /turtle1/set_pen
 * /turtle1/teleport_absolute
 * /turtle1/teleport_relative
 * /turtlesim/get_loggers
 * /turtlesim/set_logger_level


contacting node http://localhost:33083/ ...
Pid: 13511
Connections:
 * topic: /rosout
    * to: /rosout
    * direction: outbound
    * transport: TCPROS
```
뭐가 더 많다. `topic`에 연결된 것도 확인할 수 있다. 일단 이런게 있구나 하고 넘어가자.  

이번에는 실행되는 노드의 명칭을 바꿔보고자 한다. 큰 프로젝트나 협업에 있어서 이러한 네이밍은 생각보다 중요하다. 다음과 같이 변경할 수 있다.
``` bash
rosrun turtlesim turtlesim_node __name:=<new_node_name>
```
기존 명령에서 `__name:=<new_node_name>` 이 부분만 추가되었다. 같은 `turtlesim`을 실행하지만, 명확하게 이게 무엇인지 나타낼 필요가 있기 때문에 좋은 별칭을 지어주는것이 중요하다. 테스트를 위해 `jaeseung_turtle` 라고 간단하게 실행해보았다.

``` bash
$ rosnode list
/jaeseung_turtle
/rosout
```
이번엔 머리3개달린 케르베르스 거북이가 나타났다. 동시에, 다른 터미널에서 노드 리스트를 확인해보니 위와같이 내가 설정한 이름으로 노드가 실행되고 있는 것을 확인할 수 있었다.

이제 실행된 노드가 죽었는지, 잘 살아있는지 확인이 필요할 경우를 대비해 노드의 생사여부를 체크하는 명령을 아래와 같이 실행해보자.
``` bash
$ rosnode ping jaeseung_turtle
rosnode: node is [/jaeseung_turtle]
pinging /jaeseung_turtle with a timeout of 3.0s
xmlrpc reply from http://localhost:44979/	time=0.475883ms
xmlrpc reply from http://localhost:44979/	time=1.698017ms
```
`rosnode`의 `ping`이라고 하는 기능이다. 결과를 보면 `reply from ~~~ time=~~~ms` 형태로 결과가 뜨는것을 확인할 수 있는데, 해당 노드에 살아있는지 응답을 요청하고, 요청한 응답이 도달을 했다면 `reply from ~~~`이 뜬다. 내가 요청한 시점부터 응답까지 걸린 시간을 측정하여 노드의 응답속도도 확인해볼 수 있다.

## 정리
- `roscore` : ros + core  
    ros를 사용하기 위해 가장 먼저 실행하는 명렁. 다음과 같은 일들을 함.
    - master(ROS용 네임서비스) 실행
    - rosout(stdout/stderr) 노드 실행
    - 파라미터 서버(*추후 설명*) 실행


- `rosnode` : ros + node  
    노드에 대한 정보를 얻기 위해 사용되는 명령

    
- `rosrun` : ros + run  
    원하는 패키지의 노드를 실행시키는 명령