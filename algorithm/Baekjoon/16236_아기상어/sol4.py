'''success!!!'''
from collections import deque


def bfs(row, col):
    global fish
    fish = []
    q = deque()
    # row, col, distance 넣어줘
    q.append([row, col, 0])
    visited = [[0]*N for _ in range(N)]
    visited[row][col] = 1

    while q:
        r, c, d = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 범위가 경로 내에 존재하고, 아직 방문하지 않은 곳이라면
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                # 그리고 물고기가 없거나, 상어 크기보다 같거나 작은 물고기가 있는 곳이라면,
                if 0 <= matrix[rr][cc] <= shark_size:
                    visited[rr][cc] = 1  # 방문 기록 남기고
                    q.append([rr, cc, d+1])  # 탐색 경로, d 누적시키고 큐에 넣어줘
                    # 그리고 만약에 아기상어보다 작은 물고기가 있는 경우라면,
                    if 0 < matrix[rr][cc] < shark_size:
                        fish.append([rr, cc, d+1])  # 먹을 수 있는 물고기 리스트에 올려줘


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상어의 초기 위치 및 크기 변수 초기화
start_x, start_y = 0, 0
shark_size = 2

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 아기상어가 처음 출발하는 위치 찾기
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start_x = i
            start_y = j
# 상어 위치 찾았으니까 0으로 초기화해주자
matrix[start_x][start_y] = 0
# 먹은 물고기 개수 세어주는 변수 및 걸린 시간 받을 변수 초기화
eat, time = 0, 0
# 먹을 수 있는 물고기 담을 리스트 만들기
fish = []


while True:
    bfs(start_x, start_y)
    # 만약 먹을 수 있는 물고기가 더이상 없으면 time 출력 후 종료해줘,
    if not len(fish):
        print(time)
        exit()

    # 아직 먹을 수 있는 물고기가 남아있다면, 일단 우선 순위로 정렬시켜줘
    else:
        fish.sort(key=lambda x:(x[2], x[0], x[1]))
        matrix[fish[0][0]][fish[0][1]] = 0  # 그리고 먹었으니까 0 처리 해줘
        eat += 1  # 냠냠 물고기 + 1
        time += fish[0][2]  # 이동한 거리 = 걸린 시간이므로 갱신해줘
        # 시작 지점을 내가 방금 먹은 물고기 위치로 갱신해주자
        start_x = fish[0][0]
        start_y = fish[0][1]
        
        # 만약 먹은 물고기 개수가 상어 크기와 같아지면,
        if eat == shark_size:
            shark_size += 1  # 상어 크기 + 1 해주고
            eat = 0  # eat 변수 초기화 해줘
