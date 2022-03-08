---
description: >-
  여느 때와 같이 열심히 근무를 하다가 점심을 먹으러 갔다. 백신 접종을 증명하는 카카오톡 QR 코드가 화면에 출력되지 않아 한참을 기다렸다.
  그런데 나만 기다리고 있던게 아니네?
---

# BGP Hijacking

> 오늘 한국에 점심 먹는 사람이 많나보다... 무슨 날인가?

라고 생각한 태평한 나. 그리고 그런 나에게 일침을 날리듯 해킹 사고라는 소식이 들려왔다. 한줄요약하면 클레이스왑이라는 서비스가 BGP Hijacking 공격에 당했다는 건데, 아무것도 모르는 나는 다음과 같은 의문이 발생했다.

* BGP Hijacking이 뭔데?
* 클레이스왑이랑 카카오톡이랑 무슨 관련이 있는데?

그래서 일단 BGP Hijacking에 대해서 알아보고, KLAYswap 사건을 포함해서 실제로 이를 이용한 어떤 공격 사례가 있었는지 알아보고자 한다.

## What is BGP

는 내일 정처기 필기인데 20페이지밖에 안봐서 나중에 정리해야징\~😝

## Incidents

실제로 BGP Hijacking을 통해 발생했던 사건들을 알아보자. 더 다양한 사건은 [Wikipedia](https://en.wikipedia.org/wiki/BGP\_hijacking#Public\_incidents)에 기술되어 있다.

### KLAYswap

클레이스왑은 한창 떠들석했던 디파이(Defi) 서비스중 하나다. 국내 1위 디파이 서비스일 정도로 영향력은 큰 것으로 보인다. 그런 클레이스왑에서 해킹사건이 발생했다. 관련해서 클레이스왑에서 보고서를 공개했다.

{% embed url="https://medium.com/klayswap/klayswap-incident-report-feb-03-2022-70ff124aed6b" %}
KLAYswap Incident Report
{% endembed %}



## Reference

#### About BGP and Hijacking

* [https://dataportal.kr/14](https://dataportal.kr/14)
* [https://en.wikipedia.org/wiki/BGP\_hijacking](https://en.wikipedia.org/wiki/BGP\_hijacking)

#### About KLAYswap

* [https://medium.com/klayswap/klayswap-incident-report-feb-03-2022-70ff124aed6b](https://medium.com/klayswap/klayswap-incident-report-feb-03-2022-70ff124aed6b)
* [https://medium.com/s2wblog/post-mortem-of-klayswap-incident-through-bgp-hijacking-898f26727d66](https://medium.com/s2wblog/post-mortem-of-klayswap-incident-through-bgp-hijacking-898f26727d66)
* [https://www.boannews.com/media/view.asp?idx=104743](https://www.boannews.com/media/view.asp?idx=104743)
* [https://therecord.media/klayswap-crypto-users-lose-funds-after-bgp-hijack/](https://therecord.media/klayswap-crypto-users-lose-funds-after-bgp-hijack/)
