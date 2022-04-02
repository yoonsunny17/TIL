from collections import deque
from itertools import combinations
from pprint import pprint


def dfs(v):
    # v랑 연결된 노드 중에서
    for j in graph[v]:
        # 그 노드가 지금 내가 확인하려는 조합 안에 있고, 방문한 적 없으면
        if j in rlt and not visited[j]:
            visited[j] = 1  # 방문 기록 남기고
            dfs(j)  # dfs 돌리자


N = int(input())  # 총 인구수
population = list(map(int, input().split()))
total_population = sum(population)  # 총 인구수
numbs = [x for x in range(1, N+1)]
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

pprint(graph)


for k in range(N//2, N):
    for area in combinations(numbs, k):
        rlt = list(area)
        print(rlt)
        for v in rlt:
            if not visited[v]:
                dfs(v)
        rlt2 = []
        for numb in numbs:
            if numb not in rlt:
                rlt2.append(numb)
                for v in rlt2:
                    if not visited[v]:
                        dfs(v)

        print(visited)


# rlt2 = []
# if numbs[i] not in rlt:
#     rlt2.append(numbs[i])
#     for v in rlt2:
#         if not visited[v]:
#             dfs(v)




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