'''
dfs로 풀어보자!!!!
'''

import sys
from collections import deque
from pprint import pprint

sys.stdin = open('cafe.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 방문 기록 확인할 리스트
    visited = [[0]*N for _ in range(N)]

    # delta 대각선
    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]

    # 출발지점 규칙! y = x 로 행렬을 잘랐을 때 좌측에 있는 지점들에서만 출발 할 것
    # N x N 행렬일 때; (1,0), (0,1), ... , (N-2,0), (0,N-2)
    start = deque()
    for i in range(1, N-1):
        start.extend([[i, 0], [0, i]])

    while start:
        r, c = start.popleft()
        visited[r][c] = 1
        # 같은 종류의 카페 들렸는지 확인해 줄 스택 만들기
        same = deque()
        same.append(matrix[r][c])

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            while True:
                # 탐색 지점이 벗어나는 경우 멈춰!
                if not (0 <= rr <= N) and not (0 <= cc <= N):
                    same = []
                    break
                if


    # def bfs_row():
    #     while start:
    #         r = start.popleft()
    #         c = 0
    #         matrix[r][c] = 1
    #         visited[r][0] = 1
    #
    #         for i in range(4):
    #             rr = r + dr[i]
    #             cc = c + dc[i]


    # def bfs_row():
    #     start = deque()
    #     start.append(matrix[1][0])
    #     visited[1][0] = 1
    #     same.append(matrix[1][0])
    #     while start:
    #         r = start.popleft()
    #         c = 0
    #         for i in range(4):
    #             rr = r + dr[i]
    #             cc = c + dc[i]
    #             if 0 <= rr <= N and 0 <= cc <= N and not visited[rr][cc]:




    # pprint(matrix)
    # print(f'#{tc} ')

