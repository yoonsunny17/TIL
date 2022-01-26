**함수 응용**

* map(function, iterable)
  * iterable: list, tuple
  * iterable한 애들한테 각각에 대해 function을 적용한 애들을 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result, type(result))
print(list(result)) # 리스트 형변환을 통해 결과 직접 확인
```

```python
n, m = map(int, input().split()) # 인풋 넣은애들을 int형으로 바꿔줘
print(n, type(n))
print(m, type(m))
```

* filter(function, iterable)
  * 결과가 True인 것들을 filter object로 반환

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
print(list(result))
```

* zip(*iterables)

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
students = ['aiden', 'haley', 'jun']

for pair in zip(numbers, letters, students):
    print(pair)
    
#for문이랑 자주 많이 쓴다.
#만약 짝이 맞지 않는 경우, 수가 적은 쪽에 맞추어서 짝이 안맞은 놈을 버린다.
```

```python
#transpose case_ 몰라도 돼 
lst = [[1,2,3],[4,5,6],[7,8,9]] 
for i in lst:
    print(i)
print('\n-----\n')
lst2 = zip(*lst) # transpose / 전치
for i in lst2:
    print(i)
print('\n-----\n')
lst3 = list(zip(*lst))[::-1] # 90도 회전 시계 반대 방향
for i in lst3:
    print(i)
print('\n-----\n')
lst4 = zip(*lst[::-1]) # 90도 회전 시계 반대방향
for i in lst4:
    print(i)
```

* lambda 함수 : 이름이 없는 함수(익명함수)
  * lambda [parameter] : 표현식
  * return문을 가질 수 없음(return을 하긴 함)

```python
#1.
print((lambda x : x + 1)(10))
#2.
func = lambda x : x + 1
print(func(10))
```

* filter & lambda 같이 쓸 수 있다

```python
lst = [1, 2, 3, 4, 5]
filter((lambda n : n % 2), lst)
result = filter((lambda n : n % 2), lst)
print(result, type(result))
print(list(result))
```

* 재귀 함수 *(알고리즘 때 제대로 공부)*
  * 자기 자신을 호출하는 함수

