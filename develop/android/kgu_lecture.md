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
    - frame layout
        - 무언가를 넣을 프레임을 생성.
        - 한개가 딱 들어가고, 여러개 들어가면 겹쳐짐
        - 한 칸 안에 다 넣을때 사용
    - table layout
        - 테이블 만드는 레이아웃
        - `TableRow` 라는 view를 사용해서 줄을 만듬
        - 좌우로는 병합이 되는데 상하로 병합이 안됨.
        - attributes
            - stretchColumns : 빈공간을 채우도록 좌우로 늘린다.
                - 숫자를 넣으면 해당 column이 늘어난다.
                - 균등하게 늘어나게 하려면 `*`을 넣으면 된다.
            - shrinkColumns : layout overflow 발생 시 줄여서 크기 맞춤
        - layout에 들어간 자식 객체에 생기는 attributes
            - layout_column
                - 몇번 column에 배치할 것인지 설정
            - layout_span
                - 몇개의 column에 걸쳐 표현할 것인지 설정

7. Menu
    - 메뉴의 종류
        - ![image](https://user-images.githubusercontent.com/44149738/141668905-3a575db3-d05b-4763-ac5b-878db9cf5d8e.png)
        - options menu
            - 보통 앱 전체에 영향을 주는 메뉴
        - context menu
            - 보통 long click 시 표현.
            - 보통 선택한 항목에만 영향을 줌
        - popup menu
            - context menu랑 비슷함.
    - 메뉴를 만들기 위해서는 XML로 먼저 선언하는게 편하고 좋음
        ```xml
        <menu>
            <item></item>
            <item></item>
            <item>
                <menu>
                    <item></item>
                </menu>
            </item>
        </menu>
        ```
        - `res/menu/` 에 넣으면 됨. 처음엔 없어서 type을 menu로 선택해서 directory를 새로 만듬
        - `menu resource file`을 선택해서 파일 추가. 기본 xml이 적혀있음.
    - `<item>`
        - id : 아이디
        - icon : 아이콘 뜨는것
        - title : 표시 뭐라고 될건지(?) 
        - showAsAction : 앱바(?)를 사용할 때 사용.
    - option menu 사용법
        - `onCreateOptionsMenu()` 메소드를 override 해서 activity에서 메뉴를 띄워야 할 때 띄울 수 있도록 설정해주어야 한다.
            ```java
            @Override
            public boolean onCreateOptionsMenu(Menu menu) {
                MenuInflater inflater = getMenuInflater();
                inflater.inflate(R.menu.game_menu, menu);
                return true;
            }
            ```
            - inflater는 menu xml 구조를 object로 변환해주는 것을 말함.
            - `R.menu.<xml파일이름>` 으로 접근
        - `onOptionsSelected()` 메소드를 override 해서 메뉴를 선택했을 때, 액션을 지정할 수 있다.
            ```java
            public boolean onOptionsItemSelected(MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.item1:
                        // ...
                        return true;
                    case R.id.item2:
                        // ...
                        return true;
                    default:
                        return super.onOptionsItemSelected(item);
                } 
            }
        ```
    - context menu 사용법
        - long click 시 메뉴 띄워줌
        - `registerForContextMenu(View)` : View 설정
        - `onCreateContextMenu()` : 메뉴를 띄울 때 사용
            ```java
            @Override
            public void onCreateContextMenu(ContextMenu menu, View v, ContextMenuInfo menuInfo) { // 어떤 view를 클릭했을 때 뜰 건지 view를 파라미터로 설정
                super.onCreateContextMenu(menu, v, menuInfo);
                // ...
            }
            ```
        - `onContextItemSelected()` : 선택 시 액션 설정
            - `onCreateContextMenu`는 내부에서 view마다 다르게 설정하지만 본 메소드는 안에서 switch로 선택된 메뉴의 id를 한번에 구분해야함.

8. Dialog
    - 작은 팝업 창
    - subclasses
        - AlertDialog : 수업에서는 이것만 다룸
        - DatePickerDialog
        - TimePickerDialog
    - AlertDialog
        - 요소
            - title : 제목 영역(없어도 됨)
            - context area : 내용 영역
            - action buttons : 확인/취소 등 하단버튼
        - 사용법
            1. builder 세팅
                - `AlertDialog.Builder` 클래스 생성
                    ```java
                    AlertDialog.Builder builder - new AlertDialog.Builder(this);
                    ```
                - dialog 제목 정하기
                    ```java
                    builder.setTitle("dialog title~");
                    ```
                - content area에 메세지를 넣는다
                    ```java
                    builder.setMessage("message~");
                    ```
                - button 설정하기
                    - positive button -> ok 같은거
                        - `.setPositiveButton("ok", null)`
                    - negative button -> 취소 같은거
                        - `.setNegativeButton("cancel", null)`
                    - neutral button -> 기타 옵션
                        - `.setNeutralButton("neutral", null)`
                    - ![image](https://user-images.githubusercontent.com/44149738/141670127-102728ba-88f7-4a3e-8de8-635eaac1860f.png)
            2. dialog 생성
                - AlertDialog 클래스 생성
                    - `dialog = builder.create();`
                - 출력
                    - `dialog.show();`
            - ![image](https://user-images.githubusercontent.com/44149738/141670233-bfb460e7-f37d-40ca-bde6-8b466310dbc0.png)
        - context area에 선택 리스트 추가하는 방법
            - 3 종류가 있음
                - traditional single-choice list
                - persistent single-choice : radio buttons
                - persistent multiple-choice : checkboxes
            - `.setItems(String[] list, new DialogInterface.OnClickListener() {})` 메소드로 넣을 수 있음
                - 첫 번째 인자로 String 배열을 넣으면 된다.
                - 두 번째 인자로는 onclicklistener.
            - `.setMultiChoiceItems(String[] list, boolean[] checked, new DialogInterface.OnMultiChoiceClickListener() {})`
                - 두 번째 인자로 click 여부를 저장할 boolean 배열 전달
            - `.setSingleChoiceItems(String[] list, int i, new DialogInterface.OnClickListener() {})`
        - context area 커스터마이징
            - `res/layout/dialog.xml` 같은 형태로 layout xml 생성
            - inflate를 이용해서 xml 파일을 view 형태로 변환
            - builder의 `.setView()` 메소드를 이용해서 context area에 view를 설정.
9. activity
    - 안드로이드 component 4가지 (매우 중요)
        - Activity
            - 가장 기본적인 컴포넌트. 화면을 구성.
            - 화면에 뜨지 않으면 동작하지 않음.
        - Service
            - 백그라운드에서 계속 무언가를 수행할 때 사용. 문자가 온다든지.
            - 화면에 띄워져있지 않아도 실행
        - Broadcast Receiver
            - 이벤트 발생 시 수행. 전화가 온다든지.
        - Content Provider
            - 데이터를 다른 앱과 공유하는 컴포넌트
    - activity
        - 새로운 activity 만들기
            - 화면을 전환하는 방법이 MainActivity와 Fragment 두 개 있음.
            - 요즘 대세는 fragment 사용. 예쁘고, 스무스하고, 리소스 적음.
            - New - Activity - Empty Activity 선택해서 새로운 activity 만들 수 있음
                - generate a layout file 옵션을 체크
                - launcher activity 옵션은 체크 해제
                    - launcher activity는 처음 시작할 때 보이는 activity를 말함
                - 생성하면 java 파일 하나, xml 파일 하나가 생성됨.
                    - menifest 파일에도 해당 activity에 대한 내용을 추가해야함.(자동추가됨)
            - activity 사용법
                ```java
                Intent intent = new Intent(getApplicationContext(), NewActivity.class);
                startActivity(intent);
                ```
                - 종료할 때는 `finish()` 호출
10. intent
    - activity를 연다거나 무언가 할 일을 지정해줌.
    - 또는 activity 간 데이터 교환에 사용됨
    - intent 종류
        - explicit intent : 명시적으로 클래스를 지정
        - implicit intent : 정확하게 지정하지 않고, 해당 액션에 대한 최적의 동작을 수행
    - explicit intent
        - 메세지 교환
            - putExtra()
            - getExtra() / getStringExtra() / getIntExtra()
            - 두 메소드를 이용해서 교환.
        - 다시 최근 activity로 돌아가는 방법
            - 많이 사용하지만, 권장하지는 않는 방법
                - activity를 띄울 때, request code를 함께 넘김.
                - `startActivityForResult(intent, 1);`
                - 새로 띄운 activity가 종료되면 실행 시 설정해준 request code로 이전 activity는 어떤 activity로부터 넘어온 것인지 알 수 있음.
                - 종료 시 데이터를 넘길 때는 putExtra 메소드를 사용하면 됨.
                - extra를 설정해준 뒤 setResult(RESULT_OK, intent)로 결과 지정 후 finish
                - 받는쪽 intent에서는 onActivityResult(req_code, res_code, data) 메소드로 받음.
            - 새로운 방법
                ```java
                activityResultLauncher = registerForActivityResult(
                    new ActivityResultContracts.StartActivityForResult(),
                    new ActivityResultCallback<ActivityResult>() {
                        @Override
                        public void onActivityResult(ActivityResult result) {
                            Intent data = result.getData(); // 이렇게 intent를 가져올 수 있음
                            if (result.getResultCode() == Activity.RESULT_OK) {
                                // ...
                            }
                        }
                    }

                )
                ```
    - implicit intent
        - 지정하는 방식이 아니라, 정보를 주면 그거에 맞는 적합한 앱을 찾아서 띄움.
        - 예를 들면 웹페이지를 띄우라고 하면 그에 맞는 앱(사파리나 크롬 등)을 알아서 찾아서 띄움.
        - intent filter를 이용해서 앱 탐색.
        - implicit intent 사용
            - 119에 전화.
                ```java
                Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:/119"));
                startActivity(intent);
                ```
            - 웹페이지 열기
                ```java
                Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:/119"));
                intent.setAction(Intent.ACTION_VIEW);
                intent.setDataAndType(Uri.parse("https://www.google.com"), "text/html");
                intent.addCategory(Intent.CATEGORY_DEFAULT);
                startActivity(intent);
                ```
        - intent filter 핸들링 설정
            - 특정 스킴에 대해 intent filter가 앱을 찾을 때 선택지에 추가될 수 있도록 설정할 수 있다.
            - AndroidManifest 에서 설정
            - `<activity>` 안에서 선언
                ```xml
                <intent-filter>
                    <action android:name="android.intent.action.VIEW" />
                    <data android:mimeType="text/html" android:scheme="https" />
                    <category android:name="android.intent.category.DEFAULT" />
                </intent-filter>
                ```
