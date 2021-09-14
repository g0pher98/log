1. Android 소개
    - 특징
        - 리눅스 기반의 커널
        - 앱 개발 언어 : java, kotlin, c++
        - 오픈소스
    - 아키텍처  
        ![image](https://user-images.githubusercontent.com/44149738/133154116-96d432b4-b81b-4bab-8021-8387df5c7a55.png)  
        - Linux Kernel
        - HAL (Hardware Abstraction)
        - ART (Android runtime)
        - Native C/C++ libraries
        - java API framework
        - System Apps

    - 커널
        - 저수준 관리 기능, 메모리 관리, HW 접근, 보안 등의 기능이 있음
        - 카메라, 터치스크린, GPS 등을 사용하기 위해 사용
    - HAL(Hardware Abstraction Layer)
        - 하드웨어에 접근하기 위해 추상화된 영역
    - ART (Android runtime)
        - 쉽게 말해 virtual machine. jvm 대신 사용.
        - vm 특성상 성능저하는 있음.
    - Native C/C++ libraries
        - android NDK
    - java API framework
        - 실제로 개발자가 사용하는 API

2. Android Studio
    - 안드로이드를 pc에서 돌릴 수 있도록 예뮬레이팅을 지원하는 AVD(Android Virtual Device)를 지원함.