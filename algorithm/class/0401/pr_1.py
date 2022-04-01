from pprint import pprint
from collections import deque


# 재귀함수로 구현해보았습니당
def dfs(v):
    # 방문했다면 출력해줘
    visited[v] = 1
    print(v, end=' ')

    # v와 연결되어있는 노드들 중에서 아직 방문하지 않았다면 재귀 돌려!
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[v][i]:
            dfs(i)


nodes = list(map(int, input().split()))
N = max(nodes)
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(0, len(nodes), 2):
    graph[nodes[i]][nodes[i+1]] = graph[nodes[i+1]][nodes[i]] = 1

dfs(1)



