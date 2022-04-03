from collections import deque
from pprint import pprint
from itertools import combinations


# 치킨집 M개만 살려두기
# 1. 치킨집 M개 빼고 폐업시키는 함수 구현하자
def chicken(cnt):
    # 폐업 후 남은 치킨집 개수가 M개인 경우 bfs 돌리자
    if cnt == M:
        bfs()
        return

    # 치킨집 찾으면 폐업하고 다시 함수 돌려
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                matrix[i][j] = 0  # 폐업했다
                chicken(cnt-1)
                matrix[i][j] = 2  # 다른 가게 폐업해보자 (백트래킹)


# 2. 치킨집 M개에 대해 각 집에 대한 최단 치킨 거리 구하자 (bfs)
def bfs():
    global min_rlt
    # 집 위치 찾자
    house = deque()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                house.append([i, j])
    
    # deep copy 해줘
    new_matrix = [row[:] for row in matrix]
    print('==new==')
    pprint(new_matrix)

    rlt = []
    each_rlt = 0  # 최단 거리 받아줄 변수
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    # 각 집에 대해 최단 거리 구해보자
    while house:
        r, c = house.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 탐색 경로가 범위 내에 있는데,
            if 0 <= rr < N and 0 <= cc < N:
                # 그 지점이 치킨집이 아니고, 아직 방문한 기록이 없으면,
                if new_matrix[rr][cc] != 2 and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    distance[rr][cc] += 1  # 방문 기록 및 거리 표시해주고
                    house.append([rr, cc])  # 다음 이동할 경로 넣어줘
                if new_matrix[rr][cc] == 2 and not visited[rr][cc]:
                    distance[rr][cc] = distance[r][c] + 1
                    print('====matrix====')
                    pprint(new_matrix)
                    print('===check distance, visited===')
                    pprint(distance)
                    pprint(visited)


                # 그 지점이 치킨집이라면,
                # if new_matrix[rr][cc] == 2:
                #     rlt.append(distance[rr][cc]+1)  # 치킨집 까지 이동거리 더해줘
                #     # rlt.append(each_rlt)
                #     print('===check distance, visited===')
                #     pprint(distance)
                #     pprint(visited)

    for i in range(N):
        for j in range(N):
            if new_matrix[i][j] == 2:
                rlt.append(distance[i][j])

    # 더해주자
    print('===rlt===')
    print(rlt)

    min_rlt = min(min_rlt, sum(rlt))


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 집, 2 = 치킨집
min_rlt = 987654321  # 최솟값 받을 변수 초기화

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 원래 치킨집 몇개인지 세보자
kfc = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            kfc += 1

chicken(kfc)
print('===answer===')
print(min_rlt)



                

        