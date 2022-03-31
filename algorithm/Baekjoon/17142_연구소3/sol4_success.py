'''success code~!!!!!!!!!!!!!!!!!!!!!!!!'''

from collections import deque
from pprint import pprint
from itertools import combinations


def bfs(elem):
    global time
    q = deque(elem)
    for k in q:
        visited[k[0]][k[1]] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 경로가 범위 내에 존재하고, 벽이 아니면서, 아직 방문하지 않았으면
            if 0 <= rr < N and 0 <= cc < N and matrix[rr][cc] != 1 and not visited[rr][cc]:
                visited[rr][cc] = visited[r][c] + 1  # 방문 해주고, (시간 체크도 함께 해줘)
                if matrix[rr][cc] == 0:  # 그리고 만약에 탐색 지점이 통로 부분이라면,
                    time = max(time, visited[rr][cc])  # 시간 갱신도 해주자!
                q.append([rr, cc])  # 그리고 탐색 경로에 추가해줘

    # 방문 안 한 곳의 개수가 벽의 개수와 동일한 경우라면 다 전파시킨 것!
    if list(sum(visited, [])).count(0) == list(sum(matrix, [])).count(1):
        rlt.append(time)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rlt = []  # bfs 돌렸을 때 가능한 시간 받아올 리스트 초기화

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스가 들어갈 수 있는 자리 받아줄 리스트
virus = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            virus.append([i, j])

# 바이러스 자리 중에서 M개 뽑아서 조합 만들어보자!
for start in combinations(virus, M):
    time = 0  # 시간은 0으로 초기화 하고,,
    visited = [[0]*N for _ in range(N)]  # 방문기록 겸 시간체크 리스트도 만들고,,
    bfs(start)  # bfs 돌려!

# print(rlt)
if len(rlt) and min(rlt) == 0:  # 0인 경우에는 -1 하면 안돼 ..
    print(0)
elif len(rlt) and min(rlt) > 0:  # 양수인 경우에는 -1 해줘야돼
    print(min(rlt)-1)
else:
    print(-1)  # 아니면 실패니까 -1 출력