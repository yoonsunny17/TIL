import sys

T = int(input())
for tc in range(1, T + 1):
    F = int(sys.stdin.readline())
    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())

        print(a, b)
