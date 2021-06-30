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

