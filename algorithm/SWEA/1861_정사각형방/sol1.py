from collections import deque
import sys
from pprint import pprint

sys.stdin = open('square.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # delta
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs():
        q = deque()
        q.append



    # print(f'{tc}')