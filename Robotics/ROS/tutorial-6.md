# Tutorial 6
이번 장에서는 ROS의 Service와 Parameters에 대해 알아본다.  
[원문](http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams)

# rosservice 명령
ROS에서 service란 각 node가 서로 통신할 수 있는 또 다른 방법이다. 각 node는 service를 통해 요청(request)을 보내고 응답(response)을 받을 수 있다.
## rosservice 세부명령
rosservice 명령은 다음과 같은 세부 명령으로 나누어져 있다.
```
rosservice list         print information about active services
rosservice call         call the service with the provided args
rosservice type         print service type
rosservice find         find services by service type
rosservice uri          print service ROSRPC uri
```

## rosservice list
`list` 명령은 현재 활성화되어있는 service들에 대한 정보를 출력해준다. turtlesim을 실행하고있는 상태이기 때문에 관련 service들도 확인할 수 있다.
``` bash
$ rosservice list

/clear
/kill
/reset
/rosout/get_loggers
/rosout/set_logger_level
/spawn
/teleop_turtle/get_loggers
/teleop_turtle/set_logger_level
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/get_loggers
/turtlesim/set_logger_level
```

## rosservice type
type 명령은 service의 type을 출력한다.
``` bash
$ # rosservice type [service]
$ rosservice type /clear

std_srvs/Empty
```
예시로 `/clear` service의 type을 출력했는데, 해당 서비스는 서비스를 요청하거나 응답받을 때 따로 데이터를 보내거나 받지 않는 서비스이기 때문에 `Empty`가 뜨는 것을 볼 수 있다.

## rosservice call
`call`은 service를 호출하는 명령이다. 앞서 살펴본 `/clear`명령을 호출해보자
``` bash
$ # rosservice call [service] [args]
$ rosservice call /clear
```
인자가 없는 서비스기 때문에 간단하게 실행할 수 있다. 실제로 실행해보면, turtlesim에 그려져있던 선들이 모두 사라지는 것을 확인할 수 있다.

이번에는 인자를 필요로하는 `/spawn` 서비스를 call 해보려고 한다. 먼저 어떤 인자를 받는지부터 살펴보자.
``` bash
$ rosservice type /spawn | rossrv show

float32 x
float32 y
float32 theta
string name
---
string name
```
위와 같이 총 4개의 인자를 받는다. call 명령을 통해 호출해보자
``` bash
$ rosservice call /spawn 2 2 0.2 ""
```
![210619_1](/.resource/images/210619_1.PNG)
거북이가 한 마리 더 스폰된 것을 확인할 수 있다.

# rosparam 명령
ros에서 param은 `설정값` 정도로 보면 될 것 같다. 딱히 통신이라고 할건 아니고, 어떠한 프로그램을 돌릴 때, 수정가능한 옵션정도인 것 같다.

알아두어야 할 부분은 기본적으로 서버 형태로 관리된다는 점이다. ros의 param들을 관리하기 위한 별도의 서버가 local 안에 있다고 생각하면 된다. 그래서 일반적인 파일시스템처럼 파라미터도 `/path/path2/path3/param`과 같이 경로로 표현된다.


## rosparam list
```
$ rosparam list

/background_b
/background_g
/background_r
/rosdistro
/roslaunch/uris/host_localhost__33273
/rosversion
/run_id
```
우선 위와 같이 세부 명령이 있는 것을 알 수 있다. turtle 환경을 설정하는 `/background_r, g, b` 파라미터를 재설정해보자.


## rosparam get & set
``` bash
$ rosparam get /background_r
69
$ rosparam set /background_r 99
$ rosservice call /clear
```
위와 같이 `get` 또는 `set` 세부 옵션으로 파라미터를 조회 및 수정할 수 있다. 지금은 turtle 배경화면의 r, g, b중 r(red)에 해당하는 값을 99로 변경한 후 `/clear`를 통해 새로고침하여 적용했다.

꼭 특정 파라미터를 설정해주지 않아도 디렉토리(?)까지만 `get` 하면 하위 내용까지 다 나오는 것 같다. 아래와 같이 테스트해볼 수 있다.
```
$ rosparam get /

background_b: 255
background_g: 86
background_r: 99
rosdistro: 'kinetic

  '
roslaunch:
  uris: {host_localhost__33273: 'http://localhost:33273/'}
rosversion: '1.12.17

  '
run_id: 11545f5c-dad5-11eb-b9bc-08002712809d
```

## rosparam dump & load
이러한 파라미터를 저장하고 로드할 수 있는데, 다음과 같이 dump를 뜰 수 있다.
``` bash
$ rosparam get /

background_b: 255
background_g: 86
background_r: 99
rosdistro: 'kinetic

  '
roslaunch:
  uris: {host_localhost__33273: 'http://localhost:33273/'}
rosversion: '1.12.17

  '
run_id: 11545f5c-dad5-11eb-b9bc-08002712809d

$ rosparam dump dump.yaml
$ ls

(...)

dump.yaml

(...)

g0pher@g0pher-VirtualBox:~$ cat dump.yaml 
background_b: 255
background_g: 86
background_r: 99
rosdistro: 'kinetic

  '
roslaunch:
  uris: {host_localhost__33273: 'http://localhost:33273/'}
rosversion: '1.12.17

  '
run_id: 11545f5c-dad5-11eb-b9bc-08002712809d
```
`get`으로 출력한 결과가 `dump`를 이용하면 그대로 파일로 저장되는 것을 확인할 수 있다.

이번에는 저장된 파일을 로드하는 과정에 대해서 알아본다.
``` bash
g0pher@g0pher-VirtualBox:~$ rosparam load dump.yaml copy_turtle
g0pher@g0pher-VirtualBox:~$ rosparam get /
background_b: 255
background_g: 86
background_r: 99
copy_turtle:
  background_b: 255
  background_g: 86
  background_r: 99
  rosdistro: 'kinetic

    '
  roslaunch:
    uris: {host_localhost__33273: 'http://localhost:33273/'}
  rosversion: '1.12.17

    '
  run_id: 11545f5c-dad5-11eb-b9bc-08002712809d
rosdistro: 'kinetic

  '
roslaunch:
  uris: {host_localhost__33273: 'http://localhost:33273/'}
rosversion: '1.12.17

  '
run_id: 11545f5c-dad5-11eb-b9bc-08002712809d

```
`load`할 때, 로드할 namespace를 설정할 수 있는데, 위의 경우 `copy_turtle`이라는 네임스페이스를 설정해주었다. `get`으로 살펴보면 `/`에 바로 데이터가 저장되는 것이 아니라 `/copy_turtle` 안에 기존 파라미터들이 그대로 올라간 것을 확인할 수 있다.

