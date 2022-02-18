'''
1. 3 x 3 검사 함수 return 0 or 1
2. 가로 검사 함수 return 0 or 1
3. 세로 검사 함수 return 0 or 1
4. result = 1 * 2 * 3
'''

import sys

sys.stdin = open('sudoku.txt')

T = int(input())

numb_lst = [x for x in range(1, 10)]

for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]


