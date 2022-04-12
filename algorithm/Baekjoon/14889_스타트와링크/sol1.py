from collections import deque
from pprint import pprint
from itertools import combinations


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
numbs = [x for x in range(1, N+1)]
# 최솟값 갱신해 줄 변수 초기화
min_rlt = float('inf')

# 1 ~ N 까지의 숫자 중 반만 가져와서 조합 만든거가 t1
for t1 in combinations(numbs, N//2):
    # numbs에서 t1 뺀 차집합이 t2
    t2 = list(set(numbs).difference(t1))
    # 각 팀의 능력치 더해줄 변수들
    start, link = 0, 0
    # 각 팀 숫자들에서 두 개의 숫자 조합 만들어보고 더해보자
    for t in combinations(t1, 2):
        start += matrix[t[0]-1][t[1]-1]
        start += matrix[t[1]-1][t[0]-1]
    for t in combinations(t2, 2):
        link += matrix[t[0]-1][t[1]-1]
        link += matrix[t[1]-1][t[0]-1]

    # 최솟값 갱신해줘
    min_rlt = min(min_rlt, abs(start - link))

print(min_rlt)
