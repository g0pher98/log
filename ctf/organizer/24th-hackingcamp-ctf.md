# 24th Hackingcamp CTF

## \[WEB] Basic Auth

> 어디로든 문\~\~\~ 은 잠겨있습니다. 열쇠가 필요하신가요?

```python
#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask
from flask import request, url_for

from functools import wraps
from flag import FLAG 
import os, json

server = Flask(__name__)
server.secret_key = os.urandom(32)


def check_auth(f):
    @wraps(f)
    def func(*args, **kwargs):
        page = kwargs['page']
        if page.split('.')[-1] in ['js', 'css', 'png', 'jpg']:
            pass
        else:
            auth = request.authorization
            if not (auth and check_login(auth.username, auth.password)):
                return ('Wrong! who are you???😑', 401, {
                    'WWW-Authenticate': 'Basic realm="show me your id,pw"'
                })
        return f(*args, **kwargs)
    return func



def check_login(user_id, user_pw):
    with open(url_for('static', filename='account')[1:], 'r') as f:
        data = f.read().strip().split(':')
        admin_id = data[0]
        admin_pw = data[1]
        if user_id == admin_id and user_pw == admin_pw:
            return True
    return False


@server.route('/')
def main():
    return 'Welcome! go to any page!'

@server.route('/<page>')
@check_auth
def flag(page):
    if '.' in page:
        return server.send_static_file(page)
    return FLAG


if __name__ == '__main__':
    server.run(host='0.0.0.0')

```

문제 코드를 보면 로그인 성공 후 dot(.)이 없는 `/<page>` 즉, 아무 페이지나 접근하면 플래그를 주는 것을 알 수 있다. 그러나 실제로 접근해보면 `check_auth()` decorator function에 의해 HTTP Basic Authentication을 요구함을 알 수 있다. Basic Authentication에 사용되는 계정은 `/static/account`에 존재하며, 접근 시 그 내용은 아래와 같다.

```
ThisIsNotFlagJustAdminID:ThisIsNotFlagJustAdminPassword
```

위 내용을 이용해서 Basic Authentication 인증을 시도하면 로그인이 진행되지 않는다. account 파일에 접근할 때 사용한 `url_for` 함수가 webroot를 기반으로 한 경로를 반환하지만, apache2 설정을 맞추어   주지 않았기 때문이다.

취약점은 확장자 검사 시 발생한다. 기본적으로 인증이 불필요한 js, css, png, jpg와 같은 파일을 요청할 경우 확장자를 검사하여 인증 과정을 지나치도록 되어있다. 그러나 `/js` 와 같은 형태로 요청 시 split 결과가 `['js']` 가 되기 때문에 인증 로직을 우회할 수 있다.

#### FLAG

`HCAMP{c4f5d41c69c57250471bc5bb9ddb3f77ed4237a2a8b235cff0aba458ccd2e5c3}`

## \[WEB] 합격자 발표

> 아기다리고기다리던 데몬대학교 합격자가 발표되었습니다\~

```python
#! /usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request, redirect, url_for

from functools import wraps
import os, json

from db import query

server = Flask(__name__)
server.secret_key = os.urandom(32)

@server.route('/')
def main():
    return render_template('index.html')


@server.route('/lookup', methods=['POST'])
def lookup():
    name = request.form.get("name")
    birth = request.form.get("birth")
    
    # db has name, phone, candidate_no, birth, is_passed
    if not (name and birth):
        return render_template('result.html', result=None)

    result = query('SELECT * FROM prob where name="{}" and birth="{}"'.format(name, birth))
    return render_template('result.html', result=result)

if __name__ == '__main__':
    server.run(host='0.0.0.0', debug=True)
```

문제 내 서비스는 name과 birth 파라미터를 통해 POST로 합격자 조회를 요청할 수 있다. 그러나 조회 과정에서 사용되는 SELECT 쿼리에 파라미터가 검증 없이 바로 삽입되면서 SQL Injection을 수행할 수 있다. 다음과 같이 다양한 방식의 접근을 통해 문제를 해결할 수 있다.

* `" union select 1, 2, 3, 4, group_concat(name) from prob#`
* `" or 1 limit 36,1#`
* `" or name like "%HCAMP%"#`

#### FLAG

`HCAMP{5D46BCE881C8E9EAAA547453D4E15A21}`

## \[CRYPTO] Really Safe A,,,

> 이거이거 정말 안전한데 표현할 방법이 없네,,,

```python
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

e = 65537

p = getPrime(1024)
q = getPrime(1024)

N = p * q
phi = (p - 1) * (q - 1)

d = gmpy2.divm(1, e, phi)

def padding(msg):
    total_length = len(msg) + (len(msg) % 2)
    return msg.ljust(total_length, '=')

def really_secret_cipher(plaintext):
    cipher_list = []
    msg = padding(plaintext)

    for ptr in range(0, len(msg)-2, 2):
        M1 = bytes_to_long(msg[ptr:ptr+2].encode())
        C1 = gmpy2.powmod(M1, e, N)
        M2 = bytes_to_long(msg[ptr+2:ptr+4].encode())
        C2 = gmpy2.powmod(M2, e, N)

        super_C = C1 * C2
        cipher_list.append(long_to_bytes(super_C).hex())
   
    return '.'.join(cipher_list)


FLAG = "HCAMP{******}"
if __name__ == '__main__':
    encrypted_flag = really_secret_cipher(FLAG)
    with open('data.enc', 'w') as f:
        print("FLAG : " + FLAG)
        f.write(str(N) + '/' + str(e) + '/' + encrypted_flag)
```

문제 컨셉은 특정 연산을 추가해 정말 안전한 암호체계를 만들었다는 내용이다. 안전하다고 주장하는 암호체계는 다음과 같다. 암호화할 평문에서 앞 2bytes(M1)와 뒤 2bytes(M2)를 각각 암호화(C1, C2)한 뒤, 구해진 두 암호문을 곱하여 `super_C`를 생성해낸다. 이렇게 만들어진 `super_C`는 리스트에 저장하고, 평문의 현재 위치로부터 2bytes 뒤부터 다시 로직을 반복한다. 간단하게 예시를 들면 다음과 같다.

{% hint style="info" %}
평문 : "THIS IS SECRET"



Encrypt("TH")\*Encrypt("IS") -> 저장

Encrypt("IS")\*Encrypt(" I") -> 저장

Encrypt(" I")\*Encrypt("S ") -> 저장

...
{% endhint %}

여기서 위 방식의 취약점은 두 암호문의 곱에 있다. RSA에서 두 암호문의 곱은 평문 곱의 암호문과 같다.

$$
C1 * C2 = (M1^e\ mod\ N) * (M2^e\ mod\ N)\\
= (M1^e * M2^e) mod N\ \ \ \\
= (M1*M2)^e\ mod\ N\ \ \
$$

또한, 코드를 통해 평문이 `HCAMP{` 로 시작함을 알 수 있다. 이를 통해 뒤 2bytes를 브루트포스 공격으로 찾아낼 수 있다. 다음 코드는 위 취약점을 이용해 복호화 하는 코드이다.

```python
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2
import string
from binascii import unhexlify

def bruteforce(M1, super_C):
    for b1 in string.printable:
        for b2 in string.printable:
            next_m = b1 + b2
            M2 = bytes_to_long(next_m.encode()) 
            guessed_super_C = gmpy2.powmod(M1 * M2, e, N)
            #print(guessed_super_C, super_C)
            if (guessed_super_C == super_C):
                return M2
    return False
                

def crack(prev):
    result = long_to_bytes(prev)

    for cipher in enc_list:
        super_C = bytes_to_long(unhexlify(cipher)) % N
        prev = bruteforce(prev, super_C)
        result += long_to_bytes(prev)
        print('[*] status : ', result)
        if not prev :
            return False
        
    return result

data= open('data.enc', 'r').read()
seped_data_list = data.split('/')

N   = int(seped_data_list[0])
e   = int(seped_data_list[1])
enc_list = seped_data_list[2].split('.')


flag = crack(bytes_to_long(b'HC'))
print("FLAG : " + flag.decode())
```

#### FLAG

`HCAMP{277a5a11b18251b2e34b484ca77d71fe84112d280b7a2d2da6319c7087d6a717}`



