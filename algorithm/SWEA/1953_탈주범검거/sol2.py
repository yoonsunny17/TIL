from collections import deque
import sys
from pprint import pprint

sys.stdin = open('theif.txt')
'''
type 1 = 상 하 좌 우
type 2 = 상 하
type 3 = 좌 우
type 4 = 상 우
type 5 = 하 우
type 6 = 하 좌
type 7 = 상 좌
'''


def bfs(row, col, run):
    q = deque()
    q.append([row, col])
    visited[row][col] = 1
    time = 0

    while q:
        time += 1
        r, c = q.popleft()
        if time > run:
            break
        # if time < 0:
        #     break

        if matrix[r][c] == 1:
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M:
                    if matrix[rr][cc] != 0:
                        visited[rr][cc] = 1
                        q.append([rr, cc])
        # 3 x
        if matrix[r][c] == 2:
            dr = [-1, 1]
            dc = [0, 0]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0 and matrix[rr][cc] != 3:
                    # if matrix[rr][cc] != 0 and matrix[rr][cc] != 3:
                    visited[rr][cc] = 1
                    q.append([rr, cc])
        # 2 x
        if matrix[r][c] == 3:
            dr = [0, 0]
            dc = [-1, 1]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0 and matrix[rr][cc] != 2:
                    # if matrix[rr][cc] != 0 and matrix[rr][cc] != 2:
                    visited[rr][cc] = 1
                    q.append([rr, cc])
        # 4 x
        if matrix[r][c] == 4:
            dr = [-1, 0]
            dc = [0, 1]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0 and matrix[rr][cc] != 4:
                    # if matrix[rr][cc] != 0 and matrix[rr][cc] != 4:
                    visited[rr][cc] = 1
                    q.append([rr, cc])
        # 5 x
        if matrix[r][c] == 5:
            dr = [1, 0]
            dc = [0, 1]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0 and matrix[rr][cc] != 5:
                    # if matrix[rr][cc] != 0 and matrix[rr][cc] != 5:
                    visited[rr][cc] = 1
                    q.append([rr, cc])

        if matrix[r][c] == 6:
            dr = [1, 0]
            dc = [0, -1]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0:
                    # if matrix[rr][cc] != 0:
                    visited[rr][cc] = 1
                    q.append([rr, cc])

        if matrix[r][c] == 7:
            dr = [-1, 0]
            dc = [0, -1]
            for i in range(2):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] != 0:
                    # if matrix[rr][cc] != 0:
                    visited[rr][cc] = 1
                    q.append([rr, cc])

    return sum(sum(visited, []))
    # return visited, time, matrix[row][col]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    pprint(bfs(R, C, L))

    # pprint(visited)
    # while True:
    #     L -= 1
    #     cnt = bfs(R, C, L)
    #     if L == 0:
    #         break
    # print(cnt)

    # pprint(visited)
    # print(f'============{sum(sum(visited,[]))}==============')

    # print(f'#{tc} ')

