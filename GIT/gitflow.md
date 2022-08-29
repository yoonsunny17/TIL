## version control system

* version management, **not by changing the file name**
* CVS, SVN, **GIT**



## backup recovery collaboration



git은 매우매우매우매우 어렵다!

기능이 덮어지고 보태지면서 ... 매우 까다로워짐



### branch

![image-20220726113641579](gitflow.assets/image-20220726113641579.png)

![image-20220726113655479](gitflow.assets/image-20220726113655479.png)



`git log --branches --decorate`

![image-20220726113747549](gitflow.assets/image-20220726113747549.png)



`git log --branches --decorate --graph`

![image-20220726113830350](gitflow.assets/image-20220726113830350.png)

master branch와 exp branch의 공통 조상은 2이다 (지금 cursor에 가려져서 안보임)



`git log --branches --decorate --graph --oneline`

![image-20220726114005849](gitflow.assets/image-20220726114005849.png)



`git log master..exp`

![image-20220726125703246](gitflow.assets/image-20220726125703246.png)



`git diff master..exp`

![image-20220726125804283](gitflow.assets/image-20220726125804283.png)



## git flow

1. 깃을 사용하는 방법
2. 깃을 **잘** 사용하는 방법: `git flow`를 사용하는 방법



브랜치 에픽, 커밋할때 이슈번호





브랜치를 스토리단위로 했을 때는 커밋을 어떻게 하셨을까요?

​	커밋 할때에도 스토리 번호로 하신것같아요