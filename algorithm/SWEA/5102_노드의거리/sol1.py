import sys
from collections import deque

sys.stdin = open('node.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    for i in range(E):
        nodes = list(map(int, input().split()))
    S, G = map(int, input().split())
    # 방문 리스트 만들어주기; idx 보기 쉽게 +1 해줌!
    visited = [0] * (V+1)

    def bfs(node):
        q = deque()
        q.append(node)
        visited[node] = 1

        while q:
            node = q.popleft()
            if node