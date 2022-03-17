from collections import deque
from pprint import pprint

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]  # 고슴도치 방문기록 남겨줄 리스트
distance = [[0]*C for _ in range(R)] # 탈출 성공한 경우, 경로 반환해 줄 리스트

# 고슴도치와 물의 이동경로 delta 상 하 좌 우 표현
dr = dx = [-1, 1, 0, 0]
dc = dy = [0, 0, -1, 1]

def bfs():
    # 물에 대한 empty queue 생성
    water = deque()
    # 고슴도치에 대한 empty queue 생성
    cute = deque()

    # 물이 차있는 지점 찾고, 고슴도치 위치 찾기
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '*':
                water.append([i, j])

            elif matrix[i][j] == 'S':
                cute.append([i, j])
                visited[i][j] = 1

    # 초기 조건에서 물이 아예 없는 경우도 있을 것!
    if len(water) == 0:
        while cute:
            x, y = cute.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < R and 0 <= yy < C and matrix[xx][yy] != 'X':
                    if matrix[xx][yy] == 'D':
                        rlt = distance[x][y] + 1
                        return rlt
                    if matrix[xx][yy] == '.' and not visited[xx][yy]:
                        matrix[xx][yy] = 'S'
                        visited[xx][yy] = 1
                        distance[xx][yy] = distance[x][y] + 1
                        cute.append([xx, yy])

        return 'KAKTUS'

    elif len(water) >= 1:
        # 고슴도치의 이동가능 경로 큐가 빌 때까지 반복해줘
        while water and cute:
            r, c = water.popleft()
            x, y = cute.popleft()
            for i in range(4):
                # 물 탐색 방향
                rr = r + dr[i]
                cc = c + dc[i]
                # 고슴도치 탐색 방향
                xx = x + dx[i]
                yy = y + dy[i]

                # case 1. 고슴도치의 탐색 지점이 범위 내에 있는 경우
                if 0 <= xx < R and 0 <= yy < C:
                    # D에 도달했다면 최단 이동거리를 반환하자
                    if matrix[xx][yy] == 'D':
                        rlt = distance[x][y] + 1
                        return rlt

                    # 그 지점이 비어있는 곳이면서 아직 방문한 적이 없는 경우면 가자!
                    if matrix[xx][yy] == '.' and not visited[xx][yy]:
                        matrix[xx][yy] = 'S'
                        visited[xx][yy] = 1
                        distance[xx][yy] = distance[x][y] + 1
                        cute.append([xx, yy])

                # case 2. 물의 탐색 지점이 범위 내에 있는 경우
                if 0 <= rr < R and 0 <= cc < C:
                    # 그 지점이 비어있는 곳이거나 S 인 경우는 *로 바꿔주자
                    if matrix[rr][cc] == '.' or matrix[rr][cc] == 'S':
                        matrix[rr][cc] = '*'
                        water.append([rr, cc])

        # 다 돌았는데 도달을 못했으면 실패!
        return 'KAKTUS'

bfs()
print(bfs())