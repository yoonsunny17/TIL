from pprint import pprint

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

pprint(my_list, width=15)
# 1 ~ 9 순차적으로 출력; 행 우선순회
# for i in range(len(my_list)):
#     for j in range(len(my_list[0])):
#         print(my_list[i][j], end=' ')

# 열 우선순회
# for j in range(len(my_list[0])):
#     for i in range(len(my_list)):
#         print(my_list[i][j], end=' ')

# for j in range(len(my_list[0])):
#     for i in range(len(my_list)):
        # 5일 때 상하좌우에 있는 숫자 출력
        # if my_list[i][j] == 5:
        #     print(my_list[i-1][j], my_list[i+1][j], my_list[i][j-1], my_list[i][j+1])

        # delta를 이용한 경우: 상 하 좌 우 기준
        #     row_d = [-1, 1, 0, 0]
        #     col_d = [0, 0, -1, 1]
        #     for d in range(4):
        #         each_row = i + row_d[d]
        #         each_col = j + col_d[d]
        #         print(my_list[each_row][each_col])

# practice 1 - solution 1

# 1. 5 x 5 matrix 초기화 하기 ([0]*25 하고 각각의 요소에 접근해서 +1씩 해도 됨)
matrix = []
for i in range(5):
    row = [(j + i*5) for j in range(1, 6)]
    print(row)
    matrix.append(row)
# pprint(matrix)
rlt = 0
# 2. 각각의 요소의 차 구하기
# 2-1. 각 요소에 접근하기 (델타를 이용한 방법)
for r in range(len(matrix)):
    for c in range(len(matrix[0])): # 상 하 좌 우 순서로 접근
        d_row = [-1, 1, 0, 0]
        d_col = [0, 0, -1, 1]
        for d in range(4):
            each_row = r + d_row[d]
            each_col = c + d_col[d]
            
            # 범위 체크 (인덱스에러 방지)
            if each_row < 0 or each_row > 4 or each_col < 0 or each_col > 4:
                continue
            
            # 2-2. 각 요소의 차 구하기
            else:
                # print(f'target numb = {matrix[each_row][each_col]}')
                sub = matrix[r][c] - matrix[each_row][each_col]
                # 절댓값 처리하기 (삼항연산자 사용)
                sub = sub if sub >= 0 else -sub
                rlt += sub
                
print(rlt)

# practice 1 - solution 2
# 만약 1부터 25까지 순차적으로 들어간다면, 상 하 좌 우 차이의 절댓값의 합은 항상 12로 일정할 것
total = 25 * 12
# 근데 edge 부분의 요소들 중에서는 index 범위에 의해 절댓값 차의 합이 12가 되지 못하는 것들이 발생함
sub = 12 * 5
rlt = total - sub
print(rlt)

# 부분집합