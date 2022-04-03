from collections import deque
from itertools import combinations
from pprint import pprint

N, M = map(int, input().split())  # N = 세로 크기, M = 가로 크기
row, col, dire = map(int, input().split())  # (r, c), d
matrix = [list(map(int, input().split())) for _ in range(N)]

# d = 방향 [0: 북, 1: 동, 2: 남, 3: 서]
# delta // default가 왼쪽 방향으로 도는거라고 했으니까 반시계 방향으로 써주자
# 0 3 2 1 (북 서 남 동)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

print(robot)

# def dfs():
#     cleaning = deque()
#     cleaning.append(robot)
#     visited = [[0]*M for _ in range(N)]
#     # 로봇 초기 위치 방문처리 해주자
#     visited[robot[0]][robot[1]] = 1
#
#     while cleaning:
#         r, c, d = cleaning.pop()
#         # 현재 위치 기준으로 왼쪽으로 회전해줘
#         rr = r + dr[d+1]
#         cc = c + dc[d+1]
#         # case 2-a) 그 자리가 범위 밖을 벗어나지 않고, 빈 칸인데, 아직 청소가 되어있지 않은 부분이라면,
#         if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc] and not visited[rr][cc]:
#             visited[rr][cc] = visited[r][c] + 1  # 청소했다고 기록해주고
#             # cleaning.append([rr, cc, d+1])  # 다음 청소할 곳을 찾게 경로에 넣어줘
#         # case 2-c) 네 방향 모두 청소가 되어있거나, 벽인 경우에는 d 유지하면서 한칸 물러서자
#         if 0 <= rr < N and 0 <= cc < N and (matrix[rr][cc] == 1 or visited[rr][cc] != 0):

def dfs(r, c, d):
    cleaning = deque()
    cleaning.append([r, c, d])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1

    # 현재 위치의 왼쪽을 탐색해보자
    # rr = r + dr[d+1]
    # cc = c + dr[d+1]
    while cleaning:
        r, c, d = cleaning.popleft()
        rr = r + dr[d+1]
        cc = c + dc[d+1]
        # case 2-a) 탐색 방향이 범위 내에 존재하고, 청소 해야할 구간인데, 아직 청소한 적 없으면
        if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc] and not visited[rr][cc]:
            visited[rr][cc] = visited[r][c] + 1  # 청소해줘

            # if matrix[rr][cc] == 1:
            #     break
            # visited[rr][cc] = visited[r][c] + 1
                


            
            
            
            
            
        # for i in range(4):
            # rr = r + dr[i]
            # cc = c + dc[i]