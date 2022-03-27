def dfs():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in

N, M = map(int, input().split())
numbs = list(map(int, input().split()))
numbs.sort()
stack = []
