# Tutorial 14
이번 장에서는 python에서의 service와 client 노드를 생성하는 방법에 대해 소개한다.
[원문](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

# service node 개발
`scripts/add_two_ints_server.py`에 다음과 같이 코드를 작성한다.
``` python
#!/usr/bin/env python

from __future__ import print_function

# 이전에 생성했던 srv 파일을 import.
from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    '''
    handle_add_two_ints()
    서비스 요청이 들어오면 실행되는 함수.
    '''

    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))

    # 두 값의 합을 반환
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    # 노드 생성
    rospy.init_node('add_two_ints_server')

    # 서비스 생성. 실행 요청이 들어오면 handle_add_two_ints() 함수 실행.
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
```
생성 후 아래와 같이 실행권한을 추가한다.
``` bash
$ chmod +x scripts/add_two_ints_server.py
```

이후 `CMakeLists.txt`에 다음 내용을 추가한다.
``` bash
catkin_install_python(PROGRAMS scripts/add_two_ints_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

# client node 개발
`scripts/add_two_ints_client.py`에 다음과 같이 코드를 작성한다.
``` python
#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def add_two_ints_client(x, y):
    '''
    add_two_ints_client()
    실제 요청하는 함수
    '''

    # 서비스를 사용할 수 있을 때 까지 대기.
    rospy.wait_for_service('add_two_ints')

    try:
        # 서비스를 마치 일반적인 함수처럼 사용할 수 있도록 구성(proxy)
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)

        # 일반 함수처럼 서비스를 사용하는 모습
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    # 인자값 두 개를 받았을 때만 진행
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
```
생성 후 아래와 같이 실행권한을 추가한다.
``` bash
$ chmod +x scripts/add_two_ints_server.py
```

이후 `CMakeLists.txt`에 다음 내용을 추가한다.
``` bash
catkin_install_python(PROGRAMS scripts/add_two_ints_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```



# publisher node 개발
```
$ roscd beginner_tutorials
$ mkdir -p scripts
$ cd scripts
```
파이썬 스크립트 작성을 위해 scripts 디렉토리를 만든다.

디렉토리가 준비되었다면 `talker.py`에 아래와 같이 코드를 작성하자. 각 함수는 cpp때와 비슷하게 네이밍 되어있으니 자세한 설명은 생략한다.

``` python
#!/usr/bin/env python

import rospy # ros node 작성을 위해 필요
from std_msgs.msg import String # message 전송을 위해 자료형을 표현하는 용도로 필요

def talker():
    # chatter라는 topic에 publish 할 것임을 설정
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # talker라는 publish node 생성
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str) # 실제 publish
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
```
위와 같이 코드를 작성하고 `+x` 권한을 부여한 뒤, `CMakeLists.txt` 파일에 아래 내용을 추가한다.
``` bash
catkin_install_python(PROGRAMS scripts/talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

# subscriber node 개발
`lisdtener.py` 파일을 생성한 뒤 다음 코드를 추가한다.
``` python
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)

    rospy.spin() # 노드가 종료될 때까지 종료되지 않도록 함.

if __name__ == '__main__':
    listener()
```

# 빌드!
```
$ catkin_make
$ source devel/setup.bash
```

