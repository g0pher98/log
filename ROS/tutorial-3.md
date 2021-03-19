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
cd ~/catkin_ws
catkin_make
```
이제 `devel` 디렉토리 안을 보면 bash 파일이 생긴것을 볼 수 있다. 코드 살펴보면 결국에 sh 파일을 실행시키는거긴 한데, 공홈에서는 bash 실행시키는 것으로 설명되어 있으니 잔말말고 따르기로 했다.
``` bash
. ~/catkin_ws/devel/setup.bash
```
위 명령을 통해 workspace를 ROS에 올릴 수 있다고 한다.

## 패키지 의존성
의존성은 생각보다 어려운 개념이 아니다. 대부분의 프로그램이 컴퓨터의 아주 LOW한 작업부터 개발하진 않는다. WINDOW라는 OS가 ROW한 컴퓨터 자원을 관리하고, 이러한 관리 위에 각종 모듈들이 존재한다. 이러한 것들이 겹치고 겹쳐 코드 한 줄 만으로도 많은 기능을 할 수 있게 만들 수 있게 된다.

예를 들어 게임을 개발하는 것도 3D 공간상의 Object의 위치, 총알에 대한 중력계산 등과 같이 게임에 있어서 중요하긴 하지만, 하나하나 구현할 필요가 없다. 이미 어느정도 중력을 계산해주는 모듈이 존재하고, 그냥 이미지와 메인 로직을 구성해놓고 해당 모듈을 사용하기만 하면 어느정도는 잘 돌아간다. 그러나, 이러한 모듈과 같이 구축된 환경(*e.g. window*)이 바뀌거나 없다면 게임은 실행에 문제가 발생할 수 있다. 실제로 linux에서도 게임을 돌아가게 하려면 게임회사에서 리눅스 환경에 맞게 다시 개발해야한다. 그렇기 때문에 대부분 어떠한 모듈이나 환경에 의존적일 수 밖에 없고, 이 의존성을 지켜주어야 프로그램이 잘 돌아간다.

일전에 생성했던 `my_test_pkg` 패키지의 의존성을 `rospack의 depends1`명령을 통해 확인해보자.
``` bash
$ rospack depends1 my_test_pkg 
roscpp
rospy
std_msgs
```
패키지를 가장 처음 생성할 때, 옵션으로 주었던 패키지들이 의존성 리스트에 나타나는 것을 알 수 있다. 이것들이 본 패키지의 **1차 의존성**에 해당(*1차 의존성이기 때문에 depends1 명령을 이용*)하며, `package.xml` 파일에 저장된다. 해당 파일은 아래와 같이 확인할 수 있다.
``` xml
$ roscd my_test_pkg
$ cat package.xml 

<?xml version="1.0"?>
<package format="2">
  <name>my_test_pkg</name>
  <version>0.0.0</version>
  <description>The my_test_pkg package</description>

  <maintainer email="g0pher@todo.todo">g0pher</maintainer>

  <license>TODO</license>

  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>rospy</build_export_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>std_msgs</exec_depend>
</package>
```
xml 파일로 구성되어 있으며, 주석을 제외하면 위와 같다. 의존성 패키지가 있는 것을 확인할 수 있다.

한가지 알아야 할 것은 `my_test_pkg` 패키지가 여러 패키지에 의존하듯이, 이러한 패키지들도 또 다른 패키지에 의존할 수도 있다. `my_test_pkg`가 직접적으로 의존하지는 않지만, 간접적인 의존성을 가지고 있다고 볼 수 있는데, rospy를 예로 들 수 있다.
``` bash
$ rospack depends1 rospy
genpy
roscpp
rosgraph
rosgraph_msgs
roslib
std_msgs
```
위와 같이 rospy의 의존성을 가지고 있는 패키지들이 존재하는 것을 알 수 있다. 이러한 간접적인 의존성을 가진 패키지는 패키지 생성시 굳이 선언해주지 않아도 패키지가 재귀적으로 의존성 패키지를 로드하기 때문에 크게 신경쓰지 않아도 된다.  

그럼에도 한 패키지가 의존성을 가지는 모든 패키지를 확인하고 싶다면 아래와 같이 `depends` 명령을 이용하면 된다.

```
$ rospack depends my_test_pkg 
cpp_common
rostime
roscpp_traits
roscpp_serialization
...
roslib
rospy
```

## 패키지 customizing
패키지를 커스터마이징 하기 위해 구성요소였던 몇몇 파일을 직접 접근해서 수정할 수 있다. `package.xml`을 열어보면 다음과 같은 내용을 확인할 수 있다.
``` xml
<?xml version="1.0"?>
<package format="2">
  <name>my_test_pkg</name>
  <version>0.0.0</version>
  <description>The my_test_pkg package</description>

  <maintainer email="g0pher@todo.todo">g0pher</maintainer>

  <license>TODO</license>

  <buildtool_depend>catkin</buildtool_depend>

  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>

  <build_export_depend>roscpp</build_export_depend>
  <build_export_depend>rospy</build_export_depend>
  <build_export_depend>std_msgs</build_export_depend>

  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>std_msgs</exec_depend>

  <export>
  </export>
</package>
```
하나씩 차근차근 알아보자. 우선 가장 상단에 있는 프로젝트 기본 설명과 관련된 태그를 살펴보자
``` xml
<name>my_test_pkg</name>
<version>0.0.0</version>
<description>The my_test_pkg package</description>

<maintainer email="g0pher@todo.todo">g0pher</maintainer>

<license>TODO</license>
```
각 태그는 다음과 같은 역할을 한다.
- `name` : 패키지 이름.
- `version` : 현재 패키지 버전.
- `description` : 패키지에 대한 설명.  
  가능하면 한줄로 짧게 작성하는것을 권고하고있다.
- `maintainer` : 프로젝트 관리자에 대한 정보.
- `license` : 프로젝트 라이센스 명시.  
  *e.g. BSD, MIT, GPL, ...*

그 아래에 있는 의존성 태그들은 종속성에 관련된 패키지로, `build_depend`와 `exec_depend`로 나누어서 **빌드 시 필요한 패키지**와 **실행 시 필요한 패키지**를 따로 구분해서 명시할 수 있다.

