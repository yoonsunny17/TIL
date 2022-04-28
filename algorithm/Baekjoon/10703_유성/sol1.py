import sys
import pprint
R, S = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 유성과 땅 사이 거리 갱신해 줄 변수 초기화
distance = float('inf')


# 유성이 있는 경우에만 고려해야 함
# for j in range(S):
#     low_meteor = 0
#     high_ground = float('inf')
# 
#     for i in range(R):
#         # 만약 유성이라면, 가장 낮은 유성인지 확인해봐
#         if matrix[i][j] == 'X':
#             if i > low_meteor:
#                 low_meteor = i
# 
#         # 만약 땅이라면, 가장 높은 땅인지 확인해봐
#         elif matrix[i][j] == '#':
#             if i < high_ground:
#                 high_ground = i

    # 가장 낮은 유성과, 가장 높은 땅의 차이를 계산해줘
    if distance > high_ground - low_meteor - 1:
        distance = high_ground - low_meteor - 1
    print(low_meteor)
    print(high_ground)
    print('=======')

# 결과값 출력할 이차원 배열 초기화
rlt_matrix = [list('.' for _ in range(S)) for _ in range(R)]

# 충돌 후의 matrix를 구하자
for i in range(R):
    for j in range(S):
        if matrix[i][j] == 'X':
            rlt_matrix[i+distance][j] = 'X'
        if matrix[i][j] == '#':
            rlt_matrix[i][j] = '#'


for i in range(R):
    for j in range(S):
        sys.stdout.write(rlt_matrix[i][j])
    sys.stdout.write('\n')

