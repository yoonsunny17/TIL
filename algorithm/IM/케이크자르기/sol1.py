import sys

sys.stdin = open('cake2.txt')

# 가로로 잘랐을 때 up & down 부분이 total의 반씩 차지하는지 확인하는 함수
def up_down(N, matrix, total):
    r = 0
    up = 0
    while r < N - 1:
        up += sum(matrix[r])
        r += 1
        # 종료조건1. 성공한 경우
        if up == total // 2:
            return 1

        # 종료조건2. 실패한 경우
        if r == N - 1 and up != total // 2:
            return 0

# 세로로 잘랐을 때 left & right 부분이 total의 반씩 차지하는지 확인하는 함수
# 근데 세로로 자르는거 귀찮으니까 transpose 해주기
def left_right(N, matrix, total):
    c = 0
    left = 0

    # transpose
    matrix = list(map(list, zip(*matrix)))

    while c < N - 1:
        left += sum(matrix[c])
        c += 1
        # 종료조건1. 성공한 경우
        if left == total // 2:
            return 1

        # 종료조건2. 실패한 경우
        if c == N - 1 and left != total // 2:
            return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 이중 리스트 내의 모든 원소의 합을 먼저 알아야 해!
    total_sum = 0
    for i in range(N):
        total_sum += sum(matrix[i])

    rlt1 = left_right(N, matrix, total_sum)
    rlt2 = up_down(N, matrix, total_sum)

    # rlt1, rlt2 모두 1이어야 성공!
    rlt = rlt1 * rlt2
    if rlt == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
