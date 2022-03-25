from pprint import pprint
from collections import deque
import sys

sys.stdin = open('microbe.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 셀의 개수, 격리 시간, 미생물 군집의 개수
    groups = deque()  # idx 1번부터 시작하게 하려고 앞에 빈 리스트 만들어주기~
    for i in range(K):
        group = list(map(int, input().split()))  # row, col, microbe, delta
        groups.append(group)


    # 미생물들 놓아줄 이차원 리스트 만들기
    matrix = [[0]*N for _ in range(N)]
    # 경로 탐색해야 하니까 queue도 만들어주자!!!
    q = deque()

    # matrix edge 부분은 -1 처리 해주기!
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i == N-1 or j == N-1:
                matrix[i][j] = -1

    # 미생물의 첫 출발 지점 위치에 초기 미생물 수 입력해주자
    for i in range(1, len(groups)):
        row = groups[i][0]
        col = groups[i][1]
        num = groups[i][2]
        d = groups[i][3]
        for r in range(N):
            for c in range(N):
                if r == row and c == col:
                    matrix[r][c] = num
                    q.append([r, c])

    # M시간 후, 남아있는 미생물 수를 구해야 함
    def survive(M, K, matrix, d, groups):

        # delta 상 하 좌 우 = 1, 2, 3, 4
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        # 시간 다 지났으면 리턴! (종료조건)
        if not M:
            return
        # 아직 시간이 지나지 않았다면, 미생물들이 움직이겠지
        else:
            for microbe in groups:
                # 위로 이동하는 경우
                if microbe[-1] == 1:


        while q:
            q.popleft()





    # print(q)
    # pprint(matrix)
    # print(groups)
    # print()