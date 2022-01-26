## 제어문(Control Statement)

* 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
* 특정 상황에 따라 코드를 선택적으로 실행하거나 계속하여 실행하는 제어가 필요
* 제어문은 순서도(flow chart)로 표현이 가능



## 조건문(Conditional Statement)

* 참/거짓을 판단할 수 있는 조건식과 함께 사용
* 조건표현식: *if/elif/else*

```python
#example 1.
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')
print(a)
```





## for vs while

* for: 반복 가능한 애들을 꺼내준다
* while: 어떠한 조건이 **참**일 때 실행해준다
* **결과 변수 초기화** 고려하자



![](PYTHON_DAY1_2.assets/for%EB%AC%B8_odd%20list.png)



## for와 continue의 차이

![](PYTHON_DAY1_2.assets/pass%EC%99%80%20continue%EC%9D%98%20%EC%B0%A8%EC%9D%B4.png)

* pass는 그냥 없는 셈 쳐도 된다 (단, 위의 예시에서 pass를 써주지 않으면 code error가 뜨니까 써주는 것)

