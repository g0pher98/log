# Tutorial 15
이번 장에서는 앞서 개발한 service와 client를 사용해본다.
[원문](http://wiki.ros.org/ROS/Tutorials/ExaminingServiceClient)

# 실행
우선 `roscore`로 마스터를 실행해준다.
이후 다음과 같이 노드를 실행할 수 있다.
```
$ rosrun beginner_tutorials add_two_ints_server     (C++)
$ rosrun beginner_tutorials add_two_ints_server.py  (Python)
```
일단 서비스가 열렸지만 요청이 없기 때문에 아무것도 뜨지 않는다.

클라이언트는 아래와 같이 실행할 수 있다.
```
$ rosrun beginner_tutorials add_two_ints_client 1 3     (C++)
[ INFO] [1625424130.256571338]: Sum: 4
$ rosrun beginner_tutorials add_two_ints_client.py 1 3  (Python) 
[ INFO] [1625424130.256571338]: Sum: 4
```
실행하면 서비스에 1과 3에 대한 결과를 요청하고, 답변을 받아 출력한다.
현재 `1 + 3`의 결과인 `4`를 받았음을 알 수 있다.


반면에 서버의 경우 client가 켜지자 마자 요청을 받았기 때문에 server가 실행되는 터미널에도 아래와 같이 로그가 뜬다.
```
[ INFO] [1625424124.213622142]: Ready to add two ints.
[ INFO] [1625424130.256058715]: request: x=1, y=3
[ INFO] [1625424130.256163361]: sending back response: [4]
```