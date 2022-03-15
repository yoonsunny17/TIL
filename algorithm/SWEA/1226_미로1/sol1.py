import sys
from collections import deque

sys.stdin = open('maze_1.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    # delta 4방향 탐색 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    start = 0
    # 출발지점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]

    def dfs():
        # empty stack
        stack = deque()
        stack.append(start)
        visited[start[0]][start[1]] = 1
        # stack이 빌 때까지 반복
        while stack:
            r, c = stack.pop()
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                # 탐색한 지점이 범위 내에 존재하고, 도착 지점인 경우
                if 0 <= rr < 16 and 0 <= cc < 16 and maze[rr][cc] == 3:
                    # true를 반환해줘
                    return True
                # 탐색한 지점이 범위 내에 존재하고, 통로이며, 아직 방문한 적이 없는 곳인 경우
                if 0 <= rr < 16 and 0 <= cc < 16 and maze[rr][cc] != 1 and not visited[rr][cc]:
                    # 방문 기록을 남겨주고, stack에 경로 넣어줘
                    visited[rr][cc] = 1
                    stack.append([rr, cc])

        # stack이 빌 때까지 반복했는데도 경우의 수가 없다면 false를 반환해줘
        return False

    print(f'#{tc} {int(dfs())}')

