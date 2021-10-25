# Flask session decode
Flask 세션은 jwt처럼 decode할 수 있다. 다음과 같이 확인할 수 있다.

```python
import base64, zlib

session = "여기에 전체 세션을 넣는다"
encoded_content = session.split('.')[1]
padding = '=' * (8 - len(encoded_content) % 8)
zlib.decompress(base64.urlsafe_b64decode(encoded_content + padding))
```