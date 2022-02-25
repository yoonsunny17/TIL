import sys

sys.stdin = open('bomb.txt')

T = int(input()) # tc수 = 1

for tc in range(1, T + 1):
    # N= N*N행렬, P=차르봄바의 위력
    N, P = map(int, input().split())
    #print(N, P)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 본인 포함 상하좌우 OR 본인 포함 대각선 4쪽 합의 더 큰 값을 구하는것

    r = [-1, 1, 0, 0]
    c = [0, 0, -1, 1]

    # c_sum = 0
    max_sum = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            c_sum = 0
            c_sum += arr[i][j]
            for p in range(1, P+1):
                for d in range(len(r)):
                    rp = i+ (r[d] * p)
                    cp = j+ (c[d] * p)
                    if 0 <= rp < N and 0 <= cp < N:
                        c_sum += arr[rp][cp]
                    # if rp < 0 or rp > N-1 or j + cp < 0 or j + cp > N-1:
                    #     continue
                    # else:
                    #     c_sum += arr[rp][cp]

            if max_sum <= c_sum:
                max_sum = c_sum


    # 대각선
    r = [-1, 1, 1, -1]
    c = [1, 1, -1, -1]

    # x_sum = 0


    for i in range(len(arr)):
        for j in range(len(arr[0])):
            x_sum = 0
            x_sum += arr[i][j]
            for p in range(1, P + 1):
                for d in range(len(r)):
                    rp = i + (r[d] * p)
                    cp = j + (c[d] * p)
                    if 0 <= rp < N and 0 <= cp < N:
                        x_sum += arr[rp][cp]
                    # if rp < 0 or rp > N - 1 or j + cp < 0 or j + cp > N - 1:
                    #     continue
                    # else:
                    #     x_sum += arr[rp][cp]

            if max_sum <= x_sum:
                max_sum = x_sum


    print(f'#{tc} {max_sum}')
