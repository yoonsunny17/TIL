'''
sol 1 => fail!!
'''

import sys

sys.stdin = open('palindrome2.txt')

T = 10
for tc in range(1, 11):
    n = int(input())
    # 주어진 문자열을 이차원리스트로 받는다
    chars = [list(map(str, input())) for _ in range(100)]
    cnt_row = 0
    cnt_col = 0
    max_row = 0
    max_col = 0

    # row 고정, column 거꾸로 리스트 만들기
    reverse_row = []
    for r in range(len(chars)):
        reverse_row.append(chars[r][::-1])

    # 회문 비교 (row 고정)
    for i in range(len(chars)):
        for j in range(len(chars)-i-1):
            if chars[i][j] != reverse_row[i][j]: # 문자열이 같지 않다면
                cnt_row = 0 # cnt를 0으로 초기화 해줘
            else: # 만약 문자열이 동일하다면
                cnt_row += 1 # cnt에 1을 더해줘
                if max_row < cnt_row: # 만약 최댓값보다 cnt값이 더 크다면
                    max_row = cnt_row # max값에 최댓값을 저장해줘
    # print(max_row)

    # column 고정, row 거꾸로 리스트 만들기
    reverse_col = []
    for c in range(len(chars)):
        reverse_col.append(chars[::-1][c])

    # 회문 비교 (column 고정)
    for j in range(len(chars)):
        for i in range(len(chars)-j-1):
            if chars[i][j] != reverse_col[i][j]:
                cnt_col = 0
            else:
                cnt_col += 1
                if max_col < cnt_col:
                    max_col = cnt_col

    print(max_col, max_row)
