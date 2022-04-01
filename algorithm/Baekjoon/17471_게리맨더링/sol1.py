from itertools import combinations

N = int(input())
numbs = [x for x in range(1, N+1)]
population = [0] + list(map(int, input().split()))
total_sum = sum(population)  # 총 인구수!
graph = [[] for _ in range(N+1)]
nodes = []
for i in range(1, N+1):
    info = list(map(int, input().split()))
    nodes = info[1:]
    graph[i] = nodes

# print(graph)
# graph idx = 해당 노드 번호, 내부 요소 = 해당 노드에 연결되어 있는 노드들

# N개 중에서 (1, N-1) (2, N-2) ... 조합가능한 것 생각해보기
for k in range(N//2, N):
    for comb1 in combinations(numbs, k):
        print(comb1)  # 이제 조합으로 묶인 노드들이 인접해있는지 확인 해주자 (dfs)
# 1 ~ N//2 까지 가능한 조합 경우의 수 생각하면 될 것 같음
# 각 조합 경우의 수 중에서, DFS 돌려서 노드들이 연결되어있는ㅈ ㅣ확인

def dfs(elem1):
    stack = []
    stack.append(elem1)
    elem2 = tuple()
    for numb in numbs:
        if numb not in elem1:
            elem2.add(numb)
    stack.append(elem2)

    visited = [0] * (N+1)

    while stack:
        vertex = stack.pop()  # elem1 = (1, 2, 3)
        for v in vertex:


    # while stack:
    #     vertex = stack.pop()
    #     for v in vertex:
    #         if v in graph[v]:

# 연결 안되어있으면 break
# 최솟값보다 큰 경우 break
# 연결 되어있으면 인구수 합 계산 및 결과값 도출
# 최솟값 갱신
# 모든 조합 경우의 수 돌 때까지 반복