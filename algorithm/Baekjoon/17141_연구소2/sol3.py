from collections import deque
from itertools import combinations
from pprint import pprint

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# 0 : 바이러스가 퍼질 수 있는 곳
# 1 : 벽, 바이러스가 퍼질 수 없음
# 2 : 바이러스의 초기 위치가 될 수 있음

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스가 출발할 수 있는 위치들 넣어줄 list
virus = []
# 벽인 부분은 헷갈리지 않도록 문자열로 바꿔주자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = '-'
        if matrix[i][j] == 2:
            virus.append([i, j])
            matrix[i][j] = 0  # 바이러스가 지나다닐 수 있도록 0으로 바꿔주자

# virus 리스트에서 M개 뽑아서 조합 만들기
q = deque()
min_time = []
for start in combinations(virus, M):
    lst = []
    for k in start:
        q.append(k)
        visited[k[0]][k[1]] = 1  # 방문 기록 남겨줘

        # print(q)
        while q:
            r, c = q.popleft()
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < N and 0 <= cc < N and not matrix[rr][cc] and not visited[rr][cc]:
                    q.append([rr, cc])
                    visited[rr][cc] = visited[r][c] + 1

    rlt = max(map(max, visited))
    lst.append(rlt)
    pprint(visited)
    print(lst)
# print(rlt)
print()

print(min_time)

# pprint(visited)