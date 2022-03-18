from collections import deque
from pprint import pprint

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    # 물과 비버에 대한 empty queue 각각 생성해줘
    water_q = deque()
    cute_q = deque()
    cute_q.append(cute)  # 초기 비버 위치를 더해줘
    # 주의해야 할 점이, 초기 물의 위치가 몇개인지 모른다는 것!
    # 따라서 찾은 물의 위치만큼 append 해주자
    for i in range(len(water)):
        water_q.append(water[i])

    while True:
        # 비버가 더이상 움직일 수 없는 상태가 되면 while문 종료!
        if not cute_q:
            break

        # case 1. 물 먼저 채우기!
        for _ in range(len(water_q)):
            r, c = water_q.popleft()
            for i in range(4):
                wr = r + dr[i]
                wc = c + dc[i]
                # 탐색 지점이 범위 내에 존재하고, 빈 자리인 경우라면
                if 0 <= wr < R and 0 <= wc < C and matrix[wr][wc] == '.':
                    water_q.append([wr, wc])  # 탐색 경로를 저장해주고
                    matrix[wr][wc] = '*'  # 물로 바꿔줘

        # case 2. 비버 이동시키기!
        for _ in range(len(cute_q)):
            x, y = cute_q.popleft()
            for i in range(4):
                cr = x + dr[i]
                cc = y + dc[i]
                # 탐색 지점이 범위 내에 존재하면,
                if 0 <= cr < R and 0 <= cc < C:
                    # 그리고 그 지점이 빈 자리이고 아직 방문한 적이 없다면,
                    if matrix[cr][cc] == '.' and not visited[cr][cc]:
                        cute_q.append([cr, cc])  # 비버의 탐색 경로를 저장해주고,
                        visited[cr][cc] = visited[x][y] + 1  # 이동거리를 봐야하니까 1을 누적시켜주자
                    # 만약 굴에 도착했다면 이동거리를 반환해줘
                    if matrix[cr][cc] == 'D':
                        return visited[x][y]

    # while문을 다 돌았는데도 굴에 도착하지 못했다면 KAKTUS를 반환해줘
    return 'KAKTUS'


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
# 방문 리스트 만들어주기
visited = [[0 for _ in range(C)] for _ in range(R)]
# 물의 위치를 받을 리스트와, 비버의 위치를 받을 리스트를 각각 만들어주자
water = []
cute = []

for i in range(R):
    for j in range(C):
        # 물의 위치를 찾으면 리스트에 저장~
        if matrix[i][j] == '*':
            water.append([i, j])
        # 비버 위치 찾으면 리스트에 저장~
        if matrix[i][j] == 'S':
            cute.extend([i, j])  # 각 원소를 저장해주는 extend를 사용함!!!
            matrix[i][j] = '.'  # 비버의 위치를 빈 위치로 바꿔줘
            visited[i][j] = 1  # 방문 기록 남겨줘!

print(bfs())