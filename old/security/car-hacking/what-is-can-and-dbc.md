# What is CAN and DBC file?

## dbc file parser

- [DBCC](https://github.com/howerj/dbcc)
    - C 라이브러리
    - CAN-FD 지원 안됨.
- [can-dbcparser](https://github.com/downtimes/can-dbcparser)
    - C++ 라이브러리
- [dbcppp](https://github.com/xR3b0rn/dbcppp)
    - C++ 라이브러리
- [cantools](https://github.com/eerimoq/cantools)
    - python3 라이브러리
    - 꽤나 인지도있는 라이브러리인듯?
    - [document](https://cantools.readthedocs.io/en/latest/)도 만들어놨음.
    - 여러 기능이 있는데 dbc parsing도 그중 하나.

cantools가 인지도도 높고 범용적으로 사용되는 것 같아서 사용해보기로 결정.

## dbc file structure

바로 라이브러리를 사용하다보니까 dbc 파일을 잘 몰라서 이해도가 좀 떨어지는 느낌이었다. 정확하게는 몰라도 대충이라도 dbc 파일에 어떤 내용이 담겨있는지 알아볼 필요가 있었다.

- `VERSION` : 가장 먼저 나옴. 버전정보
- `NS_` : New Symbol. dbc 파일에서 사용되는 심볼 기술
- `BS_` : Baudrate.
- `BU_` : NodeName. 노드는 ECU로 이해하면 됨.
- `BO_ <message ID> <message Name>` : 메세지 선언.
    - 구조
        
        ```python
        <TX> <node>
        ```
        
    - `SG_ <signal Name>` : 시그널에 대한 세부적인 정보를 담고있음.
        - 구조
            
            ```python
            <start_bit>|<signal_size>@<byte_order><value_type> (<factor>, <offset>) [<minimum>|<maximum>] <unit> <recv_node>
            ```
            
            - start bit : data field 상에서 시그널 데이터가 시작되는 위치.
            - signal size : 시그널 데이터의 크기
            - byte order : 빅엔디안(0), 리틀엔디안(1)
            - value_type : `unsigned(+)` 또는 `signed(-)` 로 표현.
        - 예시
            
            ```python
            SG_ Temperature : 0|12@0- (0.01,250) [229.52|270.47] "degK"  PCM1,FOO
            SG_ AverageRadius : 6|6@0+ (0.1,0) [0|5] "m" Vector__XXX
            SG_ Enable : 7|1@0+ (1,0) [0|0] "-" Vector__XXX
            ```
            
- `CM_ <...>` : 주석같은 느낌
    - 구조1
        - 그냥 주석
        
        ```python
        <char_string>
        ```
        
    - 구조2
        - 노드에 대한 주석으로 보면 될듯.
        
        ```python
        BU_ <node_name> <char_string>
        ```
        
    - 구조3
        - 메세지에 대한 주석으로 보면 될듯.
        
        ```python
        BO_ <message_id> <char_string>
        ```
        
- `VAL_ <message ID> <signal Name> <...>`
    - signal 중에 데이터 자체로는 그 의미를 알 수 없고, 각각 매칭되어있는 의미가 존재할 경우 나열을 해주어야 한다.
    - 구조

        ```python
        <key> <value> <key2> <value2> ...
        ```
        

## can packet structure

파면 팔수록 can 통신에 대한 내용도 있으면 이해에 도움이 되는 것 같아서 기술

![image](https://user-images.githubusercontent.com/44149738/136655645-99039118-d567-426b-9ea4-d6ead6cae7bd.png)


정말 간단하게만 보면 패킷 구조는 위와 같음.

- `id` : ecu에 할당된 id
- `data length code` : 세번째 field인 data 부분의 크기를 말함.
- `data`: 이 부분은 정해진 규격이 없음. data로 퉁침.
    - 제조사마다 이 부분을 자유롭게 활용하게 됨.
    - 제조사마다 다르기 때문에 각기 다른 규격을 명시할 수단이 필요한데 그것이 바로 dbc.
    - dbc에 기술된 내용을 통해 특정 id로 통신하는 ecu 데이터의 data field를 해석할 수 있음.

## example analysis

```bash
$ git clone https://github.com/eerimoq/cantools
```

dbc 예제 파일을 사용하기 위해 레포 클론떠둠.

예제로 사용할 파일은 `tests/files/dbc/motohawk.dbc` 내용은 아래와 같음.

```python
VERSION "1.0"

NS_ : 
	NS_DESC_
	CM_
	BA_DEF_
	BA_
	VAL_
	CAT_DEF_
	CAT_
	FILTER
	BA_DEF_DEF_
	EV_DATA_
	ENVVAR_DATA_
	SGTYPE_
	SGTYPE_VAL_
	BA_DEF_SGTYPE_
	BA_SGTYPE_
	SIG_TYPE_REF_
	VAL_TABLE_
	SIG_GROUP_
	SIG_VALTYPE_
	SIGTYPE_VALTYPE_
	BO_TX_BU_
	BA_DEF_REL_
	BA_REL_
	BA_DEF_DEF_REL_
	BU_SG_REL_
	BU_EV_REL_
	BU_BO_REL_
	SG_MUL_VAL_

BS_:

BU_: PCM1 FOO

BO_ 496 ExampleMessage: 8 PCM1
 SG_ Temperature : 0|12@0- (0.01,250) [229.52|270.47] "degK"  PCM1,FOO
 SG_ AverageRadius : 6|6@0+ (0.1,0) [0|5] "m" Vector__XXX
 SG_ Enable : 7|1@0+ (1,0) [0|0] "-" Vector__XXX

CM_ BO_ 496 "Example message used as template in MotoHawk models.";

VAL_ 496 Enable 0 "Disabled" 1 "Enabled" ;
```

위에서 공부한 내용으로 분석해보자.

```python
VERSION "1.0"
```

버전은 `1.0`

```python
NS_ : 
	NS_DESC_
	CM_
  ...
```

여러 심볼 리스팅

뭐... 이 부분은 일단 그러려니 넘어감. 나중에 필요하면 다시 분석.

```python
BS_:
```

음... baudrate 설정 필드는 있는데 설정값이 없음.

두 가지 정도를 예상해볼 수 있음.

- baudrate는 default 값이 존재해서 값을 기입하지 않았을 수 있음.
- 값이 없음에도 필드를 기입한 이유는 `BS_` 필드는 필수 필드이기 때문일 수 있음.

더 알아보긴 귀찮으니 그렇지 않을까? 에서 마무리 ㅎㅎ 중요한 내용은 아닌듯.

```python
BU_: PCM1 FOO
```

노드를 정의함. `PCM1` 와 `FOO` 노드를 선언.

PCM이라는 단어에 의미가 있을 것 같아서 검색해보니 엔진 관련 제어를 하는 `파워트레인 제어 모듈` 이라고 함. 파워트레인이란 엔진에서부터 구동바퀴까지 그 사이의 모든 기관을 일컫는다고 함.

```python
BO_ 496 ExampleMessage: 8 PCM1
 SG_ Temperature : 0|12@0- (0.01,250) [229.52|270.47] "degK"  PCM1,FOO
 SG_ AverageRadius : 6|6@0+ (0.1,0) [0|5] "m" Vector__XXX
 SG_ Enable : 7|1@0+ (1,0) [0|0] "-" Vector__XXX
```

`ExampleMessage` 라는 메세지를 496번 id로 선언했다. can 통신이 발생하면 496번 id에 대해 본 구조를 기반으로 해석하면 된다. 이 메세지는 `Temperature` , `AverageRadius` , `Enable` 이렇게 총 3개의 시그널을 가지고 있다.

## cantools install & usage

```bash
$ pip install cantools
```

설치는 간단함.

```python
>>> import cantools
>>> dbc = cantools.database.load_file('tests/files/dbc/motohawk.dbc')
>>> dbc.messages
[message('ExampleMessage', 0x1f0, False, 8, {None: 'Example message used as template in MotoHawk models.'})]
```

예제 dbc 파일을 위와 같이 읽어올 수 있다.

```python
BO_ 496 ExampleMessage: 8 PCM1
 SG_ Temperature : 0|12@0- (0.01,250) [229.52|270.47] "degK"  PCM1,FOO
 SG_ AverageRadius : 6|6@0+ (0.1,0) [0|5] "m" Vector__XXX
 SG_ Enable : 7|1@0+ (1,0) [0|0] "-" Vector__XXX
```

dbc 파일에서 위와 같이 예제 메세지가 정의되어있는 부분이 있다. 이 부분을 읽어보자

```python
>>> from pprint import pprint
>>> msg = dbc.get_message_by_name('ExampleMessage')
>>> pprint(msg.signals)
[signal('Enable', 7, 1, 'big_endian', False, None, 1, 0, None, None, '-', False, None, {0: 'Disabled', 1: 'Enabled'}, None, None),
 signal('AverageRadius', 6, 6, 'big_endian', False, None, 0.1, 0, 0, 5, 'm', False, None, None, None, None),
 signal('Temperature', 0, 12, 'big_endian', True, None, 0.01, 250, 229.52, 270.47, 'degK', False, None, None, None, None)]
```

위와 같이 총 3개의 시그널을 읽어올 수 있다. 애초에 dbc가 구조가 기록된 파일이기 때문에 위와 같이 잘 정리된 객체 형태로 변환해주는 것으로 보인다.

```python
>>> msg.__dir__()
['_frame_id', '_is_extended_frame', '_name', '_length', '_signals', '_comments', '_senders', '_send_type', '_cycle_time', '_dbc', '_bus_name', '_signal_groups', '_codecs', '_signal_tree', '_strict', '_protocol', '__module__', '__doc__', '__init__', '_create_codec', '_create_signal_tree', 'frame_id', 'is_extended_frame', 'name', 'length', 'signals', 'signal_groups', 'comment', 'comments', 'senders', 'send_type', 'cycle_time', 'dbc', 'bus_name', 'protocol', 'signal_tree', '_get_mux_number', '_check_signals_ranges_scaling', '_check_signals', '_encode', 'encode', '_decode', 'decode', 'get_signal_by_name', 'is_multiplexed', '_check_signal', '_check_mux', '_check_signal_tree', '_check_signal_lengths', 'refresh', '__repr__', '__dict__', '__weakref__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
```

이 외에도 여러가지 쓸만한게 더 있는것 같아보인다.

```python
>>> msg.frame_id
496
>>> msg.is_extended_frame
False
>>> msg.name
'ExampleMessage'
>>> msg.length
8
>>> msg.signals
[signal('Enable', 7, 1, 'big_endian', False, None, 1, 0, None, None, '-', False, None, {0: 'Disabled', 1: 'Enabled'}, None, None), signal('AverageRadius', 6, 6, 'big_endian', False, None, 0.1, 0, 0, 5, 'm', False, None, None, None, None), signal('Temperature', 0, 12, 'big_endian', True, None, 0.01, 250, 229.52, 270.47, 'degK', False, None, None, None, None)]
>>> msg.signal_groups
[]
>>> msg.comment
'Example message used as template in MotoHawk models.'
>>> msg.comments
{None: 'Example message used as template in MotoHawk models.'}
>>> msg.senders
['PCM1']
>>> msg.send_type
>>> msg.cycle_time
>>> msg.dbc
<cantools.database.can.formats.dbc.DbcSpecifics object at 0x7f9db75e0fa0>
>>> msg.bus_name
>>> msg.protocol
>>> msg.signal_tree
['Enable', 'AverageRadius', 'Temperature']
```

이런식으로 필요한 데이터를 뽑아올 수 있는듯 하다.

signal 객체도 어떤 내용을 담고있는지 보자

```python
>>> sig1 = msg.signals[0]
>>> sig1.__dir__()
['_name', '_start', '_length', '_byte_order', '_is_signed', '_initial', '_scale', '_offset', '_minimum', '_maximum', '_decimal', '_unit', '_choices', '_dbc', '_comments', '_receivers', '_is_multiplexer', '_multiplexer_ids', '_multiplexer_signal', '_is_float', '_spn', '__module__', '__doc__', '__init__', 'name', 'start', 'length', 'byte_order', 'is_signed', 'is_float', 'initial', 'scale', 'offset', 'minimum', 'maximum', 'decimal', 'unit', 'choices', 'dbc', 'comment', 'comments', 'receivers', 'is_multiplexer', 'multiplexer_ids', 'multiplexer_signal', 'spn', 'choice_string_to_number', '__repr__', '__dict__', '__weakref__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
```

익숙해보이는 키워드들이 보인다.

```python
>>> sig1.name
'Enable'
>>> sig1.start
7
>>> sig1.length
1
>>> sig1.byte_order
'big_endian'
>>> sig1.is_signed
False
>>> sig1.is_float
False
>>> sig1.initial
>>> sig1.scale
1
>>> sig1.offset
0
>>> sig1.minimum
>>> sig1.maximum
>>> sig1.decimal
<cantools.database.can.signal.Decimal object at 0x7f9db75e0a00>
>>> sig1.unit
'-'
>>> sig1.choices
OrderedDict([(0, 'Disabled'), (1, 'Enabled')])
>>> sig1.comment
>>> sig1.comments
>>> sig1.receivers
[]
>>> sig1.is_multiplexer
False
>>> sig1.spn
```

매우 간단하게 다양한 정보들을 가져올 수 있다. 특히 `VAL_` 로 열거되어있는 데이터와 `CM_` 에 기술된 코멘트 내용까지 분석해서 signal 객체 내부에 기록해둔 것이 인상적이다.