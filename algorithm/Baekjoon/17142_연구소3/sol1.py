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
            # if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and matrix[rr][cc] != '-':
            #     if matrix[rr][cc] == 0:
            #         visited[rr][cc] = visited[r][c] + 1
            #     if matrix[rr][cc] == 2:
            #         visited[rr][cc] = visited[r][c]
            #     q.append([rr, cc])
            #     aisle -= 1

            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 0 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])
                aisle -= 1

            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 2 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1  # 둘 다 1 누적 시키는걸로? .. 벽이 아닌 경우
                q.append([rr, cc])
                # aisle -= 1

    # 바이러스 시작 지점이 1 이니까 1 빼줘서 반환해줘
    return visited[r][c] - 1, aisle, [r, c]


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 위치
# visited = [[0]*N for _ in range(N)]
min_time = 987654321

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스가 출발할 수 있는 위치들 넣어줄 list
virus = []

# 비활성화 바이러스도 바이러스가 있다고 생각해주자
# aisle = N*N - M
aisle = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = '-'
            # aisle -= 1
        elif matrix[i][j] == 2:
            virus.append([i, j])

        else:
            aisle += 1

tmp = aisle
for start in combinations(virus, M):
    aisle = tmp
    visited = [[0]*N for _ in range(N)]

    if aisle >= 1:
        time, numb, end_point = bfs(start)
        print('=======visited=======')
        pprint(visited)
        print(numb, end_point)
        print('=======end========')
        print()

        if numb == 0 and time < min_time:
            min_time = time
        print('******answer*******')

if not aisle and min_time == 987654321:
    print(-1)

elif aisle == 0:
    print(0)

else:
    print(min_time)
