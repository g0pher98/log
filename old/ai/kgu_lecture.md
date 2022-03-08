Q1.
    어떻게 하면 인공지능 시스템을 구현할 수 있는지. 접근방법(approach, =구현방법)에 대해서 설명하시오.
A1.
 
    인공지능 시스템을 구현하는 방법에는 크게 신호처리와 기호처리 두 가지로 나누어 볼 수 있다.
    <비-기호처리(신호처리)>
    신호처리는 환경과 상호작용하는 과정에서 많이 사용된다. 환경에 대한 raw한 데이터를 sensor를 통해 신호(signal)로 입력을 받고, action을 위해 대상 동력기에 signal을 출력한다. 자율주행 자동차와 같이 환경을 받아들이는 속도가 중시되는 실시간 처리에 적합하다.
    <기호처리>
    정통적인 인공지능 접근법으로, 신호를 기호로 변환하고, 지식을 기반으로 문제에 접근하는 방법이다. 처리 이전에 내부적으로 어떻게 처리를 진행할 것인지 논리적으로 추론하여 설계하고, 처리를 통해 문제의 해를 찾을 수 있도록 한다. 속도가 느리기 때문에 실시간 보다는 대규모의 고수준 문제에 접근할 때 용이하다.
    <혼합/통합적 방법>
    기호/비-기호 처리방식을 혼합한 방식이다. 실시간성이 필요한 저수준 인식과 행동제어에는 비-기호처리 방법을 적용하고, 고수준의 문제와 의사를 결정하는 부분에는 기호처리 방법을 적용한다.

Q2.

    Agent란? 
A2.

    환경과 상호작용하는 자율존재. 환경의 변화에 영향을 받으며, 환경을 통해 행동을 결정하고, 행동이 환경에 영향을 미치는 존재. 껍데기만 있는 로봇(ex 축구로봇)들은 agent라고 볼 수 없음. 여기서 행동의 결과가 가장 좋은 결과를 가져다줄 것 같은 행동을 선택할 줄 아는 agent를 rational agent라고 한다.

Q3.

    Rational한 agent를 판단하는 기준 PEAS란?
A3.

    작업환경(Task Environment)를 명세하여 Rational한 agent를 설계해야한다.
    - Sensors
    - Actuators(=effector) : 행동하는 신체부위
    - Environment
    - Performance Measure
    sensor와 actuators는 agent의 신체 일부로 볼 수 있음.
    
Q4.

    작업을 해야하는 환경의 특성에는 어떤것들이 있는가?
A4.

    세상일은 사실 이분법으로 나누기 어렵다. 그렇지만 현재 작업하는 환경에 대해 어느정도의 이해와 구별해야 접근법을 달리할 수 있기 때문에 분류할 줄 알아야 한다.
    - fully observable / partially observable
        (완전 관측가능 / 부분 관측 가능)
        세계를 얼만큼 관측이 가능한가? 대부분 완전히 관측한다는 것은 어려움. 그런 문제는 거의 없음.
		- 완전관측 예 : 바둑게임, 체스게임 등
	    - 부분관측 예 : 자율주행 등
	- deterministic / stochastic
        (결정적 / 비결정적)
        결과를 예측할 수 있는지에 대한 특성. 어떠한 행동의 결과를 예측 가능하다면 결정적. 반대로 행동을 했는데, 그 결과를 예측할 수 없다면 비결정적.
		- 결정적 예 : 바둑두기
		- 비결정적 예 : 로봇 손으로 머그컵 들기
	- static / dynamic
        (정적 / 동적)
        내가 행동을 하지 않아도. 내가 예측하지 못한 환경이 발생한다면 동적.
		- 정적 예 : 바둑두기
		- 동적 예 : 자율주행
	- discrete / continuous
        (이산적 / 연속적)
        좌표가 격자로 표현 가능한지, 실수와 같이 연속적인 수의 변화인지. 세상에는 대부분 연속적인 문제들이 많음.
		- 이산적 예 : 바둑, 체스 등
		- 연속적 예 : 자율주행, 드론, 로봇 팔 등
	- episodic / sequential
        (단편적 / 순차적)
        과거와 현재의 연관성. 현재 단편적으로 보아야 하는건지, 과거에 영향을 받아 연계해서 생각해야 하는건지.
		- 단편적 예 : 과녁 맞추기.
		- 순차적 예 : rubik cube 퍼즐 풀기, 바둑, 체스 등
	- single agent / multiagent
        (단일 에이전트 / 멀티 에이전트)
        플레이어가 1명인지 2명이상(협력 또는 경쟁)인지.
		- 단일 예 : 퍼즐
		- 멀티 예 : 축구, 농구, 포트리스 등

Q5.

    Agent 유형(types)에는 어떤 것들이 있는가?
A5.

    Agent 유형은 무척 많을 수 있겠으나, 의사결정구조 또는 행동결정 방식에 대해서 크게 4가지로 분류해볼 수 있다. 신호/비신호 처리는 인공지능을 만드는 기초적인 방식이라고 생각하면 된다. 아래 4가지 방법은 신호/비신호로 구현할 수 있다. 또한, 이 4가지 방식 모두 학습 에이전트(learning agent)로 변경할 수 있다. 실 세계에 적용할 때는 유연성(flexibility), 효율성(efficiency) 등 다양한 사항들을 고려해야한다.
    - 단순 반응형 에이전트(simple reflex agent)
        가장 기초적인 형태의 에이전트. 에이전트의 내부는 크게 "상태추정"단계와 "행동결정"단계로 나누어볼 수 있다. 상태추정단계에서는 sensors로 입력받은 데이터를 기반으로 상태를 추정한다. 행동결정단계에서는 추정된 상태를 기반으로 행동을 결정하는데, 결정은 조건에 맞게 정해진 rule에 따른다.
        - 특징
            - no plan, no goal
            - 무엇을 하는지, 무엇을 달성해야하는지 모른다.
        - 장점
            - 빠른 행동 선택, 빠른 반응
        - 제한점
            - 올바른 행동 규칙을 미리 제공해야함.
            - 과거 경험과 미래 예측에 대한 고려가 부족함
            - 동적인 상황변화에 대처하는 유연성이 떨어짐.
    - 모델-기반 반응형 에이전트(model-based reflex agent)
        상태추정을 위해 정보가 추가된다. 직전상태(state), agent가 가능한 action들이 어떤 것들이 있는지, 언제 수행할 수 있고, 수행한다면 어떤 기대효과가 있는지, 환경이 어떻게 변하는지 등의 정보가 추가된다. 반면에 행동결정단계는 단순 반응형과 같다. 이러한 특성으로 인해 상태추정에 많은 시간이 소요되지만 행동결정은 빠르게 처리된다.
        - 특징
            - 센서의 한계 : 감지 범위, 노이즈, 다양한 불확실성
            - 센서가 외부 환경의 완전한 상태정보를 제공하지 못함.
            - 별도의 내부 상태(internal state) 정보를 유지, 관리
            - 조건-행동 규칙(condition-action rule)들을 적용, 행동 결정
        - 내부상태의 관리 및 갱신
            - 2가지 지식(모델)이 필요
                - 월드모델 : 외부 환경 지식
                - 행동모델 : 행동이 환경에 미치는 효과 추정
    - 목표-기반 에이전트(goal-based agent)
        상태추정 이후, 행동을 결정하기 이전에 각 행동의 결과를 예측하여 목표(goal)에 도달할 수 있는 행동을 결정하는 에이전트
        - 특징
            - 현재상태, 목표, 실행가능한 행동과 효과에 대한 지식을 이용
            - 목표(goal) 달성을 위한 행동(action)을 결정
            - 적용 기술 : 탐색(search)과 자동계획(planning)
        - 장점
            - 목표 지향적 행위
            - 높은 자율성과 유연성
        - 단점
            - 복잡한 행동결정 과정
            - 느린 반응, 낮은 효율성
    - 유틸리티-기반 에이전트(utility-based agent)
        각 행동의 결과를 예측한 이후, 각 행동의 결과상태의 손익을 계산하는 로직이 추가된다. 이때, 손익을 계산할 때 평가 지표가 되는 가치/손익/행복 척도를 utility라고 한다.
        - 유틸리티 함수(utility function)
            - 유틸리티 : 행복/쓸모/이득
            - 각 상태의 유틸리티 값을 평가
        - 특징
            - 높은 유틸리티 값을 얻을 수 있는 행동을 선택
            - 합리적인 의사결정(rational decisions)을 요구
            - 양질의 행위(high-quality behavior)를 생성
    
Q6.

    "상태 공간 탐색 문제(state space search problem)"를 해결하기 위한 필수요소
A6.

    - states : 가능한 상태들
    - actions (=state transitions) : 가능한 행동들
    - initial state : 초기상태
    - goal condition : 목표상태
    - (?)solution
    - (?)action/path cost



Q7.

    search strategies (탐색 전략/방법)에 대해 기술
A7.

    - search directions(탐색 방향)
        - forward search(전향탐색)
        - backward search(후향탐색)
        - bidirectional search(양방향 탐색)
    - information의 유무
        - uninformed search(무정보 탐색)
            - breadth-first search(너비 우선 탐색)
            - depth-first search(깊이 우선 탐색)
            - uniform/least/lowest cost search(균일/최소/최저 비용 탐색)
            - iterative deepening search(반복적 깊이 증가 탐색)
        - informed or heuristic search(정보/휴리스틱 탐색)
            - best-first search(최적 우선 탐색)
            - a* search
            - iterative deepening a*(IDA*) search


Q8.

    탐색 전략을 평가하는 기준
A8.

    - completeness, 완전성 : 해가 있다면 언젠가는 반드시 하나 이상의 해를 찾는다.
    - time complexity, 시간 복잡도
    - space complexity, 공간 복잡도
    - optimality, 최적성 : 반드시 최적의 해를 찾는다.


Q9.

    uninformed search(무정보 탐색) 알고리즘
A9.

    - breadth-first search (너비 우선 탐색)
        - FIFO Queue와 유사
        - complete : yes
        - optimal : yes
        - time : 1+b+b^2+b^3 ... b^d = O(b^(d+1))
        - space : O(b^(d+1)) (깊이만큼 모든 노드를 메모리에 가지고있다)
    - uniform cost search (최소비용 탐색)
        - 비용이 가장 적은 노드부터 탐색. 결국 너비우선과 비슷.
        - complete : yes
        - optimal : yes
        - time : O(b^(???깊이))
        - space : O(b^(???깊이))
    - depth-first search (깊이 우선 탐색)
        - LIFO Queue와 유사.
        - complete : no (무한히 깊게 탐색하는 문제 발생)
        - optimal : no
        - time : O(b^m)
        - space : O(bm) (메모리 효율적임.)
    - depth-limited search (깊이 제한 탐색)
        - 깊이우선 탐색에 깊이 제한을 걸어둠.
        - 깊이보다 아래에 해답이 있을 경우 해를 찾을 수 없기 때문에 깊이 설정을 잘 해주어야 하는데, 이게 현실적으로 어려움.
    - iterative deepening search (IDS, 반복적 깊이 증가 탐색)
        - 너비우선과 깊이우선을 결합한 형태. 양쪽의 장점을 가져감.
        - 계산량은 다른 알고리즘에 비해서 많다. 다른 트리를 확장하기 위해 상위노드부터 다시 탐색해야하는 불필요한 연산이 반복됨.
        - 무정보 탐색 알고리즘 중에서는 그나마 가장 낫다!!
        - complete : yes
        - optimal : yes
        - time : (d+1)b^0 + db^1 + (d-1)b^2 ... b^d = O(b^d)
        - space : O(bd)

Q10.

    Repeated states(반복상태)란?
A10.

    다른 위치에 있지만, 동일한 특성의 노드는 자식노드도 동일함. 즉, 두개 모두 확장하는 행위는 불필요함. 한번 확장한 노드와 같은 특성의 노드는 확장하지 않는 방식이 graph search(그래프 탐색) 알고리즘이다. tree search는 중복 생각않고 계속 확장하기 때문에 비효율적이다.

Q11.

    Graph search(그래프 탐색)란?
A11.

    tree search 방식은 중복되는 노드에 대해서 고려하지 않는다. 동일한 특성의 노드는 자식노드도 동일하기 때문에 두 노드 모두 확장하는 것은 불필요한 리소스가 발생하는 일이다. 이를 고려하는 방식이 graph search다. 이미 확장한 노드는 다시 확장하지 않음으로써 효율성을 높인다.

Q12.

    informed or heuristic search(정보/휴리스틱 탐색) 알고리즘
A12.

    - Best-First search
        - 비용을 계산하는 평가함수(evaluation function) f(n)이 존재함.
        - 이 평가값(비용, cost)이 작은 노드부터 확장
        - 우선순위 큐(priority queue)와 유사
    - greedy best-first search
        - f(n) = h(n) (heuristic)
        - 휴리스틱 함수의 결과값이 작을수록 좋은 노드.
        - SLD
            : Straight-Line Distance
            : 목표지점까지 거리가 얼만큼 남았는지 반환
        - complete : no
        - optimal : no
        - time : O(b^m)
        - space : O(b^m)
    - A* search
        - A*의 성능은 휴리스틱 함수에 달려있다!!
        - f(n) = g(n) + h(n)
            - g(n) : 출발지에서부터 현재까지 도달하기 위한 cost
            - h(n) : 목적지와의 거리
            - f(n) : 현재 노드를 지나가는 solution 중 최소비용.
        - complete : yes
        - optimal : yes
        - time : O(b^d)
        - space : O(b^d)

Q13.

    Admissible한 Heuristics 함수란?
A13.

    휴리스틱 함수가 admissible 하기 위해서는 모든 노드에 대해서 실제비용 h(n)보다 같거나 작아야한다. 크게 예측되면 과대평가 또는 over-estimates 되었다고 한다. 휴리스틱 함수가 위 조건을 만족한다면 a* 알고리즘의 경우 complete 하게 optimal한 해를 찾는다. 다만 휴리스틱 함수에 따라 속도차이가 발생한다. 그럼에도 휴리스틱이 아무리 작은 값을 예측한다고 해도 a* 알고리즘은 어느정도 커버를 해서 해를 찾을 수 있다. admissible하도록 제작하기 위해서 h(n)에 가깝게 설정하면 자칫 값을 넘어버릴 수 있기에 안전하게 무척 낮은 값으로 설정하는 경우가 있다. 이것은 틀린 방법이 아니다.

Q14.

    dominance란?
A14.

    h1과 h2 두 개의 휴리스틱 함수가 모두 admissible할 때, h2 >= h1인 경우, h2가 h1보다 더욱 효율적인 search를 가능케 한다. 즉, h2가 h1보다 좋으며, 이를 h2가 h1을 dominates(지배?)한다고 말한다.

Q15.

    Local search algorithms(지역 탐색 알고리즘) 이란?
A15.

    - initial state와 goal이 제공되지 않음. 평가함수만 주어짐. 즉, 최적의 상태를 찾아가는 탐색방법.
    - 지역 탐색이란 현재 기준으로 주변을 탐색하여 목표에 도달하는 것을 말한다. 기존에 공부하던 방식과 연계되는게 아니라 새로운 개념임.
    - 많은 경우에 "최적화 문제"에 사용된다.
    - 경로에는 관심 없고, 최적이라고 생각하는 state에만 중점을 둔다고 볼 수 있다.
    - 지역탐색에도 탐색하는 공간이 존재한다. 그러나 기존 탐색전략과는 다르게, complete configurations를 상태공간으로 삼는다.
        - complete configuration란?
            : 체스를 예를들면, 기존방식은 각 말의 위치를 각각의 state로 본다. 그러나 이와 다르게, 모든 말들이 위치해있는 "전체상태"를 하나의 값으로 본다.
    - evaluation function (평가함수) f(s)가 주어지거나 문제 안에서 만들어야한다. 이러한 평가함수는 문제의 제약사항 등이 반영이 되어있다. 값이 클수록 좋다(?)
    - single current state를 유지하면서, 자식들의 평가값 중 개선된 노드로 이동해가면서 확장한다. optimal한 state에 도달하면 알고리즘이 종료된다.


Q16.

    Local search algorithms(지역 탐색 알고리즘) 종류
A16.

    - Hill-Climbing Search(언덕 오르기 탐색)
        - 평가치가 계속 높아지는 방향으로 가는 알고리즘
        - greedy local search -> 후퇴는 절대 하지 않음.
        - local maximum problem(지역 최적점 문제)
            - 전역적 관점에서 가장 좋은 maximum에 도달하지 못함.
            - local maximum에 도달했기 때문.
    - Simulated annealing search
        - local maximum problem을 해결하고자 하는 아이디어
            - 조금 손해보더라도 더 탐색해보자!
        - annealing이란? 담금질. 금속이 뜨거울 때 가변성이 크고, 낮으면 고정적임.
            - 시작은 온도가 뜨겁고, 시간이 지날수록 식음.
            - 온도가 뜨거울 때, 손해보는 방향이더라도 모험적인 search(bad move)를 가능케 하고, 시간이 지나 점점 식어가면, bad move를 선택하지 않도록 함.
        - 시간(t)이 지남에 따라 온도(T)를 낮춤.
        - 랜덤하게 자식을 선택.
            - 자식의 평가치가 좋으면(차이가 양수) 이동.
            - 자식의 평가치가 낮으면(차이가 음수) 확률적 이동.
                - 확률은 {(부모와 자식의 평가치 차이)/(온도)}의 제곱을 기준으로 설정. 이 확률 부분을 잘 설정하는것이 중요.
    - local beam search
        - 한쪽에서만 탐색하지 말고 양쪽에서 탐색하자! 라는 아이디어
        - 평가함수를 여러개 만들어서 다양한 관점에서 동시에 탐색.
        - 탐색 지점이 많으면 리소스가 많이 발생함. 
        - 결국에는 평가함수들이 비슷한 방향으로 탐색을 하는 현상이 발생.
            - stochastic beam search : 평가치 best가 아니어도 탐색
                - ex) Genetic Algorithms
    - genetic algorithms(GA, 유전 알고리즘)
        - 부모와 비슷한 상태를 만듬.
        - 부모의 유전정보를 조합하여 새로운 유전정보를 제작.
        - 환경에 적합하면 살아남음. 적자생존.
        - 세대를 거듭하면서 좋은 유전자만 생존.
        - 각 세대별로 k개 존재.
            - 자식세대에서 우수한 k개만 생존
                = 한 세대에 k개를 유지하는 state = population 집단
        - 자식 생성 시 돌연변이 생성.
        - 자연계에서 카피해온 방식이지만, search 관점에서 보았을 때, 병렬적 처리와 다형성이라는 큰 장점이 있음. 이것이 복잡하고 어려운 문제에서 가장 최적의 solution을 찾는 좋은 해법으로 쓰임.
        - 용어정리
            - state는 10진수 string으로 표현됨.
            - 이것을 bit로 변경한 것이 chromosome(염색체).
            - 한 bit가 gene(유전자).
            - 평가함수(evaluation function)
                == 적합도 함수(fitness funciton)
                    : 자연계에 얼마나 적합한가? 라는 의미.
            - k개의 집단 : generation(세대)
            - genetic operators : 유전 연산자
            - selection : 교배할 부모 선택(반드시 평가치가 좋은것만 사용하지는 않음)
            - crossover(교배) : 두 부모의 유전정보를 섞음.
            - mutation : 돌연변이. 특정 bit를 수정함.
        - states를 string으로 인코딩
        - 여러개의 상태들을 동시에 탐색
        - 탐색에 적합도 함수를 이용
        - 확률적인 상태 전이

Q17.

    Advaersarial search problems
    상대가 존재하는 상황(multiagent)에서의 탐색 알고리즘
A17.

    크게 competitive(경쟁)
    - 2-player game search tree
        - 가능한 state들을 tree 형태로 표현
        - 나와 상대가 번갈아가면서 layer로 나타남.
        - terminal(단말) state의 노드가 나올때까지 확장.
            - 단말상태 utility 평가 ex) 패(-1), 무(0), 승(1)
    - minimax search
        - depth fisrt search (깊이 우선 탐색)
        - 단말 노드의 평가치가 tree의 위쪽으로 전파.
        - 상대 layer의 노드들에서 상위노드로 전파될 때 min값을 전파
        - 나의 layer의 노드들에서 상위노드로 전파될 때 max값을 전파
        - 상대도 나와 동일한 상태 평가 함수를 가지고 있다고 판단.
        - 나도, 상대도 최적의 상태를 선택할 것이라고 판단.
        - complete : yes (목표상태가 있다면 도달할 수 있다)
        - optimal : yes (root노드의 평가치가 최적인가?)
        - time : 깊이우선탐색과 동일
        - space : 깊이우선탐색과 동일
        - 체스와 같이 depth가 깊은 게임의 경우 결론이 안난다.
            - infeasible하다. 현실적으로 적용 불가능하다.
    - cutoff search
        - depth limit 을 설정하고, 해당 깊이에 도달 하면 evaluation funciton으로 평가.
    - a-b pruning/search
        - max layer -> alpha
        - min layer -> beta
    - negamax search
        - min/max를 처리하는 함수를 따로 두지 않고, -1을 곱하면서 재귀하여 max 하나로 처리.



(9주차)
1. planning
    - planning이란?
        - 목표가 주어지면, 현재상태부터 목표상태까지 진행될 수 있는 여러 상태들을 상태공간이라고함.
        - 목표상태가 어디있는지 모른다. 목표상태까지 어떻게 가야하는지가 핵심.
        - action들에 대한 sequence 를 찾기 위한게 planning
        - solution은 optimal(최적)하다. (= 비용이 최저)
        - planning하는 기술은 탐색만 있는건 아니다! 학습을 통해서도 가능하다.
    - classical planning (고전적인 planning)
        - 가정
            - 환경(environment)
                - 말도 안되지만 환경을 가장 쉽게 정의한다.
                - deterministic : 결정적이다
                - static : 정적이다
                - fully observable : 세상을 관측 가능하다
                - discrete : 이산적이다.
                - single agent : 단일 객체
            - 행동(action)
                - atomic : 더이상 나눌 수 없는 행동이다
                - duration-less : 수행시간이 들지 않는다.
                - taken only one at a time : 한순간에 실행된다
            - 초기상태(initial state)
                - 명확하게 알려져 있다 (불확실한 경우가 꽤 많다)
            - 목표조건(goal condition)
                - 명확하게 제시된다.
    - state & action에 대한 표현 (!! 중요) 
        - 기호로 표현, 더 깊이들어가 논리로 표현하는 방법에 대해 알아본다.
        - 상태(state)
            - "closed world assumption" : 언급되지 않은 사실은 모두 거짓이라고 가정함.
            - 세상의 모든 형태와 관계를 서술하기 어려움이 있음.
            - 이를 단순하게 생각해서 복잡한건 없다고 가정하고 진행
            - ex) on(C,B)
        - 행동(action)
            - 모든행동은 크게 preconditions와 effect로 나누어볼 수 있다.
            - preconditions : 행동을 실행할 수 있는 환경의 전제조건.
                - ex) 앞에 장애물이 없으면 직진
            - effect : 실행 시 어떠한 환경 변화가 일어나는지
    - PDDL Representation Language: Domain, Problems
        - 구성
            - domain.pddl
                - 환경에 대한 기본 설명
                - 어떤 물체들이 있고, 누가 일을 해야하는지 등
                - 행동할 수 있는 고정적인 것들
            - task/problem.pddl
                - initial state
                - goal states
            - 예
                - blocks world
                    - domain
                        - objects(물체 종류)
                            - A, B, C, Table, ...
                        - predicates(관계 서술자들)
                            - on(x,y), ontable(x), clear(x), hold(x), ...
                        - actions(행동들)
                            - pick-up(x), put-down(x), stack(x,y), unstack(x,y), ...
                    - task/problem
                        - domain
                        - objects (물체 종류)
                        - init (초기상태)
                        - goal (목표상태)
        - 핵심은 search. 즉, 탐색이다. 
        - 탐색방법
            - forward state-space search (+heuristics)
                - 출발점에서 목표를 향해 하나씩 찾아간다
                - 대부분 A* search를 사용한다.
                - ex) fast-forward(FF), Pyperplan
            - backword state-space search (+constraints)
                - 목표에서부터 출발점 방향으로 하나씩 찾아간다
                - ex) GraphPlan
            - reduction to propositional satisfiability problem
                - 이런게 있다.
                - ex) SATPlan
            - search in the space of plans
                - 이런게 있다.
                - ex) partial order planning(pop)
    - Forward State-Space Search Planning
        - s` = (s - DEL(A)) U ADD(a)

2. Learning from Examples (사례를 통한 학습)
    - Learning 의 개념
        - 경험을 통해 작업 성능을 개선하는 것.
        - 경험이 있다면 같은 작업에 대해서 성능이 개선되는 것.
    - Learning의 필요성
        - agent system을 설계하는 designer가 실제로 구동할 때, 발생 할 모든 상황을 예측할 수 있는가? 그럴 수도 있지만 실제로는 모.든.상.황. 에 대해서는 대비할 수 없다.
        - agent가 스스로 경험을 통해 행동을 수정해야함.
        - 그리고 무슨 상황이 벌어질지는 알겠지만, 어떤 선택이 가장 최적인지 인간이 판단하기 어려울 때. 이것도 agent가 스스로 계산을 통해 판단하는게 더 좋을 수 있음
        - 필요성 정리. 상황을 예측하지 못하는 경우와 상황은 예측하지만 최적의 대처를 선택하기 어려운 경우가 발생할 수 있기 때문에 agent가 스스로 의사/행동 결정 구조를 변경할 수 있도록 learning이 필요함.
    - 학습 대상 요소들(= 무엇을 learning 해야하는가?)
        - 에이전트 유형/구조에 따라 다름
            - simple reflex, model-based reflex, goal-based, utility-based agents
            - 이러한 요소/구조들 각각이 나름대로 행동을 결정하는 방식이 각자 있음.
            - 내부 구조상 행동에 영향을 주는 부분을 찾아 변경해야한다.
        - 학습 대상 요소들
            - condition-action rules
            - world model, action model
            - goal, utility, value
    - data & knowledge 표현법
        - 모든 정보는 데이터로 표현되어야 한다.
        - 데이터 표현 방법에 따라 학습방법도 달라진다.
        - "데이터"로부터 "학습"을 통해 얻어지는 것이 "지식"이다.
        - 학습법
            - 확률 그래프(베이지안 네트워크)
            - 인공 신경망
            - 결정 트리
    - 사전지식
        - 기존 알고있는 지식이 어느정도 있는지에 따라 학습 방법이 달라진다
        - Inductive learning (귀납적 학습)
            - 다수의 구체적 사례들 -> 일반화된 지식
        - Deductive or analytical learning (연역적 또는 분석적 학습)
            - 일반화된 지식/규칙 -> 구체적인 사례/지식/규칙
    - feedback to learn from (피드백)
        - supervised learning (교사학습, 감독학습)
            - 라벨링된 학습 데이터.
            - 해당 데이터가 어떤 것인지 알려줌.
            - classification(분류) 또는 regression(회귀:수치예측) 형태로 쓰임.
        - unsupervised learning
            - input만 주고 그것이 무엇인지 알려주지 않음.
            - 스스로 기준을 세우고 판단하는 것.
            - clustering(군집화)에 사용됨.
        - reinforcement learning (강화학습)
            - 데이터가 주어지는게 아님.
            - 데이터를 습득. 경험해야함.
            - agent와 환경 사이의 상호작용을 통해 얻어야함.
            - online policy learning (온라인 정책 학습)
                - 실제로 경험을 통해 학습
                - 학습 시간이 오래걸림. 하나하나 경험해야하기 때문.

(10주차)
- Feedbacks to Learn From(피드백)
    - Learning types (depending on feedbacks)
        - supervised learning (교사학습, 감독학습)
            - 라벨링된 데이터를 준다
            - classification(분류) : 개념을 학습
                - 좌표상에서 class를 구분하는 선(경계선)을 찾음.
            - regression(회귀) : 연속된 수치값을 통해 예측값을 출력
                - 이산적인 데이터들의 규칙성을 나타내는 선을 찾음.
        - unsupervised learning(비-교사학습, 무-감독학습)
            - 입력에 대한 정답이 없다. 즉, 입력값만 존재
            - 그저 입력값들의 유사성(similarity)과 차별성(difference)을 분석
            - 일반적으로 이런 군집 개수를 주면 특징에 따라 군집화.
        - reinforcement learning(강화학습)
            - 기존(supervised/unsupervised)은 offline에서 데이터를 학습하여 online에 들어간다.
            - 강화학습인 기본적으로 online 학습이다.
            - agent가 environment에 놓인 상태에서 경험을 통해 배운다.
            - 선 행동 후 학습.
            - state에 따른 reward를 받음. 이 reward를 통해 선택에 대해 학습한다.
            - 이러한 reward를 책정하는 함수. 즉, policy가 생성됨.
                - policy p : State -> Action (상태-행동 대응 함수)
                - 가능하면 optimal(최적)한 평가면 좋음.
                - 같은 state를 마주했을 때, 좋은 평가의 action을 할지, 새로운 action을 할지.
                    - 즉, exploration(과거) / exploitation(도전) issue가 존재.

- Supervised Learning (감독/교사 학습) 맛보기
    - learning problem
        - 학습자에게는 알려져 있지 않은 함수가 있음. target function(목적함수)
        - example(input과 output의 쌍으로 구성)로 이루어진 training set(훈련집합)를 제공함.
        - 목적함수에 유사한 hypothesis(가설함수)를 찾는다.
    - test set != training set
        - 학습데이터와 테스트 데이터는 달라야 제대로된 모델 평가가 가능함.
    - generalization(일반화)
        - hypothesis가 새로운 example에 대해 잘 예측해야 한다. = 일반화.
    - classification(분류)
        - class를 잘 분류해서 출력해야한다.
    - regression(회귀)
        - 연속된 숫자를 예측한다.

- Suplervised Learning
    - h는 consistent해야한다. 즉, f에 같은 결과를 내야함.
    - 초기의 h의 모양은 제공한다. 여기서 모양이란 함수 h의 차수를 말한다.
        - 1차 함수를 예로 들면, h(x) = ax+b 인 h를 가정하고, a와 b 값을 train하여 f에 가까운 h를 찾는다.
    - Ockham's razor: h는 simplest해야한다. f가 3차함수라면 4차, 5차로도 충분히 학습이 가능하지만 학습 시간도 늘어나고, 학습데이터는 한정되어있기 때문에 의미없는 과정이 발생한다. 3차로도 충분.
        - 1차함수부터 차례대로 테스트해보는것도 좋다.

- Learning Decision Trees(DT : 결정트리)
    - 행동 선택 매커니즘
    - 각 속성들을 tree 형태로 표현.
    - 확보된 값을 가지고 머신러닝을 돌리는 것도 중요하지만 그 전에 데이터를 포멧에 맞게 가공하는것이 중요.

- Attribute-Based Representations
    - example들을 attributes(속성)에 대해 나열하여 표현한다.
    - 도메인을 잘 분석해서 영향을 주지않는. 즉, 필요없는 attribute는 제거해야 학습 속도에 영향을 미친다.

- Decision Tree Learning
    - tree에서 root node를 누구로 설정하고, 어떻게 tree구조를 뻗어나갈지 탐색.
    - 가장 주요한 attribute는 무엇인가?
        - psudo code를 보면 choose-attribute(attributes, example) 메소드로 example 하나에 대해 어떤 attribute가 잘 설명할 수 있는지 선택하는 것을 알 수 있음
    - 이런식으로 학습시켜 노드를 구성한 인공지능은 explainable한 인공지능이다.
        - 각 노드의 의미를 파악할 수 있기 때문에 인간이 추가적으로 작업할 수 있다.
    - 오류나, noize가 있는 training set이 제공되면 크게 문제가 생길 수 있다.

    - choosing an attribute
        - tree의 자식노드가 terminal인 방향으로 가는 attribute를 설정하는 것이 좋음.
        - 즉, 빨리 정리되는 방향이 좋음.
        - teminal node가 아닌 경우는 class의 엔트로피가 낮아질수록(한쪽에 쏠릴수록) 좋음.

    - Using Information Theory
        - Information Content(Entropy: 혼합도, 불순도)
        - 얼마나 서로 다른 class의 인스턴트가 섞어있는지에 대한 척도. 0~1 사이의 값.
            - P = ( p/(p+n) )
            - N = ( n/(p+n) )
            - L(P,N) = ( -P * log2(P) ) + ( -N * log2(N) )

    - Information Gain (IG : 정보획득량)
        - 결론 : IG를 계산해서 가장 높은 값을 root node를 설정하겠다.
        - IG(A) = Entropy - remainder(A)
            - A : attribute
            - remainder : A로 분리한 후에 발생한 부분집합의 평균 entropy
            - 즉, IG는 Attribute로 분리했을 때, entropy의 변화량을 뜻함.

(11주차)
- Evaluating Hypothesis (가설 평가)
    - 가설의 오류율
        - 어떠한 가설이 더 좋은지를 평가.
        - 최적의 파라미터를 결정하는 것.
        - 오류율이란? 예측값과 실제 결과를 비교하여 몇개를 틀렸는지에 대한 정보만 가지고 비교하는 것.
    - 검증 집합(validation set)
        - training set(훈련집합)
        - validation set(검증 집합)
            - 성능 검증만을 위한 데이터셋임.
            - 사실상 테스트 집합. 굳이 나눈 것.
        - test set(테스트 집합)
    - cross-validation (교차 검증)
        - 학습에 쓰인 데이터를 사용하지 않겠다! 라는 의미
        1. holdout cross-validation
            - 전체에서 test용 데이터를 별도로 확보해놓고 학습시킨다.
            - 그렇다고 한쪽 특성에 치우친 testset를 확보하는건 좋지 않다.
            - 예를 들면 각 마을을 대표하는 1명씩 뽑은것이 좋다는것과 같은 맥락.
            - 전체 데이터셋이 크다면 어느정도 랜덤하게 편향되지 않을 가능성을 기대해볼 수 있지만, 전체 셋이 작다면 편향될 확률이 매우 높다.
        2. k-fold cross-validation
            - 전체를 균등한 크기인 k개로 나눈다.
            - 1/k는 test set, (k-1)/k는 train set.
            - holdout과 같지만 여기서부터 다르다.
            - 각 조각의 역할을 바꾸어보면서 테스트해본다.
            - 데이터의 편향성을 감소시킬 순 있겠지만 검증에 시간이 오래걸린다. 
        3. leave-one-out cross-validation
            - 1개만 test용도로 남긴다.
            - 데이터가 매우 적은 경우에 사용.
            - k-fold와 같은 방식으로 검증. 다만 데이터셋을 나눌 때 크기가 1이 되도록 나누는 것.
- model selection (모델 선택)
    - 최적의 h를 찾기위한 작업
        - model selection
            - 인공지능이 모든걸 하기엔 아직 무리가 있다.
            - 그러므로 사람이 어느정도 개입을 해줘야 좋은 성능이 나올 수 있다.
            - 사람이 hypothesis의 기본적인 정의를 한다. (=인간이 기본 모델을 제공)
            - ex) h의 차수를 설정하는 것.
        - Parameter optimization
            - 지정된 정보(i.g. 차수) 안에서 best hypothesis를 찾는 것.
    - Model complexity (모델 복잡도)
        - parameter size 증가. (=변수가 많아짐)
        - 훈련 데이터의 양, 학습 시간도 비례해서 증가함.
- overfitting (과적합)
    - supervised learning은 사실상 데이터를 주고 데이터에 함수를 맞추는 과정이다.
    - 그러나 이러한 과정에서 과적합 문제가 발생할 수 있다. (=Overfitting)
    - 대부분 훈련데이터에 맞추는게 좋지만, 애초에 train data가 편향된 성격이 존재할 수 있다는 점을 간과하면 안됨.
    - 편향된 데이터에 편향될 경우, 다른 케이스의 test set이 등장할 경우 예측이 어려워질 수 있음.
    - 데이터로부터 어느정도는 학습하는게 맞지만 필요 이상으로 데이터에 맞출 경우 오히려 모델의 품질이 떨어짐.
- Loss Function(손실 함수)
    - 가설함수의 성능을 평가하는 함수.
    - 용도에 맞게 손실 함수를 수정하면 그에 맞게 모델이 학습됨.
    - 그러나 일반적으로 사용되는 형태가 있음.
    1. 0/1 loss
        - 0(정답) 또는 1(오답)으로만 평가
        - 잘 안쓰임
    2. absolute value loss
        - (예측값 - 정답값) 의 절대값. L1 loss
    3. squared error loss
        - (예측값 - 정답값) 의 제곱값. L2 loss
- Choosing the Best Hypothesis(최적의 가설 선택)
    - Empirical loss (실험적 손실)
    - Empirical loss를 최소화하는 hypothesis

- Regression with Linear Models
    - Linear Models (선형 모델)
        - 1차 함수 형태의 가설.
            - `h = (w1 * x1) + (w2 * x2) + ... + (wn * xn)`
        1. Linear Regression(선형 회귀)
            - 데이터들의 근사 함수를 찾음.
            - h의 값이 예측값으로 작용.
        2. Linear Classification(선형 분류)
            - h의 값이 범위 조건에 따라 class로 변환.
            - `if (h >= 60)` -> A class
            - `if (h < 60)` -> B class

- Univariate Linear Regression(일변수 선형 회귀)
    - 파라미터를 어떻게 학습시키는가?
    - loss function의 각 attribute에 대해 편미분하여 기울기를 구한다.
        - 여러 attribute 기울기가 0가 되는 점이 cost의 최저점.
        - 사실상 이러한 값을 찾는것이 어려움.
    - local search를 이용.
        - loss function의 기울기의 부호와 값에 따라 weight를 변경하면서 loss의 최저점을 찾는다.

- gradient descent(기울기 하강)
    1. batch(일괄적) gradient descent
        - 훈련데이터를 다 사용하고 가설 변경
        - `w0 <- w0 + a( sigma(y-h(x)) )`
        - sigma를 통해 각 loss를 한번에 계산
        - 전체에 맞춘 학습. 데이터가 클수록 속도가 너무 느림.
        - mini batch 방법으로 해소.
            - 일부에 대해서만 학습.
            - mini batch size를 작게 잡으면 stochastic이 되고, 크면 batch의 문제점이 발생.
    2. stochastic(확률적) gradient descent
        - 훈련데이터 한개마다 가설 변경
        - `w0 <- w0 + a( y-h(x) )`
        - 하나하나에 맞추려다보니 전체데이터를 맞추기 어려움.
        - 그러나 학습의 변화가 빠름. 좋은방향인지는 모르나(수렴성 미보장) 즉각적인 변화를 볼 수 있음.
    - 전체 데이터를 1번 돌 때를 epoch(에포크)라고 한다.
    - 현실적으로 batch방법을 사용하긴 하지만 두 방법 모두 사용하지 않음.
        - mini batch 사용

:12주차  
- Linear Classification (선형 분류) with a hard threshold
    - Decision boundary(결정 경계)
        - class를 구분하는 구분선을 찾음.
    - Linear decision boundary (선형 결정 경계)
        - 직선 하나로(선형적으로) 분리 가능한 경우.
        - 쉬운 문제에 해당함.
        - 세상 문제에 선형적인 것은 많지 않음.
    - threshold : 임계값. h의 결과값을 이용하여 class를 분류.
        - hard threshold
            - 값의 차이에 관계 없이 임계 초과/미만에 따라 분류.
            - 미분이 불가능하다.
        - perceptron learning rule (퍼셉트론 학습 규칙)
            - `wi <- wi + a( y-h(x) ) * xi`

- Training Error Curve (in case of using a hard threshold)
    - 고정된 learning rate를 사용했을 때, loss가 들쭉날쭉함.
    - learning rate(alpha 변수)
        - weight(가중치) 변화 폭을 결정.
    - 가변 learning rate를 사용할 경우 loss 그래프가 비교적 안정적임을 알 수 있다.

- Logistic Function (=Sigmoid Function)
    - threshold의 단점
        - 임계점과 값의 차이는 고려되지 않고, 임계 초과/미만에 따라 분류.
        - 미분이 불가능하다.
        - 결과가 임계에 따라 확 바뀌다보니 loss도 계속 크게 변함.
    - logistic function
        - 임계에 대해 보다 유연한 함수를 사용하고자 함.
        - 0과 1로 구분하는건 당연한거고, threshold가 문제가 있다는건 아니지만 계산에 용이하게 하기 위해 부드러운 손실함수를 사용하고자 함.
        - 미분 가능함.
        - 단순히 0과 1만 있는게 아니라 중간값도 있다. 하지만 결과는 0과 1로 분류됨.
        - `Logistic(z) = 1/( 1+e^(-z) )`
        - logistic function을 사용하게 되면 미분 방식이 달라지기 때문에 가중치 변경 식도 달라진다.
            - chain learning rule(체인 학습 규칙)
                - `wi <- wi + a( y-h(x) ) * h(x)(1-h(x))*xi`
                
- Training Error Curve (in case of using a logistic function)
    - hard threshold를 사용할 때 보다 loss function의 진동이 훨씬 줄게됨.
    - learning rate가 동적일 때는 효과 극대화

- Artificial Neural Networks (인공 신경망)
    - Neural network structures
    - Single-layer feed-forward networks
    - Multilayer feed-forward networks

- Neural network structures (신경망 구조)
    - neural networks
        - 뉴런이라고 하는 units들이 links에 의해 연결되어있는 구조.
    - unit
        - input function(입력함수)
        - activation function(활성함수)
            - threshold unit (perceptron: 퍼셉트론)
            - sigmoid unit
    - link
        - input link, output link로 구성.
        - activation. 즉, 활성값이 input으로 들어오며, weight(가중치)에 따라 신호의 세기가 변화한다.
    - network structure (네트워크 구조)
        - FFN(Feed Forward Network: 순방향 신경망)
            - 구조가 층별로 이루어져있으며, 신호가 전방향으로 단계별로 나아감.
            - 구조
                - input layer
                - hidden layer
                    - 중간에 껴있는 layer. 겉으로 보이지 않으므로 hidden layer라고 불린다.
                - output layer
        - RNN(Recurrent Neural Network: 순환 신경망)
            - 신호가 전방향으로만 가는게 아니라, 옆이나 뒤로 가기도 하고 반복되기도 함.
            - FFN처럼 입력에 대해서만 진행하는것이 아니라, 모델 내에 기억하고 있는 정보와 함께 처리한다.

- single-layer feed-forward NNs
    - perceptron network (퍼셉트론 망, 단일 계층 신경망)
        - xor 문제 해결이 어려움
    - learning rules(학습 규칙, 가중치 갱신 규칙)
        - perceptron learning rule (for threshold units)
        - gradient descent rule (for sigmoid units)

- multilayer feed-forward NNs
    - single-layer(단층) 모델 단점
        - 데이터가 직선으로 나타낼 수 `없는 경우 single-layer(단층) 모델로 해결하기 어려움.
        - 선형 분리가 가능한 샘플이라고 하더라도 3차원에서의 구분은 더이상 선이 아닌 평면임.
        - 2차원에서도 샘플이 선형 분리`가 불가능하다면 직선이 아닌 곡선으로 표현해야함.
    - 뉴런의 개수가 증가하고, multi-layer로 구조가 변경되면서 역전파라는 방법을 통해 뉴런을 학습시킨다.
        - 결국엔 lost value를 줄이는 방향으로 변화한다는 기반은 같음.

- backpropagation algorithm(역-전파 알고리즘)
    - multi-layer 모델에서 layer를 학습시키기 위한 알고리즘.
    - 최종적으로 발생한 loss 값에 대해서 이전 layer에게 가중치에 맞게 계산하여 분배.

:13주차
- Nonparametric Models (비-모수 모델)
    - parametric 이란, 학습 과정동안 파라미터값을 알아내는 과정임. 학습시간이 정말 오래걸리지만, 실제 처리는 비교적 빠름.
    - nonparametric는 가설함수가 존재하지 않음. 학습이라는 것이 거의 없기 때문에, 실제 실행 시 바빠진다. 
    - instance-based learning (개체-기반 학습)
    - k-nearest neighbors (k-NN) models
        - 가장 가까운 이웃 k개 인스턴스(입력 데이터)의 유사도.
        - 과거의 examples들과 유사한지 비교.
    - k-NN classification
        - 주변 k개의 데이터들의 class를 살펴보고 다수의 class로 결정
        - k가 커질수록 하나를 결정할 때 여러개를 검사해야하므로 시간이 오래걸린다.
        - 이를 보완하기 위해 하이브리드형 구조도 나옴.
        - 신경망으로는 복잡한 경계선을 얻기 어려움.
        - 작은 수의 데이터가 복잡한 관계로 이루어져있으면 k-NN이 유용할 수 있음.
    - k-NN regression
        - average 방식 : k개 평균. 주변 노드가 동일한 기여도(weight)를 가짐
        - linear regression 방식 : k개 노드와의 오차를 최소화.
    - Locally weighted regression(지역 가중 회귀)
        - 가까울수록 가중치를 높이고, 멀수록 가중치를 낮춤.
        - 가중치를 어떻게 구하는가? -> Kernel function (커널함수)
            - K(Distance(x_example, x_test))
            - weight를 거리에 반비례하도록 만들어주는 함수.
            - 직접 구현할수도 있음.

- Reinforcement Learning
    - agent와 environmetn와의 상호작용. state -> action -> reward.
    - state에 대해 어떻게 action을 할지는 policy를 따른다.
        - 상태마다 적절한 행동이 구조적으로 확립시킨 시퀀스와는 다르다.
        - policy는 비결정성이 높은 환경. 어떤 환경이 올지는 모르겠지만 policy에 따라 행동.

- Markov Decision Process (MDP)
    - 학습과정이 따로 있는게 아니라 처음부터 최선을 다해서 action한다.
    - 한번에 끝나는게 아니라, 과거가 현재에 영향을 미치고 현재가 미래에 영향을 미치는 환경에서의 결정을 [순차 의사 결정]이라고 한다.
    - 순차 의사 결정 단계를 줄이는 것.
    - MDP는 튜플이다. <S, A, P, R, y>
        - State
        - Actions
        - 동일한 행동에도 다른 state로 전이되는 경우 확률(Probability matrix)적인 판단을 하게됨.
        - Reward Function

- Value Functions
    - 가치함수
    - 종류
        - state-Value function
        - optimal state-Value function
        - action-value function, Q function
        - optimal Q function

    - V는 state에 대한 가치평가(state value function)
    - Q는 action에 대한 가치평가(action value function)

- Bellman Equation
    - Q Learning을 하기위한 핵심. 신경망의 뉴런 급.
    - V와 Q의 관계를 통해 Q'에 의해 Q를 구하고, V'에 의해 V를 구할 수 있게됨.
    - 벨만공식 : Q(s,a) <- Reward(s,a) + gamma * maxQ(s', a')
        - 중요한 것은 action 이후, 각 행동의 Q값 중 가장 큰 값을 연산하여 이전 state에 대한 Q 갱신에 사용한다는 점이다.
        - action 이후의 max Q값이 작으면 해당 행동의 Q값은 낮아진다.
    - 3가지 상태, 2가지 가능한 행동. 그러면 총 6개. 이 6개에 대해 Q값들이 모두 있어야 하며, 이 값들이 제대로 평가되어야 한다. 이를 잘 판단하는 가치함수(Q)가 필요함. Q를 계속 개선시켜나가면서 더이상 개선되지 않고 수렴한다면 적절하게 얻었다고 생각할 수 있다.
    - 잘 학습된 Q값들을 가지고 있다면 그것을 policy로 하여 진행할 수 있다.
    - 강화학습의 궁극적인 목표는 이러한 optimal(최적)한 policy를 구하는 것이다.
    - 그래서 Q learning은 Value-based RL (가치 기반 강화학습)의 대표적인 예라고 할 수 있다.
    
:14주차
- Q Tables
    - 각 state, action에 대한 Q값을 저장해야하는데 그 때 사용하는 방법이 table형태. 2차원 배열이라고 생각하면 될듯.
    - q table의 크기 = state 개수 * action 개수

- Q learning algorithm
    - 방법
        - q table 기억공간을 잡아놓고, 0으로 초기화한다.
        - 최초 state를 설정.
        - 아래 반복
            - 행동을 하나 선택해서 수행(행동 선택 전략에 의해 결정)
            - 행동에 대한 reward를 받음
            - 다음 상태로 넘어감. (s')
            - 벨만공식에 의해 s 상태에 대한 Q 업데이트
            - 다음 상태를 현재상태로 둠.
    - 초기가 0이기 때문에 처음에는 reward에 의해 q가 정해짐.
    
    - 행동 선택 전략
        - exploitation
            - 모험을 하지 않음.
            - 큰 값의 Q만 탐색.
            - 탐색이 끝났다면, 이미 q값이 계산된 상태로 어느 길이 좋은지 알고 있으면 굳이 모험하지 않고 exploitation 방식의 행동 선택을 하게 됨.
        - exploration
            - 확률 기반 선택 방법
            - 확률만큼 랜덤하게 선택
            - 학습 초기에는 보상이 낮을 수도 있는 exploration 많이하게됨.

- Convergence of Q Learning
    - 수렴조건
        - MDP(Markov Decision Process)을 만족해야함. 상태전이나 보상이 직전상태에서 무슨 행동을 했는가에 따라 변함.
        - 보상을 줄 때, 아주 크거나 작으면 안된다. 작은 특정 범위 내에서 주어야한다.
        - q learning을 하게되면 q table의 모든 것이 수렴되어야 하는데, 그러기 위해서는 같은 경험을 여러번 반복하면서 q가 수렴될때까지 진행해야하는데, 그 반복 과정이 무한할 수 있음.
            - 일반적인 경우 status는 200개는 거뜬히 넘는 경우가 많다.
            - action도 일반적으로 단순하진 않다.
            - 결국 실제 문제에 적용하게되면 q table이 엄청 커진다.
            - 수많은 table상의 cell을 수없이 돌아다니면서 모든 cell이 수렴될때까지 시간이 오래걸린다.

- Value Function Approximation
    - Table 형태의 Q learning(Tabulur Q Learning)의 한계.
        - 상태공간(state space) 혹은 행동공간(action space)이 큰 경우.
        - 큰 메모리공간, 수많은 경험을 위한 탐색, 긴 학습시간.
        - Convergence 문제 발생.
        
        - 특히 현실문제에 적용할 때, infinite state space / infinite action space 의 경우 문제가 더욱 심각해짐.

    - 그에 대한 대안으로 NEURAL NETWORK를 사용
        - value function을 Q table 대신 신경망으로 대체한다. -> 무슨 의미?
            - 신경망을 supervised learning 형태로 사용하는게 아님.
            - status와 action이 들어가면 q값이 얼마가 나올지 예측하게 됨.
            - 이렇게되면 경험하지 못한 부분에 대해서도 q를 예측할 수 있음.
            - 즉, 일반화(generalization) 능력이 뛰어남.
            - 게다가 메모리를 얼마 차지하지도 않음.
            - NN(state, action) = Q
        - 구글에서 q learning에 신경망을 성공적으로 접목함.
            - DQN : Q-Neural Network Learning
            - Deep Neural Network + Reinforcement Learning = Deep RL
            - DQN 구조
                - NN(s) = 각 행동에 대한 q값.

- Deep Q-Networks, DQN
    - 기본적으로 가치 기반으로 동작하는 심층 강화학습. (value-based Deep RL)
    - google deepmind에서 개발.
    - Q-Network 학습.
    - 여기서 의문점이 들 수 있음.
        - DQN은 input으로 state만 줌.
        - 그러나 NN을 학습시키기 위해서는 state를 줌과 동시에 결과가 맞는지 판단하려면 action에 대한 값을 제공해야함.
        - 그런데 action은 제공하지 않음.
        - 그러면 어떻게 학습시키지?
    - 위 의문점에 대한 답.
        - DQN에서는 여전히 학습을 위한 목적함수로 손실함수(loss function)를 사용한다.
        - loss는 [실제값 - 예측값]의 형태다.
        - 실제 값 부분이 문제인데, 이것은 벨만 공식을 이용한다.
    - 구글이 DQN을 성공으로 이끈 요소는 따로있음.
        - 이 요소가 없었다면 성공하지 못했을 것.
            - loss를 구현할 때, 실제값이 계속 바뀌다보니 실제로 잘 수렴이 되지 않음. => 제대로 학습이 되지 않음.
        - 다음 두 개가 그것에 해당
            - Experience Replay Buffer/Memory (경험 재현 메모리)
            - Fixed Q-targets

    - Experience Replay Buffer/Memory (경험 재현 메모리)
        - 학습이 잘 되지 않은 문제점이 경험의 순차성이라고 판단.
            - 즉, 연속된 경험 데이터 간의 과도한 상호 관계성(의존성)이 문제.
            - 수렴을 방해하는 요인이 됨.
            - 즉, 내가 경험하지 못한 것에 대한 예측을 잘 못함.
        - q learning 특성상 경험은 순차적으로밖에 할 수 없음. 이건 건들수 없음. 그러나 학습을 할 때 순서를 바꿀 수 있지 않을까? 라는 아이디어.
        - 경험 데이터를 바로 학습에 쓰지 않고 버퍼에 저장. 버퍼가 찰때까지 그냥 저장
        - 버퍼가 차고 나서부터는 번갈아가면서 버퍼에 넣고 빼고를 진행함.
            - 경험을 하면 그 데이터는 버퍼에 넣고
            - 버퍼가 차면 랜덤하게 하나 선택해서 그걸로 학습함.
        - 더 나아가서는 버퍼에서 한개를 넣고, 뺄때는 한개만 뽑는게 아니라 하나보다 많은 mini batch 개수 만큼 랜덤하게 뽑아서 학습.
        
        - 장점
            - 학습에 쓰이는 데이터가 경험한 순서대로 학습하는게 아니라 그것과는 무관하게 학습. 즉, 상호 관계성을 배제
            - 동일 경험을 q 갱신에 여러번 재사용.
        
    - Fixed Q-target
        - loss 함수를 구성할 때, 실제 값을 계산하는 함수도 결국엔 예측 NN을 이용하게 된다. 갱신이 동시에 되는 격. 이 부분이 문제라고 판단.
            - 안정적인 손실 축소와 Q 네트워크의 학습이 어려움
        - Q 네트워크를 2개로 분리해서 해결.
            - target network (예측 Q NN)
                - 예측값 산출
            - local network (타켓 Q NN)
                - 실제값 산출

            - target 갱신 주기를 predict 보다 느리게 설정.
                - DQN의 경우 predict : 4회 업데이트, target : 1회 업데이트

- policy gradient
    - policy-based RL
        - 그동안 공부한 value-based RL과 관점을 달리함.
        - state를 주면 action을 반환하는 policy network를 구성.
        - 큰 상태/행동 공간 문제에 적용 가능
        - 상대적으로 데이터 효율성은 낮음
            - 학습데이터가 진짜 많이 필요함.
            - 학습 시간도 오래걸림.
        - 학습에 사용되는 object function이 loss가 아님.
            - 초기상태부터 지금까지의 행동을 했을 때의 reward 합.
            - 최대화하는 방향 == object function의 기울기(미분값)가 증가하는 방향 !!!!!!!
    - 알고리즘
        - REINFORCE (기본형. 성능이 좋지는 않음.)
        - Actor-Critic(AC),
          Advantage Actor-Critic(A2C),
          Asynchronous Advantage Actor-Critic(A3C)
        - TRPO, PPO (현재로써 성능이 좋음.)


- Unsupervised Clustering
    - supervised는 classification, regression같은 경우에 많이 쓰인다.
    - unsupervised는 군집화(clustering)에 많이 쓰임
    - 크게 두가지로 분류
        - partitioning algorithms(분할 알고리즘)
            - 주어진 데이터를 특정 성격에 맞게 분할하는 알고리즘.
            - 처음에 랜덤하게 파티션을 나누었다가, 조금씩 맞춰가는 방식.
            - 알고리즘
                - k-means (k 평균)
        - Hierarchical algorithms(계층적 알고리즘)
            - tree 모양으로 군집화를 점차 변형
            - 알고리즘
                - top-down
                    - 전체를 하나의 클러스터로 보고, 점점 쪼개는 방식
                - bottom-up
                    - 여러`개의 클러스터로 보고, 점점 합쳐나가는 방식

- K-Means Clustering
    - "k-평균 군집화"
    - 몇개의 클러스터로 분리할지 k를 처음에 사람이 제공.
    - k개의 군집을 임의로 만들기 위해 군집의 중심점 k개를 랜덤하게 설정
    - 훈련데이터 각각은 k개의 중심점과의 거리를 계산하여 어떠한 군집에 속할지 선택. (= 군집의 멤버가 확보가 되는 과정)
    - 아까 임의로 잡았던 중심점을 변경. 군집 내 데이터(data point cloud)들을 기반(평균)으로 이동. 이를 반복함.
    - 중심점이 수렴되어 변하지 않으면 안정화 되었다고 볼 수 있다. 클러스터가 확립된 상태.

    - 그러나 출발점에 따라 군집화가 적절하게 나뉘지 않을 수도 있다.

    - 문제점
        - 군집 개수 결정 문제
            - 처음에 사람이 k개의 군집 개수를 지정해 주어야 하는데, 이게 어려움.
        - 초기 군집 중심 선택 문제 (seed choice)
            - 출발점에 따라 군집화가 적절하게 나뉘지 않을 수도 있다.
            - 할때마다 틀려서 optimal하다고 말하기도 애매
        - 이상치 문제(outliers)
            - 소수의 데이터가 일반적인 데이터와는 달리 어떠한 속성값이 매우 크거나 작은 경우. 일반적으로 튀는 데이터는 대부분 에러다. 이렇듯 데이터가 튀는 성향을 가질 경우, 군집에 영향을 줄 수도 있기 때문에 애초에 그런 데이터를 제외하고 진행하는게 나을 수도 있다. 그러나 사람이 직접 해야하는 부분이라서 어려움이 있다.
    
- Hierarchical algorithms(계층적 알고리즘)
    - Top-down
        - 큰 군집을 점차 나누는 형태
        - 군집 내에 유사성이 크게 떨어지는 군집으로 분할
    - Bottom-up
        - 작은 여러 군집을 합치는 형태
        - 유사도가 높은 군집을 병합

:15주차

- Deep Learning / Deep Neural Network 개념
    - Shallow Learning VS Deep Learning
        - Shallow Learning
            - 대부분 raw 데이터를 그대로 가지고 신경망에 넣는 경우는 거의 없음.
            -  대부분 신경망을 돌리기 전에 RAW한 데이터를 feature 데이터로 변환하는 전처리가 있음.
                - 유명한 feature 추출법
                    - SIFT
                    - HOG
            - 원래 사이즈보다는 작고, 정보량은 많은 그런 전처리가 좋음.
            - 사실상 전처리가 끝나고 맨 끝 분류기(classifier)에서만 ML이 사용됨. 층도 많을 필요 없음. 아주 얕아서 Shallow 이름이 붙어진듯.
        - Deep Learning
            - 그동안은 feature를 추출하는 부분은 인간의 지식에 의해 규정되었었다. (shallow)
            - 그러나 오늘날에 와서는 feature 추출부분까지 신경망이 사용됨.
            - NN Block들이 계속 연결되어있음. 최종적으로 classifier의 input으로 작용.
            - feature : CNN -> Classifier : FC(Fully connected)/MLP 형태
            - End to End Training. 이제 전처리 없이 raw 데이터를 주면 알아서 feature 추출부터 classifier까지 진행됨.
            - 하지만 구조가 엄청 복잡해졌기 때문에 데이터셋은 훨씬 더 많이 필요하다.

    - Deep Neural Networks / Deep Learning
        - 최근에 들어서 성공한 이유
            - 큰 학습데이터 생성이 가능. 수많은 서비스를 운영하면서 생긴 데이터들. (포털사이트, Wiki, 스트리밍 사이트 등)
            - 병렬처리해야하는 연산이 많아졌는데, 병렬 연산 전용인 GPU가 성능이 많이 좋아졌음.
            - 간단해진 활성함수(뉴런의 끝에 있는 함수) 알고리즘(ReLU)
            - 일부 노드만 갱신하는 dropout 기술의 등장
            - 데이터의 편차가 심해지면 학습에 도움이 안되기 때문에 이를 중간중간 데이터를 정규화해주는 normalization 기술의 등장

            - 결국 위와 같은 것들 덕분에 깊은 layer의 학습도 잘 됨. 정리하면 다음 3가지 요인이라고 볼 수 있음
                - 충분한 학습 데이터
                - 인프라와 컴퓨팅파워
                - ML 알고리즘


- DNN의 구성 요소와 종류
    - Convolution, Pooling, Normalization, FC
    - Convolutional Neural Netowrks(CNN)
    - Long Short-Term Memory(LSTM)
    - Gated Recurrent Unit(GRU)

- Convolutional Networks(CNN)
    - feature를 자동으로 뽑을 수 있게 됨.
    - 위 이유로 raw데이터만 넣어도 사용할 수 있는 end to end 학습이 가능.
    - feed-forward network
        - 한방향으로만 데이터가 전달되는 방식.
        - raw 이미지가 들어가서 feature을 추출하기까지의 과정은 다음과 같다.
            1. input image
            2. convolution layer
            3. Non-linearity
                - 활성함수 층. 비 선형성으로 변환.
            4. Pooling
            5. Normalization
            6. feature maps
    - Convolution
        - Line filtering
            - 가중치 격자(kernel)가 하나 있고, image pixel에 대해서 연산을 진행함. 격자(kernel) 크기만큼의 pixel들을 한개의 대표값으로 계산하는 원리. 있어보이는 말로 지역의 특성값 이라고 함.
            - 결과 image는 대표값으로 이루어져있음.(크기가 작아짐)
            - 만약 결과 크기가 같도록 하고싶다면 겉 matrix를 0으로 padding하면 같은 크기를 얻을 수 있음.
    - ReLU Nonlinearity
        - sigmoid는 학습을 위해 미분할 때, 계산이 복잡함.
        - 0보다 작으면 0, 0보다 크면 점차 증가하는 그래프
        - 미분하면 0보다 큰 영역은 1로 보면 됨. 간단해서 학습이 잘됨.
    - Pooling
        - 쓸때도 있고, 안쓸때도 있음.
        - 원래 데이터로부터 뽑아낸(convolution) 지역적 특성 데이터가 최종 판단할 때, 지역적 특성이 너무 예민하게 작용하면 문제가 발생.
        - 예를 들면 사람얼굴을 인식할 때, 사람인지 아닌지 탐지하는것도 중요하지만 고개를 약간 기울였을 때도 사람을 인식해야 함. 이렇게 일반적인 데이터와 다르지만 동일하게 인식해야 하는 경우 지역적 특성에 너무 의존하게되면 인식을 못하게 된다고 생각하면 됨.
        - 그럼 어떻게 지역적 특성을 없애지? -> 지역을 두루뭉실하게 pixel 범위를 잡아서 하나의 값으로 평가하면 됨.
            - max pooling : kernel 내 point 최대값
            - average pooling : kernel 내 point 평균값

- Recurrent Neural Networks(RNN : 순환신경망)
    - 데이터가 순서가 있는. 즉, 시계열/순차적 데이터를 처리할 때 좋음.
    - CNN에서 사용했던 feed forward 방식은 앞으로만 진행됨. 순환신경망은 이런 방식이 아님. 정보가 다시 이전 layer로 돌아갈 수도 있음.
    - 노드가 데이터를 처리할 때, 이전 데이터를 인자로 받음. (점화식같은건가)
    - 이전 데이터가 계속 다음 연산에 사용되기 때문에 데이터를 "기억"하는 성격이 있다고 볼 수 있다.
    - RNN state의 update와 output
        - input : x_t
        - update hidden state
            - h_t = tanh(Weights_hh * 직전h_t + Weights_xh * x_t)
            - Weights는 training을 통해 변경
        - output vector
            - y_hat = Weight_hy * h_t

    - 사용가능 분야 (feat 노드 연결 구조)
        - one to one
            - feed forward 방식. 앞으로만 전진.
            - CNN이 이 구조를 사용.
        - one to many
            - 입력은 하나가 들어오는데, 이것으로 여러개의 출력을 냄. 
            - 예 : image captioning(이미지의 상황을 문장으로 설명)
        - many to one
            - 여러개가 들어오면, 최종적으로 한개를 출력.
            - 예 : Document/Video Classification
        - many to many
            - 여러개 들어오고, 여러개 나감.
            - 구조에 따라서 시간차를 어떻게 줄 것인지 변경할 수 있음.
            - 예 : Language Translation, Autonomos Driving
        - Natural Language processing(NLP:자연어처리)
        - Speech Recognition
        - Video processing
    - 학습은 역전파(backpropagation) 방식을 이용해 진행.
        - 모든 반복을 거쳐서 결과를 도출해야지만 학습이 가능하다.
        - Loss가 도출되면 backward로 loss를 전파한다.
        - 여기서도 앞선 노드의 loss가 뒤쪽의 loss로 작용한다. RNN 성격상 학습에도 시간적으로 학습이 됨.
    - Long-term dependency problem
        - 지금까지 공부한 것이 순수한(단순한) RNN이다. (vanilla RNN)
        - 이렇게 단순한 RNN은 데이터간 시간차이가 큰 경우(long-term)에 고려하기가 어렵다는 단점이 있다. 즉, 시간적으로 멀리 떨어져있는 데이터의 연관성을 고려하지 못하기 때문에 이런 데이터 시간격차를 고려해야하는 문제에서는 사용하기에 적합하지 않음.
        - 이러한 문제를 해결하기 위해 나타난게 LSTM모델이다.

- Long Short-Term Memory (LSTM)
    - 시간적으로 멀리 떨어져있는 신호도 갈수록 죽지 않고 잘 전달될 수 있도록 개선된 RNN모델.
    - 가장 많이 사용되는 모델.
    - 비유하자면 스위치 같은 역할들이 있는데 이러한 파라미터들이 복잡하게 구성되어있어서 오래된 신호도 잘 살려서 진행이 됨. 결국 예측이 잘됨.
    - 그러나 구조가 너무 복잡해서(파라미터 수가 너무 많아서) 학습의 문제가 있음.

- Gated Recurrent Unit (GRU)
    - LSTM 구조의 복잡성으로인해 학습이 잘 되지 않는다는 단점을 보완하기 위해 구조상 존재했던 스위치(파라미터) 개수를 2개로 확 줄임.
    - 물론 예측 능력에 있어서는 LSTM에 훨씬 좋음.
    - 대신 학습이 비교적 잘됨. 빠름.
    - 순전히 정확도만을 따진다면 LSTM을 사용하는게 맞음.

- ImageNet ILSVRC : image clasification
    - ImageNet이라는 표준화된 데이터를 가지고 모델 성능 대결.
    - 꽤 오래된 대회.
    - 인간은 5퍼센트의 에러율을 보임.
    - 2011년까지는 25.8%의 에러율. 
    - 2012년부터 DNN을 사용했고, 그때부터 error율이 확 줄어들었음.
        - 시작은 AlexNet 16.4% 에러율
        - 가장 마지막인 구글에서 만든 GoogleNet(22 layers) 6.7% 에러율
    - 2015년 Resnet이 3.5% 에러율로, 사람을 뛰어넘음.
    
    - AlexNet(2012)
        - Convolution layer를 5개나 주고, FC layer 3개 해서 총합 8 layer사용.
        - 각 layer가 어떤 결과를 내주는지 궁금해서 visualization 기술들이 개발됨.
        - 실제로 보니까 feature가 점점 고수준으로 발전해 나가는 것을 확인할 수 있음
            - pixel -> 재질 -> 형체 -> ...
    
    - ResNet(2015)
        - 152 layer 사용. ㄷㄷ
            - 대부분 layer가 feature 추출에 사용됨.

    - 잘 동작하는 모델을 구성하기 위해서는 CNN이 좋다!, RNN이 좋다! 이런건 없음. 인공지능이 해결해야하는 환경에 맞춰서 적절한 모델을 결합해서 어떤 부분은 CNN을 쓰고, 시간적 요소가 고려해야하는 부분에서는 RNN을, classification이 중요한 부분은 FC를 이용한다든지 이런식으로 분할하여 결합하고, 더욱 복잡하게 할수록 더 재밌고 좋은 모델이 나올 수 있음.
        - 예를 들면 강아지가 뛰는 영상이 있다고 치면, 이미지로부터 feature를 추출하기 위해 아주 깊은 CNN 구조를 사용. 이미지가 어떤 상황인지 문장으로 추출하기 위해서 추출된 feature를 input으로 하는 여러 LSTM layer로 구성하여 "강아지가 뛰고있다"라는 문장을 도출해낼 수 있음. (Google15)
