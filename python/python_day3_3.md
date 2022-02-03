## 함수의 문서화(Doc-String)

* Naming Convention
  * 좋은 함수화 parameter 이름을 짓는 방법
    * snake case, camel case

* map: map(function, iterable)

  * 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

  * input 값들을 숫자로 바로 활용하고 싶을 때 map 활용

    ```python
    n, m = map(int, input().split())
    ```

    

## 함수 응용

* 내장 함수

* map(function, iterable)

* filter(function, iterable) : 결과가 True인 것들을 filter object로 반환

* zip(*iterables) :  튜플을 원소로 하는 zip object를 반환

* lambda [parameter] : 표현식

  ```python
  #람다함수
  def odd(n):
      return n % 2
  
  print(list(filter(odd, range(5)))) # filter가 true값 반환
  print*list(filter(lambda n: n % 2, range(5)))
  ```

* 재귀함수(recursive function) : 자기 자신을 호출하는 함수

  * 1개 이상의 **base case(종료되는 상황)**가 존재하고, 수렴하도록 작성 (중요!)

    ```python
    f(4) = 4 * f(3)
    f(3) = 3 * f(2)
    f(2) = 2 * f(1)
    f(1) = 1
    =================
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n* factorial(n-1)
    factorial(4) #output: 24
    ==================
    def fact(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    ```
    
    => 반복문으로도 작성 가능하지만, 재귀적 표현이 가장 자연스럽고 간단함
    
    => 숫자 커질수록 반복문이 처리속도 훨씬 빠르긴 함



*********

### 모듈과 패키지

* 모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
* 패키지: 특정 기능과 관련된 여러 모듈의 집합



### 사용자 모듈과 패키지

* 모듈 만들기 - check

* 패키지 만들기
  * 모든 폴더에는 **__init\_\_.py**를 만들어서 구분



### 가상환경

* venv: 가상 환경을 만들고 관리하는 데 사용되는 모듈