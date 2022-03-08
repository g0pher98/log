# git4
git 사용능력 높이기

## git reset을 해버린 상황. 다시 돌아가려면?
```
git history
```
위와 같이 git history를 통해 commit 리스트를 확인 한 후 다음과 같이 예전 commit으로 완전히 돌아가버리자.
```
git reset --hard <COMMIT_HASH>
```
이렇게 하면 `git history`를 사용해도 다시 원래의 commit을 알 수 없다. working directory까지 완전히 이전 commit 상태로 돌아와 버린다. 어떻게 다시 이전으로 되돌릴 수 있을까?

다행인 점은 `git reset --hard`를 한다고 해서 앞선 commit들이 사라지는 건 아니다. commit hash를 알고있다면 `git reset --hard`를 다시 해서 앞으로 돌아갈 수 있다. 앞서 `git history`로 출력해놓은 커밋들이 있기 때문에 다시 원래대로 돌아갈 수 있다.

그러나 지금처럼 history를 출력해놓지 않아서 앞선 commit hash를 알 수 없는 상황이라면 어떻게 해야할까?

reflog 명령을 사용할 수 있다. reference log의 줄임말로, 헤드가 이때까지 가리켜왔던 커밋들을 기록해놓은 것을 볼 수 있다. 
```
git reflog
```
위 명령을 통해 최신 commit hash를 몰라도 찾아낼 수 있다.

## 커밋 히스토리를 보는 다양한 방법
git log
`--pretty=oneline` : 한 줄로 예쁘게 출력
`--all` : 모든 브랜치의 커밋 내용을 볼 수 있음. 그러나 브랜치 구별이 어려움.
`--graph` : 브랜치와의 관계가 잘 드러나도록 출력


## git GUI 툴
- Sourcetree

GUI 툴은 CLI에 비해 가독성도 높고 편리하지만, CLI를 쓸줄 아는 상태에서 사용하는 것이 좋다!


## 깔끔한 커밋 히스토리를 원할 땐, merge 대신 rebase
merge를 하게되면 merge 과정이 기록된 새로운 commit이 추가된다. 그러나 이러한 커밋들이 복잡하고 불필요하다고 생각된다면 더욱 깔끔하게 두 브랜치를 합칠 수도 있는데, rebase를 통해 가능하다.
```
git rebase --continue
```
위와 같이 충돌이 일어난 rebase를 계속 진행하도록 명령을 입력할 수 있다. merge로 한다면 이 과정이 commit으로 추가되지만, rebase를 할 경우 합치려는 branch를 애초에 거친 것과 같은 효과를 낸다. 즉, branch를 합친것이 아니라 애초에 commit을 통해 거쳐온 것과 같은 형태를 띈다.

merge와의 차이점은 분명한데, rebase는 두 브랜치를 합칠 때 새로운 커밋을 만들지 않고, 그렇기 때문에 commit history를 깔끔하게 관리할 수 있다.

실제로는 두 브랜치가 합쳐졌다는 내용이 필요한 경우 merge를 통해서 합치면 되고, 브랜치 병합 정보 필요 없이 commit이 깔끔하길 원한다면 rebase를 사용하면 된다.

## 작업 내용 임시 저장하기
working directory가 commit 되지 않은 상태에서 브랜치를 변경하거나 변동이 발생할 경우 working directory 내 데이터가 사라질 수 있기 때문에 경고가 뜨는데, 이런 경우 작업 내용을 임시로 저장할 수 있다.
```
git stash
```
stash는 안전한 곳에 보관한다는 뜻을 가지고 있는데, 이 명령을 통해서 스택구조의 저장공간에 작업 내용을 저장할 수 있다. 저장되면 working directory는 초기상태로 돌아간다. 저장된 작업들은 다음과 같이 확인할 수 있다.
```
git stash list
```
저장된 작업 내용을 불러올 때는 다음과 같이 사용할 수 있다.
```
git stash apply <STASH_HASH or STASH_ID:생략시 최근>
```
`stash` 명령은 이 외에도 잘못된 브랜치에서 작업하고 있는 경우에도 자주 사용된다. 잘못된 브랜치에서 `stash`로 저장 후, 원래 작업해야하는 브랜치로 `checkout` 후 불러오는 방식으로 사용 가능하다.

`apply`로 작업한 내용은, stash list에서 삭제할 필요가 있다. 다음과 같이 삭제가 가능하다.
```
git stash drop <STASH_HASH or STASH_ID:생략시 최근>
```
적용과 동시에 삭제도 해주는 명령도 존재한다.
```
git stash pop <STASH_HASH or STASH_ID:생략시 최근>
```
저장한 작업을 다시 사용할 필요가 있다면 `apply`, 다시는 사용하지 않을 예정이라면 `pop`을 사용하면 된다.


## 필요한 커밋만 가져오는 방법
다른 브랜치에서 작업한 내용을 merge 하기보다 특정 커밋 내용만 필요한 경우도 있다. 이 경우 다음과 같이 특정 commit만 가져올 수 있다.
```
git cherry-pick <COMMIT_HASH>
```
cherry picker : 본인에게 유리한 것만 선택하는 사람
cherry pick : 좋은 것만 골라먹다

원하는 작업이 들어있는 커밋만 가져와서 현재 브랜치에 추가하는 명령.

## 여러 커밋을 하나의 커밋으로 만들기
짜잘한 수정사항이 여러번 commit 되면서 불필요한 커밋이 많아지는 경우도 있다. 이런 경우 하나로 합칠 필요가 있는데, `git reset`의 `--mixed`나 `--soft`와 같이 working directory에 반영되지 않는 방식을 통해 특정 commit으로 되돌린 후 한꺼번에 commit 하면 된다.
