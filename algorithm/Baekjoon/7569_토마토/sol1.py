from collections import deque
from pprint import pprint

M, N, H = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
matrix = []
for _ in range(H):
    matrix.append(box)

# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             print(matrix[])
# # 삼차원 방문 리스트 만들기
# visited = [[[0]*M for _ in range(N)] for _ in range(H)]
# # pprint(visited)
#
# # dx, dy, dx 상 하 좌 우 앞 뒤 표현해주기 (dx; M-axis, dy; N-axis, dz; H-axis)
# dx = [0, 0, 0, 0, 1, -1]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [1, -1, 0, 0, 0, 0]
#
# # 너비우선탐색
# def bfs():
#     q = deque()
#     # 시작지점 찾아줘! = 익은 토마토의 위치를 찾아줘!
#     for i in range(H):
#         for j in range(N):
#             for k in range(M):
#                 if matrix[i][j][k] == 1:
#                     q.append([i, j, k])
#                     # visited[i][j][k] = 1
#
#     while q:
#         x, y, z = q.popleft()
#         # 3차원 delta 탐색
#         for i in range(6):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             zz = z + dz[i]
#             # 탐색한 지점이 범위 내에 있으면서 안익은 토마토가 있는 곳이라면,
#             if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and matrix[zz][yy][xx] == 0:
#                 # 토마토를 익혀주고 며칠 걸렸는지 세어주자
#                 matrix[zz][yy][xx] = matrix[z][y][x] + 1
#                 # 그리고 큐에 경로 넣어줘
#                 q.append([zz, yy, xx])
#
#     return matrix
#
#
# bfs()
# print(matrix)


# for _ in range(H):
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*M for _ in range(N)]
#
#     # dx, dy, dz (dx; M-axis, dy; N-axis, dz; H-axis)
#     # 상 하 좌 우 앞 뒤
#     dx = [0, 0, 0, 0, 1, -1]
#     dy = [0, 0, -1, 1, 0, 0]
#     dz = [1, -1, 0, 0, 0, 0]
#
#     for i in range(H):
#         for j in range(N):
#             for k in range(M):
#
#
#     def bfs():
#         q = deque()


# for _ in range(H):
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0]*M for _ in range(N)]
#     # dx, dy, dz 정의하면 되겠징
#     # dx = M, dy = N, dz = H
#     # delta 상 하 좌 우 앞 뒤
#     dx = [0, 0, 0, 0, 1, -1]
#     dy = [0, 0, -1, 1, 0, 0]
#     dz = [1, -1, 0, 0, 0, 0]
#
#     def bfs():
#         q = deque()
#         for i in rang



