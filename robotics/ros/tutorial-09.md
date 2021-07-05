# Tutorial 9
이번 장에서는 msg 및 srv파일과 rosmsg, rossrv 및 roscp 명령에어에 대해 알아본다.  
[원문](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)

# msg?
`msg`는 ROS가 통신할 때 사용하는 메세지가 어떤 형태로 구성되어있는지 기술되어있는 파일이다. ROS 각 노드가 언어가 다를 수 있기 때문에(python, c++, ...) msg로 명시해주어서 여러 언어가 호환되도록 설정할 수 있는 듯 하다.

## msg 데이터 형태
msg 파일 내용에 들어갈 수 있는 데이터 타입은 다음과 같다.
```
int8, int16, int32, int64 (plus uint*)
float32, float64
string
time, duration
other msg files
배열과 가변길이 배열
```
여기에 추가로 `Header`라는 특수한 형태의 데이터 타입도 존재한다. 실제로 msg 파일을 살펴보면 아래와 같다.
```
Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist
```

## msg 만들어보기
`msg` 파일은 패키지의 `msg 디렉토리`에 위치한다. 예제에서는 `beginner_tutorials`라는 패키지를 이용하여 실습을 진행한다. 다음과 같이 msg 파일을 만들어 볼 수 있다.
``` bash
$ roscd beginner_tutorials # 패키지 디렉토리로 이동
$ mkdir msg # msg 디렉토리 생성
$ echo "int64 num" > msg/Num.msg # .msg 파일 생성 및 데이터 삽입
```
현재 `int64` 타입의 `num` 데이터를 사용하겠다고 `Num.msg` 파일에 삽입했다. 지금은 `echo` 명령으로 한 줄만 삽입했지만, 여러 데이터를 추가해서 더 복잡한 구조의 파일을 만들 수 있다.

`msg` 파일을 생성했다면 `package.xml`를 열어서 주석되어있는 코드 중 아래에 해당하는 코드 부분만 주석을 해제한다.
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
빌드 및 실행 시 메세지 관련 처리에 필요한 부분으로 보이나 아직 자세하게는 알아보지 않아도 될 것 같다. 간단하게 필요한 의존성 패키지를 설정해주는 과정이라고 보아도 무방할 것 같다.

위 설정이 완료되었다면 이번에는 실제 의존성 연결을 하기 위해 `CMakeLists.txt` 파일을 수정해야한다. `find_package()` 라는 함수 부분을 찾아서 다음과 같이 `message_generation` 부분만 추가하면 된다.
```
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```
또한, `catkin_package()`에도 의존성을 명시해주어야 한다.
```
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime
  ...
)
```
다음으로는 `add_message_files()`에 msg 파일을 올려주어야 한다. 주석처리 되어있을텐데, 이를 제거해주고 아래와 같이 설정한다.
```
add_message_files(
  FILES
  Num.msg
)
```

이번에도 주석처리되어있는 `generate_messages()` 함수에서 주석을 제거해서 아래와 같이 만들어준다.
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```
끄읏!

## rosmsg 사용법
``` bash
# rosmsg show [message type]
$ rosmsg show beginner_tutorials/Num
int64 num
$ rosmsg show Num # 패키지명을 생략할 수도 있다.
int64 num
```
위 명령으로 원하는 msg 데이터를 조회해볼 수 있다.

# srv?
`srv`는 ROS 서비스가 받는 데이터에 대한 구조를 나타낸다. `request`와 `response` 이렇게 두 파트로 나누어져있다. 패키지의 `srv 디렉토리`에 위치한다. `srv`도 `msg`와 마찬가지로 ROS 특성상 다양한 언어와의 호환성을 위해 서비스의 데이터 타입을 파일로써 표현하는 것으로 보인다.

우선 다음과 같이 다른 패키지에서 예시로 복사해오자
```
$ roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv
$ cat srv/AddTwoInts.srv 
int64 a
int64 b
---
int64 sum
```
내용을 확인해보면 `---` 와 같은 구분선으로 상/하가 구분되어있다. 여기서 `a, b`가 request이고, `sum`
msg 생성때와 마찬가지로 `package.xml`를 열어서 주석되어있는 코드 중 아래에 해당하는 코드 부분만 주석을 해제한다. 이미 진행했으면 하지 않아도 된다.
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```
`CMakeLists.txt` 파일도 마찬가지로 수정한다.
``` bash
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation # 이곳
)

(...)

add_service_files(
  FILES
  AddTwoInts.srv # 이곳
)
```

## rossrv 사용법
아래와 같이 srv 내용을 확인할 수 있다.
``` bash
# rossrv show <service type>
$ rossrv show beginner_tutorials/AddTwoInts
int64 a
int64 b
---
int64 sum

$ rossrv show AddTwoInts[beginner_tutorials/AddTwoInts]:
int64 a
int64 b
---
int64 sum

[rospy_tutorials/AddTwoInts]:
int64 a
int64 b
---
int64 sum
```
msg와 마찬가지로 패키지 명은 생략할 수 있다. 다만, 현재 서비스가 roscp로 복사한 데이터기 때문에 동일한 이름의 서비스가 두 개가 존재하는 것을 확인할 수 있다.
