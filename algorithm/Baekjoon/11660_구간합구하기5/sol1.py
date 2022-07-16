'''
A, B, C, D 4 구간으로 나누어서 생각하자
우리가 구해야 하는 부분은 D 구간임
'''
from pprint import pprint
import sys

N, M = map(int, input().split())

# 원래 행렬 받아주기
matrix = [list(map(int, input().split())) for _ in range(N)]

# 각 열마다 행렬 합 구하기
for r in range(N):
    for c in range(N):
        if c != 0:
            matrix[r][c] += matrix[r][c-1]


# M개의 줄동안 들어오는 4개의 수 받아주기 (한 줄에 x1, y1, x2, y2 들어옴)
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 답 받아줄 변수 설정 초기화
    cnt = 0

    for k in range(x1-1, x2):
        if y1 != 1:
            cnt -= matrix[k][y1-2]
        cnt += matrix[k][y2-1]

    print(cnt)

# pprint(matrix)