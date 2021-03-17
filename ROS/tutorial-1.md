# Tutorial 1
ROS를 설치하고 나서, 기본적인 환경 구성에 대해 알아본다.

## 환경관리
``` bash
env | grep ROS
```
위 명령어를 통해 ROS 프로그램에 정상적으로 접근할 수 있도록 환경이 세팅되어있는지 먼저 확인해야 한다. 만약 위 명령을 실행했을 때, 아무런 결과도 나타나지 않는다면, 아래 명령어로 세팅을 다시 해주어야한다.
``` bash
source /opt/ros/kinetic/setup.bash
```
나의 경우, 처음 설치했을 때 해당 콘솔의 환경에 바로 반영되지 않아서 `~/.bashrc`를 재설정해주었다. 그냥 콘솔을 껐다가 다시 켜도 된다.

## ROS Workspace 생성하기
ROS 설치가 되었다면, `/home` 디렉토리에 `catkin_ws`라는 공간이 생긴 것을 확인할 수 있다. 다음과 같이 해당 디렉토리에 가서 workspace를 형성해줄 수 있다.
``` bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
실제로 workspace를 만드는 것은 `catkin_make` 명령어가 진행한다. 이 명령어를 실행하기 위해 src 디렉터리가 필요해서 만든 것으로 생각된다. 실제로 src 디렉토리에 들어가보면 `CMakeLists.txt` 파일이 생성된 것을 아래와 같이 확인할 수 있다.
``` bash
$ cd ~/catkin_ws/src/

$ ls -al
total 8
drwxrwxr-x 2 g0pher g0pher 4096  3월 16 02:23 .
drwxrwxr-x 5 g0pher g0pher 4096  3월 16 02:23 ..
lrwxrwxrwx 1 g0pher g0pher   50  3월 16 02:23 CMakeLists.txt -> /opt/ros/kinetic/share/catkin/cmake/toplevel.cmake
```
또한, src 말고도 `build`와 `devel` 디렉토리가 형성된 것을 아래와 같이 확인할 수 있다.
``` bash
$ cd ~/catkin_ws

$ ls
build  devel  src

$ ls build
atomic_configure  catkin_make.cache    CTestConfiguration.ini  Makefile
catkin            CMakeCache.txt       CTestCustom.cmake       test_results
catkin_generated  CMakeFiles           CTestTestfile.cmake
CATKIN_IGNORE     cmake_install.cmake  gtest

$ ls devel
cmake.lock  lib               local_setup.sh   setup.bash  _setup_util.py
env.sh      local_setup.bash  local_setup.zsh  setup.sh    setup.zsh
```
이제 작업공간이 구성되었으니, 이 공간을 활용할 수 있도록 작업환경을 구성해주어야 한다. 다음과 같이 bash 파일을 환경에 올리면 된다.
``` bash
source devel/setup.bash
```
작업환경이 제대로 설정되었는지 확인하기 위해 아래와 같이 `ROS_PACKAGE_PATH` 환경변수를 출력해본다.
``` bash
$ echo $ROS_PACKAGE_PATH
/home/g0pher/catkin_ws/src:/opt/ros/kinetic/share
```
위와 같이 경로들이 잘 뜨면 제대로 설정이 되었다고 볼 수 있다.