import sys
from pprint import pprint

sys.stdin = open('simulation.txt')

T = int(input())
di = (1, -1, 0, 0)
dj = (0, 0, -1, 1)
for tc in range(1, T + 1):
    N = int(input())  # 원자의 개수
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 1. 좌표**2
    for i in range(len(matrix)):
        matrix[i][0] *= 2
        matrix[i][1] *= 2
    rlt = 0

    # 좌표 끝에서 끝 -2000 ~ 2000
    for _ in range(4002):
        # 1. 좌표 이동
        for i in range(len(matrix)):
            matrix[i][0] += dj[matrix[i][2]]
            matrix[i][1] += di[matrix[i][2]]

        # 2. 좌표 중복되면 삭제 후보
        ddel, v = set(), set()
        for i in range(len(matrix)):
            cj, ci = matrix[i][0], matrix[i][1]
            if (cj, ci) in v:
                ddel.add((cj, ci))
            v.add((ci, cj))

        # 3. 삭제리스트에 있으면 삭제
        for i in range(len(matrix)-1, -1, -1):
            if (matrix[i][0], matrix[i][1]) in ddel:
                rlt += matrix[i][3]
                matrix.pop(i)

        # 하나 남았으면 끝!
        if len(matrix) < 2:
            break

    print(f'#{tc} {rlt}')

