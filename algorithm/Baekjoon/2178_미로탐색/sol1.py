from collections import deque
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최소 칸 수 출력 = BFS 돌리기


def bfs():
    # 큐 생성하고, 시작점 넣어줘
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1  # 방문 기록도 남겨줘

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 이동할 수 있는 칸이고, 아직 방문한 적이 없으면,
            if 0 <= rr < N and 0 <= cc < M and matrix[rr][cc] == 1 and not visited[rr][cc]:
                # 방문기록이자 얼마나 이동했는지 체크해주고
                visited[rr][cc] = visited[r][c] + 1
                # 근데 도착지점에 다왔다면 끝!
                if rr == N-1 and cc == M-1:
                    return visited[rr][cc]
                # 다음 탐색 경로 넣어줘
                q.append([rr, cc])


rlt = bfs()
print(rlt)
pprint(visited, width=20)