### Review

```python
class Person:
    cnt = 0 # 클래스 변수
    
    def __init__(self, name):
        self.name = name
        Person.cnt += 1 # 인스턴스 하나 호출할때마다 cnt 1씩 증가시키고 싶음
        
aiden = Peson('aiden')
aiden.cnt = 3 # 인스턴스 변수,, 그리고 사실 클래스 변수에 있는 cnt 쓰면 안됨

yoonsun = Peson('yoonsun')
print(yoonsun.cnt)

```

* self
  * 모든 method는 self keyword를 가져야 한다
  * 인스턴스 자기 자신이다

* instance method (클래스 안에 정의된 함수)
  * 메소드 => 함수
  * 인스턴스 변수를 사용하거나, 변수에 값을 설정하는 메소드
  * self를 받아야 함
* class method
  * @classmethod
  * @ : 데코레이터 => 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  * 함수가 여러개이고, 같은 기능을 반복해야 할 경우 데코레이터를 사용함

```python
def time_display_decorator(origin_func):
    def decorated():
        print(dt.now())
        origin_func()
        print('----')
    return decorated

@time_display_decorator
def test_a():
    print('test_a')
@time_display_decorator
def test_b():
    print('test_b')
    
    
test_a() # time_display_decorator(test_a)() => time_display_decorator함수로 test_a를 호출하고, 그다음 decorated()을 return

        # time_display_decorator()

test_b()
```

* 클래스 메소드
  * 호출 시, 첫번째 인자로 클래스(cls)가 호출됨 => instance(self) 자리에 cls가 들어간다 생각
  * 인스턴스를 생성하지 않아도 호출이 가능하다

* @staticmethod

  * 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 경우

  * 속성을 다루지 않고, 단지 기능만을 하는 메소드 정의 시 사용



*************

### 객체 지향의 핵심 4가지 (이거 반드시 출제) ###

> **추상화** 

* 현실 세계를 프로그램 설계에 반영
* 공통된 속성과 메소드를 뽑아내는 과정

> **상속**

* 두 클래스 사이 부모 자식 관계를 정립하는 것
* 클래스는 상속이 가능함
  * 모든 파이썬 class는 object를 상속 받음
  * ```class ChildClass(ParentClass):``` 
  * ParentClass를 상속받아서 ChildClass를 만들겠습니다
* 부모클래스의 모든 속성들이 상속되므로, **코드 재사용성이 높아짐**
* ```super()``` : 자식클래스에서 부모클래스를 사용하고 싶은 경우

> **다중상속**

* 두개 이상의 클래스를 상속받는 겨우
* 중복된 속성이나 메소드가 있는 경우 상속 순서에 의해 결정됨

> **다형성(Polymorphism)**

* 동일 메소드가 클래스에 따라 다르게 행동할 수 있음
* 서.다. 클래스에 속한 객체들이 동일 메세지에 대해 다른 방식으로 응답될 수 있음
* 메소드 오버라이딩
  * 상속받은 메소드를 재정의

> **캡슐화**

* 객체의 일부 구현 내용에 대해 외부로부터 직접적인 액세스를 차단
  * 속성 메서드를 묶는 작업
  * '은닉성' => 접근에 대한 권한
* 접근제어자 종류
  * Public Access Modifier : 다 가능
  * Protected : 나랑, 내 자식만 *(의 class 안에서만)* 가능 => class 안에서만 속성과 메소드에 접근 가능하게 함
  * Private : 나만 가능
    * 위에서 아래로 갈수록 접근이 힘들어진다

* Public
  * 언더바 없이 시작하는 메소드나 속성 ```self.name, self.age```
  * 일반적으로 작성되는 메소드와 속서의 대다수
* Protected
  * **언더바 1개**로 시작하는 메소드나 속성 ```self._age``` 
  * 하위 클래스 오버라이드 허용
  * 클래스 밖에서 호출 한다고 error 발생하는 것은 아님. 그냥 유저가 조심해야함
* Private
  * **언더바 2개**로 시작하는 메소드나 속성 ```self.__age``` 
  * 나만 접근 가능 (하위클래스 상속 및 호출 불가능 => class 바깥에서 호출하므로)
  * 외부 호출 불가능 =>  error 발생

> **getter 메소드와 setter 메소드**

* getter메소드: 변수 값 읽는 메소드
  * @property 데코레이터 사용

* setter메소드: 변수 값 읽는 메소드
  * @변수.setter 데코레이터 사용

  