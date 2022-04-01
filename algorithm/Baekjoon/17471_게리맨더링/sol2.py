from collections import deque
from itertools import combinations
from pprint import pprint

N = int(input())  # 총 인구수
population = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]  # 1번 idx 부터 시작
for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

for k in range(N//2, N):
    for area in combinations(population, k):
        print(list(area))


# 굳이 둘 다 구할 필요가 없는거같기도?
# print(graph)
# area_1, area_2 = [], []
# for k in range(N//2, N):
#     for area in combinations(population, k):
#         area_1.append(list(area))
#
# lst = []
# for i in range(len(population)):
#     if population[i] not in area_1:
#         lst.append(population[i])
#         area_2.append(lst)
#                 # print(area_2) 
#                 # print('===')
# print(area_1)
# print(area_2)