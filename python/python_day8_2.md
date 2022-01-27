> **메소드 정리**

* Python Methods
  * Instance Methods 
    * self 매개변수를 통해 동일한 객체에 정의된 속성 및 다른 메소드에 접근 가능
    * 클래스 자체에도 접근 가능 => 인스턴스 메소드가 클래스 상태를 수정할 수 있음
  * @ Class Methods
    * 클래스를 가리키는 cls 매개변수를 받음
    * cls인자에만 접근 가능하므로, 객체 인스턴스 상태를 수정할 수 없음
  * @ Static Methods
    * 유틸리티, 작동을 할 때 사용
    * 주로 해당 클래스로 한정하는 용도로 사용
    * 인자를 받을 수 있음 ```def func(x, *args, **kwargs)```



> **객체 지향의 핵심개념 4가지**
>
> 추상화, 상속, 다형성, 캡슐화

* 추상화: 현실 세계를 프로그램 설계에 반영
* **상속**
  * 두 클래스 사이 부모-자식 관계를 정립하는 것
  * 클래스는 상속이 가능함 --> 모든 파이썬 클래스는 object를 상속받음

> **상속 관련 함수와 메소드**

* isinstance(object, classinfo)
  * classinfo의 **instance**이거나 **subclass**인 경우 **True**

* issubclass(class, classinfo)

  * class가 **classinfo**의 **subclass**인 경우 **True**

    ```python
    # bool = 0, 1
    # int = 0, 1, 2, 3, ...
    issubclass(bool, int) #=> True
    # float와 int는 별개 class를 가지고 있음 (위치가 바뀌어도 False)
    issubclass(float, int) #=> False
    ```

* super()

  * 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

    * 자식 클래스 인스턴스 내부에서 ```super().__init__ ``` 사용하면 됨 (다시 작성 필요)

    ```python
    class Person:
        population = 0
        
        @staticmethod
        def add_population():
            Person.population += 1
            
    class Student(Person):
        population = 0
            
    Person.add_population()
    print(Person.population) #=> print할 때마다 1씩 증가
    
    Student.add_population()
    print(Persion.population) #=> print 눌러도 숫자 증가가 안됨 0만 출력
    
    # why?  @staticmethod로 설정해주었기 때문! (아직 이해 덜됐음)
    ```

    ```python
    class Person:
        population = 0
        
        @classmethod
        def add_population(cls):
            cls.population += 1
            
    class Student(Person):
        population = 0
            
    Person.add_population()
    print(Person.population)
    
    Student.add_population()
    print(Persion.population) 
    
    # 함수에서 무언가를 쓰고싶을 때에는 무조건 input 으로 넘겨주어야 함
    # @classmethod를 사용
    ```

    

> **다중 상속**

* 두개 이상의 클래스를 상속받는 경우
* 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정됨**
* mro 메소드 (Method Resolution Order)



> **다형성**

* 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
* 서로다른 클래스에 속해있는 객체들이 *동일 메세지에 대해 다른 반응을 출력* 가능

* 메소드 오버라이딩 : 상속받은 메소드를 재정의



> **캡슐화** 



> **getter 메소드와 setter 메소드**

* getter 메소드 : 변수의 값을 읽는 메소드
  * @property 데코레이터 사용

* setter 메소드 : 변수의 값을 설정하는 성격의 메소드
  * @변수.setter 사용





