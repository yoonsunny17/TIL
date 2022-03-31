from itertools import combinations
from pprint import pprint
from collections import deque
'''
나보다 큰 물고기가 있으면 : 못먹고 못지나가
나랑 같은 크기 물고기라면 : 못먹고 지나갈수 있어
나보다 작은 크기 물고기라면 : 먹고 지나갈 수 있어

아기상어의 현재 크기만큼 물고기 마릿수 먹으면 상어 크기 + 1 증가
가장 가까운 물고기부터 섭취
여러마리라면, 윗쪽부터 섭취, 위에 여러마리인 경우 왼쪽부터 섭취
'''


def bfs(depart, size):
    q = deque()
    visited = [[0]*N for _ in range(N)]
    distance = 0
    q.append([depart[0], depart[1]])  # 상어의 위치(row, col), 이동 거리
    visited[depart[0]][depart[1]] = 1
    fish = []

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 방문한 적이 없으면
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                # 그리고 그 지점이 아기상어의 현재 크기보다 작거나 같으면
                if matrix[rr][cc] <= size:
                    q.append([rr, cc])  # 큐에 탐색 경로, 이동거리 갱신해서 넣어줘
                    visited[rr][cc] = 1  # 방문기록 남겨줘
                    distance += 1
                    # 그리고 만약에 그 지점이 0도 아니고, 상어 크기랑 같지도 않다면 (= 상어 크기보다 작은 물고기라면)
                    if 0 < matrix[rr][cc] < size:
                        fish.append([distance+1, rr, cc])

    return sorted(fish)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 아기상어 초기 위치 및 크기 변수 초기화
start_x, start_y = 0, 0
shark_size = 2

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

start = 0

for i in range(N):
    for j in range(N):
        # 아기상어 초기 위치 찾아줭
        if matrix[i][j] == 9:
            start = [i, j]

# 상어 초기 위치 0으로 초기화 해주자
matrix[start[0]][start[1]] = 0

# 몇 마리 먹었는지, 얼마나 걸렸는지 세어 줄 변수 초기화
eat, time = 0, 0

while True:
    left_fish = bfs(start, shark_size)

    # 먹을 수 있는 물고기가 더이상 없으면,
    if not len(left_fish):
        break

    # 거리(시간), 다음 위치 좌표 가져오기
    dist, x, y = left_fish.pop()
    time += dist
    # 물고기 먹었음을 표시해주기
    eat += 1
    # 상어 크기만큼 물고기를 먹었으면 상어 크기 +1, eat 초기화 해줘
    if start_size == eat:
        start_size += 1
        eat = 0


print(time)