1. 웹과 JSP 프로그래밍 이해하기
    - 웹의 동작 원리
        - 웹은 기본적으로 클라이언트/서버 방식으로 동작
        - 널리 쓰이는 웹서버
            - 아파치, 톰캣, IIS, ...
    - 정적 웹 / 동적 웹
        - 정적 : HTML
        - 동적 : PHP, ASP, JSP, 스프링, node.js, HTML5
    - 프론트 / 백
        - presentation layer (프론트엔드)
        - data access layer (백엔드)
    - 웹 프로그래밍 / JSP
        - 웹 프로그래밍 언어
            - 프론트 / 백 언어로 구분
            - JAVA 기반인 JSP는 서버 측 웹 프로그래밍 언어 중 하나
            - 서블릿이 자바 코드 안에 HTML코드를 추가하는 방식이라면, 반대로 JSP는 HTML 코드 안에 자바 코드를 추가하는 형태임.
        - JSP 특징
            - 서블릿 기술에서 사용하는 기능을 모두 사용할 수 있음. 즉, **서블릿 기술의 확장**이다.
            - `presentation logic(view)`와  `business logic(model)`을 분리해서 사용할 수 있기 때문에 **유지관리가 용이**하다.
            - 재컴파일 및 배포하지 않아도 수정 시 즉시 적용됨. 즉, **빠른 개발이 가능**하다.
            - `JSTL` 라이브러리를 잘 사용하면 **코드 길이를 줄일 수 있다**.
    - JSP 처리과정
        1. Hello.jsp 요청
        2. Hello.jsp -> Hello_jsp.java : 서블릿 프로그램 생성(번역)
        3. Hello_jsp.java -> Hello.jsp.class : 컴파일.
        - `*.class`를 생성하는 역할은 JSP 컨테이너가 담당.
        - 톰캣은 JSP 컨테이너가 포함된 웹 서버임.
    - JSP 생명주기
        ![image](https://user-images.githubusercontent.com/44149738/132366811-24769552-f899-4721-8c11-5866dedf27fc.png)

        - `jspinit()` : 최초 한 번정도 인스턴스의 모든 객체를 초기화 함. 데이터베이스, 파일에 대한 초기화 포함.
        - `_jspService()` : request와 response를 하기 위한 메소드 실행
        - `jspDestroy()` : response를 통해 실행되고있는 jsp를 제거. 디비 연결을 해제하고, 파일 리소스를 해제하는 등의 작업이 해당됨.

2. JSP 개발환경 구축하기
    - JSP 개발 환경 도구
        - 자바 : 자바개발키트(JDK) / 실행환경(JRE)
            1. https://www.oracle.com/java 에서 jdk 다운로드
                - https://www.oracle.com/java/technologies/javase/jdk14-archive-downloads.html
                - 14버전에 맞추려면 위 아카이브에서 다운
            2. 설치 후 환경 변수 설정.
        - 웹서버 : 톰캣
            1. https://tomcat.apache.org 에서 9버전 core 부분 zip 파일 다운로드
            2. 압축 해제 후 내부 디렉토리 C 드라이브로 이동
        - IDE : 이클립스
            1. https://www.eclipse.org/downloads/packages/ 접속
            2. `Eclipse IDE for Enterprise Java and Web Developers` 다운로드
            3. TIP : zip 파일로 설치. exe로 하면 추가 설치 필요.
        - 이클립스와 톰캣 서버 연동
            1. 이클립스 [New] - [Other]
                - [Server - Server] - [Apache - Tomcat v9.0]
    
    - 프로젝트 만드록 실행하기
        1. 프로젝트 생성하기
        2. JSP 페이지 작성하기
        3. 프로젝트 실행하기
    - 동적 웹 프로젝트의 구조
        ![image](https://user-images.githubusercontent.com/44149738/132373305-5754f737-f0fa-486a-a7e3-9ef79ee8c007.png)


3. 스크립트 태그 
    - 기본적으로 `<% ... %>` 형태로 사용
    - jsp 컨테이너가 이러한 java 코드가 담긴 스크립트 태그를 먼저 처리.
    - 종류
        - 선언문(declaration)
            - 자바 변수나 메소드를 전역으로 정의
            - `<%! ... %>`
        - 스크립틀릿(scriptlet)
            - 자바 로직 코드를 작성
            - `<% ... %>`
        - 표현문(expression)
            - 변수, 계산식, 메소드 호출 결과를 문자열 형태로 출력
            - `<%= ... %>`
        - 주석
            - `<%-- ... --%>`
    
    - 선언문 태그
        - 변수 또는 메소드가 전역으로 사용됨.

4. 액션 태그
    - 서버나 클라이언트에게 어떠한 행동을하도록 명령하는 태그
    - `<jsp: ... />` 를 사용
    - forward 액션 태그
        - 출력 버퍼에 저장되어있던 내용을 모두 삭제하고 forward 액션 태그에 설정된 페이지로 프로그램의 제어가 이동
        - 제어는 다른 파일로 이동해도 client의 url에는 처음 요청한 주소가 유지됨.
        - page 속성값
            - 이동할 페이지의 외부 파일명
            - 스크립트 태그를 이용하여 jsp 페이지에 직접 자바 코드를 작성하는 것을 피하기 위해 사용. 유지보수를 효율적으로 하는 것이 목적
    - include 액션 태그
        - jsp 특정 영역에 외부 파일의 내용을 포함하는 태그
        - html, jsp, 서블릿 페이지 등을 포함할 수 있음.
        - page 옵션
            - include 할 페이지
        - flush 옵션
            - 출력버퍼를 지울 것인지에 대한 설정
    - param 액션 태그
        - 현재 jsp 페이지에서 다른 페이지에 정보를 전달하는 태그
        - forward나 include와 같은 태그를 사용할 때, 파라미터를 넘기기 위해서 사용하는 태그
    - useBean 액션 태그
        - 자바빈즈를 사용하기 위한 태그
        - 파라미터
            - id : 자바빈즈 식별자(변수명이라고 생각하면 될듯)
            - class : 자바빈즈 이름
            - scope : 얼만큼 살아있는지 설정
                - page, request, session 

5. 자바빈즈
    - `.java`를 사용할 수 있음
    - 보통 코드가 무거워지는 것을 방지하고 jsp에 주요코드를 넣는것을 방지하기 위해서 `client - jsp - .java - db` 와 같은 형태로 중간에 껴서 사용.
    - 사용 규칙
        - java.io.Serializable 인터페이스를 구현해야 한다
        - 인수가 없는 기본 생성자가 있어야 한다
        - 프로퍼티는 private 접근 지정자로 설정해야 한다.
        - getter/setter() 메소드가 존재해야 한다.
        - java.io.Serializable 인터페이스는 생략 가능하지만, 객체 직렬화는 제공해야함.

    - 자바빈즈 액션태그
        - setProperty 액션태그
        - getProperty 액션태그

6. 내장객체
    - jsp 페이지에서 사용할 수 있도록 **jsp 컨테이너에 미리 정의된 객체**
    - import 문 없이 자유롭게 사용 가능
    - 객체 생성 안해도 직접 호출해서 사용 가능
    - 내장 객체의 종류
        - ![image](https://user-images.githubusercontent.com/44149738/136025394-2bbc84be-9ca0-4875-980b-d12e654187a6.png)
    - request 내장 객체
        - jsp에서 가장 많이 사용되는 기본 내장 객체
        - 웹 브라우저에서 서버의 jsp 페이지로 전달하는 정보를 저장
        - 파라미터 관련 메소드
            - getParameter()
            - getParameterValues()
            - getParameterNames()
            - getParameterMap()
        - HTTP 헤더 관련 메소드
            - getHeader()
            - getHeaders()
            - getHeaderNames()
            - getIntHeader()
            - getDateHeader()
            - getCookies()
        - 웹 브라우저/서버 관련 메소드
            - getRemoteAddr()
            - getContentLength()
            - getProtocol()
            - getServerName()
            - getServerPort()
            - getMethod()
            - getRequestURI()
            - ...
    - response 내장 객체
        - 요청 처리 결과
        - `<jsp:forawrd />` 와 response.sendRedirect 차이점
            - forward는 uri는 유지된 채 제어권만 넘김
            - redirect는 아예 넘어가버림
        - 페이지 이동 메소드
            - sendRedirect()
        - 응답 컨텐츠 관련 메소드
            - sendError(404, "not found")
            - setStatus()
            - setContentType()
            - getContentType()
            - ...
            - setIntHeader("Refresh", 3) // 3초마다 새로고침
    - out 내장 객체
        - 스크립틀릿 태그의 표현문 태그(`<%= %>`)와 같은 결과
        - 메소드
            - print()
            - println()
            - newLine()
            - clearBuffer()
            - flush()
            - isAutoFlush()

7. 폼(form)
    - 사용자가 웹 브라우저를 통해 작성된 데이터를 한번에 웹 서버로 전송하는 양식
    - 메소드
        - get : url에 데이터를 넣어서 전송하는 방식
        - post : 데이터를 별도로 첨부하여 전달하는 방식
    - 데이터 입력 태그
        - input
        - select - option
        - textarea
    - form 데이터 처리하기
        - request 내장 객체를 이용
        ```jsp
        String 변수 = request.getParameter(요청 파라미터 이름);
        String[] 변수 = request.getParameterValues(요청 파라미터 이름);
        ```
        - setCharacterEncoding('UTF-8') : 인코딩 설정
        - getParameterNames() : 파라미터 name 리스트 가져오기
        - hasMoreElements()
        - nextElement()

8. file upload
    - form 태그를 사용하여 전송
        - form에 `enctype="multipart/form-data"` 있어야 함
        - POST로 보내야함
    - 단순한 자바 코드로 작성하여 처리할 수 없어서 오픈 라이브러리를 사용
        - 오픈 라이브러리 종류
            - cos.jar
                - MultiparRequest 이용
                    - 파일 자체만 다루는 클래스
                    - 한글 인코딩 값을 얻기 쉬움.
                    - 서버에 동일 파일명이 있으면 자동으로 변경
                - 가장 간단한 방법
                - `com.oreilly.servlet.*`
                - `com.oreilly.servlet.multipart.*`
            - commonsfileupload.jar
                - 아파치 api 사용
                - 편리하고 강력한 기능
                - 서버의 메모리상에서 파일 처리가 가능하도록 지원
                - `org.apache.commons.fileupload.*`
                - commons.apache.org 에서 다운
                - 메소드
                    - ![image](https://user-images.githubusercontent.com/44149738/137807409-36e6cf16-fa44-4c74-b25c-9f655aa3b75a.png)
            - ![image](https://user-images.githubusercontent.com/44149738/137805295-dc9c9b3f-897b-4c1a-8d1d-97c5ab184e3d.png)
    
9. 유효성 검사
    - 사용자 입력값 검사
    - 백엔드는 리소스가 많이 들기 때문에 프론트에서 검사. (ㄴㅖ,,??!?!?!?!???)
    - 사용자 실수 등 예상 가능한 오류 등을 방지할 수 있기 때문.
    - 유효성 검사를 위한 핸들러 함수
        - js를 통한 코드 작성
            - 속도가 빠르고 서버에 과부하를 주지 않음
        - 과정
            1. 태그의 속성을 이용하여 핸들러 함수 설정
                - form의 onsubmit
                - submit input의 onclick
            2. script 태그를 이용해서 핸들러 함수 작성
            3. form 태그의 name 속성 등을 이용하여 사용자 입력값에 접근
    - 유효성 검사 처리 방법
        - 기본 유효성 검사 : 데이터 값의 존재 유무
            - 데이터 길이 확인하기
            - 숫자 여부 확인하기
                - `isNaN()` 함수를 사용하여 숫자인지 검사
                    - isNotaNumber 의 약자
                    - 숫자면 false, 숫자가 아니면 true
        - 데이터 형식 유효성 검사 : 특정 패턴에 일치하는지 확인
            - 기본 유효성검사보다 복잡함.
            - 정규표현식(regualr expression)을 사용
            - 정규표현식
                - 문자열의 특정 형태를 찾아내기 위해 패턴으로 표현한 수식
                - 사용 방법
                    1. 객체 초기화를 통한 사용방법
                        - 표현식이 거의 바뀌지 않는 경우 상수처럼 사용.
                    2. RegExp 객체를 사용하는 방법
                        - 정규표현식이 자주 변경될 때 사용.

10. 다국어처리
    - 다양한 언어와 지역에서 기술변경 없이 소프트웨어에 바로 적용하는 것.
    - 다국어는 다양한 언어와 지역에 적용될 수 있도록 하는 국제화(internationalization, i18n)와 언어별 구성 요소를 추가하여 특정 지역의 언어나 문화에 맞추는 지역화(localization, L10n)를 포함.
    - 지역화
        - 특정 언어와 지역에 맞게 적합화 하는 것.
        - L10n으로 표기
        - 고려되는 사항
            - 숫자, 날짜, 시간, 화폐, 키보드, 문자열 순서 및 정렬, 심벌, 아이콘, 색상
            - 문화별 오해의 소지가 있는 문자나 그림
            - 지역별 법률 차이
    - 국제화
        - 다국어 지원
        - i18n 으로 표기
        - 어느 국가에서나 사용할 수 있도록 하는 지역화 기능을 포함
        - 다음과 같은 처리를 포함해서 지원해야함
            - 유니코드의 사용이나 기존 인코딩을 적절히 처리. 사용자 인터페이스에 표시할 문자열에는 문자 코드가 포함되지 않도록 설계 및 개발해야 함.
        - 세로/가로/우->좌 쓰기 등 언어의 특정을 반영하는 처리 등을 지원해야 함.
        - 언어적,지역적,문화적 특성 등에 대한 사용자 설정 지원
        - 지역화 정보를 코드와 분리
    - locale 클래스를 이용한 다국어 처리
        - request 내장 객체를 이용하여 브라우저에 정의된 언어나 국가정보를 가져오는 방법
        - `java.util.Locale request.getLocale();
        - jsp 페이지에 page 디렉티브 태그(`<%@ %>`)의 import 속성으로 java.util.Locale을 설정
        - 메소드 종류
            - ![image](https://user-images.githubusercontent.com/44149738/139557442-0b7b4e8f-d5af-4a09-85de-8e94da6dd56c.png)
        - 언어설정
            - response.setHeader('Content-Language', 'es')
            - 위와 같이 헤더 설정을 통해 해당 국가별 언어를 제대로 표현할 수 있음.
        - 시간설정
            - java.text.DateFormat import
            - response.getDateTimeInstance() 사용
        - 화폐설정
            - java.text.NumberFormat import
            - NumberFormat.getCurrencyInstance(locale) 사용
    - JSTL fmt 태그를 이용한 다국어 처리
        - taglib prefix로 jstl 사용을 선언
        - JSTL 태그의 종류
            - ![image](https://user-images.githubusercontent.com/44149738/139563874-50648207-8453-4e27-a25f-d8bb6ec83542.png)
            - setLocale 태그 : 국제화 태그가 사용할 locale을 설정
            - requestEncoding 태그 : 요청 파라미터의 문자 인코딩을 설정하는 태그
            - 메세지 처리 태그
                - 메시지 처리 태그에서 사용하는 파일로, 메시지 번들이라고도 함
                - 리소스 번들로 사용하는 파일은 보통 `/WEB-INF/classes/` 폴더에 있음.
                    - 근데 실습에서는 `/src/.../com/bundle/`에 넣네?
                    - ![image](https://user-images.githubusercontent.com/44149738/139565913-b68e0429-6034-48e3-89c8-577beab10949.png)
                - `java.util.Properties` 클래스에 정의된 방법으로 메시지를 읽어오기 때문에 확장자가 `properties`인 파일이 반드시 있어야 함.
            - properties를 생성하는 방법 두 가지
                1. 메모장에서 작성 후, 저장할 때 filename.properties로 저장
                2. 이클립스에서 생성하는 경우
                    - ctrl + n (fild > new > other), wizards에 text 검색
                    - 이후 general > untitled text file 선택
                    - 영어 아무거나 저장 후 한국어 넣고 다시 저장.
                        - 오류가 뜨면 utf-8로 저장
                        - ![image](https://user-images.githubusercontent.com/44149738/139566015-e149a36b-5242-444f-a6e1-8aa0aa3e0df9.png)
            - properties 파일 종류
                - ![image](https://user-images.githubusercontent.com/44149738/139564292-83760d56-15cb-4ea4-a958-7936240a8e55.png)
            - bundle 태그
                - `<fmt:bundle basename="리소스번들" ... >` 형태로 사용
                - 사용할 리소스 번들을 설정하는 태그
            - message 태그
                - `<fmt:message key=".. .">` 형태로 사용
                - bundle 태그에서 설정한 리소스 번들에서 메세지를 읽어와 출력
            - setBundle 태그
                - `<fmt:setBundle ...>` 형태로 사용
                - 리소스 번들을 가져와서 변수로 저장한 후 jsp 페이지 어디에서나 사용할 수 있는 태그 
            - format Number 태그
                - 숫자를 형식에 맞춰 출력하는 태그
            - timeZone
                - 사용자 locale에 따라 날짜를 출력하는 방법

11. 시큐리티
    - 허가된 사용자만이 특정 페이지에 접근할 수 있도록 제한하는 기능
    - 종류
        - 인증(authentication)
            - 사용자 이름과 암호를 확인하여 수행
        - 권한 부여(authorization)
            - 접근할 수 있는 사람인지 확인하여 승인
    - 처리방법
        - 선언적 시큐리티 : web.xml에 작성해서 인증 수행
        - 프로그래밍적 시큐리티
    - 선언적 시큐리티
        - 역할 설정 방법
            ```xml            
            <security-role>
                <role-name>역할이름</role-name>
            </security-role>
            ```
        - 제약사항 설정 방법
            ```xml
            <security-constraint>
                <web-resource-collection>웹 자원에 대한 접근 설정</web-resource-collection>
                <auth-constraint>웹 자원에 접근할 수 있는 인증된 사용자 설정</auth-constraint>
                <user-data-constraint>데이터 정송 시 데이터 보호 설정</user-data-constraint>
            </security-constraint>
            ```
            - ![image](https://user-images.githubusercontent.com/44149738/142765776-633043fc-5fae-4534-87b0-ddf568d3653e.png)
            - ![image](https://user-images.githubusercontent.com/44149738/142765821-55d52750-93a1-4f42-9a90-bfd069851f5d.png)
            - `user-data-constraint` - `transport-guarantee`
                - ![image](https://user-images.githubusercontent.com/44149738/142765924-a63905f0-cbd1-4996-ab79-199d5ff57cc3.png)
        - 인증 설정
            - `login-config`를 사용
                - ![image](https://user-images.githubusercontent.com/44149738/142766074-ba635bc7-4ffd-4729-b8b1-2292b878f2ab.png)
                - `auth-method`
                    - ![image](https://user-images.githubusercontent.com/44149738/142766163-676c1c16-88c4-4660-acbe-fc75caf984e2.png)
                    - FORM 속성을 사용하게 되면 action 및 name을 고정해야함
                        - ![image](https://user-images.githubusercontent.com/44149738/142766273-b39e24f5-bfd5-4476-9505-9567400558c5.png)
                    - form 사용 시 `form-login-config` 사용.
                        - ![image](https://user-images.githubusercontent.com/44149738/142766361-3028b7d4-be9c-4505-8ca1-5b5de629fd9d.png)


