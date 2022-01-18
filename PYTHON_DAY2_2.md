**1번. 갯수 구하기**

```python
students = ['김철수', '이영희', '조민지']

print(len(students))
```



**2번. 득표수 구하기**

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

for student in students:
    if student == '이영희':
        cnt += 1
print(cnt)
```



**3번. 최댓값 구하기 / 4번. 최솟값 구하기**

```python
#n,m을 list의 첫 항목의 값으로 설정해도 가능
#n = numbers[0] 이런식으로!
numbers = [7, 10, 22, 4, 3, 17]
n = -1
for number in numbers:
    if number > n:
        n = number
print(n)

m = 100
for number in numbers:
    if number < m:
        m = number
print(m)
```



**5번. 최댓값과 등장 횟수 구하기**

```python
numbers = [7, 10, 22, 7, 22, 22]

n = numbers[0]
for number in numbers:
    if number > n:
        n = number
        
cnt = 0
for number in numbers:
    if number == n:
        cnt += 1

print(n, cnt)
```



**6번. 5의 개수 구하기**

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

cnt = 0
for number in numbers:
    if number == 5:
        cnt += 1
print(cnt)
```

```python
i = 0
five = 0
while i < len(numbers):
    if numbers[i] == 5:
        five += 1
print(five)
```



**7번. 'a'가 싫어**

```python
word = input()
i = 0

for i in range(len(word)):
    if word[i] == 'a':
        pass
    elif word[i] != 'a':
        print('{0}' .format(word[i]), end='')
        i += 1
```

```python
word = input()
rlt_str = ''
for ch in word:
    if ch != 'a':
        rlt_str += ch
        
print(rlt_str)
```



**8번. 단어 뒤집기**

```python
word = input()

print(word[::-1])
```

