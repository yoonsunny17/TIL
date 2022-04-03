from collections import deque
from pprint import pprint


# 치킨집 M개만 살려두기
# 1. 치킨집 M개 빼고 폐업시키는 함수 구현하자
def chicken(cnt):
    # 폐업 후 남은 치킨집 개수가 M개인 경우 bfs 돌리자
    if cnt == M:
        # 집 위치 찾자
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    start = [i, j]

                    bfs(start)
        return

    # 치킨집 찾으면 폐업하고 다시 함수 돌려
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                matrix[i][j] = 0  # 폐업했다
                chicken(cnt-1)
                matrix[i][j] = 2  # 다른 가게 폐업해보자 (백트래킹)


def bfs(start):
    global min_rlt, rlt

    house = deque()
    house.append([start[0], start[1]])
    # 집 위치 찾자
    # house = deque()
    # for i in range(N):
    #     for j in range(N):
    #         if matrix[i][j] == 1:
    #             house.append([i, j])

    # deep copy 해줘
    new_matrix = [row[:] for row in matrix]
    print('==========new matrix==========')
    pprint(new_matrix)

    distance = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # rlt = []
    while house:
        r, c = house.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 있는데 아직 집이 아닌 경우
            if 0 <= rr < N and 0 <= cc < N:
                if new_matrix[rr][cc] != 2 and not visited[rr][cc]:
                    # 이동한 거리 누적시켜주고, 다음 탐색 경로 넣어줘
                    visited[rr][cc] = 1
                    distance[rr][cc] = distance[r][c] + 1
                    house.append([rr, cc])
                if new_matrix[rr][cc] == 2 and not visited[rr][cc]:
                    rlt.append(distance[r][c]+1)

    print('======distance======')
    pprint(distance)

    print('=======rlt list=======')
    print(rlt)
    print('=======each sum========')
    print(sum(rlt))
    # print('지금은 0 나온다')
    # min_rlt = min(min_rlt, rlt)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 집, 2 = 치킨집
min_rlt = 987654321  # 최솟값 받을 변수 초기화
rlt = []
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
