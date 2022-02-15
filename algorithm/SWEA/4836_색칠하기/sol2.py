import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 칠할 영역 개수
    arr = [[0]*10 for _ in range(10)] # 10 x 10 이차원 리스트 만들기// 모든 요소는 0으로 초기화
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # 두 좌표와 R or B를 나타내는 정보 받기

        # color == 1 : RED, color == 2 : BLUE
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1: # red인 경우
                    arr[r][c] += 1 # 해당 영역에 1 더해주기

                if color == 2: # blue인 경우
                    arr[r][c] += 2 # 해당 영역에 2 더해주기

    # 리스트 요소값이 3이라면, 보라색인 영역이므로 cnt += 1
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
