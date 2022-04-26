# function in JavaScript

* 참조 타입 중 하나로써 function 타입에 속함
* JS에서 함수를 정의하는 방법은 주로 2가지
  * 함수 선언식
  * 함수 표현식

![image-20220426103826286](javascript_day2.assets/image-20220426103826286.png)

![image-20220426104857681](javascript_day2.assets/image-20220426104857681.png)

* 익명함수 (람다함수) 사용한 경우

![image-20220426105045145](javascript_day2.assets/image-20220426105045145.png)



* 함수 선언식 (function statement, declaration)
* 함수 표현식

![image-20220426110051272](javascript_day2.assets/image-20220426110051272.png)

![image-20220426110307816](javascript_day2.assets/image-20220426110307816.png)

![image-20220426110410893](javascript_day2.assets/image-20220426110410893.png)

![image-20220426110541493](javascript_day2.assets/image-20220426110541493.png)

* 매개변수와 인자의 개수 불일치를 허용한다 :star:
  * 인자의 개수가 더 많은 경우/적은 경우/없는 경우 다 상관없음

![image-20220426110643782](javascript_day2.assets/image-20220426110643782.png)

![image-20220426110752325](javascript_day2.assets/image-20220426110752325.png)

![image-20220426110808307](javascript_day2.assets/image-20220426110808307.png)



* 근데.. 매개변수와 인자 개수가 불일치하는 경우에.. 나머지 인자들을 배열로 받아서 보여주면 안될까??
  * `...` 연산자 사용! (**rest parameter**)

![image-20220426111035863](javascript_day2.assets/image-20220426111035863.png)

![image-20220426111141181](javascript_day2.assets/image-20220426111141181.png)



![image-20220426111335675](javascript_day2.assets/image-20220426111335675.png)

![image-20220426111739194](javascript_day2.assets/image-20220426111739194.png)



* `...` operator (어느 위치에 붙냐에 따라 이름이 달라진다) :star:
  * rest operator
  * spread operator

![image-20220426112436510](javascript_day2.assets/image-20220426112436510.png)



**Arrow Function**

* 함수를 비교적 간결하게 정의할 수 있는 문법
* function 키워드 생략 가능

![image-20220426130328527](javascript_day2.assets/image-20220426130328527.png)

![image-20220426131128701](javascript_day2.assets/image-20220426131128701.png)

![image-20220426131203530](javascript_day2.assets/image-20220426131203530.png)

* 함수 호출의 위치가 중요한 것이 아니라, 함수 선언의 위치가 중요하다



**문자열(String)**

![image-20220426131448329](javascript_day2.assets/image-20220426131448329.png)

![image-20220426131704736](javascript_day2.assets/image-20220426131704736.png)

![image-20220426131757213](javascript_day2.assets/image-20220426131757213.png)

![image-20220426132001162](javascript_day2.assets/image-20220426132001162.png)

![image-20220426132209509](javascript_day2.assets/image-20220426132209509.png)

![image-20220426132319113](javascript_day2.assets/image-20220426132319113.png)

![image-20220426132411533](javascript_day2.assets/image-20220426132411533.png)

![image-20220426132556553](javascript_day2.assets/image-20220426132556553.png)

![image-20220426132640201](javascript_day2.assets/image-20220426132640201.png)

![image-20220426132801965](javascript_day2.assets/image-20220426132801965.png)

![image-20220426132852197](javascript_day2.assets/image-20220426132852197.png)

* spread operator(`...`)를 사용하여 shallow copy에 활용 가능

  * deep copy 불가
  * 1차원 배열인 경우 deep copy가 일어나는 것 처럼 보일 수 있겠지만 함정이라는 것!
  * 2차원 배열인 경우로 확인해보기

  ![image-20220426133233817](javascript_day2.assets/image-20220426133233817.png)

![image-20220426134217986](javascript_day2.assets/image-20220426134217986.png)

**`forEach` practice**

![image-20220426135642777](javascript_day2.assets/image-20220426135642777.png)