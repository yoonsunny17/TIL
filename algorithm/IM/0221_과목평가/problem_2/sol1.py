import sys
from pprint import pprint

sys.stdin = open('input_prob_2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # case 1. 3 x 3 배열 합 구하기 => 9개 안되면 0 출력
    max_rlt1 = 0
    for r in range(N):
        for c in range(N):
            rlt1 = 0 # 각 원소 중심으로 합 초기화 되니까! 여기서 변수 설정
            cnt = 0 # 9개 모두 더해졌는지 확인해줄 변수
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r+i < N and 0 <= c+j < N:
                        rlt1 += matrix[r+i][c+j]
                        cnt += 1

            if cnt == 9: # 3 x 3 합 조건 만족하는 경우,
                if max_rlt1 < rlt1:
                    max_rlt1 = rlt1
                    
    # case 2. 4 방향 원소 합 구하기
    max_rlt2 = 0
    for r in range(N):
        for c in range(N):
            rlt2 = 0
            rlt2 += matrix[r][c] # 우선 자기 자신 먼저 더해주기
            power = matrix[r][c] # 더해줄 range 설정
            # delta 상 하 좌 우 순서로 표현
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            # IndexError 조심
            for i in range(4):
                for p in range(1, power): # dr * p , dc * p 이고, power - 1 까지
                    if 0 <= r + dr[i] * p < N and 0 <= c + dc[i] * p < N:
                        rlt2 += matrix[r+dr[i]*p][c+dc[i]*p]

            if max_rlt2 < rlt2:
                max_rlt2 = rlt2

    if max_rlt1 >= max_rlt2:
        print(f'#{tc} {max_rlt1}')
    else:
        print(f'#{tc} {max_rlt2}')


