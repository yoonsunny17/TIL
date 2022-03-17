from collections import deque
from pprint import pprint

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
distance = [[0]*C for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

water = deque()

def bfs_1():
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '*':
                water.append([i, j])

    while water:
        r, c = water.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 있고,
            if 0 <= rr < R and 0 <= cc < C


