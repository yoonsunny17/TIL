# 레포지토리

* 저장소: 커밋이 저장되는 곳

* git init: 로컬 레포지토리 생성
  * .git 폴더 생성: git이 관리하는 모든 정보들이 들어있는 곳(DONT TOUCH)
  * 

* git status:  현재 레포지토리에 git이 어떤 상태인지를 체크
* README.md: 내 레포지토리에 대한 설명서 같은 역할을 하는 파일
* touch<file name>: 폴더 생성
* git add
  * staging area로 올리는 역할
  * git에게 추적하는 파일임을 선언

* git commit -m "message"

* git commit (enter) : 빠져나오는 방법 esc 누른 뒤 :wq (enter)

* vi README.md (enter) --> i (enter):수정모드 --> 내용 작성 --> esc :wq (enter)



## Public vs Private

* Public: 누구나 볼 수 있고, 다운(clone) 받을 수 있음. 단, push는 나만 가능하다!
* Private: 나의 repo를 나만 볼 수 있고, 나만 push가 가능하다!

​	

# PUSH 전에는 PULL이 있다



## 같은 repository를 여러명이 사용하는 경우

* 동시에 pull을 하게 되는 경우: **conflict** 가 발생!!



### confilct 해결방법

1. "code ." 을 통해 vs를 연다
2. 필요없는 contents를 지운다.
3. 저장한다
4. git bash) git add, commit, push

