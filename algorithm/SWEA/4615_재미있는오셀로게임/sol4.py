import sys
from collections import deque
from pprint import pprint

sys.stdin = open('game.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # turn queue; row, col, color 받아줌
    turn = deque()
    for _ in range(M):
        turn.append(list(map(int, input().split())))
    # pprint(turn)

    # 오셀로 보드판을 만들자! 단, idx와 주어진 순서가 동일하도록 만들자
    board = [[0]*(N+2) for _ in range(N+2)]

    # 시작 전 흰돌 2개, 검은돌 2개 놓고 시작하자
    # 검은 돌 = 1, 흰 돌 = 2
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1

    # delta 상 하 좌 우 대각선(clockwise)
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]

    # 이제 차례대로 돌을 놓을거야
    while turn:
        r, c, color = turn.popleft()
        # 갇힌 돌 저장해 줄 리스트 생성
        check = []
        board[r][c] = color
        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]
            # 일단 한방향으로 탐색 진행해야 해!
            while True:
                # 탐색 지점에 아무것도 없는 경우
                if not board[rr][cc]:
                    check = []  # 아예 초기화를 해줘!
                    break
                # 그 지점에 같은 색의 돌을 만났다면
                if board[rr][cc] == color:
                    break  # 그만 바꿔주고 다음 차례로 넘어가줘
                # 만약 모서리에 돌이 들어가면 못바꿔줘
                if rr == 1 or rr == N or cc == 1 or cc == N:
                    check = []
                    break
                # 나머지 경우에는 돌을 바꿔주어야 하니까, 일단 리스트에 저장해줘
                else:
                    check.append([rr, cc])

                # 한방향 탐색 끝났으면 다른 방향으로 탐색 하자
                rr = rr + dr[i]
                cc = cc + dc[i]

            # 탐색을 다 했다면, 돌을 바꿔주야지
            for x, y in check:
                if color == 1:
                    board[x][y] = 2
                if color == 2:
                    board[x][y] = 1



        # 검은 돌, 흰 돌 개수 세어줄 변수 초기화
        black = white = 0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if board[i][j] == 2:
                    white += 1
                if board[i][j] == 1:
                    black += 1

        print(f'#{tc} {black} {white}')
        print('==========start============')
        pprint(board)
        print('==========end============')

