from itertools import combinations
from pprint import pprint
from collections import deque


# bfs 돌릴거얌
def bfs(x, y, grow):
    # 경로 탐색 위한 queue, 방문 기록 리스트, 거리 체크 리스트 만들자
    q = deque()
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    # 아기 상어 경로 넣어주고 방문 기록 남겨줘
    q.append([x, y])
    visited[x][y] = 1
    # 먹을 수 있는 물고기 리스트 만들기
    fish = deque()

    # queue 가 빌 때까지
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 존재하고, 아직 방문하지 않은 곳인 경우
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                # 그리고 그 위치의 물고기 크기가 상어의 크기보다 작거나 같은 경우라면, 지나갈 수 있어
                if matrix[rr][cc] <= grow:
                    q.append([rr, cc])
                    # visited[rr][cc] = visited[r][c] + 1
                    visited[rr][cc] = 1
                    distance[rr][cc] = distance[r][c] + 1
                    # 근데 물고기를 먹을 수 있는 경우는 상어보다 작은 크기인 경우만 가능해
                    if 0 < matrix[rr][cc] < grow:
                        fish.append([distance[rr][cc], rr, cc])

    # 가까운 물고기 먼저 > 위쪽 물고기 > 왼쪽 물고기
    return sorted(fish, key=lambda x: (x[0], x[1], x[2]))


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 방문 기록 리스트 일단 만들어주자 (여기다 둘지, 옮길지 생각 잘해)
# visited = [[0]*N for _ in range(N)]
'''
나보다 큰 물고기가 있으면 : 못먹고 못지나가
나랑 같은 크기 물고기라면 : 못먹고 지나갈수 있어
나보다 작은 크기 물고기라면 : 먹고 지나갈 수 있어

아기상어의 현재 크기만큼 물고기 마릿수 먹으면 상어 크기 + 1 증가
가장 가까운 물고기부터 섭취
여러마리라면, 윗쪽부터 섭취, 위에 여러마리인 경우 왼쪽부터 섭취
'''

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 얼마나 걸렸는지, 얼마나 먹었는지 세어 줄 변수 초기화
time, eat = 0, 0
# 아기 상어의 성장을 갱신해 줄 변수 초기화
start_x, start_y = 0, 0
shark = 2

# 상어의 초기 위치 찾자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start_x = i
            start_y = j


while True:
    adult = bfs(start_x, start_y, shark)

    # 먹을 수 있는 물고기가 다 떨어졌으면 엄마 불러
    if not len(adult):
        break

    # popleft 해서 dis, row, col 가져와
    dis, row, col = adult.pop(0)

    # dis 누적값 = 걸린 시간
    time += dis

    # 아기 상어가 다녀가면서 물고기 먹은 곳은 0으로 바꿔줘
    matrix[start_x][start_y] = 0
    matrix[row][col] = 0

    # 물고기 한마리 먹었다!
    eat += 1

    # 만약 먹은 물고기 개수가 상어 크기랑 같아진다면, 상어 크기 +1 증가
    if eat == shark:
        shark += 1
        eat = 0  # 먹은 물고기 개수 초기화 시켜줘

print(time)



