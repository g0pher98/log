---
description: angr 장인이 되고 싶어졌다
---

# Angr

Symbolic Execution 기법을 이용한 CTF Solver 라이브러리.

프로젝트 자체가 재밌고, 활용도가 높을 것 같아서 angr 장인이 되고 싶어졌다.

## angr\_ctf

angr\_ctf는 angr를 실습해 볼 수 있도록 단계 별 문제를 만들어 놓은 레포다. 위 레포에 있는 문제를 풀어보며 angr에 익숙해질 수 있다.

{% embed url="https://github.com/jakespringer/angr_ctf" %}
angr\_ctf github repository
{% endembed %}

### 00\_angr\_find

![main() decompile with ghidra](<../../.gitbook/assets/image (1) (1).png>)

#### ex.py

```python
import angr

proj = angr.Project('./00_angr_find')

state = proj.factory.entry_state() # start from entry

simulator = proj.factory.simgr(state)


goal_addr = 0x804868f # push "Good Job"

simulator.explore(find = goal_addr)

if simulator.found:
    solution_state = simulator.found[0]
    posix = solution_state.posix
    print(posix.dumps(1)) # stdout
    print(posix.dumps(0)) # stdin
else:
    raise Exception('no solution')

```

#### RESULT&#x20;

```
b'Enter the password: '
b'IICLTGRK'
```



### 01\_angr\_avoid

![main() disassemble with ghidra](<../../.gitbook/assets/image (12).png>)

main 함수는 헥스레이가 동작하지 않았다. 어셈으로 보면 `maybe_good` 함수와 `avoid_me` 함수를 무척 많이 실행함을 알 수 있다. main이 어디까지인지,,,, ㄷㄷ

![maybe\_good() decompile with ghidra](<../../.gitbook/assets/image (13) (1).png>)

#### ex.py

```python
import angr
import pwn

binary_path = './01_angr_avoid'

proj = angr.Project(binary_path)
elf = pwn.ELF(binary_path)

state = proj.factory.entry_state() # start from entry

simulator = proj.factory.simgr(state)


simulator.explore(
    find = 0x80485f7, # push "Good Job."
    avoid = elf.symbols['avoid_me'] # avoid!
)

if simulator.found:
    solution_state = simulator.found[0]
    posix = solution_state.posix
    print(posix.dumps(1)) # stdout
    print(posix.dumps(0)) # stdin
else:
    raise Exception('no solution')

```

#### RESULT

```
b'Enter the password: '
b'JLVUSGJZ'
```



### 02\_angr\_find\_condition

00번 문제랑 유사함. find와 avoid에 python function을 전달할 수 있음을 알려주는 문제.

```python
import angr
import pwn
import sys

binary_path = sys.argv[1]

proj = angr.Project(binary_path)

state = proj.factory.entry_state() # start from entry

simulator = proj.factory.simgr(state)


def finder(state):
    stdout = state.posix.dumps(1)
    if b"Good Job." in stdout:
        return True

    return False

def avoider(state):
    stdout = state.posix.dumps(1)
    if b"Try again." in stdout:
        return True
    
    return False

simulator.explore(
    find = finder,
    avoid = avoider
)

if simulator.found:
    solution_state = simulator.found[0]
    posix = solution_state.posix
    print(posix.dumps(1)) # stdout
    print(posix.dumps(0)) # stdin
else:
    raise Exception('no solution')

```

#### RESULT

```
b'Enter the password: Good Job.\n'
b'OHYJUMBE'
```



### 03\_angr\_symbolic\_registers

![main() decompile with ghidra](<../../.gitbook/assets/image (11).png>)

```python
import angr
import pwn
import sys

binary_path = sys.argv[1]

proj = angr.Project(binary_path)

state = proj.factory.entry_state() # start from entry

simulator = proj.factory.simgr(state)

simulator.explore(
    find = 0x804892a # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    posix = solution_state.posix
    print(posix.dumps(1)) # stdout
    print(posix.dumps(0)) # stdin
else:
    raise Exception('no solution')

```

음??? scanf로 여러 값을 입력받는 상황을 angr가 잘 인식하지 못한다고 했는데, 그새 업데이트가 된 것지 그냥 find 주소만 넣어주면 알아서 잘 찾는다,,, angr 클라스,,, 하지만 문제 제목에 맞게 레지스터를 활용하는 예제이기 때문에 다시 풀어보자

![get\_user\_input() disassemble](<../../.gitbook/assets/image (8).png>)

`get_user_input()` 함수의 어셈코드부터 살펴보면 EAX, EBX, EDX 레지스터에 입력받은 데이터를 넣고 return 한다.

![after get\_user\_input()](<../../.gitbook/assets/image (9).png>)

호출 이후에는 레지스터로 전달받은 데이터를 스택에 저장한다. 호출 바로 다음에서 레지스터에 원하는 값을 넣어 동작하도록 설정하면 된다.

```python
import angr
import pwn
import sys
import claripy

binary_path = sys.argv[1]

proj = angr.Project(binary_path)

state = proj.factory.blank_state(addr = 0x080488c7) # start after get_user_input()

# set regs
pw_list = [claripy.BVS('pw %d' % i, 32) for i in range(3)]

state.regs.eax = pw_list[0]
state.regs.ebx = pw_list[1]
state.regs.edx = pw_list[2]


simulator = proj.factory.simgr(state)

simulator.explore(
    find = 0x804892a # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    for pw in pw_list:
        print(hex(solution_state.solver.eval(pw)))
else:
    raise Exception('no solution')

```

#### RESULT

```
0xe9b37483
0x7aab5fde
0x8f5b48ea
```



### 04\_angr\_symbolic\_stack

![handle\_user() decompile](<../../.gitbook/assets/image (10).png>)

위 문제 역시 목적지만 넣어줘도 알아서 잘 푼다. 문제 의도에 맞게 스택을 조작해서 풀어보자.

```python
import angr
import pwn
import sys
import claripy

binary_path = sys.argv[1]

proj = angr.Project(binary_path)

state = proj.factory.blank_state(addr = 0x080486ae) # start after scanf()

# set stack
pw_list = [claripy.BVS('pw %d' % i, 32) for i in range(2)]
state.regs.ebp = state.regs.esp
state.regs.esp -= 0x08
state.stack_push(pw_list[0])
state.stack_push(pw_list[1])
state.regs.esp -= 0x08

simulator = proj.factory.simgr(state)

simulator.explore(
    find = 0x80486fb # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    for pw in pw_list:
        print(solution_state.solver.eval(pw))
else:
    raise Exception('no solution')


```

#### RESULT

```
2089710965
12847883
```



### 05\_angr\_symbolic\_memory

![main() decompile](../../.gitbook/assets/image.png)

전역변수에 심볼을 넣어서 푸는 문제인듯.

```python
import angr
import pwn
import sys
import claripy

binary_path = sys.argv[1]

proj = angr.Project(binary_path)

state = proj.factory.blank_state(addr = 0x8048618) # start after scanf()


# set memory
buf_addr = [0xab232c0, 0xab232c8, 0xab232d0, 0xab232d8]
pw_list = [claripy.BVS('pw %d' % i, 8*8) for i in range(4)]
for i in range(4):
    state.memory.store(buf_addr[i], pw_list[i])



simulator = proj.factory.simgr(state)
simulator.explore(
    find = 0x8048684 # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    for pw in pw_list:
        print(solution_state.solver.eval(pw, cast_to=bytes))
else:
    raise Exception('no solution')

```

#### RESULT

```
b'OJQVXIVX'
b'LLEAOODW'
b'UVCWUVVC'
b'AJXJMVKA'
```



### 06\_angr\_symbolic\_dynamic\_memory

![main() decompile](<../../.gitbook/assets/image (13).png>)

이번엔 힙 할당을 받은 경우기 때문에 동적 메모리 대신에 심볼을 넣어야 한다. bss와 같이 읽고 쓸 수 있는 영역에 심볼을 올리고, 이를 fake heap으로 사용하면 된다.

```python
import angr
import pwn
import sys
import claripy

binary_path = sys.argv[1]

proj = angr.Project(binary_path)
elf = pwn.ELF(binary_path)

state = proj.factory.blank_state(addr = 0x80486af) # start after scanf()

# set dynamic memory
pw_list = [claripy.BVS('pw %d' % i, 8*8) for i in range(2)]

state.memory.store(elf.bss() + 10, pw_list[0])
state.memory.store(elf.bss() + 19, pw_list[1])

state.mem[elf.symbols['buffer0']].uint32_t = elf.bss() + 10
state.mem[elf.symbols['buffer1']].uint32_t =  elf.bss() + 19

simulator = proj.factory.simgr(state)
simulator.explore(
    find = 0x8048775 # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    #print(solution_state.posix.dumps(0))
    for pw in pw_list:
        print(solution_state.solver.eval(pw, cast_to=bytes))
else:
    raise Exception('no solution')


```

#### RESULT

```
b'OFIJHOXV'
b'FBQISOZO'
```



### 07\_angr\_symbolic\_file

![main() decompile](<../../.gitbook/assets/image (3).png>)

음,,, 제목도 그렇고 파일입출력 시 심볼 사용방법에 대한 문제인 줄 알았는데, 그냥 표준입력을 통해 해결이 되는 문제였다. 뭐,,,지,,,?

```python
import angr
import pwn
import sys
import claripy

binary_path = sys.argv[1]

proj = angr.Project(binary_path)
elf = pwn.ELF(binary_path)

state = proj.factory.entry_state()

simulator = proj.factory.simgr(state)
simulator.explore(
    find = 0x80489a1 # push "Good Job."
)

if simulator.found:
    solution_state = simulator.found[0]
    print(solution_state.posix.dumps(0))
else:
    raise Exception('no solution')


```

#### RESULT

```
OBAXRUZT\x00@\x16;8\x10\x0c"@\x80\x83\x04B*\xca\x00$\x10"\x89\xe9J\xa0\xcc$A:\x01#J"\x84\x04\x05\x00\x04\x02\x14)\x02:\x0c\x80AM"\x0e\x0c\x01IJN\x1c\xa7\x89\x88
```



### 08\_angr\_constraints



### 09\_angr\_hooks





### 10\_angr\_simprocedures



### 11\_angr\_sim\_scanf



### 12\_angr\_veritesting



### 13\_angr\_static\_binary



### 14\_angr\_shared\_library



### 15\_angr\_arbitrary\_read



### 16\_angr\_arbitrary\_write



### 17\_angr\_arbitrary\_jump



















## Reference

* [https://hackyboiz.github.io/2021/07/10/j0ker/angr\_part1/](https://hackyboiz.github.io/2021/07/10/j0ker/angr\_part1/)
* [https://hackyboiz.github.io/2021/07/21/j0ker/angr\_part2/](https://hackyboiz.github.io/2021/07/21/j0ker/angr\_part2/)
* [https://hackyboiz.github.io/2021/08/04/j0ker/angr\_part3](https://hackyboiz.github.io/2021/08/04/j0ker/angr\_part3)/
* [https://blog.naver.com/PostView.nhn?blogId=outdoorfrog\&logNo=221765687571\&parentCategoryNo=\&categoryNo=12\&viewDate=\&isShowPopularPosts=true\&from=search](https://blog.naver.com/PostView.nhn?blogId=outdoorfrog\&logNo=221765687571\&parentCategoryNo=\&categoryNo=12\&viewDate=\&isShowPopularPosts=true\&from=search)
*









