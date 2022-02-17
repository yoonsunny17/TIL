import sys

sys.stdin = open('sudoku.txt')

T = int(input())
for tc in range(1, T + 1):
    data = [list(map(int, input().split())) for _ in range(9)]
    # print(f'#{tc} ')
    print(data)
