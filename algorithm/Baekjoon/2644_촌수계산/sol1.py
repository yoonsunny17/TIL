from pprint import pprint
from collections import deque

n = int(input())
target1, target2 = map(int, input().split())
numb = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(numb):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)