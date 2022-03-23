from itertools import combinations
import sys

sys.stdin = open('shelves.txt')

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split()) # 직원의 수, 선반의 높이
    tall = list(map(int, input().split()))
    
    # tall 리스트 원소에 대한 부분집합 만들기
    lst = []
    for i in range(0, len(tall)+1):
        comb = combinations(tall, i)
        lst.extend(comb)

    # 탑과 선반 높이의 차를 구하고, 그 중 최솟값 구하기
    rlt = 987654321
    for j in lst:
        if 0 <= sum(j) - B < rlt:
            rlt = sum(j) - B

    print(f'#{tc} {rlt}')

