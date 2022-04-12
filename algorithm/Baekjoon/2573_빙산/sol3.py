''' success 성공했지만 많이 참고했음... 다시 한번 봐야해 '''
from collections import deque
from pprint import pprint


# 1. 얼음이 다 녹았는지 확인해주는 함수
# 전체가 0 이라면 0을 반환해줘
def melt_ice():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                return False
    return True


# 2. 빙산의 위치를 찾았다면, 빙산 주변에 0의 개수를 찾아줘
# 단, 원래 matrix로 0의 개수를 찾아야 하니까 deepcopy 써주고, 여기 함수에선 원래 matrix 사용해야돼
# 그리고 여기 함수 나가서 new matrix 갱신해주기
def cnt_zero(r, c):
    cnt = 0
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < M and not matrix[rr][cc]:
            cnt += 1
    return cnt


# 3. 빙산 덩어리가 몇개인지 세어줘
def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and new_matrix[rr][cc] and not visited[rr][cc]:
                visited[rr][cc] = 1
                new_matrix[rr][cc] = 0
                q.append([rr, cc])


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 시간 세어줄 변수 초기화
time = 0

while True:
    time += 1
    # 만약 얼음이 다 녹았다면 0 출력하고 끝!
    if melt_ice():
        print(0)
        break

    # 빙산 주변 0 개수만큼 빙산 녹여주면서 갱신해줄 matrix 만들어줘!
    new_matrix = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 원래 matrix에서 0이 아닌 위치 찾았다면, 빙산 주변의 0개수 찾아주자
            if matrix[i][j] != 0:
                zero = cnt_zero(i, j)
                # new = 빙산의 높이 - 주변 0의 개수
                new = matrix[i][j] - zero
                new_matrix[i][j] = (new if new >= 0 else 0)  # 음수면 0 처리해줘!
    # deepcopy!!
    matrix = [row[:] for row in new_matrix]

    # 빙산 덩어리 개수 몇개인지 세어줄 변수 초기화
    cnt_ice = 0
    for i in range(N):
        for j in range(M):
            # 새로 갱신되는 matrix에서 빙산이 남아있으면 bfs 돌려주고, 빙산 개수 세어줘
            if new_matrix[i][j] != 0:
                bfs(i, j)
                cnt_ice += 1

    # 다 녹을 때까지 덩어리가 2개 이상이면 얼마나 걸렸는지 반환 해줘
    if cnt_ice >= 2:
        print(time)
        break
