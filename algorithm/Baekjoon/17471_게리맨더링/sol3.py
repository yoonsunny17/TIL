''' set에 difference 라는 좋은 기능이 있구나 .... '''

from collections import deque
from itertools import combinations
from pprint import pprint


def check(area):
    q = deque()
    visited = [0] * (N + 1)
    q.append(area[0])
    visited[area[0]] = 1

    while q:
        v = q.popleft()
        for j in graph[v]:
            if j in area and not visited[j]:
                visited[j] = 1
                q.append(j)

    return visited


def calc(A, B):
    p1, p2 = 0, 0
    # 그룹 1의 인구 수
    for a in A:
        p1 += population[a-1]
    # 그룹 2의 인구 수
    for b in B:
        p2 += population[b-1]

    # 두 그룹 인구수 차이를 구하고 반환해줘
    p = abs(p1 - p2)
    return p


N = int(input())  # 총 구역 개수
population = list(map(int, input().split()))  # 각 구역당 인구수
numbs = [x for x in range(1, N+1)]  # 각 구역 번호
graph = [[] for _ in range(N+1)]  # 각 구역이 인접해 있는 구역 나타낸 그래프
rlt = []  # 최종 값 받을 리스트

for i in range(1, N+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

# 무조건 두 그룹으로 나뉘어야 하고, 조합을 사용할 것이기 때문에 N//2까지만 돌리면 된당
for k in range(1, N//2+1):
    # numbs 에서 k 개 뽑아 만든 area_1와,
    for area_1 in combinations(numbs, k):
        # area_1과 차집합인 area_2를 만들자 !!! (difference 내장함수는 set type 에서만 적용 가능함)
        area_2 = tuple(set(numbs).difference(area_1))
        
        # 만약 각각 visited 에 체크된 1 개수가 지역 수와 같으면, 두 지역간 인구 수 차이 구해줘
        if sum(check(area_1)) + sum(check(area_2)) == N:
            # print(calc(area_1, area_2))
            rlt.append(calc(area_1, area_2))

# rlt 비어있으면 -1 반환하고, 아니면 최솟값 출력 합시당
if not len(rlt):
    print(-1)
else:
    print(min(rlt))
