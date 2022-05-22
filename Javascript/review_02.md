# JS review

* 데이터 타입 종류
  * JS 모든 값은 특정한 데이터 타입을 가짐
  * 크게 원시 타입(primitive type)과 참조 타입(reference type)으로 분류됨
    * 원시 타입(primitive type)
      * 객체가 아닌 기본 타입
      * 변수에 해당 타입의 값이 담김
      * 다른 변수에 복사할 때 실제 값이 복사됨
    * 참조 타입(reference type)
      * 객체 타입의 자료형
      * 변수에 해당 객체의 참조 값이 담김
      * 다른 변수에 복사할 때 참조 값이 복사됨

* 원시 타입
  * 숫자(number) 타입
    * 정수, 실수 구분이 없음
    * 부동소수점 형식을 따름
    * NaN (Not-A-Number)
  * 문자열(string) 타입
    * 템플릿 리터럴
      * 따옴표 대신 backtick을 사용
      * ${expression} 형태로 사용
  * undefined
    * 변수 선언 시 아무 값도 할당하지 않으면 자바스크립트가 자동으로 할당
  * null
    * 변수의 값이 없음을 **의도적으로 표현**할 때 사용
  * Boolean 타입
    * true, false (소문자 주의)