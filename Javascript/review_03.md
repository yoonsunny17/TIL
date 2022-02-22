# JS review

*****

## 조건문

* `if` statement
  * `if, else if, else`
  * 블록 스코프 생성
* `switch` statement
  * 표현식(expression)의 결과값을 이용한 조건문
  * 표현식의 결과값과 case문의 오른쪽 값을 비교
  * break 및 default문은 선택적으로 사용 가능
  * break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
  * 블록 스코프 생성



## 반복문

* `while`

* `for`

  * 세미콜론(;)으로 구분되는 세 부분으로 구성

* `for ... in`

  * 주로 객체(*js에서 객체는 dictionary; key-valuef로 이루어진거*)의 속성들을 순회할 때 사용
  * 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

* `for ... of`

  * **반복 가능한 객체**를 순회하며 값을 꺼낼 때 사용
    * **반복 가능한 객체: array, map, set, string**

  ```javascript
  const fruits = ['딸기', '바나나', '메론']
  for (let fruits of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
  }
  // 딸기!
  // 바나나!
  // 메론!
  
  for (const fruits of fruits) {
    // fruit 재할당 불가
    console.log(fruit)
  }
  
  // === 얘는 가능함 === // 
  for (const fruit of fruits) {
    console.log(fruit + '!')
  }
  // 딸기!
  // 바나나!
  // 메론!
  ```

  