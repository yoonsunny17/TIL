from collections import deque
from pprint import pprint


def cleaning(r, c, d):
    global cnt
    
    # 만약 현재 지점이 빈 칸인 경우, 청소 해주고 개수 세어줘
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        cnt += 1
        
    # 그 다음에 로봇의 사방을 탐색할건데,
    for _ in range(4):
        # 우선 왼쪽으로 회전시킨 후 탐색해줘
        dd = (d+3) % 4
        rr = r + dr[dd]
        cc = c + dc[dd]

        # 만약 그 지점이 아직 청소 안한 곳이라면,
        if matrix[rr][cc] == 0:
            # 재귀함수 호출해서 청소 시켜줘
            cleaning(rr, cc, dd)
            return

        # if문 안에서 dd에 대해 왼쪽 다 회전 탐색 했으면, 새로운 방향으로 갱신해줘
        d = dd
        
    # for문을 나왔다 = 청소 안한 곳이 없다
    # 후진을 해야한다
    dd = (d+2) % 4
    rr = r + dr[dd]
    cc = c + dc[dd]
    # 만약 후진했는데 그 위치가 벽이면 청소 끝!
    if matrix[rr][cc] == 1:
        return
    # 벽은 아니고 이미 청소한 부분이면 다시 청소할 수 있는지 찾으러 가자
    else:
        cleaning(rr, cc, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0 = 빈칸 (청소해야함), 1 = 벽
matrix = [list(map(int, input().split())) for _ in range(N)]

# delta 북(0) 동(1) 남(2) 서(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
cleaning(r, c, d)

print(cnt)
