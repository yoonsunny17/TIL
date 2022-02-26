from pprint import pprint
import sys

sys.stdin = open('cake.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    pprint(matrix)
    # print(f'#{tc} ')

