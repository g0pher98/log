# Frida
V8기반 js injection 후킹 꿀툴! 여러 os에서 사용 가능하지만 안드로이드 분석 기준으로 작성한다

## 설치
우선 frida python library와 안드로이드를 예뮬레이팅할 녹스 플레이어를 설치해야한다. 녹스는 GUI 기반이라 그냥 검색해서 설치하면 된다. 녹스를 설치하면 adb 프로그램이 같이 설치되는데, 이 프로그램을 자주 사용하기 때문에 환경변수에 추가해야 한다. `Program Files\Nox\bin` 폴더를 찾아서 환경변수에 올려주면 된다.

python 라이브러리는 아래 명령으로 간단하게 설치 가능하다. 버전은 선택이지만 일단 무난하게 보장된 버전을 사용하는게 정신건강에 좋다.
```
pip install frida==12.6.11
pip install frida-tools==2.2.0
```

### nox 세팅
먼저 안드로이드를 루팅해주어야 한다.  
- nox 설정 > 기본설정 > 시작항목 > ROOT켜기


개발자 모드로 바꿔서 USB 디버깅 옵션도 켜준다.
- 안드로이드 설정 > 태블릿 상태 > 빌드번호 5번 연속 터치
- 안드로이드 설정 > 개발자 옵션 > USB 디버깅 > On


### frida server 설치
후킹 코드를 작성해서 실제로 디바이스에 접근할 수 있도록 해주는 frida server를 설치해주어야 한다. 아래 링크에서 다운받을 수 있다.

https://github.com/frida/frida/releases

다양한 OS, 다양한 세부버전을 지원하기 때문에 굉장히 많은데, 다음과 같이 adb를 사용해서 OS 비트수를 확인할 수 있다.
```
adb shell getprop ro.product.cpu.abi
```
나의 경우 `x86`으로, 32bit 운영체제를 사용하고 있음을 알 수 있다. 이제 깃헙으로 돌아가서 `frida-server`를 검색해보자

![image](https://user-images.githubusercontent.com/44149738/138778058-8c5733ee-5159-4db8-99e2-3f97c412218b.png)

본인 환경에 맞게 다운받으면 된다. 나의 경우 `frida-server-15.1.8-android-x86.xz`를 다운받았다. 이제 다음과 같이 adb를 이용해서 안드로이드 기기 안의 `/data/local/tmp` 위치에 업로드하자

```
adb push ./frida-server-15.1.8-android-x86 /data/local/tmp
adb shell "chmod 777 /data/local/tmp/frida-server-15.1.8-android-x86"
adb shell "/data/local/tmp/frida-server-15.1.8-android-x86 &"
```
위와 같이 업로드, 권한설정, 실행 순서로 명령을 실행시키면 서버가 정상적으로 구동된다.

### 간단한 테스트
```
> frida-ps -U
```
위 명령으로 안드로이드에서 실행중인 프로세스 리스트를 볼 수 있다. 코드를 짜서 접근을 해야하는데, js 파일을 짜서 frida로 실행시켜도 되고, python으로 코드를 짤 수도 있다.
- javascript 예시
    ```javascript
    setImmediate(function() {
        Java.perform(function() {
            var pkg = Java.use("com.example.test")
            pkg.test.value = 1
        }) 
    })
    ```
- python 예시
    ```python
    import frida, sys

    def on_message(message, data):
        print(message)

    PACKAGE_NAME = "com.package.test"

    jscode = """
    console.log("[+] Start Script");

    Java.perform(function() {
        console.log("[+] Hooking System.exit");
        var exitClass = Java.use("java.lang.System");
        exitClass.exit.implementation = function() {
            console.log("[+] System.exit called");
        }
    });
    """

    process = frida.get_usb_device(1).attach(PACKAGE_NAME)
    script = process.create_script(jscode)
    script.on('message', on_message)
    print('[+] Running Hook')
    script.load()
    sys.stdin.read()
    ```
