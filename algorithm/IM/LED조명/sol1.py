import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pattern = list(map(int, input().split())) # 원하는 패턴

    # print(f'#{tc} ')

