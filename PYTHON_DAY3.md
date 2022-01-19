## 함수

* **Decomposition**: 기능을 분해, 재사용 가능하게 만들기 위해 사용

* **Abstraction**: 복잡한 내용을 몰라도 사용할 수 있도록(블랙박스), 재사용성과 가독성 및 생산성 증가 

  (=> 이 두가지가 함수를 사용하는 가장 중요한 이유!)



### 함수 기초

* 함수(Function):
  * 특정 기능을 하는 코드 조각의 묶음
  * 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출해서 간편히 사용

* 사용자 함수:

  * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

    ```python
    def function_name(parameter):
        #code block
        return returning_value
    ```

  * pstdev 함수 (파이썬 표준 라이브러리 - statistics) *내장함수를 한번 더 묶어서 간단히*

    ```python
    import statistics
    values = [1, 2, 3, 4, 5, 6, 7]
    statistics.pstdev(values)
    ```

* 함수 기본 구조

  * 선언과 호출

    * **함수의 선언**은 **def 키워드** 사용

    * 함수는 **함수명()** 으로 **호출**

      ```python
      def cube(number): # 함수의 이름, input의 이름
          return number ** 3 #logic 작성
      
      print(cube(10)) #결과값
      ```

  

### 함수의 결과값

* Void function
  * 명시적인 return값이 없는 경우; **None**을 반환하고 종료

* Value returning function

  * 함수 실행 후, return문을 통해 값 반환

  * return하게 되면 값 반환 후 바로 종료

    ```python
    a = print('Hello') #a가 명시적인 return값이 없으므로
    b = float('3.5')
    
    print(a,b) #여기서 None값이 출력된다
    ```

    ```python
    def m(x, y):
        return x - y
        return x * y
    
    print(m(1,2)) #-1이 출력: return을 만나는 순간 종료된다
    ```

    ```python
    def m(x, y):
        return x - y, x * y
    
    print(m(1,2)) #튜플 타입의 (-1,2)값 하나를 반환
    ```

    ```python
    def rectangle(width, height):
        return width * height, (width + height) * 2
    
    print(rectangle(30, 20))
    #(600, 100) => 하나의 튜플로 결과값 도출
    ```

    

### 함수의 입력

* Parameter & Argument
  * parameter : 함수 실행 시, 함수 내부에서 사용되는 식별자
  * argument : 함수 호출 시, 넣어주는 이름

* Positional Arguments: 기본적으로 함수 호출 시 위치에 따라 함수 내에 전달됨

```python
def add(x, y):
    return x + y

print(add(1, 2)) #위치- 내부에서 바인딩 x = 1; y =2
print(add(y=2, x=1)) #키워드 - 직접 지정
print(add(x=1, 2)) # 키워드를 지정하는 순간 의미 없어짐 => SyntaxError
print(add(1, y=2)) # 위치 지정.. 키워드가 뒤에 있으면 얘는 에러 안뜸
```

* 정해지지 않은 여러 개의 Arguments 처리 **Packing & Unpacking**

* 별표 두개(**)를 사용하면 dictionary로 packing 가능하다

**********

함수

정의든 호출이든 키워드 인자 다음에 위치 인자가 못온다

*********

### 함수의 범위(Scope)

* 함수는 코드 **내부에 local scope를 생성**하고, 그 **외의 공간인 global scope**로 구분
* 함수는 가장 기본 : local scope
* local 함수를 blackbox 밖으로 함수를 꺼내주고 싶다면 return을 써서 반환해주어야 한다

* global 함수 잘못쓰면 에러가 발생했을 때 해결하기 어려워지기 때문에 남용하지 말 것!
* global에서 선언된 a=10이 있고, local에서 선언된 a=5가 있다면, a가 5로 재할당 된 게 아니라 글로벌과 로컬에서의 a가 다른 것 = > 별개의 변수로 선언된 것

### Summary

함수는 블랙박스이다! => LEGB 순으로 이름을 찾아나간다