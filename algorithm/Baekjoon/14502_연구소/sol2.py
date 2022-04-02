from collections import deque
from pprint import pprint
from itertools import combinations


def change_walls(new_walls, matrix):
    for w in new_walls:
        matrix[w[0]][w[1]] = 1

    return matrix


def bfs(new_matrix):
    global zero

    visited = [[0]*M for _ in range(N)]  # 방문 리스트는 bfs 돌릴 때마다 초기화해줘

    while virus:
        r, c = virus.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 존재하고, 빈 칸인데, 아직 방문한 적 없으면,
            if 0 <= rr < N and 0 <= cc < M and not new_matrix[rr][cc] and not visited[rr][cc]:
                new_matrix[rr][cc] = 2  # 방문해주고 (바이러스 퍼뜨리고)
                zero -= 1  # 빈칸 개수 하나 깎아주고
                visited[rr][cc] = 1  # 방문 기록 남겨주고
                virus.append([rr, cc])  # 다음 퍼트릴 경로 가자~
    # 남은 빈칸 개수 반환 해줘
    return zero


N, M = map(int, input().split())  # N = 세로 길이, M = 가로 길이
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 위치
min_cnt = 987654321
# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스 위치 찾자
virus = deque()

# 빈 칸 위치 찾자 (벽 세울 수 있는 위치)
install_walls = []

# 총 빈칸 개수 세자
zero = -3  # 벽 세개 세우는거 고려해서 3 빼고 시작

for i in range(N):
    for j in range(M):
        # 만약 빈 칸인 경우라면, 벽 설치 가능!
        if matrix[i][j] == 0:
            install_walls.append([i, j])
            zero += 1  # 빈칸 개수도 세어주고,,
        # 바이러스 위치도 찾아줘
        if matrix[i][j] == 2:
            virus.append([i, j])

temp = zero
# 벽 설치 가능한 빈 칸들 중에서 3개를 뽑아보자
for install in combinations(install_walls, 3):
    new_walls = list(install)  # 리스트 형태로 받았고
    new_matrix = change_walls(new_walls, matrix)  # 벽으로 바꿔줬엉
    zero = temp  # 세어준 빈칸 개수 가져오고, 글로벌 선언 해줘
    # 벽 설치 후에 bfs 돌렸을 때 바이러스가 퍼지지 않는 빈 칸이 몇개인지 세어보자

    # bfs 돌린다음 남은 빈칸 개수 세어줘
    cnt = bfs(new_matrix)
    pprint(matrix)
    if cnt >= min_cnt:
        continue
    # 그리고 최솟값 갱신 가능하면 갱신해줘
    if cnt < min_cnt:
        min_cnt = cnt


print(min_cnt)

            




# while True:
#     if not len(installed):
#         break
#
#     new_walls = installed.pop()
#     three_walls(new_walls)
#
# # 벽 세개 짓기
# def three_walls(new_walls):
#     for i in range():
# #
#
# # print(install[0], install[1], install[2])
#
# pprint(installed)
