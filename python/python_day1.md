## Python 스크립트 실행

* IDE(통합개발환경, 각 언어에 특화된 환경을 제공. *ex. Pycharm*)
* Text editor(*ex. VS code*)



## 코드 스타일 가이드

* 코드를 **어떻게 작성할지**에 대한 가이드라인

* 파이썬에서 제안하는 스타일 가이드

  * **PEP8**

    

## 들여쓰기(Identation)

* Space Sensitive
  * 문장을 구분할 때, 중괄호{} 대신 들여쓰기<>를 사용
  * 들여쓰기는  space 4번



## 변수(Variable)

* '=' : 할당한다 (*같다는 의미가 아님*)

* 변수란?

  * 어떠한 값을 넣기 위한 박스

  * 객체(object): 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

    --> 파이써는 **객체지향 언어**이며, 모든 것이 객체로 구현되어 있음

  * 동일 변수에 다른 객체를 언제든 할당 가능함. 즉, 참조하는 객체가 바뀔 수 있기 때문에 변수라고 불림
  * 할당 연산자(=)를 통해 값을 *할당(assignment)*
  * **type()**: 변수의 type이 무엇인지 구분하는 것이 매우 중요

* 변수 할당
  * 같은 값을 동시에 할당할 수 있음
  * 다른 값을 동시에 할당할 수 있음(multiple assignment)

* 식별자(Identifiers)
  * 변수의 이름짓기
  * 파이썬 객체를 식별하는 데 사용하는 이름(name)
  * rules
    * 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
    * 첫 글자에 숫자 올 수 없음
    * 길이제한 없고, 대소문자 구별

* 사용자 입력

  * input([prompt])
    * 사용자로부터 값을 즉시 입력받을 수 있는 내장 함수

  * 주석

    * 한 줄 주석
      * 주석으로 처리될 내용 앞에 # 입력

    * 여러 줄의 주석
      * """ 또는 ''' 사용이 편함



## 파이썬 자료형(Python Datatype)

* None: *값이 없음*을 표현하기 위한 타입인 None Type
* 불린(Boolean): 특정 데이터가 True인제 False인지 검증
  * bool(0), bool(''), bool([]) = False
  * bool([0]) = True

### 수치형 (Numeric Type)

* 정수(Int)

  * 모든 정수의 타입은 int
  * 매우 큰 수를 나타낼 때 *오버플러우*가 발생하지 않음

  * 진수표현
    * 2진수: 0b (0b10)
    * 8진수: 0x (0x10)
    * 16진수: 0o (0o10)

* 실수(Float)

  * 정수가 아닌 모든 실수는 float 타입

  * 부동소수점

    * 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현

    * 이 과정에서 floating point rounding error가 발생하여, 예상치 못한 결과가 발생

    * *3.14 - 3.02 == 0.12* : False!!!!! (왼쪽 다항식의 결과값은 0.1200000000000001임)

      1. 임의의 작은 수 

         ```python
         abs(a - b) <= 1e-10
         ```

         (True)

      2. system 상의 machine epsilon

         ```python
         import sys
         print(abs(a - b) <= sys.float_info.epsilon)
         print(sys.float_info.epsilon)
         ```

         (True)

         *epsilon* 두 수의 차이를 나타냄

      3. math.isclose(a, b) : True

         ```python
         import math
         math.isclose(a, b)
         ```

         (True)

* 복소수(Complex)
  * 실수부와 허수부로 구성된 복소수는 모두 complex type

### 문자열(String Type)

* 모든 문자는 str 타입
* 문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기
  * PEP8에서는 소스코드 내에서 문장부호 통일 유지하도록 함

* Immutable

  ```python
  a = 'my string!'
  a[-1] = '!'
  ```

  특정 값 하나만 바꿀 수 없음

* Iterable

  ```python
  a = '123'
  for char in a:
      print(char)
  ```

* Escape sequence

  * 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\)를 활용하여 구분

    ```python
    print('이 다음은 엔터.\n그리고 탭\t탭')
    ```

* String interpolation(문자열 사이에 변수를 넣고 싶다)

  * %-formatting

  * str.format()

  * f-strings : python 3.6+

    ```python
    f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일'
    ```



### 컨테이너(Container)

* 컨테이너란?
  * 여러 개의 값을 담을 수 있는 것(객체)으로, **서로 다른 자료형을 저장**할 수 있음
  * 가변형/불변형, 시퀀스형/비시퀀스형으로 구분 가능(여기는 나중에 따로 정리)

* 리스트(List) : [] 사용
* 튜플(Tuple) : () 사용, 수정 불가능(immutable)

* 레인지(Range)
  * 기본형 : range(n) => 0부터 n-1까지의 숫자 seq
  * 범위 지정 : range(n, m) => n부터 m-1까지의 숫자 seq
  * 범위 및 스텝 지정 : range(n, m, s) => n부터 m-1까지 s만큼 증가시키는 숫자 seq

* 패킹/언패킹 연산자(Packing/Unpacking Operator)
  * 컨테이너로 묶기 = 패킹, 컨테이너 풀기 = 언패킹



### 비시퀀스 컨테이너

* 셋(set)
  * **순서없이** 0개 이상의 해시가능한 객체를 참조하는 자료형
  * {} 혹은 set()을 통해 생성
  * 중복 값 제거
  * 빈 중괄호의 type은 dictionary형 (set() 으로 하면 빈 set 나옴)
  * 순서가 없어서 특정 값에 접근할 수 없음
  * 다른 컨테이너에서 **중복된 값을 쉽게 제거**할 수 있음

* 딕셔너리(dictionary)
  * **순서없이** 키-값(key-value) 쌍으로 이뤄진 객체를 참조하는 자료형
  * Dictionary의 키(key) => 해시가능한 불변 자료형만 가능
  * 값(value) => 어떤 값이든 상관 없음
  * {} 혹은 dict()을 통해 생성



### 형 변환(Typecasting)

* 자료형 변환
* 암시적 형 변환: 컴퓨터가 알아서 형을 변환시킴
* 명시적 형 변환: 우리가 컴퓨터한테 형을 변환시키라고 명시하는 것



### 연산자(Operator)

* \+ \- \* / // % ** 

* ```python
  divmod(x, y) : x를 y로 나누었을 때 몫과 나머지가 출력됨
  ```

* 논리 연산자: and*(둘다 참이어야 참)*, or*(하나만 참이어도 참)*, not*(반대를 출력)*

  * 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값을 반환
    * and 연산에서 첫번재 값이 False인 경우 무조건 False => 첫번째 값 반환
    * or 연산에서 첫번째 값이 True인 경우 무조건 True => 첫번째 값 반환

* 복합 연산자
* 식별 연산자
* 멤버십 연산자
* 시퀀스형 연산자
* 인덱싱(Indexing): 시퀀스의 특정 인덱스 값에 접근 (*해당 인덱스가 없는 경우 **IndexError***)

* 슬라이싱(Slicing): 시퀀스를 특정 단위로 슬라이싱

* 연산자 우선 순위 지킬 것!