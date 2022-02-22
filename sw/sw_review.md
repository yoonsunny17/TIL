> 좋은 알고리즘이란?

* 정확성, 작업량, 메모리 사용량, 단순성, 최적성으로 판단

* **시간 복잡도** 



> Bubble sort

* 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
  * 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  * 시간 복잡도: O(n^2)

```python
# 오름차순
def BubbleSort_up(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
# 내림차순
def BubbleSort_down(arr):
    for j in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```



> Counting sort

* data에서 각 항목들의 발생 횟수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다
* 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정한다 (누적으로 바꾸기)
* 역순으로 counts를 감소시키고 temp에 1을 삽입한다
  * 시간 복잡도: O(n+k)

```python
def Counting_Sort(A, B, k):
    # A [] => 입력 배열 (1 to k)
    # B [] => 정렬된 배열
    # C [] => 카운트 배열
    
    C = [0] * (k+1)
    
    for i in range(0, len(A)):
        C[A[i]] += 1
        
    for i in range(1, len(C)):
        C[i] += C[i-1]
        
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```



*******

> 2차원 배열

`arr = [list(map(int, input().split())) for _ in range(N)]`

```python
# 행 우선순회
for r in range(n):
    for c in range(n):
        arr[r][c]...
        
# 열 우선순회
for c in range(n):
    for r in range(n):
        arr[r][c]...
        
# 지그재그 순회
for r in range(n):
    for c in range(m):
        arr[r][c + (m-1-2*c) * (i%2)]
```

```python
# 전치행렬 만들기
arr = [[1,2,3],[4,5,6],[7,8,9]]

# sol 1
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
# sol 2
arr_t = list(map(list, zip(*arr)))
```

> 비트 연산자

```python
# 비트 연산자
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(1<<n): # 1<<n: 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1<<j): # i의 j번 비트가 1인 경우
            print(arr[j], end=' ')
    print()
print()
```



******

> ASCII code

* 128문자 표현
  * A = 65, a = 97

> 패턴 매칭

* Brute force

  ```python
  arr = input()
  search = input()
  n = len(arr)
  m = len(search)
  
  def BruteForce(search, arr):
      i = 0
      j = 0
      while i < n and j < m:
          if arr[i] != search[m]:
              i = i - j
              j = -1
          i += 1
          j += 1
      if j == m:
          return i-m
      else:
          return -1 # 검색 실패
  ```

* KMP 알고리즘
  * 시간 복잡도: O(M+N)

* 보이어-무어 알고리즘
  * 오른쪽 => 왼쪽으로 비교

* KMP와 보이어-무어 알고리즘의 차이점?
  * 보이어-무어는 오른쪽부터 검사한다는 것이 가장 큰 차이점
  * 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는다면 패턴의 길이만큼 이동한다.