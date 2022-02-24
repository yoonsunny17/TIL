### 스택2 review

> 계산기

* 중위표기법 => 후위표기법으로 바꾸어 컴퓨터가 알아볼 수 있도록 표현
* 후위표기법으로 표현된 수식을 계산
* `icp(in-coming priority)` `isp(in-stack priority)`
  * icp : 스택으로 들어올 때 우선순위
  * isp : 스택에 들어있을 때 우선순위
  * icp가 top에 존재하는 token의 isp보다 더 큰 경우에만 stack에 넣는다!
    * icp > isp => **push**
    * `)` 을 만나면, `(`을 만날 때까지 연산자들을 pop 해준다