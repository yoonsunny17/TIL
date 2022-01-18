## Review

**python**

*인터프리터 언어 (python)vs 컴파일 언어*

* 소스 코드 작성하였을 때 중간 스텝마다 run하는 것이 인터프리터, 코드 완성 끝나고 나서 run하는 것이 컴파일
* java는 인터프리터 언어이면서 동시에 컴파일 언어이다

*객체 지향 프로그래밍(Object Orientied Programming)*

* 프로그래밍의 크기가 점점 커지니까 객체라는 것을 설계하기가 힘들어짐

**********

******

**파이썬 개발환경 종류**

* 대화형 환경
  * 파이썬 기본 interpreter
  * jupyter notebook

* 스크립트 실행
  * .py 파일을 작성
  * IDE: Pycharm, 파이썬에 특화된 프로그램 (debugging할 때 좀 더 이해하기 쉽게 보여줌)
  * Text Editor: Visual Studio Code 거의 모든 언어들을 지원함 *+익스텐션 설치하면 파이참같이 비슷해짐* 



**코드 스타일 가이드**

* 코드를 *어떻게 작성할지*에 대한 가이드라인
* 파이썬에서 제안하는 스타일 가이드 [PEP8](https://www.python.org/dev/peps/pep-0008/#indentation)

*****

**주석(Comment)**을 다는 습관을 들이자!

********

**정수(Int)**

* 매우 큰 수를 나타낼 때 *오버플로우가 발생하지 않음*



**문자열(String Type)**

* %-formatting
* str.format()
* f-strings (이거 써보기 바람!)



**Packing & Unpacking**

* 이 부분들 다시 공부하기!



**셋(Set)**

* 0개 이상의 *해시 가능*한 



**Dictionary**

* key-value 쌍으로 이루어짐



**자료형 변환(Typecasting)**

* 암시적 형 변환: *편하지만, 위험하다*
* 명시적 형 변환



**멤버십 연산자**

* in/ not in으로 시퀀스 포함 여부를 확인할 수 있음
  * Bool형으로 반환



**프로그램 구성 단위**

* 함수(Function)
* 모듈(Module)
* 패키지(Package)
* 라이브러리(Library)



**************

## 제어문

### 조건문

* 참/거짓을 판단할 수 있는 조건식과 함께 사용



**조건 표현식** 

```python
value = num if num >= 0 else -num
```

```python
if num >= 0:
    value = num
else:
    value = -num
```





### 반복문

**while문**

* 조건식이 참인 경우 계속 반복

**for문**

```python
chars = input()
happy

for idx in range(len(chars))
    print(chars(idx))
```

* 사실은 출력문에서 `print( , end='')` 이렇게 end의 자리가 숨겨져 있다! 

* 딕셔너리 순회 (복습필요)
* enumerate 순회
  * 인덱스와 객체를 쌍으로 담은 열거형 객체 반환
    * *(index, value)* 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['영희', '철수', '영민']
for idx, member in enumerate(members):
    print(idx, member)
```



* List Comprehension *이해력, 포함, 압축.. list를 좀 압축해서 잘 이해하는거 => 코드줄이기*

  * 표현식과 제어문을 통해 특정 값을 가진 리스트를 간결하게 생성하는 방법

    ```python
    #1
    [<expression> for <variable> in <iterable>]
    #2 추천 별로 안함
    [<expression> for <variable> in <iterable> if <조건식>]
    ```



**반복문 제어**

* break: 반복문 종료
* continue