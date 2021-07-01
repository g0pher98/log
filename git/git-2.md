# git2
branch

## 브랜치 기본
``` bash
git branch <BRANCH_NAME> # 브랜치 생성
git checkout <BRANCH_NAME> # 브랜치 이동
git branch # 브랜치 리스트 보기
git branch -d <BRANCH_NAME> # 브랜치 삭제
git branch -b <BRANCH_NAME> # 브랜치 생성 후 이동 

```

## 브랜치 병합
``` bash
git merge <BRANCH_NAME_FOR_MERGE> # 현재 브랜치에 다른 브랜치의 변경사항을 합침
# 충돌(conflict) 시 충돌난 부분만 수정해서 그냥 add 후 commit 하면 됨.
git merge --abort # merge를 취소하는 명령. 
```

# push
``` bash
git remote add origin https://github.com/g0pher98/g0pher98
```
`origin` 을 사용하는 이유는 해당 원격 레포의 별칭을 달아주는 것이다. 위와 같이 설정하면 앞으로 origin으로 해당 원격 레포를 가리킬 수 있다.

```
git push -u origin master
```
`-u(--set-upstream)`의 경우 앞으로 기본적으로 적용할 branch를 설정한다고 생각하면 된다. 이후로는 `git push` 만으로도 설정된 레포로 적용이 된다.
```
git push origin master:master
```
로컬의 특정 브랜치를 리모트의 특정 브랜치로 push 할 때는 위와 같이사용하면 된다. 콜론(:) 기준으로 좌측이 로컬, 우측이 리모트.

# Detached HEAD
일반적으로 HEAD는 직접적으로 commit을 가리키지 않는다. 커밋을 가리키는 브랜치들이 있고, HEAD는 사실 이러한 브랜치를 가리키는 것이다. 그러나 HEAD가 commit을 직접적으로 가리키도록 할 수도 있는데 다음과 같이 `checkout`을 사용하면 된다.
```
git checkout <COMMIT_HASH>
```
이처럼 HEAD가 커밋을 직접적으로 가리키는 것을 `Detached HEAD`라고 한다. 브랜치로부터 떨어졌기 때문에 detached 라는 단어를 사용한다. `Detached HEAD`를 사용하는 이유가 몇가지 있는데 다