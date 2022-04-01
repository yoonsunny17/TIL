from pprint import pprint
from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        n = q.popleft()
        print(n, end=' ')

        for i in range(1, N+1):
            if visited[i] == 0 and graph[n][i]:
                q.append(i)
                visited[i] = 1


nodes = list(map(int, input().split()))
N = max(nodes)
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(0, len(nodes), 2):
    graph[nodes[i]][nodes[i+1]] = graph[nodes[i+1]][nodes[i]] = 1

bfs(1)
