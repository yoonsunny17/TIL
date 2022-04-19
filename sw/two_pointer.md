# two pointer algorithm

```python
# BOJ
3273, 2470, 1806, 1644(+2960 에라토스테네스의 체)
```



**배열의 인덱스를 가리키는 2개의 포인터를 설정하고, 이를 옮겨가며 내가 원하는 값을 찾는 알고리즘**

리스트에 담긴 데이터에 순차적으로 접근해야 할 때는 **시작점과 끝점 즉, 2개의 점**으로 접근할 데이터의 범위를 표현할 수 있다

* 투 포인터 알고리즘의 동작 과정
  1. 시작점 (start)과 끝점 (end)이 첫 번째 원소의 인덱스(0)을 가리키도록 한다
  2. 현재 부분의 합이 **M과 동일**하다면 **count**한다
  3. 현재 부분 합이 **M보다 작다**면 **end를 1 증가**시킨다
  4. 현재 부분 합이 **M보다 크다**면 **start를 1 증가**시킨다
  5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정을 반복한다

* 투 포인터 알고리즘 예제

  ```python
  # 데이터의 개수 N, 찾고자 하는 부분 합 M
  N, M = 5, 5
  # 전체 수열
  arr = [1, 2, 3, 4, 5]
  
  count = 0  # 부분합이 M일 때 +1 해줄 변수
  interval_sum = 0  # 중간 과정마다 더해나갈 변수
  end = 0  # end pointer
  
  # start를 차례대로 증가시키면서 반복
  for start in range(N):
      # end를 범위 내에서 가능한 만큼 이동시키기
      # 중간 합이 M보다 작고, end pointer가 N보다 작은 동안 반복 가능
      while interval_sum < M and end < N:
          interval_sum += arr[end]  # 중간 합 누적해주고
          end += 1  # end pointer 하나씩 왼쪽에서 오른쪽으로 이동해주기
          
      # 부분 합이 M인 경우 cnt +1 
      if interval_sum == M:
          count += 1
      # start pointer 옮기기 전에 값은 빼주기 (start pointer를 이동시켜야 하므로)
      interval_sum -= data[start]
  
  print(count)
  ```

  



********

case 1. 두 수의 합

case 2. 구간 합