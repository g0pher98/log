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
    - 안드로이드 애플리케이션 resource
        - drawable
            - 그림파일
        - layout
            - 앱 레이아웃
        - mipmap
            - 아이콘
        - values
            - colors.xml : 색 관련 값
            - strings.xml : 문자 관련 값
                - `<string name="submit">제출</string>` 형태로 선언
                - `@string/submit` 형태로 사용
    - View
        - textview, button 등 눈에 보이는 객체는 모두 view라고 부른다.
        - 원하는 view 객체에 접근하기 위해서는 `findViewById()`를 사용하면 된다.
            - findViewById(R.id.myView)
    - 버튼 클릭 이벤트
        ```java
        public void onClickButton(View v) {
            Toast.makeText(this, "제출되었습니다", Toast.LENGTH_SHORT).show();
        }
        ```
        - 이벤트를 직접 설정해줄 수도 있음
            ```java
            TextView title = (TextView) findViewById(R.id.title1);
            title.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Toast.makeText(getApplicationContext(), "회원가입을 진행중입니다", Toast.LENGTH_SHORT).show();
                }
            });
            ```
    - 안드로이드 프로젝트 구조
        - `/java` : java 코드
        - `/res` : 리소스 모음
        - `/manifests` : 어플리케이션 정보를 저장
            - 아이콘, 앱 이름, 테마, activity 정보 등이 존재
        - `/Gradle Scripts` : 컴파일 시 필요 파일 존재. 민감하니 가능한 건드리지 말기.

4. View
    - 화면에 보여지는 모든 것들은 View 클래스를 상속해서 만들어짐.
    - layout의 경우 ViewGroup을 상속받음
    - ![image](https://user-images.githubusercontent.com/44149738/138570461-b320354c-db1e-4878-b0bc-55958ce36fc6.png)
    - View를 직접 쓸 일은 거의 없음. 대부분 상속받은 뒤쪽 클래스들을 사용.
    - view의 속성
        - 모든 object들이 공통으로 갖게되는 속성
        - id : 위젯의 id
            - `@+id/button1` 포맷으로 선언
            - `(Button)findViewById(R.id.button1)` 형태로 찾음.
        - layout_width, layout_height
            - 가로세로 크기
            - 절대적, 상대적 다 가능
            - match_parent
                - 내부 view에 맞춤
            - wrap_content
                - 상위 레이아웃에 맞춤
        - background
            - `#RRGGBB` 포멧의 색상 사용
            - `#aaRRGGBB` 형태의 투명도 설정도 가능
        - padding
            - 위젯 내부 object와 위젯 사이의 공간
        - margin
            - 위젯 바깥쪽 여백
        - visibility
            - gone(2) : 그냥 없는 것
            - invisiable(1) : 있는데 안보임
            - visible(0) : 보임.
        - enabled, clickable
            - true/false 값을 가짐
            - enabled : 비활성화 여부
            - clickable : 클릭 시 이벤트 유무.
    - 단위
        - px(pixels) : 픽셀의 크기가 기기마다 다름. -> 모바일에서는 되도록 쓰지말자.
        - in(inches) : 실제 인치 크기
        - mm(milimeters) : 실제 mm크기
        - pt(points)
        - dp(density-independent pixels) : 제일 많이 씀. 단위면적당 들어가는 픽셀수.
        - sp(scale-independent pixels) : dp와 같으나, 사용자의 글씨 크기에 맞춤. font size에 많이 사용.

5. basic widget
    - TextView
        - 텍스트를 보여줄 때 사용.
        - 보여지기만 하고, 사용자가 수정은 안됨.
            - EditText 라고 따로 있음.
        - 속성
            - text
            - textColor
            - textSize
            - textStyle : bold | italic | normal
            - singleLine : 레이아웃을 넘어갔을 시 줄바꿈 여부(싱글라인인 경우 넘어가는건 ... 처리됨)
        - java코드에서 수정
            - ![image](https://user-images.githubusercontent.com/44149738/138571743-f33dbdf0-3e35-46b9-a724-f26a67e47383.png)
    - button
        - 버튼
        - setOnclickListener() 메소드로 클릭 이벤트 지정해줌
            ``` java
            b.setOnclickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Toast.makeText(getApplicationContext(), "Click!", Toast.LENGTH_SHORT).show();
                }
            })
            ```
    - EditText
        - input창
        - input의 성격에 따라 속성이 다름.(비번, 이메일, 숫자 등)
        - getText() 메소드는 Editable 객체를 반환.
            - string으로 사용하고 싶으면 toString()으로 변환해주면 됨.
    - CompoundButtons
        - 클릭할 때마다 상태가 바뀌는 버튼
        - button을 상속한 클래스
        - subclasses
            - CheckBox
            - RadioButton
                - 이 객체는 radio group을 이용해서 객체들을 묶어주어야 한다.
            - Switch
            - ToggleButton
        - isChecked() 메소드를 이용해서 체크 여부를 확인
        - setOnCheckedChangeListener를 통해서 체크가 변경되었을 때를 감지
            ```java
            c.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
                @Override
                public void onCheckedChanged(CompoundButton compundButton, boolean b) {
                    if (b) {
                        // ...
                    }
                }
            })
            ```
    - ImageView & ImageButton
        - 이미지를 표시 및 이미지가 들어간 버튼
        - ImageView가 View를 상속
        - ImageButton이 ImageView를 상속
        - image는 `res/drawable`에 넣어두고 `@drawable/ImageID` 형태로 가져온다.
        - attributes(속성)
            - src : 이미지 참조
            - maxHeight
            - maxWidth
            - scaleType : 이미지 확대/축소/이동 등을 할 때 사이즈를 어떻게 맞출 것인지 설정.
        - 이미지 등록
            - 파일명은 변수명 설정과 동일한 규칙을 따르도록 수정해야한다.
            - xml로 이미지를 만들 수 있음. (like svg)
            - 드래그앤드롭으로 넣을 수 있음.
        - xml에서 `app:srcCompat="@drawable/sample1"` 이렇게 삽입할 수 있다.
        - java에서 image를 넣는 방법
            - setImageDrawable() 사용하지 말것!!!
            - setImageResource(R.drawable.sample2) 사용

6. Layout
    - overview
        - user interface를 선언하는 것
        - attributes
            - orientation : 가로세로
            - gravity : 어디를 기준으로 배치될 것인가. 블록이 쌓이는 기준
            - padding
            - layout_weight : 비율 설정
            - baselineAligned : 글씨의 가장 하단 줄을 맞추는 옵션
        - layout type
            - constraint layout
                - 반응형을 만들기 위함.
            - linear layout
                - 한 방향으로 선형으로 배치할 때 사용
                - 구조가 유연하지는 않음.
            - frame layout
            - table layout
    - linear layout
        - 한줄로 배치하는 것
        - 가로(horizontal)/세로(vertical) 방향으로 배치 가능
