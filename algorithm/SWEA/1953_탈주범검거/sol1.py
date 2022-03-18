from collections import deque
import sys
from pprint import pprint

sys.stdin = open('theif.txt')

def bfs(i, j, time):
    q = deque()
    q.append([i, j])  # 시작 지점 인덱스
    visited[i][j] = 1
    time -= 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc]


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    # delta 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 터널 구조물 타입마다 갈 수 있는 위치
    '''
    type 1 = 상 하 좌 우
    type 2 = 상 하
    type 3 = 좌 우
    type 4 = 상 우
    type 5 = 하 우
    type 6 = 하 좌
    type 7 = 상 좌
    '''


    pprint(matrix)
    
    print(f'#{tc} ')

