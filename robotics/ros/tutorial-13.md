# Tutorial 13
이번 장에서는 C++에서의 service와 client 노드를 생성하는 방법에 대해 소개한다.
[원문](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29)

# service node 개발
`src/add_two_ints_server.cpp`에 아래와 같이 코드를 작성한다.
``` c++
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"

bool add(beginner_tutorials::AddTwoInts::Request  &req,
         beginner_tutorials::AddTwoInts::Response &res)
{
  /*
   * bool add()
   * 두 int를 받아들여서 합하고, bool 형 결과값을 반환하는 함수.
   * 서비스 요청이 들어오면 실행된다.
   */

  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  // 노드 생성
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHandle n;

  // advertiseService() 함수를 통해 ros에 advertise 된다.
  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}
```

# client node 개발
`src/add_two_ints_client.cpp`에 아래와 같이 코드를 작성한다.
``` c++
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  // 노드 생성
  ros::init(argc, argv, "add_two_ints_client");
  
  // 실행인자 검사. 명령어 포함 3개(인자가 2개)가 아니라면 종료.
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;

  // 실제 client를 생성하는 부분
  ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");

  // service 클래스 인스턴스를 생성하고, 인자값 저장.
  beginner_tutorials::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  
  // 실제로 service를 call하는 부분
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0;
}
```

# 빌드!
`CMakeLists.txt` 파일에 아래와 같이 추가한다.
```
add_executable(add_two_ints_server src/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server beginner_tutorials_gencpp)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client beginner_tutorials_gencpp)
```
이후, catkin_make를 진행한다.
```
$ cd ~/catkin_ws
$ catkin_make
```
