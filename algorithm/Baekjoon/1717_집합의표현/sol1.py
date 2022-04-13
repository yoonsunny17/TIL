import sys
from collections import deque
sys.setrecursionlimit(100000)
from pprint import pprint


# 서로소인 집합을 합해주자
def union(x, y):
    i = find(x)
    j = find(y)

    parent[max(i, j)] = min(i, j)


# 부모를 찾자
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
parent = [x for x in range(n+1)]  # 0 부터 n까지 !
# 선입선출
q = deque(info)

while q:
    # check = 0 or 1, a 와 b 는 집합 숫자를 의미
    # check = 0 일 때 union 함수 돌리고,, 1일 때 find 함수 돌리기!
    check, a, b = q.popleft()
    if check == 0:
        union(a, b)
    if check == 1:
        if find(a) != find(b):
            print('NO')
        else:
            print('YES')