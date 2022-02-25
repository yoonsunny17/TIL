from pprint import pprint
from collections import deque
import sys

sys.stdin = open('maze.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)] # 방문기록 넣어 줄 이차원 리스트 만들어두기

    # start 지점 어디인지 찾고 시작!
    start = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]

    # 탐색 가능한 방향; 하 상 우 좌
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # dfs를 통해 미로 완전 탐색!!
    def dfs():
        stack = deque([[start[0], start[1]]])
        visited[start[0]][start[1]] = 1 # 방문한 곳에 1로 표시해주기
        while stack: # stack이 not empty면 True!
            r, c = stack.pop() # stack이 차있는 동안 r,c를 stack에서 pop 해주자
            for i in range(4): # delta 돌꺼야
                rr = r + dr[i]
                cc = c + dc[i]
                # rr과 cc가 range 내에 있고, 도착 지점을 만났다면,
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] == 3:
                    return True # True를 반환해줘!!

                # rr과 cc가 range 내에 있고, 벽도 아니면서, 아직 방문한 기록이 없다면,
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] != 1 and not visited[rr][cc]:
                    stack.append([rr, cc]) # stack에 현 지점을 push해주고
                    visited[rr][cc] = 1 # 방문 기록을 남겨줘

        return False

    print(f'#{tc} {int(dfs())}')


