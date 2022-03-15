import sys
from collections import deque

sys.stdin = open('pizza.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    q = deque()

    
    print(f'#{tc} ')

