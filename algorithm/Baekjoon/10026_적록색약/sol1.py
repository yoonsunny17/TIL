from collections import deque
from pprint import pprint

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



# 색약이 아닌경우
def bfs_1():
    cnt_1 = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 아직 방문한 적이 없는데
            if 0 <= rr < N and 0 <= cc < N and colors[rr][cc] == colors[r][c] and not visited[rr][cc]:
                # 그 지점이 동일한 색이라면 방문 체크 후 경로에 추가해줘
                visited[rr][cc] = 1
                q.append([rr, cc])
            # 동일한 색이 아니라면 영역 카운트 해줘
            cnt_1 += 1

    return cnt_1

# 색약인 경우 G와 R 구분이 안됨
def bfs_2(matrix):
    cnt_2 = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dr[i]
            # 탐색 지점이 범위 내에 존재하고, 아직 방문한 적이 없는데
            if 0 <= rr < N and 0 <= cc < N and colors[rr][cc] == colors[r][c] and not visited[rr][cc]:
                visited[rr][cc] = 1
                q.append([rr, cc])
            cnt_2 += 1

    return cnt_2


N = int(input())
colors = [list(input()) for _ in range(N)]
# 방문기록 남길 리스트와 empty queue 생성
visited = [[0]*N for _ in range(N)]
q = deque()
q.append([0, 0])
visited[0][0] = 1

rlt_1 = bfs_1()

for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'
            rlt_2 = bfs_2(colors)

print(rlt_1, rlt_2)