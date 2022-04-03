from collections import deque
from pprint import pprint


def bfs(x, y, graph):
    q = deque()
    q.append([x, y])
    cnt = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # if 0 > rr or N <= rr or 0 > cc or N <= cc:
            #     continue
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 1:
                matrix[rr][cc] = 0
                q.append([rr, cc])
                cnt += 1

    return cnt


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# pprint(matrix)

rlt = []  # 결과값 받아줄 리스트 최종 출력해줄 것

# 1인 경우 bfs를 돌리기
max_numb = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            numb = bfs(i, j, matrix)
            if numb == 1:
                rlt.append(1)
            else:
                rlt.append(numb-1)

rlt.sort()

print(len(rlt))
for i in rlt:
    print(i)