# Android Fiddler
안드로이드 앱 분석에 fidder를 사용해보려고 했는데 처음이라 쉽지 않다.

1. fiddler에서 remote에서도 proxy로 접근하도록 설정해야한다.
    - Tools > Options... > Connections
    - port 설정(default: 8888)
    - Allow remote computers to connect 체크.
2. 안드로이드 설정의 wifi 설정에서 프록시 설정을 해주어야 한다.
    - 설정 > Wi-Fi
    - 연결되어있는 Wi-Fi를 누르고있으면 `네트워크 수정` 메뉴가 뜸.
    - `고급 옵션`에서 프록시를 `수동`으로 변경해주고 fiddler가 있는 host의 ip와 아까 fiddler에서 설정한 port 정보를 입력.

여기까지 진행하면 fiddler에 패킷을 띄우는 것 까지는 가능하다.

### 인증서 이슈
안드로이드 7부터는 인증서 이슈가 있다. 최대 만료일에 대한 조건(39개월 이내)도 존재하고, 사용자가 설치한 인증서를 따로 분류해서 기존 방식으로 fiddler 인증서를 신뢰되도록 설정할 수 없다.

그래서 fiddler에서 만료기간을 커스터마이징한 인증서를 다운받은 후 adb로 안드로이드에 직접 삽입해서 이를 신뢰할 수 있는 인증서 목록에 등록해야한다. 다음과 같은 순서로 진행한다.

1. fiddler 인증서 만료기간 변경
    - QuickExec창 (alt + q)에서 다음 명령 실행
        - 만료기간 설정(360일)
            ```
            PREFS SET fiddler.certmaker.validdays 360
            ```
        - 유효기간 시작 일자 설정(1일전)
            ```
            PREFS SET fiddler.certmaker.gracedays 1
            ```
    - Tools > Options > HTTPS > Actions > Reset All Certificates
    - fiddler 재시작
    - Tools > Options > HTTPS > Actions > Export Root Certificates to Desktop
        - 바탕화면에 `.cer` 인증서 생김.
2. android 포맷에 맞게 인증서 변경
    - 바탕화면에 생성된 `.cer` 인증서의 확장자 `.der`로 변경.
    - cmd에서 desktop으로 이동 후 다음 명령 실행
        - 인증서 포멧을 pem으로 변경
            ```
            openssl x509 -inform DER -in FiddlerRoot.der -out FiddlerRoot.pem
            ```
        - 인증서 해시값 확인
            ```
            openssl x509 -inform PEM -subject_hash_old -in FiddlerRoot.pem
            ```
            - 가장 윗줄에 있는 hash 값을 복사
    - 인증서 hash 값으로 인증서 파일명 변경
        - `~~~.pem` -> `<hash>.0`
3. android에 인증서 적용
    - 인증서 안드로이드에 업로드
        ```
        adb push ???.0 /sdcard/Download
        ```
    - 신뢰 가능한 인증서에 추가
        ```
        > adb shell
        $ su
        # mount -o remount,rw /system
        # cd /system/etc/security/cacerts
        # mv /sdcard/Download/???.0 .
        # chmod 644 ???.0
        ```
    - 앱 재부팅
    - 잘 적용되었는지 확인
        - 설정 > 보안 > 신뢰할 수 있는 자격증명
        - Fiddler 관련 인증서 찾기

위와 같은 과정을 통해 인증서 이슈를 해결할 수 있다.

### 참고자료
- https://blog.jhyeon.dev/2021/05/03/android-cert-210503/
- https://blog.naver.com/minhoo920/221912836094
- https://blog.naver.com/PostView.naver?blogId=best798&logNo=222144681366&parentCategoryNo=14&categoryNo=&viewDate=&isShowPopularPosts=true&from=search
- https://hackcatml.tistory.com/62