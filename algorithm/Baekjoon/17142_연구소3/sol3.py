from collections import deque
from pprint import pprint
from itertools import combinations

def bfs(elem):
    global aisle
    visited = [[0] * N for _ in range(N)]
    q = deque(elem)
    for k in q:
        visited[k[0]][k[1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 안에 존재하고, 벽이 아니면서, 아직 방문한 적이 없다면
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] != 1 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1 # 방문기록 및 시간 기록해주자
                if matrix[rr][cc] == 0:  # 그리고 만약에 탐색 지점이 통로라면,
                    aisle -= 1
                    matrix[rr][cc] = 2
                    q.append([rr, cc])
                if matrix[rr][cc] == 2:
                    q.append([rr, cc])

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0 and visited[i][j] == 0:
                return -1

    return visited[rr][cc] - 1



N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
min_time = 987654321
# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 바이러스가 들어갈 수 있는 자리 모아 둘 리스트
virus = []
# 통로 세어 줄 변수 초기화: 0인것만 세어주자
aisle = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            aisle += 1
        if matrix[i][j] == 2:
            virus.append([i, j])

temp = aisle
# virus에서 M개만큼 뽑아서 조합을 이뤄보자!
for start in combinations(virus, M):
    aisle = temp
    time = bfs(start)

    if aisle == 0 and time < min_time:
        min_time = time

if min_time == 987654321:
    print(-1)
else:
    print(min_time)