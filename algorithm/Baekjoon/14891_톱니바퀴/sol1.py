from collections import deque
from pprint import pprint
from itertools import combinations

numbs = [list(map(int, input().split())) for _ in range(4)]
K = int(input())
for _ in range(K):
    info = list(map(int, input().split()))