'''
while문 써볼까?
'''
import sys

sys.stdin = open('puzzle.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    rlt = 0

    for c in range(N):
        word = 0
        for r in range(N):
            if puzzle[r][c] == 1:
                word += 1
            else:
                if word == K:
                    rlt += 1
                word = 0
        if word == K:
            rlt += 1

    for r in range(N):
        word = 0
        for c in range(N):
            if puzzle[r][c] == 1:
                word += 1
            else:
                if word == K:
                    rlt += 1
                word = 0
        if word == K:
            rlt += 1

    print(f'#{tc} {rlt}')

