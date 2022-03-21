import sys
from collections import deque
from pprint import pprint

sys.stdin = open('game.txt')

# delta 상 하 좌 우 대각선(clockwise)
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 4, 6, 8 중 하나
    # empty queue 생성 후 차례대로 넣어주기
    turn = deque()
    for _ in range(M):
        turn.append(list(map(int, input().split())))
    board = [[0]*(N+2) for _ in range(N+2)]  # idx와 자리 번호 동일하게 만들자

    if N == 4:
        # case1. N = 4
        board[2][2] = board[3][3] = 2
        board[2][3] = board[3][2] = 1
    elif N == 6:
        # case2. N = 6
        board[3][3] = board[4][4] = 2
        board[3][4] = board[4][3] = 1

    else:
        # case3. N = 8
        board[4][4] = board[5][5] = 2
        board[4][5] = board[5][4] = 1

    print('========original==========')
    pprint(board)
    print('========original==========')

    # 흑돌 차례인 경우
    def black():
        r = start[0]
        c = start[1]
        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색하는 지점이 범위 내에 있는데, 그 지점이 흰 돌이라면, 검은돌로 바꿀거야
            if 1 <= rr <= N and 1 <= cc <= N and board[rr][cc] == 2:
                # 단, 검은 돌 사이에 있는 흰 돌만 바꿔야 해
                while True:
                    board[rr][cc] = 1
                    r = rr
                    c = cc
                    # 바꾸다가 검은 돌을 만나는 경우 그만 바꿔
                    if board[r][c]:
                        break


    # 백돌 차례인 경우
    def white():
        r = start[0]
        c = start[1]
        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색하는 지점이 범위 내에 있는데, 그 지점이 흰 돌이라면, 검은돌로 바꿀거야
            if 1 <= rr <= N and 1 <= cc <= N and board[rr][cc]:
                # 단, 검은 돌 사이에 있는 흰 돌만 바꿔야 해
                while True:
                    board[rr][cc] = 2
                    r = rr
                    c = cc
                    # 바꾸다가 검은 돌을 만나는 경우 그만 바꿔
                    if board[r][c] == 2:
                        break


    while turn:
        start = turn.popleft()
        if start[-1]:
            board[start[0]][start[1]] = 1
            black()

        if start[-1] == 2:
            board[start[0]][start[1]] = 2
            white()

        print('=======before========')
        pprint(board)
        print('=======after========')
    # pprint(board)