# Topic 1
git이란? 버전관리 프로그램.

## 버전관리란?
파일의 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템.

## 버전관리의 장점
1. 최종버전까지 거친 과정을 볼 수 있음.
2. 실수할 경우 과거로 돌아갈 수 있음.

## 역사
초기 리누스 토발즈가 리눅스를 버전관리하기위해 BitKeeper라는 툴을 사용함. 그러나 리눅스 커뮤니티 개발자 한명이 동작 원리를 분석하고자 했다가 bitkeeper와 사이가 멀어지면서 유료화가 됨. 결국 리누스 토발즈가 직접 만들었음. 이것이 깃(git)

### 초기 설계 목표
- 빠른 속도
- 단순한 디자인
- 비선형 개발 지원 (= 수천개의 브랜치를 병행할 수 있음.)
- 완전 분산형 시스템
- 리눅스처럼 거대한 프로젝트도 속도저하 문제 없이 관리할 수 있는 시스템

## git은 무엇의 약자?
정해져있지 않음. 리누스 토발즈가 git 수정사항에 적어놓은 내용을 보면 원하는대로 해석될 수 있다고 함.

## 기본

### repository
프로젝트를 담기 위한 디렉토리와 같은 공간을 `프로젝트 디렉토리`라고 할 때, 이러한 프로젝트 디렉토리의 변화를 기록할 수 있음. git이 이러한 기록을 하는 공간을 `repository`라고 함. 정확하게는 프로젝트의 변경사항이 저장되어있는 `.git` 폴더가 `repository`다.

### 3가지 작업영역 
1. working directory : 현재 작업중인 디렉토리
2. staging area : add를 한 파일들이 존재하는 영역
3. repository : commit 이력들이 저장되어있는 영역
    - local repository
    - remote repository

### add
``` git
git add <FILE_PATH_TO_ADD>
```
staging area에 추가.

### reset
```
git reset <FILE_PATH_TO_RESET>
```
staging area에서 제거. 즉, add 취소.
```
git reset --hard <COMMIT_HASH>
```
과거 커밋으로 돌아가고 싶을 때 사용할 수 있음. working directory가 바뀜.

### commit
``` bash
git commit -m "<COMMIT_MESSAGE>"
git commit --amend # 가장 최신 커밋에 반영
```
로컬 레포에 commit. 자세한 설명이 필요한 커밋의 경우는 `-m` 옵션을 사용하는것보다 없이 커밋해서 vim을이용해서 자세한 내용을 기록하는 것이 좋다. 커밋 메세지가 길어질 경우에는 프로젝트마다 규칙이 존재하는데, [git에서 공식적으로 권장하는 사항](https://git-scm.com/docs/git-commit#_discussion)은 다음과 같다.
1. 커밋 메세지의 제목과 상세설명 사이에는 한 줄 비우기
    ```
    Add g0pher's function

    this commit is ...
    ```
2. 커밋 메세지의 제목 뒤에 온점(.) 붙이지 않기
3. 커밋 메세지의 제목 첫 번째 알파벳은 대문자로 작성하기
4. 커밋 메세지의 제목은 명령조로 작성.
    - Fix it (o)
    - Fixed it (x)
    - Fixes it (x)
5. 커밋의 상세 내용에는 아래와 같은 내용을 적기
    - 왜 커밋을 했는지
    - 어떤 문제가 있었고
    - 적용한 해결책이 어떤 효과를 가지는지
6. 다른 사람들이 코드를 이해한다고 가정하지 말고 최대한 친절하게 작성.

이 뿐만 아니라 커밋할 때 알아야 할 가이드라인도 존재한다. 내용은 아래와 같다.
1. 하나의 커밋에는 더도말고 하나의 수정 및 이슈를 해결한 내용만 남기기.
2. 전체 코드를 실행했을 때 에러가 발생하지 않는 상태인 경우에만 커밋.
    - 상황에 따라 과거 커밋을 실행해야할수도 있기 때문에 모든 커밋은 실행가능한 형태여야함.


### push
```
git push
```
로컬 레포를 원격 레포로 올림

### pull
```
git pull
```
원격 레포의 변경사항으로 로컬 레포를 업데이트

### log
``` bash
git log
git log --pretty=oneline # 커밋 당 한줄씩 출력하도록 하는 명령
```
커밋 내역들을 볼 수 있음. 각 커밋 해시들과 메세지를 확인할 수 있음.

### show
``` bash
git show <COMMIT_HASH>
```
특정 커밋에 대한 상세 내용을 보는 명령. 커밋 해시는 앞 4자리 정도만 쳐줘도 됨.

### alias
```
git config alias.history 'log --pretty=oneline'
```
긴 명령을 짧게 사용하기 위함. 위 예제는 `git log --pretty=online` 명령을 `git history`로 aliasing 하기 위한 코드.

### diff
```
git diff <COMMIT_HASH_1> <COMMIT_HASH_2>
```
두 커밋 사이의 변화 확인하는 명령.
