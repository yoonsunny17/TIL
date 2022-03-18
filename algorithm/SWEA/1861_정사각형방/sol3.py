import sys
from collections import deque

sys.stdin = open('square.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    q = deque()
    room = deque()

    q.append([row, col])
    visited[row][col] = 1
    room.append(matrix[row][col])

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and abs(matrix[rr][cc] - matrix[r][c]):
                q.append([rr, cc])
                visited[rr][cc] = 1
                room.append(matrix[rr][cc])

    return min(room), len(room)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    numb = N + 1
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp_num, temp_cnt = bfs(i, j)
                if cnt < temp_cnt:
                    cnt = temp_cnt
                    numb = temp_num
                elif cnt == temp_cnt and numb > temp_num:
                    numb = temp_num

    print(f'#{tc} {numb} {cnt}')

