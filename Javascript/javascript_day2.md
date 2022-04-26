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

![image-20220426141337314](javascript_day2.assets/image-20220426141337314.png)

![image-20220426141722397](javascript_day2.assets/image-20220426141722397.png)

![image-20220426141920730](javascript_day2.assets/image-20220426141920730.png)

![image-20220426142752274](javascript_day2.assets/image-20220426142752274.png)

![image-20220426143150990](javascript_day2.assets/image-20220426143150990.png)

![image-20220426143505972](javascript_day2.assets/image-20220426143505972.png)

* `some` method
  * 배열의 요소 중 **하나라도 true 이면 true를 반환**

* `every` method
  * 배열의 **모든 요소가 true이면 true를 반환**



### 객체(Objects)

**객체의 정의와 특징**

* 객체는 속성(property의 집합)이며,  중괄호 내부에 `key`와 `value`의 쌍으로 표현
* `key`는 문자열 타입만 가능
* `value`는 모든 타입(함수 포함) 가능
* 객체 요소 접근은 점 또는 대괄호로 가능

![image-20220426150704907](javascript_day2.assets/image-20220426150704907.png)

![image-20220426151240852](javascript_day2.assets/image-20220426151240852.png)

* 세번째 반환값이 `NaN` 인 이유!
  * 메서드가 아닌 객체에서 바로 쓰는 this는 window를 의미한다

![image-20220426151803685](javascript_day2.assets/image-20220426151803685.png)

![image-20220426152413961](javascript_day2.assets/image-20220426152413961.png)

![image-20220426153139966](javascript_day2.assets/image-20220426153139966.png)

![image-20220426153755770](javascript_day2.assets/image-20220426153755770.png)



**JSON**

* JS에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  * `JSON.parse()`
    * JSON => 자바스크립트 객체
  * `JSON.stringify()`
    * 자바스크립트 객체 => JSON

![image-20220426155935339](javascript_day2.assets/image-20220426155935339.png)



**lodash**

* A modern JavaScript utility library
  * 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
  * array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공



![image-20220426162043172](javascript_day2.assets/image-20220426162043172.png)

* deep copy

![image-20220426161842749](javascript_day2.assets/image-20220426161842749.png)