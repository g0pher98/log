# How to install ROS
많은 한국 자료가 Ubuntu를 사용하기 때문에, `Ubuntu 16.04`에서 ROS를 구동하고자 한다. ROS에 집중하기 위해 ubuntu 설치에 대한 내용은 다루지 않으며, 설치는 표윤석 박사님이 공유해주신 [스크립트](https://cafe.naver.com/openrt/14575)를 이용하여 간단하게 진행한다.

여러 글과, 스크립트 개발자의 글에서도 가상환경에서는 구동하지 말라고 했지만 똥고집을 부려보고자 한다. ~~아무리 생각해도 멀티부팅은 마음에 안들어서~~

## 스크립트 다운로드 및 실행
본 스크립트는 Ubuntu 16.04 LTS 버전에 최적화되어있는 코드다. Ubuntu 버전이 다르다면 해당 버전에 맞는 스크립트를 찾는게 정신건강에 좋다.
``` bash
#스크립트 다운로드
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_kinetic.sh
```

``` bash
# 실행이 가능하도록 권한설정
chmod 755 ./install_ros_kinetic.sh
# 실행
./install_ros_kinetic.sh
```
위와 같은 명령을 통해 수많은 설치 과정을 간단하게(~~2시간 걸리던데요 선생님;;~~) 진행할 수 있다.

스크립트가 아닌 자세한 설치과정이 궁금하다면 [레퍼런스](#Reference) 참조.

## 설치 확인

설치가 끝났다면 `roscore` 명령을 입력했을 때, 아래와 같이 정상적으로 실행이 되면 설치가 완료된 것이다.
![roscore](/.resource/210316_0251.PNG)  
그러나 개발자분이 마지막에 신경을 써주시지 못한 부분이 있어서 `roscore`을 실행하면 오류가 발생한다.
``` bash
source ~/.bashrc
```
위 명령을 통해 설치한 내용을 적용하면 정상적으로 잘 작동한다.



# Reference
### 2장 ROS 설치하기
https://robertchoi.gitbook.io/ros/install
### [ROS] ROS Kinetic install on Ubuntu 16.04.1 LTS
https://m.blog.naver.com/opusk/220984001237