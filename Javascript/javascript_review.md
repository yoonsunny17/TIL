* DOM, DOM tree
* 변수와 식별자 3가지
  * var 함수 스코프, 호이스팅 가능(var가 밑에 있는 것을 미리 아는 것), 재선언, 재할당 가능
    * 호이스팅: 변수 선언 이전의 위치에서 접근 시 error가 나지 않고 undefined 반환
  * let 재할당 가능, 블록 스코프, 재선언 불가능
  * const 재할당 불가능, 블록 스코프, 재선언 불가능

* 선언, 할당, 초기화
* 데이터 타입 종류 분류 알아두기
  * number가 int와 float으로 나누어지지 않는다는 특징
  * 참조타입은 모두 object로 퉁침
    * array는 idx가 key인 특수한 object임
  * undefined와 null의 차이?
    * 동작상의 차이가 없음
    * 선언하면서 할당하지 않으면 자동으로 undefined가 할당됨
    * 값이 없음을 의도적으로 표현할 때 사용하는 것이 null
    * `typeof` 알아두기
* 파이썬에서는 비어있는 object는 항상 거짓인데, JS에서는 object가 항상 참임
  * 파이썬에선 `print(bool[]) = False` 임
* 연산자
  * `==` : 비교 시 암묵적 타입 변환을 통해 타입을 일치시킨 후 비교
    * 파이썬에서 `bool(1 == '1')`은 False인데, JS에서는 True
  * `===`: 엄격한 비교가 이루어지고, 암묵적 타입 변환이 발생하지 않음
    * 파이썬에서 `bool(1 === true)`는 True인데 JS는 false
* 삼항연산자
  * and &&
  * or ||
  * not |
* `if, else if, else`
* 조건문 `switch statement`
  * switch에는 break가 있어야 함!
  * break가 없는 경우, 밑에 조건문까지 다 출력됨

* 반복문 :star:
  * while
  * for (초기; 조건; 실행)
    * 초기= 한번 실행, 조건=매번 검사, 실행=매번 실행
  * for in
    * 객체의 **속성값 순회**에 유용
  * for of
    * 반복 가능한 **객체 순회** 시 사용
* JS 함수 정의하는 방법 2가지
  * 함수 선언식
  * 함수 표현식
* JS의 함수는 일급 객체에 해당
  * 일급 객체 :star:
    * 변수에 할당 가능
    * 함수의 매개변수로 전달 가능
    * 함수의 반환 값으로 사용 가능

* arrow function
  * function 생략 가능
  * 함수의 매개변수가 하나인 경우, `'()'`도 생략 가능
  * 함수 몸통이 표현식 하나인 경우, `'{}'`과 `return`도 생략 가능

* methods
  * 문자열
  * 배열 `forEach, map, filter, reduce ...` 

* Objects
  * key: value 쌍으로 표현
  * key는 문자열 타입만 가능
  * value는 모든 타입 가능
  * 자바스크립트의 객체는 JSON이다



* DOM 선택 메서드
  * `document.querySelector(selector)`
  * `document.querySelectorAll(selector)`
  * selector로 id, class, tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능

* DOM 속성 메서드
  * `Element.setAttribute(name, value)`
    * 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
  * `Element.getAttribute(attributeName)`
    * 해당 요소의 지정된 값을 반환

* DOM 삭제 메서드
  * `ChildNode.remove()`
    * Node가 속한 트리에서 해당 Node를 제거
  * `Node.removeChild()`
    * DOM에서 자식 Node를 제거하고 제거된 Node를 반환

* Event
  * `EventTarget.addEventListener(type, listener)`
    * type = 반응할 이벤트 유형
    * listener = 지정된 타입의 이벤트가 발생 시 알림을 받는 객체.. 함수가 들어오는 경우, 그 함수는 **콜백함수**이다 !!
  * `event.preventDefault()`
    * 현재 이벤트의 기본 동작을 중단
    * HTML 요소의 기본 동작을 작동하지 않게 막음