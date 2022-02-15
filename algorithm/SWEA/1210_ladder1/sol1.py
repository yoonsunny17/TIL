import sys

sys.stdin = open('ladder1.txt')


T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]

    # delta
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    idx = 0 # 0 = up, 1 = left, 2 = right

    # 도착점에서 출발점으로 역으로 탐색할 것
    # row = 99 시작, arr[99][c] == 2 만족하는 c값 구하기
    for j in range(102):
        if arr[99][j] == 2:
            c = j
    r = 99

    while True:
        # 종료조건 먼저 설정
        if r == 0 and arr[0][c] == 1:
            rlt = c-1 # padding으로 양옆에 0, 0 붙여주었으므로 -1 해주기
            break

        # 왼쪽에 1 있으면 왼쪽으로 가다가 0나오면 stop
        # indexError 조심할 것
        if arr[r][c-1]:
            idx = 1
            while True:
                r += dr[idx]
                c += dc[idx]
                if arr[r][c-1] == 0:
                    break

        # 오른쪽에 1 있으면 오른쪽으로 가다가 0나오면 stop
        # indexError 조심할 것
        elif arr[r][c + 1]:
            idx = 2
            while True:
                r += dr[idx]
                c += dc[idx]
                if arr[r][c + 1] == 0:
                    break

        # 왼쪽, 오른쪽에 1 발견하지 못했으면 위쪽으로 직진
        idx = 0
        r += dr[idx]
        c += dc[idx]

    print(f'#{tc} {rlt}')