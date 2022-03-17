from collections import deque
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# pprint(matrix)

# delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 0]

def bfs():
    # empty queue 만들고, 시작은 무조건 0,0에서 시작한다
    q = deque()
    q.append([0, 0])
    # 방문기록, 치즈위치 확인해줄 리스트 각각 만들기
    visited = [[0]*M for _ in range(N)]
    cheese = [[0]*M for _ in range(N)]
    melt = 0
    melt_lst = []
    # 시작지점 방문기록에 기록해주기
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하는 경우, 그 지점이 빈 자리이고 아직 방문하지 않은 자리라면,
            if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc] and not visited[rr][cc]:
                # 경로에 넣고, 방문 기록을 남기자
                q.append([rr, cc])
                visited[rr][cc] = 1
            # 탐색 지점에 치즈가 있다면,
            elif 0 <= rr < N and 0 <= cc < M and matrix[rr][cc]:
                # 치즈 발견했음 +1 체크하자
                cheese[rr][cc] += 1

        # cheese matrix에서 값이 2 이상이라면 녹을 수 있어
        for i in range(N):
            for j in range(M):
                if cheese[i][j] >= 2:
                    melt += 1 # 녹은 치즈 개수 세어주고,
                    cheese[i][j] = 0  # 치즈를 녹여주고
                    visited[i][j] = 1  # 방문기록 남겨주고

    return cheese


pprint(bfs())