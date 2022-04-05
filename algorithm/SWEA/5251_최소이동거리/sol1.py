import sys

sys.stdin = open('min_distance.txt')

T = int(input())


for tc in range(1, T + 1):
    N, E = map(int, input().split())
    for _ in range(E):
        s, e, w = map(int, input().split())

    graph = [[float('inf')]]
    
    print(f'#{tc} ')

