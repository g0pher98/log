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

3. 간단한 앱 개발
    - Constrain Layout
        - 가로, 세로 하나의 기준점이 있기만 하면 자리가 정해짐.
        - 하나라도 정해지지 않을 경우 해당 축의 처음으로 이동하는데, 좌측 상단이 기준임.
    - xml에서 button 생성
        - layout_width, layout_height는 필수
        - 안드로이드에서 크기는 보통 "dp" 라는 단위를 사용
        - wrap_content 크기를 주면 내용물에 따라 유연하게 늘어남.
        - match_parent 크기를 주면 부모에 맞춤. layout일 경우 layout에 맞게 최대치로 늘어남.
        - 0dp를 주면 match_constraint 크기를 갖게 되며, 동일 layer의 object를 제외하고 최대치로 늘어남.
    - 모든 위젯에는 id 속성이 있음
        - id : object를 찾을 때, 접근할 때 사용하는 구분정보.
            - `@+id/NewId`
                - `@` : 앱에
                - `+id` : id를 추가한다
                - `/NewId` : 다음 데이터로
        - 접근 시 `R.id.NewId` 형태로 접근.
            - R이라는 리소스 영역에 정수형 상수로 저장됨.