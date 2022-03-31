import sys
from pprint import pprint

sys.stdin = open('cart.txt')

# function 1. 수열 찾는 함수
# def f(i, cnt):
#     global min_rlt
#
#     # cnt 값이 min_rlt 보다 작을 때만 계산 이어나가보자
#     if cnt < min_rlt:
#         if len(cart) == N:
#             cnt += matrix[i][0]
#             min_rlt = cnt
#             return
#
#         for j in range(1, N):
#             if j not in cart:
#                 cart.append(j)
#                 cnt += matrix[i][j]
#                 f(j, cnt)
#                 cart.pop()

def f(i, cnt):
    global min_rlt

    if len(cart) == N-1:
        if cnt < min_rlt:
            cnt += matrix[i][0]
            min_rlt = cnt
            return

    for j in range(1, N):
        if j not in cart and not matrix[i][j-1]:
            cart.append(j)
            f(j, cnt + matrix[i][j-1])
            cart.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_rlt = 987654321
    # pprint(matrix)
    cart = []

    for i in range(1, N):
        cart.append(i)
        f(0, matrix[0][i])

    print(f'#{tc} {min_rlt}')

