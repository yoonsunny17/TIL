from collections import deque
from itertools import combinations
from pprint import pprint
from time import time

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# delta 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# stack = deque()
# stack.append([0, 0])
# visited[0][0] = 1

max_cnt = 0
max_rlt = 0
min_cnt = float('inf')


# 가운데 손가락 모양 빼고 네개에 대한 dfs
# row, col, 테트리스 네개 숫자 담아줄 cnt 리스트
def tetris(r, c, idx, cnt):
    global max_cnt

    # 리스트에 숫자 네개가 담겼다면,
    if idx == 4:
        if max_cnt < cnt:
            max_cnt = max(max_cnt, cnt)

    else:
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and not visited[rr][cc]:
                visited[rr][cc] = 1
                tetris(rr, cc, idx+1, cnt+matrix[rr][cc])
                visited[rr][cc] = 0


# 가운데 손가락 모양...이거 골칫덩어리구만
# 생각해보면 matrix의 edge 부분 빼고는 모든 부분을 중심을 해서 네방향 탐색을 시킬 수 있음
# case 1. 네방향 탐색을 했는데, 한 방향이 index 벗어나서 세방향 탐색밖에 못하는 경우 => 그냥 그대로 더하기
# case 2. 네방향 모두 탐색가능한 경우, sort 해서 slicing으로 큰것들만 더하기
# 그다음에 최댓값 갱신시키기
def cross(r, c):
    global max_rlt

    rlt = 0
    center = matrix[r][c]  # 중심 원소값
    d_lst = []  # 네방향 탐색 후 숫자 넣어줄 리스트

    # 리스트에 숫자가 세개 담겨 있는 경우
    if len(d_lst) == 3:
        rlt = center + sum(d_lst)
    # if len(d_lst) == 3:
    #     d_lst.append(center)
    #     return d_lst
        # 최댓값 갱신 가능하면 갱신해주기
        # rlt = center + sum(d_lst)
        # if rlt > max_rlt:
        #     max_rlt = max(max_rlt, rlt)

    if len(d_lst) == 4:
        d_lst.sort()
        rlt = center + sum(d_lst[1:])
    # 리스트에 숫자가 네개 담겨있는 경우 = 네방향 탐색 가능한 경우
    # if len(d_lst) == 4:
    #     # 오름차순 정렬 후 맨 앞에 있는 작은 수 빼고 더해준 뒤, 최댓값 갱신해주기
    #     d_lst.sort()
    #     d_lst = d_lst[1:]
    #     # d_lst.append(center)
    #     return d_lst
        # rlt = center + sum(d_lst[1:])
        # if rlt > max_rlt:
        #     max_rlt = max(max_rlt, rlt)

    else:
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위에 존재하는 경우라면 탐색 리스트에 숫자 담아주기
            if 0 <= rr < N and 0 <= cc < M:
                d_lst.append(matrix[rr][cc])

    if rlt > max_rlt:
        max_rlt = max(max_rlt, rlt)
    return rlt

# def cross(r, c):
#     d_lst = []
#
#     for i in range(4):
#         rr = r + dr[i]
#         cc = c + dc[i]
#         if 0 <= rr < N and 0 <= cc < M:



for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        tetris(i, j, 1, matrix[i][j])
        visited[i][j] = 0


# ans = max(max_rlt, max_cnt)
# print(ans)