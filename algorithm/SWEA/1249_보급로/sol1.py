''' BFS 변형 '''
''' 최소 가중치를 갱신해 나가는 방향으로 풀어나가자! '''
from collections import deque
from pprint import pprint
import sys

sys.stdin = open('supply.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # delta 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dr[i]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                visited[rr][cc] = 1
                q.append([rr, cc])


            # if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and matrix[rr][cc] != matrix[N - 1][N - 1]:
            #     visited[rr][cc] = 1
            #     q.append([rr, cc])
            #     cnt += matrix[rr][cc]
            # if rr == N - 1 and cc == N - 1:


    # print(f'#{tc} ')

