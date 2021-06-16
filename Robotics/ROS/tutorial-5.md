# Tutorial 4
이번 장에서는 ROS의 토픽(topic) 개념에 대해 알아본다.  
[원문](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)  

## ros turtle 실행하기
가장 먼저 ros를 사용하기 위해 roscore를 실행시킨다.
``` bash
$ roscore
```
오류가 뜬다면 roscore를 다른 터미널에서 이미 실행중일 확률이 높다. 이미 실행중이라면 종료하자.


본격적으로 turtle 게임을 아래 명령으로 실행시켜보자.
``` bash
$ rosrun turtlesim turtlesim_node
```
이제 거북이를 조종할 방법이 필요한데 아래 키보드 관련 노드를 실행하여 키보드로 거북이를 이동시킬 수 있도록 하자.
``` bash
$ rosrun turtlesim turtle_teleop_key
```
이제 키보드의 방향키를 사용하여 거북이를 조종할 수 있다.  
![210615_1935](/.resource/images/210615_1935.PNG)

## ROS 토픽
`turtlesim_node`와 `turtle_teleop_key` 노드는 ROS Topic을 통해 서로 통신하고 있다. `turtle_teleop_key`는 방향키 입력에 대한 키보드 데이터를 topic에 **publishing**(게시)하고, `turtlesim`은 동일한 topic을 **subscribes**(구독)하여 키보드 데이터를 받아온다. 이를 시각적으로 보여주는 `rqt_graph`를 사용해서 실제로 어떻게 node와 topic이 구성되어있는지 확인해보자

### rqt_graph
`rqt_graph`는 시스템에서 발생하는 상황들을 동적인 그래프로 시각화한다. 설치되어있지 않은 경우 다음과 같이 설치할 수 있다.
``` bash
$ sudo apt-get install ros-<distro>-rqt
$ sudo apt-get install ros-<distro>-rqt-common-plugins
```
사용중인 시스템에 맞게 `<distro>` 부분은 변경해서 진행하면 된다. 나는 kinetic으로 진행했다.

이제 `rqt_graph`를 실행시켜보자
``` bash
$ rosrun rqt_graph rqt_graph
```
![210616_1523](/.resource/images/210616_1523.PNG)
위와 같은 화면을 볼 수 있다. 동그란 부분이 node이며, 화살표로 표시된 것이 topic이다. 현재 `/turtle1/cmd_vel`라는 이름을 가진 topic 위에서 `/teleop_turtle` node와 `/turtlesim` node가 서로 통신하고 있음을 알 수 있다.

### rostopic 소개
`rostopic`을 이용하면 ROS topic들에 대한 정보를 얻을 수 있다.
``` bash
$ rostopic -h

...

rostopic bw     display bandwidth used by topic
rostopic echo   print messages to screen
rostopic hz     display publishing rate of topic    
rostopic list   print information about active topics
rostopic pub    publish data to topic
rostopic type   print topic type

...
```
위와 같이 rostopic에는 세부적인 명령이 존재하는 것을 알 수 있다. 각 세부명령들에 대해 알아보자.

### rostopic echo
`rostopic echo` 명령은 topic에 published 되는 데이터를 볼 수 있는 명령이다. 아래와 같이 사용할 수 있다.
``` bash
$ # rostopic echo [topic]
$ rostopic echo /turtle1/cmd_vel
```
이렇게 되면 아래와 같이 `cmd_vel` topic에 publishing 하고있는 `turtle_teleop_key` 노드가 발행하고있는 데이터를 확인할 수 있다.
``` bash
$ rostopic echo /turtle1/cmd_vel
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
```
이 상태에서 다른 터미널에서 `rqt_grpah`를 통해 현재 상태를 확인해보면, rostopic echo 명령을 통해 topic으로부터 데이터를 받아보고 있기 때문에 다음과 같이 subscribe 하고있는 노드가 하나 생성된 것을 확인할 수 있다.
![210616_1539](/.resource/images/210616_1539.PNG)

### rostopic list
`rostopic list` 명령은 현재 활성화되어있는 모든 topic의 리스트를 보여준다.
``` bash
$ rostopic list -h
Usage: rostopic list [/topic]

Options:
  -h, --help            show this help message and exit
  -b BAGFILE, --bag=BAGFILE
                        list topics in .bag file
  -v, --verbose         list full details about each topic
  -p                    list only publishers
  -s                    list only subscribers
```
이 명령에는 세부적인 옵션들이 있는데, `verbose` 옵션을 사용하여 각 topic들에 대한 세부사항을 출력해보자.
``` bash
$ rostopic list -v

Published topics:
 * /turtle1/color_sensor [turtlesim/Color] 1 publisher
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 publisher
 * /rosout [rosgraph_msgs/Log] 3 publishers
 * /rosout_agg [rosgraph_msgs/Log] 1 publisher
 * /turtle1/pose [turtlesim/Pose] 1 publisher

Subscribed topics:
 * /turtle1/cmd_vel [geometry_msgs/Twist] 2 subscribers
 * /rosout [rosgraph_msgs/Log] 1 subscriber
```

### rostopic type
`rostopic type` 명령은 publishing 중인 topic의 message type에 대한 정보를 반환한다.
``` bash
$ rostopic type /turtle1/cmd_vel
geometry_msgs/Twist
```
message에 대한 세부정보는 `rosmsg` 명령을 통해서 확인할 수 있다.
``` bash
$ rosmsg show geometry_msgs/Twist

geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
또는 위 두 명령을 합쳐서 다음과 같이 확인할 수도 있다.
``` bash
$ rostopic type /turtle1/cmd_vel | rosmsg show

geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
이를 통해 turtlesim이 입력받는 데이터의 구조를 알 수 있다. 이제 이를 이용하여 turtlesim에 키보드 입력 데이터를 수동으로 publish 할 수 있다. 

### rostopic pub
`rostopic pub` 명령은 활성화되어있는 topic에 데이터를 publish 할 수 있는 명령이다. 아래와 같이 사용할 수 있다.
``` bash
$ # rostopic pub [topic] [msg_type] [args]
$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```
위 명령은 2.0의 속도와 1.8의 각속도로 이동하라는 단일 메세지를 보내는 명령이다. 각 옵션의 의미는 다음과 같다.
- `-1` : 1번 수행 후 종료.
- `--` : 다음으로 오는 데이터는 옵션이 아닌 데이터 그 자체임을 뜻하는 구분자.

지금은 `-1` 옵션을 주었기 때문에 한번만 수행 후 종료되지만, 이를 반복해서 실행하기 위해서는 `-r` 옵션을 주면 된다. 아래와 같이 사용할 수 있다.
``` bash
$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
```
1Hz 속도로 반복하는 것을 확인할 수 있다. 이제 `rqt_graph`를 이용해서 구조를 다시 확인해보자

![210616_1629](/.resource/images/210616_1629.PNG)

거북이는 계속 원을 그리고 있고, 그래프 상에서는 publishing 중인 node가 하나 더 추가된 것을 확인할 수 있다.

### rostopic hz
`rostopic hz` 명령은 데이터가 publish 되는 주기를 반환한다.
``` bash
$ rostopic hz /turtle1/pose

subscribed to [/turtle1/pose]
average rate: 59.354
        min: 0.005s max: 0.027s std dev: 0.00284s window: 58
average rate: 59.459
        min: 0.005s max: 0.027s std dev: 0.00271s window: 118
average rate: 59.539
        min: 0.004s max: 0.030s std dev: 0.00339s window: 177
average rate: 59.492
        min: 0.004s max: 0.030s std dev: 0.00380s window: 237
average rate: 59.463
        min: 0.004s max: 0.030s std dev: 0.00380s window: 290
```
위 정보를 통해 turtlesim이 대충 60 Hz의 속도로 거북이에 대한 데이터를 publish 하고 있음을 알 수 있다.

## rqt_plot
`rqt_plot`은 topic에 publish 되는 데이터의 지표를 그래프로 나타내는 노드다. 다음 명령으로 실행할 수 있다.
``` bash
$ rosrun rqt_plot rqt_plot
```
실행하면 아래와 같은 화면이 뜨고 일단 아무것도 나타나지 않는다. 좌측 상단의 topic input창에 `/turtle1/pose/x`를 입력하고 엔터를 누르면 x에 대한 그래프가 뜬다. 마찬가지로 `/turtle1/pose/y`도 삽입하면 x와 y에 대한 그래프를 볼 수 있다.
![210616_1648](/.resource/images/210616_1648.PNG)

