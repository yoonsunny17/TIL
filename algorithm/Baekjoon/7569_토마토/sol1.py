import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

for _ in range(H):
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]