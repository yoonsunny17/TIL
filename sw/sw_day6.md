> 스택

* 스택의 pop 알고리즘

  ```python
  def pop():
      if len(s) == 0:
          # underflow
          return
      else:
          return s.pop(-1)
  ```

* 저장소를 동적으로 할당하여 스택을 구현한다
  * 메모리를 효율적으로 사용할 수 있음



> 괄호 검사

`if((i == 0) && (j == 0))`

* 여는 괄호가 있을 때 스택에 push
* 괄호 수식이 끝났는데 스택에 괄호가 남아있으면 False 반환!
* 닫는 괄호를 만났을 때 stack 안의 여는 괄호와 짝을 비교하고 다르면 False!

* 괄호 검사 함수 만들기 :star:

  

> Function call

* 함수 호출과 복귀의 반복

* 재귀 호출

  * factorial

  * 피보나치 수열

    ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n-1) + fibo(n-2)
    ```

    * 피보나치 수를 구하는 함수를 재귀함수로 구현하는 경우, 연산량이 상당히 많다; 엄청난 중복 호출이 존재한다
    * Memoization (위의 문제를 해결하기 위한 방안)



> Memoization (메모이제이션)

* 이전에 계산한 값을 메모리에 저장하여 매번 다시 계산하지 않도록 하는 기술
* memoization = '메모리에 넣기 (to put in memory)'

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화한다
# memo[0]을 0으로, memo[1]은 1로 초기화 한다
# recursive 방식

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
```



> DP(Dynamic Programming)

* 메모이제이션을 사용한 프로그래밍 기법
* DP array
* 피보나치 수 DP 적용
  * 문제를 부분 문제로 분할한다
  * 부분 문제로 나누는 일을 끝냈다면 가장 작은 부분 문제부터 해를 구한다

* recursive 방식

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화한다
# memo[0]을 0으로, memo[1]은 1로 초기화 한다
# recursive 방식

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
```

* iterative 방식

```python
def fibo2(n):
    f = [0, 1]
    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    
    return f[n]
```

