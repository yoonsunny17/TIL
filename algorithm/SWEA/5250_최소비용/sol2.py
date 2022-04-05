''' 다익스트라로 풀어보자 !!! '''
import sys
from collections import deque

sys.stdin = open('minimum.txt')

def dijkstra(s, V):
    visited = [0] * (V+1)

    visited[s] = 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    D = [0] * (N+1)
    dijkstra(0, V)

    print(f'#{tc} {rlt}')

