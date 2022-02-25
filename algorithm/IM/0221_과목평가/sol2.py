import sys

sys.stdin = open('input_prob_2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]  # N x N 이차원 리스트

    # 3 x 3 배열 합 구하기
    max_grid = 0
    for r in range(N):
        for c in range(N):

            rlt_grid = 0
            cnt = 0 # 3x3 합이 맞는지 확인 => 원소 0개 모두 더해진 것이 맞는지 확인
            for i in range(-1, 2): # 원소 중심으로 -1, 0, 1 (delta)
                for j in range(-1, 2):
                    if 0 <= r + i < N and 0 <= c + j < N:
                        rlt_grid += lst[r + i][c + j]
                        cnt += 1

            if cnt == 9:
                if max_grid < rlt_grid:
                    max_grid = rlt_grid


    # crazy arcade 구하기
    max_cross = 0
    for r in range(N):
        for c in range(N):
            rlt_cross = 0
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]

            power = lst[r][c]
            rlt_cross += power

            for d in range(4):
                for p in range(1, power):
                    dr = r + d_row[d] * p
                    dc = c + d_col[d] * p

                    if 0 <= dr < N and 0 <= dc < N:
                        rlt_cross += lst[dr][dc]

            if max_cross < rlt_cross:
                max_cross = rlt_cross


    if max_grid > max_cross:
        print(f'#{tc} {max_grid}')
    else:
        print(f'#{tc} {max_cross}')