# Powershell과 명령 프롬프트의 차이점?

## 명령 프롬프트는 unix 언어 미지원

명령 프롬프트; **CLI (=COMMAND LINE INTERFACE)**

CLI와 상반되는 개념 **GUI(=GRAPHIC USER INTERFACE)**

### 간단한 Unix/Linux 명령어

* 현재 위치의 폴더, 파일 목록보기: ls
* 현재 위치 이동하기 cd<path>
  * **cd..** 상위 폴더로 이동

* 폴더 생성하기 mkdir<name>

* 파일 생성하기 touch<name>

* 삭제하기 

  * 파일을 삭제하는 경우: rm<name>

  * 폴더를 삭제하는 경우: rm -r<name>

    

### Git bash (unix/linux 언어 사용 가능)

**물결(~)** = user의 home directory



# Git 기본기

## Repository

특정 디렉토리를 버전 관리하는 **저장소**

* *git init* 명령어로 로컬 저장소를 생성
* *.git* 디렉토리에 모든 히스토리가 저장되어 있음

​	지금 상태를 **특정 버전**으로 남길 때, 그 특정 버젼을 **커밋(commit)**이라고 한다.



## 커밋(Commit)

3가지 영역을 바탕으로 동작

- working directory (racingground): 내가 작업하는 실제 디렉토리
- staging area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
- repository(.git 폴더): 커밋들이 저장되는 곳

working directory (untracked) -- **git add** \-- staging area(tracked(git):변경된 사항들이 모두 staging area로 올라감) -- **git commit** \-- repository(commit01,02,03 ...)

**git status** : 현재 git의 상태를 알 수 있음

**git add**

**git add .** : 파일이 너무 많을 때 *추적되지 않은 모든 파일*과 추척하고 있는 파일 중 *수정된 파일*을 모두 **Staging Area**에 올린다

**git commit -m "commit_message"** 커밋 메세지는 알아보기 쉽도록 자세하게 작성하기

* git config user.name"user_name"
* git config user.email"user_email"
* 완료 후
* git config --list (enter)
  * user.name과 user.email에 잘 들어가 있는지 확인해주면 됨
  * git config — global user.name  바꿀이름
    git config — global user.email 바꿀이메일

* git diff
* git log
* commit 아이디 엄청 복잡함 그거 굳이 다 칠 필요 없고 앞에 네자리만 쳐줘도 구분 가능

## github에서 code를 직접 수정할 경우는 거어어어어어어의 없을 것이다!

### git에서 코드 수정한 뒤 pull/push를 통해 github에 연동시킴

* git clone {remote_repo} : remote repo를 local로 복사
* git push origin master : local repo의 최신 commit을 remote repo로 push
  * 근데 아까 그냥 git push까지 입력하고 명령햇는데 가능했던 이유?
    * branch가 하나였기 때문에 상관이 없었던 것이다!

github repo와 loca repo 연동 시키는 작업!

- git remote add origin {remote_repo} :remote를 더해줄거야
- git push *-u* origin master
  * -u : remote add해준 경우 이후에 쓰는 옵션, local에 있는 master를 remote로 보내는 과정!

## TIL (Today I Learned) Project

* 매일 내가 배운 것을 md으로 정리해서 문서화 하는 것
* 신입 개발자에게 요구되는 가장 큰 능력 (꾸준히 학습)
* 장기 프로젝트! *1일 1커밋*  가쟈~

