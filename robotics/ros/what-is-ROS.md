# What is ROS?
`ROS`는 Robot Operating System의 약자로, `오픈소스 기반` 로봇설계 꿀툴이다. ROS의 OS가 무려 Operating System의 약자여서 Linux나 window같은 os와 착각할 수 있는데, 다르다. 그저 operating 하는 system이라는 점에서 os인 것이고, OS 위에서 돌아가는 일반적인 사용자 프로그램이다.

사용법이 쉬워보이진 않지만, 무척 체계적인 구조로 추상화가 되어있어서 저수준으로 센서나 하드웨어 모듈을 개발하지 않아도 설계를 진행할 수 있는 프로그램인 것 같다.

추상화도 추상화지만 기본적으로 제공하고 확장으로 추가할 수 있는 모듈이 많아서 저수준 개발은 대부분 퉁칠 수 있으니 꿀이 뚝뚝 떨어지는 툴이 아닐수가 없다.

## 목표
ROS의 궁극적인 목표는 로봇연구 및 개발에 있어서 `코드 재사용성`을 높이는 것이다. 즉, 내가 굳이 개발하지 않아도 선대 개발고수님들이 만들어놓으신 기능들을 친히 가져다 사용하는 것을 장려한다는 것. 보안적인 측면에서는 그리 좋은 방법은 아니지만 이는 설계 구현에 있어서 시간을 매우 크게 단축해서 생산성을 높일 수 있다.

ROS는 대규모 런타임 시스템과 개발 프로세스에 적합하고자하는 목표를 가지고 있다. 이를 위해 다양한 방법을 통해 개발 프로세스를 간소화 하는데, 대표적인 예가 앞서말한 추상화다. 또한, 추상화 되어있는 모듈들을 개별적으로 실행하고, 각 프로세스(*ROS에서는 node라고 함*)를 분산처리하는 구조를 가지고 있다. 이렇게 구현된 프로세스들을 패키지로 묶어서 공유할 수 있어, 협업에도 능하다. 그야말로 효자.

언어 독립성을 목표로 하기 때문에 다양한 언어로 구현할 수 있어, 수많은 로봇공학자들의 등긁개가 되어주지 않았을까 조심스레 생각해본다.

## 국내 커뮤니티
- [Oroca](http://www.oroca.org/)  
    로봇공학과 관련된 다양한 공개강좌, 세미나, 모임 등이 활성화 되어있는 네이버카페.
- [로봇공학을 위한 열린 모임 페이스북](https://www.facebook.com/groups/KoreanRobotics)  
    일반인과 전문가가 로봇 관련 정보를 공유하는 페이스북 그룹.
- [로봇소스](https://community.robotsource.org/)  
    글로벌 커뮤니티 형태로, DIY 로봇 관련 자료가 공유되어있다.

# Reference
### ROS Introduction
http://wiki.ros.org/ROS/Introduction
### 1장 ROS 개론
https://robertchoi.gitbook.io/ros/1
### [ROS] 1-1. ROS(Robot Operating System) 소개
https://taemian.tistory.com/entry/ROSRobot-Operating-System-%EC%86%8C%EA%B0%9C