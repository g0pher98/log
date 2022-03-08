# Tutorial 10
이번 장에서는 C++에서의 publish 및 subscriber 노드를 생성하는 방법에 대해 소개한다.
[원문](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)

# publisher node 개발
```
$ roscd beginner_tutorials
$ mkdir -p src
```
기본적으로 노드 관련 코드는 패키지 내부의 `src` 디렉터리에 존재한다. 코드 생성 이전에 `src` 폴더가 없다면 생성해주어야 한다.

디렉토리가 준비되었다면 `src/talker.cpp`에 아래와 같이 코드를 작성하자 
```  c++
#include "ros/ros.h" // ROS 관련 코드를 사용하기 위한 include문.
#include "std_msgs/String.h"

#include <sstream>

/**
 * 이 코드는 ROS로 messages 통신을 하는 과정에 대한 코드다.
 */
int main(int argc, char **argv)
{
  /**
   * ros::init()
   * 이 함수는 실행 시 전달되는 인자(argc 및 argv)를 사용하여 ros::init을 진행한다.
   * 앞 두 인자는 기본적으로 들어가기 때문에 일단은 크게 중요하지 않고,
   * "talker"라는 문자열이 전달된 세 번째 인자는 노드 이름이다.
   * 추후 이 코드가 실행되는 노드에 접근 시, talker로 접근하면 되는 듯 하다.
   * 물론 노드 이름은 시스템에서 유일해야한다.
   */
  ros::init(argc, argv, "talker");

  /**
   * NodeHandle은 ROS 통신을 위해 node를 관리할 수 있는 주요한 기능이다.
   * 선언되면 노드가 초기화되고, 종료되면 노드가 닫힌다.
   */
  ros::NodeHandle n;

  /**
   * advertise() 함수는 ROS에 publish할 수 있는 방법이다.
   * 첫 번째 인자를 보면 chatter라는 topic에 publish 하는 것을 알 수 있다.
   * 두 번째 인자를 보면 publish하는 데이터를 보관할 수 있는 용량을 1000개로 잡고있음을 알 수 있다.
   */
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  ros::Rate loop_rate(10); // 데이터를 보내기 위한 텀(Hz). 일시적으로 잠깐 멈춤.

  /**
   * count 변수는 총 보낸 메세지 개수를 세기 위함.
   * 이는 각 메세지 별 고유값을 생성하기 위함.
   */
  int count = 0;
  while (ros::ok())
  {
    /**
     * 아래에 선언한 msg가 실제 메세지에 해당하는 부분이다.
     * 이 변수를 채운 후에 publish 하면 된다.
     */
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());

    /**
     * publish() 함수는 실제로 메세지를 보내는 방법이다. 
     * 인자로 message를 받는다. 이 message의 타입은 파라미터 타입과 일치해야한다.
     */
    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}
```

# subscriber node 개발
`src/listener.cpp`에 아래와 같이 코드를 작성한다.
``` c++
#include "ros/ros.h"
#include "std_msgs/String.h"

/**
 * 이번에는 subscribe하는 코드를 작성하는 법에 대해 알아본다.
 */
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;

  /**
   * 반대로 1000개의 메세지가 가득 차면 그때부터 수신받으면서 오래된 메세지를 하나씩 없애나간다.
   * 데이터가 들어올 때 반응할 chatterCallback 함수도 인자로 설정되어있음을 알 수 있다.
   */
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();

  return 0;
}
```

# 빌드!
앞서 작성한 코드를 node로 실행하기 위해서는 우선 실행 가능한 형태로 빌드해야한다. 우선 의존성 문제부터 해결하기 위해 CMakeLists.txt 파일을 수정한다.

``` bash
cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES Num.msg)
add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

## 위의 항목들 확인이 끝났으면 아래 내용을 가장 밑에 추가
add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener beginner_tutorials_generate_messages_cpp)
```
이후 `catkin_make`와 `source` 명령을 통해 빌드를 완료한다.