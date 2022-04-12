''' fail ...! '''
from collections import deque
from pprint import pprint


def bfs(i, j, visited):
    q = deque()
    q.append([i, j])
    melting_q = deque()  # 빙하가 녹는 위치와 얼마나 녹았는지를 저장해줄 큐
    visited[i][j] = 1

    while q:
        r, c = q.popleft()
        melt_cnt = 0
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 있고, 아직 방문을 안한 경우인데,
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc]:
                # 아직 빙산이 다 녹지 않아서 남아있는 곳이라면
                if matrix[rr][cc] != 0:
                    visited[rr][cc] = 1  # 방문 체크 하고
                    q.append([rr, cc])  # 큐에 넣어줘
                # 만약 네 방향 모두 탐색 했는데 모두 0이라면 다 녹아버린거야
                else:
                    melt_cnt += 1
        if melt_cnt:
            melting_q.append([r, c, melt_cnt])

    return melting_q


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

time = 0  # 시간 얼마나 지났는지 세어 줄 변수 초기화

while True:
    ice = 0  # 빙산의 개수 세어줄 변수 초기화
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 빙하이면서 아직 방문한 적이 없다면,
            if matrix[i][j] != 0 and not visited:
                ice += 1  # 빙산 개수 +1 해주고
                melt = bfs(i, j, visited)  # bfs 돌려서 얼음 녹여주자

                while melt:
                    x, y, k = melt.popleft()
                    matrix[x][y] = max(matrix[x][y]-k, 0)

    if ice == 0:
        time = 0
        break
    if ice >= 2:
        break
    time += 1

print(time)