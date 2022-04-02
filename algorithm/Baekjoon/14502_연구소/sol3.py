from collections import deque
from itertools import combinations
from pprint import pprint


# 1. 벽 세우는 함수 구현 (설치 가능한 빈칸 세개 모이면 ==> 바이러스 퍼뜨리는 함수로 넘어가도록)
def change_walls(cnt):
    # bfs 함수 돌릴 수 있는 조건 = 벽 세울 수 있는 빈 칸 세개 모았을 때
    if cnt == 3:
        bfs()
        return

    # 우선 빈 칸을 찾자
    for i in range(N):
        for j in range(M):
            # 빈칸 위치 찾았다면
            if matrix[i][j] == 0:
                matrix[i][j] = 1  # 벽 설치해주고
                change_walls(cnt + 1)  # cnt +1 갱신 해서 재귀 돌려줘
                matrix[i][j] = 0  # 백트래킹


# 2. 바이러스 퍼뜨리는 함수 구현
def bfs():
    global max_rlt
    virus = deque()
    rlt = 0
    new_matrix = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_matrix[i][j] = matrix[i][j]
            # 바이러스 위치 찾아주기
            if matrix[i][j] == 2:
                virus.append([i, j])

    while virus:
        r, c = virus.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 존재하고, 빈 칸인 경우라면,
            if 0 <= rr < N and 0 <= cc < M and not new_matrix[rr][cc]:
                new_matrix[rr][cc] = 2  # 바이러스 퍼뜨려주고
                virus.append([rr, cc])  # 새로운 바이러스 탐색 경로 넣어줘

    # 빈 칸 개수 세어주기
    for i in range(N):
        for j in range(M):
            if new_matrix[i][j] == 0:
                rlt += 1

    max_rlt = max(max_rlt, rlt)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 위치

max_rlt = 0  # 최댓값 갱신해줄 변수

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


change_walls(0)
print(max_rlt)








