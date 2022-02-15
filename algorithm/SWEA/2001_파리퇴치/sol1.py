import sys

sys.stdin = open('fly.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)] # N x N 이차원 리스트 만들기

    kill = [] # 죽인 파리 수 넣을 리스트 초기화
    for r in range(N-M+1):
        for c in range(N-M+1):
            fly = 0 # 몇마리 죽였는지 받을 변수
            for dr in range(M):
                for dc in range(M):
                    fly += lst[r+dr][c+dc]

            kill.append(fly)

    max_rlt = kill[0] # 죽인 파리 수의 최댓값 구하기
    for i in range(len(kill)):
        if kill[i] >= max_rlt:
            max_rlt = kill[i]

    print(f'#{tc} {max_rlt}')


