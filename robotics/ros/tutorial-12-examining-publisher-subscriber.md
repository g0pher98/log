# Tutorial 12
이번 장에서는 앞서 개발한 publish 및 subscriber 노드를 사용해본다.
[원문](http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber)


# publisher 실행
우선 `roscore`로 마스터를 실행해준다.
이후 다음과 같이 노드를 실행할 수 있다.
```
$ rosrun beginner_tutorials talker      (C++)
$ rosrun beginner_tutorials talker.py   (Python) 
```
어차피 ros의 구조 하에 관리되므로, 어떤 언어를 사용하든 상관없다. 아무거나 실행해도 된다. 실행 과정에서 오류가 발생할 수 있는데, [oops repo](https://github.com/g0pher98/Oops/blob/main/ros.md)를 참고하길 바란다.

실행하면 아래와 같이 뜬다.
```
[INFO] [WallTime: 1314931831.774057] hello world 1314931831.77
[INFO] [WallTime: 1314931832.775497] hello world 1314931832.77
[INFO] [WallTime: 1314931833.778937] hello world 1314931833.78
[INFO] [WallTime: 1314931834.782059] hello world 1314931834.78
[INFO] [WallTime: 1314931835.784853] hello world 1314931835.78
[INFO] [WallTime: 1314931836.788106] hello world 1314931836.79
```
`hello world`라는 문구가 주기적으로 출력되는 것을 확인할 수 있다.


# subscriber 실행
```
$ rosrun beginner_tutorials listener     (C++)
$ rosrun beginner_tutorials listener.py  (Python) 
```
subscriber도 마찬가지로 언어와 관계없이 아무거나 실행시켜주면 된다. 실행하면 아래와 같이 출력된다.
```
[INFO] [WallTime: 1314931969.258941] /listener_17657_1314931968795I heard hello world 1314931969.26
[INFO] [WallTime: 1314931970.262246] /listener_17657_1314931968795I heard hello world 1314931970.26
[INFO] [WallTime: 1314931971.266348] /listener_17657_1314931968795I heard hello world 1314931971.26
[INFO] [WallTime: 1314931972.270429] /listener_17657_1314931968795I heard hello world 1314931972.27
[INFO] [WallTime: 1314931973.274382] /listener_17657_1314931968795I heard hello world 1314931973.27
[INFO] [WallTime: 1314931974.277694] /listener_17657_1314931968795I heard hello world 1314931974.28
[INFO] [WallTime: 1314931975.283708] /listener_17657_1314931968795I heard hello world 1314931975.28
```
`I heard` 라는 문구가 출력됨을 알 수 있다.