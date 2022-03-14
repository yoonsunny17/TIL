'''
이거는 그냥 외우자..!
DFS, BFS를 구현하기 위해서는 트리나 그래프의 구조를 가지고 있어야 서로 연결된 노드들을 파악 가능하다
따라서 2차원 행렬을 만들고, 해당 숫자들이 연결되어 있으면 1로 표현해주는 방식으로 진행
idx 맞추기 위해 (N+1)*(N+1) 행렬을 만들자
'''

import sys

N, M, V = map(int, sys.stdin.readline().split())
# 모두 0을 가지는 이차원 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

# 간선이 연결하는 두 정점의 번호 연결시키기
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # 해당 노드들이 연결되어 있다면 행렬의 요소값을 1로 바꿔주자
    graph[a][b] = graph[b][a] = 1

# 깊이 우선 탐색 (DFS) 재귀 사용해봄
def dfs(V):
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)

# 너비 우선 탐색 (BFS) while문 사용해서 queue의 요소가 다 비워질 때까지 반복
def bfs(V):
    # 방문해야 할 곳을 순서대로 넣을 큐 생성 후 첫 정점 넣어주기
    queue = [V]

    # dfs 완료했으면 visited가 모두 1로 되어있을 것이므로 반대로 체크하기
    visited[V] = 0

    # 큐가 비워질 때까지
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0


dfs(V)
print()
bfs(V)

