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
  * 인스턴 스 자기 자신이다

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

