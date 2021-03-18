# Tutorial 3
이번 장에서는 패키지를 직접 생성해본다.

## 패키지 구성 조건
패키지를 생성하기 위해 패키지의 구조에 대해 알아야 한다. 간단하게 다음과 같은 구조로 이루어져있다.
```
my_package/
    CMakeLists.txt
    package.xml
```
내가 원하는 패키지 명(*e.g. my_package*)이 있을 것이다. 우선 디렉토리를 하나 생성하고, 그 안에 `CMakeLists.txt`와 `package.xml` 파일을 만들어야 한다. 각각 다음과 같은 역할을 한다.
- package.xml  
    패키지에 대한 기본, 상세 정보들을 포함하고 있다.
- CMakeLists.txt  
    catkin을 사용하는 패키지를 사용한다면 이 파일이 있어야 한다.

> ***catkin?***  
> *과거 rosbuild가 사리지고 새로나온 ros build 시스템*

## catkin Workspace
기본적으로 단일 패키지만 가지고도 독립적으로 빌드가 가능하지만, ros에서는 workspace를 생성하는 것을 권장하고 있다. 간소화된 catkin workspace 구조는 다음과 같다.
```
workspace_folder/        -- catkin 워크스페이스
  src/                   -- 소스 디렉토리
    CMakeLists.txt       -- 최상위 CMake 파일.
    package_1/
      CMakeLists.txt     -- package_1 패키지의 CMake 파일 
      package.xml        -- package_1 패키지의 manifest 파일
    ...
    package_n/
      CMakeLists.txt     -- package_n 패키지의 CMake 파일 
      package.xml        -- package_n 패키지의 manifest 파일
```
간단한 구조인데, 간단해보이지 않는다고 해서 두려워할 것은 없다. 이미 1장에서 catkin_make로 `/home/catkin_ws/` 디렉토리를 workspace로 구성해두었다.

## 패키지 생성
다음과 같이 workspace에서 `catkin_create_pkg` 명령으로 catkin 패키지를 생성할 수 있다.
``` bash
cd ~/catkin_ws/src
catkin_create_pkg my_test_pkg std_msgs rospy roscpp
```
위 명령에 뭐가 많긴 한데 떼어보면 별것 없다. `catkin_create_pkg` 명령으로 `my_test_pkg`라는 이름의 패키지를 생성해주는 것이다. 추후 다루겠지만 개발 과정에서 필요한 다른 패키지들을 포함시켜두어야 하는데 이를 **의존성**이라고 하며, `std_msgs`와 `rospy`, `roscpp`가 그것이다. 추가 패키지는 나중에 다시 다루겠지만, 간단히 각 추가 패키지의 역할은 다음과 같다.
- std_msgs : 노드간 메세지 송수신
- rospy : python 패키지
- roscpp : C++ 패키지

아무튼 위 명령을 통해 패키지를 생성하면 다음과 같이 디렉토리가 생성된 것을 확인할 수 있다.
``` bash
$ ls ~/catkin_ws/src/
CMakeLists.txt  my_test_pkg

$ ls ~/catkin_ws/src/my_test_pkg/
CMakeLists.txt  include  package.xml  src
```
앞서 설명한 workspace 구조와 기반은 같고, 추가로 파일 몇개가 더 생성되어있음을 알 수 있다.

## workspace 빌드
앞서 패키지를 생성하며 workspace 구조를 완성했다. 이제 준비가 되었으니 실제로 이 workspace를 사용할 수 있도록 빌드하는 과정이 필요한데 정말 간단하다.
``` bash

```
