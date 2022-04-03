import sys
from pprint import pprint

sys.stdin = open('snail.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    # delta 시계방향 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 초기 좌표 및 이동 방향 idx 초기화
    r, c, idx = 0, 0, 0

    for numb in range(1, N**2+1):
        matrix[r][c] = numb
        r += dr[idx]
        c += dc[idx]

        if r < 0 or r >= N or c < 0 or c >= N or matrix[r][c] != 0:
            r -= dr[idx]
            c -= dc[idx]

            idx = (idx+1) % 4

            r += dr[idx]
            c += dc[idx]

    # pprint(matrix)
    # print()
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()