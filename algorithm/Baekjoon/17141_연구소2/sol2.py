from collections import deque
from itertools import combinations
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# 0 : 바이러스가 퍼질 수 있는 곳
# 1 : 벽, 바이러스가 퍼질 수 없음
# 2 : 바이러스의 초기 위치가 될 수 있음

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

start = []
# 벽인 부분은 헷갈리지 않도록 -1로 바꿔주자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = -1
        elif matrix[i][j] == 2:
            start.append([i, j])

virus = deque(list(combinations(start, M)))
# M개의 바이러스 위치에 대해서, 한 자리씩 bfs 한번씩 돌려주자
# 하나씩 돌릴때마다, 바이러스 퍼질 수 있는 위치는 0인 곳만 가능하다는 조건으로 설정
# 돌리고 나서, 각 행렬 요소 하나씩 돌면서 최솟값으로 갱신해줘 (visited 행렬로 하자)
# 그리고 바이러스 개수만큼 다 끝났으면 그 행렬에서 최댓값을 뽑아줘
# 이거를 deque 요소 개수만큼 (조합 개수만큼) 반복하면 되지 않을까?
# pprint(virus)

for i in range(len(virus)):
    repeat = virus.popleft()

    for j in range(len(repeat)):
        v = repeat[i]

        print(v)

def bfs():
    q = deque()
    q.append([row, col])  # 초기위치
    visited[row][col] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dr[i]
            if 0 <= rr < N and 0 <= cc < N and not matrix[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1
                q.append([rr, cc])

    return visited



# while virus:
#     v1, v2, v3 = virus.popleft()
#     # print(v1, v2, v3)
#     # 각각에 대해서 bfs를 돌리면 될거같은뎅
#     for i in range(4):

    
# pprint(start)
# pprint(virus)
# pprint(matrix)
# print('===============')
