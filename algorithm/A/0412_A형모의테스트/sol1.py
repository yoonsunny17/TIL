import sys
from pprint import pprint

sys.stdin = open('algo1_input.txt')


def dfs(r, c, idx, rlt):
    global max_rlt

    if idx == 4:
        if max_rlt < rlt:
            max_rlt = max(max_rlt, rlt)

    else:
        for i in range(6):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재할 때
            if 0 <= rr < 2*H and 0 <= cc < W:
                # 근데 만약 그 지점의 값이 0이면 continue
                # if new_matrix[rr][cc] == 0:
                #     continue
                if new_matrix[rr][cc] == 0:
                    continue

                # 0이 아니고, 방문한 적이 없는 곳이라면
                if new_matrix[rr][cc] != 0 and not visited[rr][cc]:
                    visited[rr][cc] = 1
                    dfs(rr, cc, idx+1, rlt + new_matrix[rr][cc])
                    dfs(r, c, idx+1, rlt + new_matrix[rr][cc])  # fuck you!!!!
                    visited[rr][cc] = 0


T = int(input())
for tc in range(1, T + 1):
    W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    new_matrix = [[0]*W for _ in range(2*H)]

    # 원래 matrix에 대해 생각해봐
    for i in range(H):
        for j in range(W):
            # j idx가 짝수라면 윗줄에, 홀수면 아랫줄에 적어줘
            if not j % 2:
                new_matrix[i*2][j] = matrix[i][j]
            else:
                new_matrix[i*2+1][j] = matrix[i][j]

    # new_matrix에 대해 dfs 돌릴거야
    visited = [[0]*W for _ in range(2*H)]
    max_rlt = 0  # 최댓값 받아줄 변수 초기화

    # delta 탐색 방향은 좌 우 제외하고,,, 상 하 대각선 (clockwise)
    dr = [1, 2, 1, -1, -2, -1]
    dc = [1, 0, -1, -1, 0, 1]

    # dfs + backtracking 쓸거임

    for x in range(2*H):
        for y in range(W):
            # 0 이 아닌 경우에만!
            if new_matrix[x][y]:
                visited[x][y] = 1
                dfs(x, y, 1, new_matrix[x][y])
                visited[x][y] = 0

    pprint(new_matrix)
    print(f'#{tc} {pow(max_rlt, 2)}')