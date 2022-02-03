> 함수

* 특정한 기능을 하는 코드의 조각(묶음)
* 필요 시에만 호출하여 간편히 사용

* 내장함수 :star:

  ```len(), list(), max(), min() ... ```

* 사용자 함수: 직접 함수 작성 가능

* 선언과 호출: 호출할 때에는 '함수명()'로 한다 
* Error 나는 것 매우 주의해야 함

> 함수의 결과값 :star:

* void function
  * **명시적인 return값이 없는 경우, None 반환 후 종료**

* value returning function

  * **함수 실행 후, return문을 통해 값 반환**

  * return을 하게 되면, 값 반환 후 함수 바로 종료

    ```python
    a = print('hello')
    b = float('3.5')
    print(a, b)
    '''
    hello => return이 없음
    None 3.5
    '''
    # return은 함수 안에서만 사용되는 키워드
    # print는 출력을 위해 사용되는 함수
    ```

    ```python
    # case 1.
    def m(x, y):
        return x - y
        return x * y
    
    print(m(1, 2)) #=> x-y 값만 반환된다
    
    # case 2.
    def m(x, y):
        return x - y, x * y
    
    print(m(1, 2)) #=> (-1, 2)
    print(type(m(1, 2)))#=> tuple 형식으로 값 하나가 반환되었음을 확인
    ```

> 함수의 입력(Input)

* parameter & argument

  ```python
  def function(ham):   # parameter : ham => 정의
      return ham
  
  function('spam')     # argument : 'spam' => 함수 호출 시 전달되는 값
  ```

  ```python
  print(add(1, 2)) # 3
  print(add(y=2, x=1)) # 3
  print(add(x=1, 2)) # SyntaxError: positional argument follows keyword argument
  #=> 키워드로 지정하는 순간 위치가 이미 박살남.
  print(add(1, y=2)) # 위치 지정... 키워드가 앞에 지정되면 뒤에도 지정되어야 함
  ```

* 정해지지 않은 여러 개의 Arguments 처리(*)

  ```python
  def add(*args):   # 몇개의 input이 올 지 몰라서 * 사용해서 packing을 함
      for arg is args:
          print(arg)
  ```

  ```python
  # keyword arguments packing/unpacking 연산자
  # 함수가 임의의 개수 argument를 keyword argumetn로 호출될 수 있도록 지정
  # argument들은 dict으로 묶여서 처리, parameter에 **를 붙여 표현
  def family(**kwargs):
      for key, value in kwargs:
          print(key, ":", value)
  family(father= 'John', mother = 'Jane', me = 'John Jr.')
  #=> dict 형태로 출력된다
  ```

  

