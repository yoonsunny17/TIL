from pprint import pprint

# matrix 이차원 리스트 만들기
matrix = []
for i in range(5):
    row = [(j + 5*i) for j in range(1, 6)]
    matrix.append(row)

rlt = 0 # 결과값 받을 변수 초기화

# 델타 이용하여 각 요소에 접근하기
for r in range(len(matrix)):
    for c in range(len(matrix[0])): # 좌 하 우 상 순서로 접근 (시계방향)
        d_row = [0, 1, 0, -1]
        d_col = [1, 0, -1, 0]
        for d in range(4):
            dr = r + d_row[d]
            dc = c + d_col[d]

            # 범위 체크 (indexError 방지)
            # 유효한 인덱스 범위 내에 있는 경우
            if 0 <= dr < len(matrix) and 0 <= dc < len(matrix):
                sub = matrix[r][c] - matrix[dr][dc]
                # 절댓값 처리해주기
                if sub < 0:
                    sub = -sub
                rlt += sub

print(rlt)


# pprint(matrix)

