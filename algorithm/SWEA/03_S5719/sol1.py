import sys
from collections import deque

sys.stdin = open('input_S5719.txt')

T = int(input())
for tc in range(1, T + 1):
    F, N = map(int, input().split())

    layer = deque([map(int, input().split())])

    