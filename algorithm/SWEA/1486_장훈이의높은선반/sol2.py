from itertools import combinations
import sys

sys.stdin = open('shelves.txt')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())  # 직원의 수, 선반의 높이
    tall = list(map(int, input().split()))

    rlt = 987654321
    for i in range(0, len(tall) + 1):
        for comb in combinations(tall, i):
            if 0 <= sum(comb) - B < rlt:
                rlt = sum(comb) - B

    print(f'#{tc} {rlt}')
