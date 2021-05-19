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
                - goadl states
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

(12주차)  
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

- 

