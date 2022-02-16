import sys

sys.stdin = open('puzzle.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} ')

