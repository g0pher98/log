# Tutorial 2
ROS도 어떻게 보면 Operating System이다. OS라는 무거운 타이틀을 달고있는 만큼 filesystem이 있고, linux의 기본 명령어로 이러한 파일시스템을 이용하기에는 상당한 불편함이 따른다. ROS는 편의를 위해 파일시스템을 이용할 수 있는 다양한 편리한 명령어들을 제공한다.

## package
ROS에서 package란 소프트웨어를 구성하는 단위이다. ROS가 여러 프로그램을 병렬적으로 처리한다는 점을 고려하면 package는 이러한 프로그램의 구성요소로 볼 수 있을 것 같다.

본 실습에서는 예제 패키지를 이용하여 진행하게 되며, 이를 위해 아래와 같이 튜토리얼 관련 프로그램을 설치해야한다. (*이게 정확히 뭔지는 아직은 잘 모르겠음*)
``` bash
# distro : indigo, kinetic ...
sudo apt-get install ros-<distro>-ros-tutorials
```
`<distro>` 부분에는 Ubuntu 버전에 따라 설치된 ROS 명칭을 입력하면 된다. 나는 16.04 버전 Ubuntu를 사용하기 때문에 `kinetic`을 입력했다.

## rospack 명령어
rospack은 `ros + pack(age)`를 뜻하며, 말그대로 패키지를 관리하는데에 사용하는 명령어다. rospack 명령이 제공하는 기능 중 `find` 기능을 다음과 같이 사용해볼 수 있다.
``` bash
$ rospack find turtle_tf
/opt/ros/kinetic/share/turtle_tf

$ rospack find roscpp
/opt/ros/kinetic/share/roscpp
```
찾고싶은 패키지 이름을 입력하면 해당 패키지가 있는 경로를 알려준다. 정말 친절하다.
> 패키지 이름이 정확히 기억이 안난다?  

그렇다해도 걱정할 필요가 없다. 기본적으로 linux와 같이 tab으로 탐색할 수 있는 기능이 있어서 앞글자만 알아도 패키지를 찾을 수 있고 다음과 같이 `list` 기능을 이용해 전체 패키지를 출력해서 찾을 수 있다.
``` bash
rospack list
```

## roscd 명령어
이 명령도 직관적으로 `ros + cd`임을 알 수 있다. 이것도 정말 편한데, 패키지 디렉터리로 이동하는 비용을 감소시킬 수 있다. 예를 들어 본 명령이 없었다면 다음과 같이 해당 디렉토리로 이동해야한다.
``` bash
$ rospack find roscpp
/opt/ros/kinetic/share/roscpp

$ cd /opt/ros/kinetic/share/roscpp
```
만약 roscd를 이용한다?
``` bash
$ roscd roscpp
```
무려 명령이 반이나 줄었다. 뿐만 아니다. 패키지 내부 경로를 입력하면 알아서 해당 디렉토리까지 이동해준다.
```
$ roscd roscpp/cmake

$ pwd
/opt/ros/kinetic/share/roscpp/cmake
```
눈치를 챘을 수도 있겠지만, 패키지들이 있는 경로는 비슷하다. `tutorial-1`에서 설정해주었던 환경변수를 보면 알 수 있는데, 확인해보면 다음과 같다.
```
$ echo $ROS_PACKAGE_PATH
/home/g0pher/catkin_ws/src:/opt/ros/kinetic/share
```
`:(콜론)`을 기준으로 경로가 나뉘는데, 위의 경우 두 개의 경로가 있다. package를 탐색할 때, 이 환경변수를 참조해서 두 경로에 해당 패키지가 있는지 검색한다. 그렇기 때문에 tutorial-1에서 진행했던 환경 세팅이 중요한 것이다.




추가로, `roscd log` 명령을 이용하면 ROS가 로그 파일을 저장하는 폴더로 이동한다. 원래는 로그가 나오지만 나는 한번도 ROS 프로그램을 실행한적이 없기 때문에 다음과 같이 활성화된 ros가 없다는 오류가 뜬다.
``` bash
$ roscd log
No active roscore
```

## rosls 명령어
이쯤되면 설명 안해도 안다. `ros + ls` 명령이다. 다음과 같이 패키지 내부 파일 및 디렉토리를 나열해준다.
```
$ rosls roscpp_tutorials/
cmake  launch  package.xml  srv
```