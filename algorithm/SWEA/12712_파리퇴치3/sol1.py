import sys

sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # + 형태로 뿌려지는 경우
    max_rlt1 = 0
    for r in range(N):
        for c in range(N):
            # 상 하 좌 우
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            rlt1 = matrix[r][c] # 우선 중심 먼저 더해주기
            for i in range(4):
                for m in range(1, M): # 1부터 M-1까지 곱해주기
                    r1 = r + dr[i]*m
                    c1 = c + dc[i]*m
                    if 0 <= r1 < N and 0 <= c1 < N:
                        rlt1 += matrix[r1][c1]

            if max_rlt1 < rlt1:
                max_rlt1 = rlt1

    # cross 형태로 뿌려지는 경우
    max_rlt2 = 0
    for r in range(N):
        for c in range(N):
            # 대각선 시계방향
            ir = [-1, 1, 1, -1]
            ic = [1, 1, -1, -1]
            rlt2 = matrix[r][c] # 우선 중심 먼저 더해주기
            for j in range(4):
                for m in range(1, M):
                    r2 = r + ir[j]*m
                    c2 = c + ic[j]*m
                    if 0 <= r2 < N and 0 <= c2 < N:
                        rlt2 += matrix[r2][c2]

            if max_rlt2 < rlt2:
                max_rlt2 = rlt2

    max_kill = max(max_rlt1, max_rlt2)
    print(f'#{tc} {max_kill}')
    # if max_rlt1 > max_rlt2:
    #     print(f'#{tc} {max_rlt1}')
    # else:
    #     print(f'#{tc} {max_rlt2}')