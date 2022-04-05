''' BFS 로 풀었음 !!! '''
from pprint import pprint
from collections import deque
import sys

sys.stdin = open('minimum.txt')


def bfs(si, sj, ei, ej):
    q = deque()
    visited = [[float('inf')]*N for _ in range(N)]  # 최소 비용으로 갱신해줘야 하므로 초기값을 충분히 큰 값으로 초기화!

    q.append([si, sj])
    visited[si][sj] = 0

    # delta 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하는 경우에만 고려해보자
            if 0 <= rr < N and 0 <= cc < N:
                # 우선 높이 차에 대해서도 고려해줄 건데, 초기값은 0이야
                diff = 0
                # 만약 다음번에 탐색하는 지점이 더 높은 위치라면, 그 위치의 차 만큼 diff 를 고려해줘
                if matrix[rr][cc] > matrix[r][c]:
                    diff = matrix[rr][cc] - matrix[r][c]
                # 그리고 만약에 이전에 방문 리스트에 기록해줬던 값보다 지금 계산해본 값이 더 저렴하다면, 이번 값으로 갱신해줘
                if visited[rr][cc] > visited[r][c] + diff + 1:
                    visited[rr][cc] = visited[r][c] + diff + 1
                    q.append([rr, cc])

    return visited[ei][ej]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    rlt = bfs(0, 0, N-1, N-1)

    print(f'#{tc} {rlt}')

