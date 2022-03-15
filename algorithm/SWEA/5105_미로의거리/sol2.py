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

    # delta 상 하 좌 우 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 너비우선탐색
    def bfs():
        q = deque()
        # start 지점 찾기 = 2인 지점 찾기; q에 넣어주고, 방문기록 남겨주자
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    q.append([i, j])
                    visited[i][j] = 1

        while q:
            r, c = q.popleft()
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                # 탐색한 지점이 범위 내에 존재하고, 도착 지점인 경우라면
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] == 3:
                    return distance[r][c] # 최종 distance를 반환해줘

                # 탐색한 지점이 범위 내에 존재하고, 통로인 부분이라면
                if 0 <= rr < N and 0 <= cc < N and maze[rr][cc] == 0 and not visited[rr][cc]:
                    distance[rr][cc] = distance[r][c] + 1
                    q.append([rr, cc]) # q에 더해주고
                    visited[rr][cc] = 1 # 방문기록 남겨줘

        # stack이 비었는데도 3을 못찾았다면 0을 반환해줘
        return 0

    print(f'#{tc} {int(bfs())}')

