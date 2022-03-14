from collections import deque
from pprint import pprint

M, N, H = map(int, input().split())

box = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

# dx, dy, dx 상 하 좌 우 앞 뒤 표현해주기 (dx; M-axis, dy; N-axis, dz; H-axis)
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i, j, k])

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            xx = x + dx[i]
            yy = y + dy[i]
            zz = z + dz[i]
            if 0 <= xx < M and 0 <= yy < N and 0 <= zz < H and box[zz][yy][xx] == 0:
                box[zz][yy][xx] = box[z][y][x] + 1
                q.append([zz, yy, xx])

    return box


bfs()
rlt = 0

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            else:
                if k > rlt:
                    rlt = k

print(rlt - 1)

