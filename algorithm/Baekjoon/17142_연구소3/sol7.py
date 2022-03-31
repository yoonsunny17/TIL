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
            # 탐색 경로가 범위 내에 존재하고, 0이면서, 아직 방문한 적 없으면,
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 0 and not visited[rr][cc]:
                aisle -= 1  # 통로 개수 하나 빼구
                visited[rr][cc] = visited[r][c] + 1  # 방문 기록이자 걸린 시간을 기록하고
                q.append([rr, cc])  # 탐색 경로 넣어주자

            # 탐색 경로가 범위 내에 존재하고, 벽이 아니면서, 아직 방문한 적 없으면,
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] == 2 and not visited[rr][cc]:
                aisle -= 1
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])
                if aisle == 0:
                    return visited[rr][cc], aisle

    return visited[r][c] - 1, aisle


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 통로 세어 줄 변수 초기화: 0인것만 세어주자
aisle = N**2 - M
# 바이러스가 들어갈 수 있는 자리 모아 둘 리스트
virus = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            aisle -= 1
        if matrix[i][j] == 2:
            virus.append([i, j])

# 최솟값 갱신해 줄 변수 초기화
min_time = 987654321
# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

temp = aisle
# virus에서 M개만큼 뽑아서 조합을 이뤄보자!
for start in combinations(virus, M):
    aisle = temp
    visited = [[0]*N for _ in range(N)]
    # 이제 여기서 bfs 돌리면 되는데...
    time, left_aisle = bfs(start)

    if left_aisle == 0 and time < min_time:
        min_time = time

if min_time == 987654321:
    print(-1)
else:
    print(min_time)

