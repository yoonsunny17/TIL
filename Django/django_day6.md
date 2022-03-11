## GIT Branch

> master branch

* 상용되는 branch

![image-20220311090939248](django_day6.assets/image-20220311090939248.png)

* 빨간 부분 = master branch
* 노란 부분 = master branch와 별개의 부분. 조작을 해도 master branch에 영향이 가지 않는다.



> 명령어

* `git branch` : 브랜치 목록 확인
* `git branch <branch_name>` : 새로운 브랜치 생성
* `git branch -d <branch_name>` : 특정 브랜치 삭제 (병합된 브랜치만 삭제)
* `git brach -D <branch_name>` : 강제 삭제

* `git log`
* `git log --oneline`
* `git log --oneline --all`
* `git log --oneline --all --graph`
* `git switch <branch_name>` : 다른 브랜치로 이동
* `git switch -c <branch_name>` : 브랜치를 새로 생성과 동시에 이동 (`git branch <branch_name>` 과정 필요 없음)

![image-20220311091955524](django_day6.assets/image-20220311091955524.png)

![image-20220311092044322](django_day6.assets/image-20220311092044322.png)

* master-3 라는 가장 최신 commit에서 login이라는 branch를 만든 것

![image-20220311092144338](django_day6.assets/image-20220311092144338.png)

* 이후 master-4를 새로 만들어주면, (HEAD -> master) 는 master-4 를 가리키고 있다
* login 브랜치는 여전히 master-3를 가리킴

![image-20220311092416455](django_day6.assets/image-20220311092416455.png)

* `git switch login`을 통해 현재 브랜치 위치를 바꿀 수 있음

![image-20220311092518524](django_day6.assets/image-20220311092518524.png)

* branch가 login으로 바뀌면서 test.txt 또한 자동으로 바뀐다!

![image-20220311092642783](django_day6.assets/image-20220311092642783.png)

![image-20220311093037915](django_day6.assets/image-20220311093037915.png)



* 삭제하고 싶은데 not fully merged 병합되지 않아서 에러난다~

![image-20220311093335509](django_day6.assets/image-20220311093335509.png)

* 병합 상관 없이 삭제하고 싶은 경우: `git brach -D <branch_name>`

*********

## merge (병합)

* `git merge <병합할 브랜치 이름>`
  * merge 하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야 함