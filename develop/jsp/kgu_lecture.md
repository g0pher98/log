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
