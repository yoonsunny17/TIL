import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline


'''
1st bfs
각각의 섬을 구분해주기

2nd bfs
최단 다리 찾기
'''


# delta 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 각각의 섬울 구분해주는 bfs
def bfs1(i, j):
    global cnt
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    matrix[i][j] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            # 탐색 범위가 경로 내에 존재하고, matrix == 1이면서, 아직 방문하지 않은 곳이라면
            if 0 <= xx < N and 0 <= yy < N and matrix[xx][yy] == 1 and not visited[xx][yy]:
                q.append([xx, yy])
                matrix[xx][yy] = cnt
                visited[xx][yy] = 1


# 최단 길이의 다리 구하자
def bfs2(w):
    global answer
    bridge = [[-1]*N for _ in range(N)]  # 다리의 거리를 저장해 줄 배열
    q = deque()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == w:
                q.append([i, j])
                bridge[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            # 탐색 지점이 범위 내에 존재하는 경우라면,
            if 0 <= xx < N and 0 <= yy < N:
                # 그리고 다른 섬을 만났을 때 다리 길이와, 기존의 답을 비교해서 최단 길이를 선택하자
                if matrix[xx][yy] > 0 and matrix[xx][yy] != w:
                    answer = min(answer, bridge[x][y])

                # 그리고 바다를 만났다면 다리 길이는 +1씩 증가해줘
                if matrix[xx][yy] == 0 and bridge[xx][yy] == -1:
                    bridge[xx][yy] = bridge[x][y] + 1
                    q.append([xx, yy])


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 1  # 섬 번호 붙여줄거임
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        # 만약 탐색 범위가 방문하지 않았고, 1이라면,
        if not visited[i][j] and matrix[i][j]:
            # bfs1 을 돌리고, cnt += 1 해줘
            bfs1(i, j)
            cnt += 1

# bfs1 돌렸을때 이쁘게 나오는지 확인
# pprint(matrix)

for i in range(1, cnt):
    bfs2(i)

print(answer)

