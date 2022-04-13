import sys
from pprint import pprint
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
matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

# matrix idx에 맞게 0 ~ N-1 parent 리스트 초기화 해주자
parent = [x for x in range(N)]

for i in range(N):
    for j in range(N):
        # 두 도시가 연결되어있는데 아직 find 함수가 같지 않으면 union 돌려줘
        if matrix[i][j] and find(i) != find(j):
            union(i, j)

# 연결되어있는 도시에 대해 union-find 다 돌리고 나서, 연결되어 있는 루트대로 여행을 한다면,
# 여행 계획 루트의 부모는 모두 동일할 것이고, 아니라면 다를 것이야
rlt = set()
for k in range(M):
    rlt.add(parent[plan[k] - 1])
# print(len(rlt))

if len(rlt) == 1:
    print('YES')
else:
    print('NO')