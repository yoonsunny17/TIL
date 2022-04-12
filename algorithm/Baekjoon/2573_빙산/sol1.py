''' 형진오빠 코드 참고 '''
from collections import deque

def bfs():
    global time
    while True:
        q = deque()
        visited = [[0]*M for _ in range(N)]
        ice = 0  # 빙산 개수 세어줄 변수 초기화
        time += 1  # 시간 얼마나 지났는지 세어줄거임
        
        for r in range(N):
            for c in range(M):
                # 만약 빙산인 지점이라면, 네방향 탐색하면서 주변에 0이 있는지 보자
                if matrix[r][c]:
                    for i in range(4):
                        rr = r + dr[i]
                        cc = c + dc[i]
                        # 탐색 지점이 범위 내에 있고, 0이 붙어있는 빙산이라면, 빙산을 일단 큐에 넣어줘 (나중에 녹일것)
                        if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc]:
                            q.append([r, c])

                # 빙하끼리 붙어있는지 확인해볼거야
                if matrix[r][c] and not visited[r][c]:
                    q2 = deque()
                    q2.append([r, c])
                    ice += 1
                    visited[r][c] = ice
                    while q2:
                        r, c = q2.popleft()
                        for i in range(4):
                            rr = r + dr[i]
                            cc = c + dc[i]
                            # 탐색 지점이 범위 내에 존재하고, 빙산이면서, 아직 방문한 적이 없는 곳이면
                            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] and not visited[rr][cc]:
                                # 방문 기록에 몇번째 덩어리인지 체크해주고, 다음 탐색 경로에 넣어주겟어
                                visited[rr][cc] = ice
                                q2.append([rr, cc])

        # 0 과 인접해있던 빙하들 한꺼번에 녹여주자
        while q:
            m, n = q.pop()
            if matrix[m][n] > 0:
                matrix[m][n] -= 1

        # matrix[r][c]값이 없으면 time = 0 반환..
        if not ice:
            time = 0
            return

        # 빙산 덩어리가 두개 이상 분리되면 경과된 시간 -1 반환해
        if ice >= 2:
            time -= 1
            return


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# pprint(matrix)

# 빙산 주변의 상 하 좌 우 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
time = 0
bfs()
print(time)

