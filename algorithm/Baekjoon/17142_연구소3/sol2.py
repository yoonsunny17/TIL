'''fail....!'''
from collections import deque
from pprint import pprint
from itertools import combinations

def bfs(elem):
    global aisle

    q = deque(elem)
    for k in q:
        visited[k[0]][k[1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] != 1 and not visited[rr][cc]:
                aisle -= 1
                if matrix[rr][cc] == 2 and aisle == 0:
                    return visited[r][c], aisle, [r, c]
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])
            # if 0 <= rr < N and 0 <= cc < N and not matrix[rr][cc] and not visited[rr][cc]:
            #     aisle -= 1
            #     visited[rr][cc] = visited[r][c] + 1
            #     q.append([rr, cc])
            #
            # if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 2 and not visited[rr][cc]:
            #     aisle -= 1
            #     if aisle == 0:
            #         return visited[r][c] - 1, aisle, [r, c]
            #     visited[rr][cc] = visited[r][c] + 1
            #     q.append([rr, cc])

    # 바이러스 시작 지점이 1 이니까 1 빼줘서 반환해줘
    return visited[r][c] - 1, aisle, [r, c]


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

min_time = 987654321

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

virus = []

aisle = N*N - M
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = '-'
            aisle -= 1
        elif matrix[i][j] == 2:
            virus.append([i, j])

tmp = aisle
for start in combinations(virus, M):
    aisle = tmp
    visited = [[0]*N for _ in range(N)]

    time, numb, end_point = bfs(start)

    print('=======start=======')
    pprint(visited)
    print('=======end=======')
    print()

    if numb == 0 and time < min_time:
        min_time = time

if min_time == 987654321:
    print(-1)
else:
    print(min_time)