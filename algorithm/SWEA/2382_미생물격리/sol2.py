import sys
from pprint import pprint
from collections import deque

sys.stdin = open('microbe.txt')


# 이제 M 시간동안 이동을 반복해주면 될듯
def survive(N, M):

    while M != 0:
        r, c, num, dir = groups.popleft()  # 군집 하나씩 꺼내와서 이동 시켜보자
        M -= 1
        # 주어진 방향대로 나아가야 해~~
        for i in range(4):
            rr = r + dr[dir - 1]
            cc = c + dc[dir - 1]
            # 한시간 지났을 때 이동한 위치가 어떤지에 따라 경우를 나누어서 생각해보자
            # case 1. 가면 안될 곳을 간 경우 = 미생물 수//2, 방향 반대로 바꿔!
            if not rr or not cc or rr == N - 1 or cc == N - 1:
                num = num // 2
                dir = opp[dir]
                groups.append([rr, cc, num, dir])
            # case 2. 다른 군집과 같은 위치에서 만날 경우 = 미생물 수 합치고, 원래 미생물 수 많았던 군집의 이동방향을 따르자
            if matrix[rr][cc] > 0:
                if matrix[rr][cc] > num:  # 나보다 큰 군집을 만난 경우
                    dir = 0
                else:
                    dir = dir  # 나보다 작은 군집을 만난 경우
                matrix[rr][cc] += num
                groups.append([rr, cc, num, dir])
            # case 3. 나머지 경우 = 다른 군집과 만나지 않고, 안전한 위치에서 이동하는 경우
            if 0 < rr < N - 1 and 0 < cc < N - 1 and not matrix[rr][cc]:
                matrix[rr][cc] = num
                groups.append([rr, cc, num, dir])
            # case 4. 미생물이 다 없어진 경우, pop 하고 끝
            if num == 0:
                continue

    return matrix


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 각 군집들에 대한 정보들을 받을 queue 생성 후 초기 정보 넣어주자!
    groups = deque()
    for i in range(K):
        group = list(map(int, input().split()))
        groups.append(group)

    # 미생물들이 이동할 수 있는 matrix 만들기
    matrix = [[0]*N for _ in range(N)]
    # 그리고 edge 부분들은 위험한 부분임을 표시하기 위해 -1 로 표시해주자
    for i in range(N):
        for j in range(N):
            if not i or not j or i == N-1 or j == N-1:
                matrix[i][j] = -1

    # 미생물들의 첫 출발 지점에 초기 미생물 수 입력해주자
    for i in range(len(groups)):
        row = groups[i][0]
        col = groups[i][1]
        num = groups[i][2]
        matrix[row][col] = num

    # delta 상 하 좌 우 = 1, 2, 3, 4
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # opposite direction
    dir = [0, 1, 2, 3, 4]
    opp = [0, 2, 1, 4, 3]

    rlt = 0
    for i in range(N):
        for j in range(N):
            if not i or not j or i == N-1 or j == N-1:
                continue
            else:
                rlt += matrix[i][j]

    print(rlt)

    pprint(matrix)
    print()
    pprint(groups)
    # while groups:
    #     rlt = groups.popleft()
    #     print(rlt)
    # print(f'#{tc} ')

