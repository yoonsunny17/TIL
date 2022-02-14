import sys

sys.stdin = open('sum.txt')

T = 10
for tc in range(1, 11):
    n = int(input())
    matrix = [] # 이중 리스트 만들 리스트
    max_row = 0 # row 합 중 가장 큰 값 받을 변수
    max_col = 0 # column 합 중 가장 큰 값 받을 변수
    max_d1 = 0 # 좌측상단-> 우측하단 대각선 합 받을 변수
    max_d2 = 0 # 우측상단 -> 좌측하단 대각선 합 받을 변수
    rlt = [] # 위의 네 가지 변수 받을 리스트

    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row) # 이차원 리스트 완성

    # 각 행 요소의 합 리스트에 받기
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix)):
            row_sum += matrix[i][j]
            if row_sum >= max_row:
                max_row = row_sum
    rlt.append(max_row)

    # 각 열 요소의 합 리스트에 받기
    for j in range(len(matrix)):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
            if col_sum >= max_col:
                max_col = col_sum
    rlt.append(max_col)

    # 대각선 1 합 구하기
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                max_d1 += matrix[i][j]
    rlt.append(max_d1)

    # 대각선 2 합 구하기
    for i in range(len(matrix)):
        max_d2 = 0
        for j in range(len(matrix)-1, -1, -1):
            max_d2 += matrix[i][j]
    rlt.append(max_d2)

    max_total = 0
    for i in range(len(rlt)):
        if rlt[i] >= max_total:
            max_total = rlt[i]
    print(f'#{tc} {max_total}')
