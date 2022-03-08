# Tutorial 11
이번 장에서는 python에서의 publish 및 subscriber 노드를 생성하는 방법에 대해 소개한다.
[원문](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

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

