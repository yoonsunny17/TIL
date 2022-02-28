from pprint import pprint
import sys

sys.stdin = open('bomb.txt')

def bomb(N, P, arr):
    # case 1. 상 하 좌 우 터뜨리기
    kill1 = 0
    for r in range(N):
        for c in range(N):
            rlt1 = 0
            v_row = [-1, 1, 0, 0]
            v_col = [0, 0, -1, 1]
            
            rlt1 += arr[r][c] # 우선 자기 자신을 더해주자
            
            # 주어진 p값만큼 이동하면서 폭탄을 터뜨리자
            for i in range(4):
                for p in range(1, P+1):
                    vr = r + v_row[i] * p
                    vc = c + v_col[i] * p

                    # range 범위 안에 있다면, rlt1 에 값 누적하기
                    if 0 <= vr < N and 0 <= vc < N:
                        rlt1 += arr[vr][vc]

            # 최댓값 구하기
            if kill1 < rlt1:
                kill1 = rlt1

    # case 2. 대각선 터뜨리기
    kill2 = 0
    for r in range(N):
        for c in range(N):
            rlt2 = 0
            c_row = [-1, 1, 1, -1]
            c_col = [1, 1, -1, -1]

            rlt2 += arr[r][c] # 우선 자기 자신을 더해주자

            # 주어진 p 값 만큼 이동하면서 폭탄을 터뜨리자
            for j in range(4):
                for p in range(1, P+1):
                    cr = r + c_row[j] * p
                    cc = c + c_col[j] * p

                    # range 범위 내에 해당되는 경우에만 rlt2에 값 누적하자
                    if 0 <= cr < N and 0 <= cc < N:
                        rlt2 += arr[cr][cc]

            # 최댓값 구하기
            if kill2 < rlt2:
                kill2 = rlt2

    # 실제 최댓값은 kill1, kill2 중에 더 큰 값
    max_kill = max(kill1, kill2)
    return max_kill


T = int(input())
for tc in range(1, T + 1):
    N, power = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # pprint(matrix)

    sol = bomb(N, power, matrix)

    print(f'#{tc} {sol}')

