from collections import deque
import sys
from pprint import pprint

sys.stdin = open('game.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    turn = deque()
    for _ in range(M):
        turn.append(list(map(int, input().split())))
    board = [[0]*(N+2) for _ in range(N+2)]  # index 번호랑 위치를 동일하게 해주자

    # 게임 시작할 때 흑돌 두개, 백돌 두개 놓고 시작하기
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2  # 백돌 두개!
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1  # 흑돌 두개!

    # delta 상 하 좌 우 대각선(clockwise)
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]
    print('======start======')
    pprint(board)
    print('======end======')
    while turn:
        # 위치 및 돌의 색깔 순서대로 꺼내오기
        r, c, color = turn.popleft()
        board[r][c] = color  # 해당되는 색깔의 숫자로 채워주자

        for i in range(8):
            rr = r + dr[i]
            cc = c + dc[i]
            check = []  # 색 바꿀 돌 넣어줄 리스트
            while True:  # 일단 한 방향으로 쭉 탐색해봐
                # 탐색하는 지점이 밖을 벗어난다면 안돼
                if not (0 <= rr <= N) and not (0 <= cc <= N):
                    check = []
                    break
                # 탐색 지점에 아무것도 없는 경우 바꿀게 없지
                if not board[rr][cc]:
                    check = []
                    break
                # 같은 색의 돌을 만났으면 색 바꾸는거 그만 멈 춰!
                if board[rr][cc] == color:
                    break
                # 나머지 경우 = 색깔 바꿔야하는 경우
                else:
                    check.append([rr, cc])
                
                # 한방향 탐색 반복
                rr = rr + dr[i]
                cc = cc + dc[i]

            # 탐색 끝났으면 check 안에 넣어둔 돌들의 색을 바꿔주자
            for i, j in check:
                board[i][j] = color

        ## 바뀌는거 확인 ##
        # print('======start======')
        # pprint(board)
        # print('======start======')

    # 최종적으로 각 돌의 개수를 세어주자
    black = white = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
    # pprint(board)

