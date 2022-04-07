from collections import deque
from pprint import pprint


N, K = map(int, input().split())  # 행렬의 크기 N, 세균의 개수 1 ~ K개
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = []  # 바이러스 번호 낮은애들부터 퍼뜨릴거야
S, X, Y = map(int, input().split())  # S초 뒤 위치 (X, Y) 의 세균 종류

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            virus.append([matrix[i][j], i, j, 0])  # virus num, row, col, time
virus.sort()
q = deque(virus)
# pprint(matrix)
# pprint(virus)

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# pprint(virus)

# q가 빌 때까지 반복해줘
while q:
    # 바이러스 크기 작은애들부터 순서대로 한번씩 퍼뜨려줘
    v, r, c, t = q.popleft()
    # 근데 만약에 주어진 시간 다 쓰면 끝이야
    if t == S:
        break
    # 아직 시간이 남았다면, 바이러스 퍼뜨려줘
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        # 만약 탐색 지점이 범위 내에 존재하고, visited == 0 이거나, 나보다 더 큰 바이러스가 있는 경우에는 내가 차지할거얌
        if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
            visited[rr][cc] = v
            virus.append([v, rr, cc, t+1])


print(visited[X-1][Y-1])


