# 우선순위 큐 (heap)

 

**우선순위큐** : pop을 했을 때 우선순위가 제일 낮은 것이 pop이 되는 것

힙 트리 : heappop : 힙의 최솟값을 반환하는 함수, O(logN)

```python
from heapq import heappush, heappop

q = []

# q에 숫자를 집어넣는 방법
heappush(q, 10)
heappush(q, 5)
heappush(q, 8)
...
print(q) # q의 맨 앞이 가장 작은 수가 나옴 (그 다음 수들은 우선순위 없음)

while q:
	print(heappop(q))
    # q 안에서 가장 작은 애를 출력해줘
```



**다익스트라 알고리즘 최적화 => heapq 사용해서 할 수 있음~!!!!!!**

