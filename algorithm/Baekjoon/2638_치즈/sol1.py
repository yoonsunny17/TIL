from collections import deque
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우 delta 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    # empty queue 생성 후 시작지점 넣어주기
    q = deque()
    # 가장자리에는 치즈가 놓이지 않으므로 matrix[0][0]부터 탐색 시작하기
    q.append([0, 0])
    # 방문기록 남겨줄 이차원 리스트, 치즈 있는 위치 체크할 이차원 리스트 만들어주기
    visited = [[0] * M for _ in range(N)]
    cheese = [[0] * M for _ in range(N)]
    # 방명록 남기고~
    visited[0][0] = 1

    # q가 빌 때까지 반복하자
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 있고, 빈 자리이며 아직 방문한 적 없으면,
            if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc] and not visited[rr][cc]:
                # 방문 기록을 남겨주고, q에 경로를 남겨줘
                visited[rr][cc] = 1
                q.append([rr, cc])
            # 탐색 지점이 범위 내에 있는데, 치즈인 부분이라면,
            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc]:
                # 치즈가 있다는 것을 체크해주자
                cheese[rr][cc] += 1

    # 녹는 치즈 개수 세어줄 변수
    melt = 0
    # 만약 cheese matrix에서 값이 2 이상인 부분이라면 녹을 수 있어!
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 2:
                melt += 1
                cheese[i][j] = 0
                visited[i][j] = 1
                matrix[i][j] = 0 # 치즈를 녹였으니 빈부분이 되었다는 것을 matrix에도 표시해줘야해!!!

    return melt


time = -1
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time)