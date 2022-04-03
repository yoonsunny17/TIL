import sys
sys.setrecursionlimit(10**6)


def dfs(v):
    # 방문기록을 남겨주자
    visited[v] = 1
    
    # 해당 노드와 연결되어있는 노드들 중에서,
    for i in graph[v]:
        # 아직 방문한 적이 없다면,
        if not visited[i]:
            # dfs 재귀 호출해줘요
            dfs(i)


N, M = map(int, input().split())
# 인접행렬 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0]*(N+1)
cnt = 0  # connected component 개수 세어줄 변수 초기화
# print(graph)
# print(visited)

for i in range(1, N+1):  # 1 부터 N 의 노드 중 i 노드에 대해서
    if not visited[i]:  # i 노드에 방문하지 않았다면
        dfs(i)  # dfs를 해줘!
        cnt += 1  # dfs 탐색이 끝났다 = connected component 하나 찾았다

print(cnt)
