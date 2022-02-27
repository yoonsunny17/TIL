import sys
from pprint import pprint

sys.stdin = open('input_prob_1.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_rlt = 0 # 최댓값 받을 변수 초기화

    # case 1. r + K - 1 < N
    for r in range(N):
        rlt = 0 # 매 행마다 rlt 초기화 되어야 함!
        # case 1. r + K - 1 < N
        if r + K - 1 < N:
            for c in range(r, r + K):
                rlt += matrix[r][c]
            if max_rlt < rlt:
                max_rlt = rlt

        # case 2. r + K - 1 >= N
        else:
            for c in range(r, N):
                rlt += matrix[r][c]
            if max_rlt < rlt:
                max_rlt = rlt

    print(f'#{tc} {max_rlt}')