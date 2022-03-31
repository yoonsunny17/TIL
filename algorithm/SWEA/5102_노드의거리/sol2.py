import sys

sys.stdin = open('node.txt')


def bfs(start):
    q = []
    visited[start] = 1
    q.append(start)

    while q:
        node = q.pop(0)
        for i in range(1, V+1):
            if i in graph[node] and not visited[i]:
                visited[i] = visited[node] + 1
                q.append(i)

    return visited


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    visited = [0] * (V+1)

    bfs(S)
    print(f'#{tc} {(visited[G]-1) if visited[G] !=  0 else 0}')
    # if visited[G] != 0:
    #     print(visited[G]-1)
    # else:
    #     print(-1)
