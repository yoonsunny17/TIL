import sys
from pprint import pprint
from collections import deque
sys.setrecursionlimit(100000)


def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


N = int(input())
M = int(input())
matrix = [[0] + list(map(int, input().split())) for _ in range(N+1)]
plan = list(map(int, input().split()))
# 1번부터 N번까지 각자를 부모로 가지도록 초기화
parent = [x for x in range(1, N+1)]

for i in range(N):
    for j in range(N):
        # 서로 연결이 되어있는데, 부모가 동일하게 설정되어 있지 않으면 합쳐줘
        if matrix[i][j] == 1 and find(i) != find(j):
            union(i, j)

print(parent)


pprint(matrix)
print(plan)