from collections import deque
from pprint import pprint


def bfs(r, c, cnt):
    q = deque()
    q.append([r, c])
    # 시작 지점의 요소가 1이면 visited 1 넣어줘
    visited[r][c] = 1
    cnt += 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N:
                if matrix[rr][cc] == 1 and not visited[rr][cc]:
                    visited[rr][cc] = visited[r][c] + 1
                    cnt += 1
                    q.append([rr, cc])
                else:
                    q.append([rr, cc])
                    # pprint(visited)

    return cnt


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# pprint(matrix)


# print(bfs(0))
rlt = []
visited = [[0]*N for _ in range(N)]
max_numb = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            numb = bfs(i, j, 0)
            if numb > max_numb:
                max_numb = numb
                rlt.append(max_numb)

print(rlt)


# print(f'{len(sorted(rlt))}')
# for i in sorted(rlt):
#     print(i)

