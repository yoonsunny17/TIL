import sys
from collections import deque

sys.stdin = open('maze_distance.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 방문 기록 리스트 만들기
    visited = [[0]*N for _ in range(N)]
    # 거리 체크해 줄 리스트 만들기 (최종 반환해줄 것)
    distance = [[0]*N for _ in range(N)]
    # 경로가 두개 이상일 경우 고려!!!
    rlt = []
    # delta 상 하 좌 우 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 깊이우선탐색
    def dfs():
        stack = deque()
        # start 지점 찾기 = 2인 지점 찾기; stack에 넣어주고, 방문기록 남겨주자
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    stack.append([i, j])
                    visited[i][j] = 1

        # stack이 빌 때까지,
        while stack:
            r, c = stack.pop()
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                # 탐색한 지점이 범위 내에 존재하고, 도착 지점인 경우라면
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] == 3:
                    rlt.append(distance[r][c]) # 방문 기록을 반환해줘
                    return rlt

                # 탐색한 지점이 범위 내에 존재하고, 통로인 부분이라면
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] == 0 and not visited[rr][cc]:
                    distance[rr][cc] = distance[r][c] + 1
                    stack.append([rr, cc]) # stack에 더해주고
                    visited[rr][cc] = 1 # 방문기록 남겨줘

        # stack이 비었는데도 3을 못찾았다면 0을 반환해줘
        return 0

    dfs()

    # 경로가 하나인 경우에는 바로 반환해줘
    if len(rlt) == 1:
        print(f'#{tc} {rlt[0]}')
    # 경로가 두개인 겨우에는 최단거리 반환해줘
    elif len(rlt) >= 2:
        print(f'#{tc} {min(rlt)}')
    # 없으면 0 반환해줘
    else:
        print(f'#{tc} {int(dfs())}')
