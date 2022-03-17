from collections import deque

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]  # 고슴도치 방문기록 남겨줄 리스트
distance = [[0]*C for _ in range(R)] # 탈출 성공한 경우, 경로 반환해 줄 리스트

# delta 상 하 좌 우 표현
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque()

def bfs():
    # q가 빌 때까지 반복할거야
    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색한 지점이 범위 내에 존재하는 경우
            if 0 <= rr < R and 0 <= cc < C:
                # case 1. 고슴도치인 경우: 이동 가능한 경우를 고려하자
                if matrix[r][c] == 'S':
                    if matrix[rr][cc] == '.':
                        matrix[rr][cc] = 'S'
                        distance[rr][cc] = distance[r][c] + 1
                        q.append([rr, cc])
                    if matrix[rr][cc] == 'D':
                        rlt = distance[r][c] + 1
                        return rlt

                # case 2. 물인 경우: 물이 찰 수 있는 경우를 고려하자
                elif matrix[r][c] == '*' and (matrix[rr][cc] == '.' or matrix[rr][cc] == 'S'):
                    matrix[rr][cc] = '*'
                    q.append([rr, cc])


    # 다 돌았는데 이동경로 찾지 못한 경우
    return 'KAKTUS'
bfs()
print(bfs())
