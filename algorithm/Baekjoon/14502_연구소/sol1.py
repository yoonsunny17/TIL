from collections import deque
from pprint import pprint
from itertools import combinations


# 각 경우에 대해 벽으로 바꾸는 함수 만들어주자
def change_wall(aisle):
    for one in aisle:
        matrix[one[0]][one[1]] = 1


# 바이러스 퍼지는거 봐야해
def bfs(start, aisle):

    q = deque()
    q.append(start[0])
    visited = [[0]*M for _ in range(N)]
    visited[start[0][0]][start[0][1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 존재하고, 방문한 적 없으면서, 빈칸인 경우
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc] and not matrix[rr][cc]:
                # 바이러스 퍼뜨리자
                matrix[rr][cc] = 2
                visited[rr][cc] = 1
                aisle -= 1
                q.append([rr, cc])

    return aisle


N, M = map(int, input().split())  # N = 세로 길이, M = 가로 길이
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 위치
max_cnt = 0  # 최댓값 갱신할 변수 초기화
cnt = 0
# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스 위치 찾자
virus = []
# 벽 설치할 수 있는 위치 찾자
walls = []
zero = -3  # 벽 3개 설치 고려
for i in range(N):
    for j in range(M):
        # 만약 빈 칸인 곳이라면, 벽 설치 가능~
        if matrix[i][j] == 0:
            zero += 1
            walls.append([i, j])
        # 바이러스 위치 찾아줘 bfs 돌려야돼
        if matrix[i][j] == 2:
            virus.append([i, j])

rlt = []
# 다 찾았으면 거기서 벽 설치할 위치 3개 뽑아줘
for install in combinations(walls, 3):
    # 그리고 각각을 벽으로 바꿔보고, 바이러스에 대해 bfs 돌려보자
    # print(install)
    rlt.append(install)
    # change_wall(install)
print(rlt)

for change in rlt:
    change_wall(change)
    # 벽 설치 했으면, 바이러스 애들 bfs 돌리자
    # rlt.append(bfs(virus, zero))

# print(rlt)

# pprint(matrix)
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] == 0:
#                 cnt += 1
#
#     rlt.append(cnt)
#
# print(rlt)


