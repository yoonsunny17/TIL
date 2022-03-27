import sys
from pprint import pprint
from collections import deque

sys.stdin = open('microbe.txt')

# delta 상 하 좌 우 1 2 3 4
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상 하 좌 우 방향 번호 및 거꾸로 바뀔 때 번호 표현해주기
dire = [0, 1, 2, 3, 4]
opp = [0, 2, 1, 4, 3]


# bfs 를 구현해주고, M만큼 반복해주는 식으로 하자
def bfs(N, M):
    # groups = 초기 위치 들어있는 큐

    # groups 이 빌 때까지 반복해줘
    while M != 0:
        r, c, num, d = groups.popleft()  # row, col, numbers, direction 꺼내기
        M -= 1
        for d in dire[1:]:
            rr = r + dr[d - 1]
            cc = c + dc[d - 1]
            # case 1. 이동하려는 지점이 matrix edge 지점인 경우 = 미생물 수//2, 방향 반대로!
            if 0 <= rr < N and 0 <= cc < N and not rr or not cc or rr == N-1 or cc == N-1:
                num = num//2
                d = opp[d]
                matrix[rr][cc] = num
                groups.append([rr, cc, num, d])
            # case 2. 이동하려는 지점에서 다른 군집들을 만나는 경우
            if 0 < rr < N-1 and 0 < cc < N-1 and matrix[rr][cc] > 0:
                # 나보다 큰 군집을 만난 경우라면, 그 군집에게 흡수되고 사라져 ㅠㅠ
                if matrix[rr][cc] > num:
                    matrix[rr][cc] += num
                # 나보다 작은 군집을 만난 경우라면, 그 군집을 흡수해!
                else:
                    num += matrix[rr][cc]
                    matrix[rr][cc] += num
                    groups.append([rr, cc, num, d])
            # case 3. 나머지 경우 = edge도 아니고, 다른 군집을 만나지도 않는 경우
            if 0 < rr < N-1 and 0 < cc < N-1 and not matrix[rr][cc]:
                matrix[rr][cc] = num
                groups.append([rr, cc, num, d])


    # 끝나면 matrix를 반환해보자
    return matrix, groups


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    groups = deque()  # 각 군집들의 정보들을 받을 큐 생성!!
    for _ in range(K):
        groups.append(list(map(int, input().split())))
    # pprint(groups)

    # 미생물들의 위치를 표현해 줄 이차원 리스트 만들기
    matrix = [[0]*N for _ in range(N)]

    for i in range(len(groups)):
        row = groups[i][0]
        col = groups[i][1]
        matrix[row][col] = groups[i][2]

    pprint(bfs(N, M))