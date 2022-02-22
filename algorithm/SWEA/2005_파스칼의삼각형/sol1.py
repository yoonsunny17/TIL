import sys

sys.stdin = open('pascal.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 1 이상 10 이하
    triangle = [[0] * N for _ in range(N)] # 이중 리스트 만들기

    for i in range(N):
        for j in range(i+1):
            if i == j or j == 0:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print(f'#{tc}')
    for i in range(len(triangle)):
        for j in range(len(triangle)):
            if triangle[i][j] != 0:
                print(triangle[i][j], end=' ')
        print()


