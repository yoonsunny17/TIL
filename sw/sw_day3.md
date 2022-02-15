## APS (Algorithm Problem Solving)

> 2차원 배열의 선언

* 1차원 list를 묶어놓은 list

```python
# 한칸씩 띄우고 받는 경우
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 없이 받는 경우
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
```

* **이렇게 만들면 안돼!!**

```python
arr = [[0]*3]*4
```

> 2차원 배열의 접근

* 열 우선 순회

```python
# i 행의 좌표
# j 행의 좌표
for j in range(m):
    for j in range(n):
        Array[i][j] # 필요한 연산 수행
```

* 지그재그 순회

```python
# i 행의 좌표
# j 행의 좌표
for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)] # 필요한 연산 수행
```

* 델타를 이용한 2차 배열 탐색

  * 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

  ```python
  arr[0...N-1][0...N-1] # N*N 배열
  di[] <- [0, 1, 0, -1] # 상하좌우
  dj[] <- [1, 0, -1, 0]
  for i : 0 -> N-1
      for j : 0 -> N-1:
              for k in range(4):
                  ni <- i + di[k]
                  nj <- j + dj[k]
                  if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스면
                  	test(arr[ni][nj])
  ```

  ```python
  # example
  arr = [[1,2,3], [4,5,6], [7,8,9]]
  N = 3
  for i in range(N):
      for j in range(N):
          for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 우 하 좌 상 순서
              ni = i + di
              nj = j + dj
              if 0 <= ni < N and 0 <= nj < N: #유효 인덱스
                  print(i, j, arr[ni][nj])
  
          print()
  ```

* 전치 행렬 (transpose)
  * 행과 열의 좌표를 바꿔주는 것

```python
# i : 행의 좌표
# j : 열의 좌표
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



* 부분집합
  * 공집합, 진부분집합(나 자신을 뺀 부분집합)
  * 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.



* 비트 연산자

  * 1 bit (0 or 1) --> 8 bit = 1 byte

  * ```python
    & #=> 비트 단위로 and 연산을 한다.
    | #=> 비트 단위로 or 연산을 한다.
    << #=> 피연산자의 비트 열을 인쪽으로 이동시킨다.
    >> #=> 피연산자의 비트 열을 오른쪽으로 이동시킨다.
    ```

  * `i&(1<<j)` i의 j번째 비트가 1인지 아닌지를 리턴한다



* 이진 검색(Binary Search) :star: **up down 게임**