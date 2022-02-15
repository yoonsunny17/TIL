from pprint import pprint
import sys

sys.stdin = open('snail.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)] # N x N 이차원 리스트
    r = c = 0 # matrix[0][0] 부터 시작
    # 달팽이 행렬 규칙 => 우 하 좌 상 순서로 숫자 들어감
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    idx = 0 # di, dj의 idx 값 초기화

    for n in range(1, N**2 + 1): # 1부터 N*N까지 숫자 넣어주어야 함
        matrix[r][c] = n
        r += di[idx]
        c += dj[idx]

        # indexError 또는 이미 값이 들어있는 요소 만나는 경우 방향 틀기
        if r < 0 or c < 0 or r >= N or c >= N or matrix[r][c] != 0:
            # 일단 r, c 초기화
            r -= di[idx]
            c -= dj[idx]
            
            # idx 는 0, 1, 2, 3을 순환함; 초기화 값이 0이었으므로 그 다음값은 1
            idx = (idx + 1) % 4 # 뺑뺑이 코드 꼭 숙지 하고 있어야 함!!!!
            r += di[idx]
            c += dj[idx]

    print(f'#{tc}')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()