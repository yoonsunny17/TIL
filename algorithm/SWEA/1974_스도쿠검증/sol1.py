'''
1. 3 x 3 검사 함수 return 0 or 1
2. 가로 검사 함수 return 0 or 1
3. 세로 검사 함수 return 0 or 1
4. result = 1 * 2 * 3
'''

import sys

sys.stdin = open('sudoku.txt')

T = int(input())


for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    rlt_1 = rlt_2 = rlt_3 = 1

    # grid matrix check
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            grid_lst = [0] * 10
            for dr in range(3):
                for dc in range(3):
                    grid_lst[matrix[r+dr][c+dc]] += 1

            for i in range(1, 10): # range 설정 조심~!
                if grid_lst[i] != 1:
                    rlt_1 *= 0
                    break

    # row matrix check
    # col matrix check
    for r in range(9):
        row_lst = [0] * 10
        col_lst = [0] * 10
        for c in range(9):
            row_lst[matrix[r][c]] += 1
            col_lst[matrix[c][r]] += 1

        for i in range(1, 10):
            if row_lst[i] != 1:
                rlt_2 *= 0
                break
            if col_lst[i] != 1:
                rlt_3 *= 0
                break

    print(f'#{tc} {rlt_1 * rlt_2 * rlt_3}')














