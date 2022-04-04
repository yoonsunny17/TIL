import sys

sys.stdin = open('n_queen.txt')

def check(si, sj):
    # 1. 위쪽 방향
    for i in range(si-1, -1, -1):
        if visited[i][sj] == 1:
            return 0

    # 2. 좌측 대각선 위
    i, j = si-1, sj-1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return 0
        i, j = i-1, j-1

    # 3. 우상단
    i, j = si-1, sj+1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return 0
        i, j = i-1, j+1

    # 3 방향 퀸 없음 : 성공!
    return 1


def dfs(n):
    global rlt

    # N까지 다다른 경우 = 성공했음
    if n == N:
        rlt += 1
        return

    for j in range(N):
        # n행 j열
        if check(n, j):
            visited[n][j] = 1
            dfs(n+1)
            visited[n][j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    rlt = 0
    dfs(0)  # 제일 꼭대기부터

    print(f'#{tc} {rlt}')