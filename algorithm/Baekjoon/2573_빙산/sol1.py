from collections import deque
from pprint import pprint


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# pprint(matrix)

# 빙산 주변의 상 하 좌 우 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0이 아닌 곳 만나면 녹을 수 있는지 확인해보기
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            