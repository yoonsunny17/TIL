# 탈출
from collections import deque
import sys

input = sys.stdin.readline
# 방향 설정
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


# BFS 함수 선언
def BFS():
    # 물과 비버를 deque로 선언하고
    # 스타트 지점을 append 해주고
    # 처음에 물이 몇개인지 모르기에 찾은 물의 위치만큼 append
    q_biber = deque()
    q_water = deque()
    q_biber.append(biber_pos)
    for i in range(len(water_pos)):
        q_water.append(water_pos[i])

    # 반복문
    while True:
        # 비버가 더이상 움직일 수 없다면 while문 종료
        if not q_biber:
            break
        # q_water에 담겨있는 값들을 꺼내서 범위 안에 있고 탐색 범위가 .이라면
        # matrix의 . => * 바꿈
        for _ in range(len(q_water)):
            iw, jw = q_water.popleft()
            for k in range(4):
                niw = iw + di[k]
                njw = jw + dj[k]
                if 0 <= niw < r and 0 <= njw < c and matrix[niw][njw] == '.':
                    q_water.append([niw, njw])
                    matrix[niw][njw] = '*'

        # 물의 진행이 끝났으면 비버의 움직임 탐색
        # q_biber에 있는 값도 여러개 이기 때문에 for문을 돌림
        # 물의 진행이 끝나고 탐색하는 것이여서 .과 방문했는지만 조건을 설정해도
        # 모든 test case가 통과함
        # D를 만날 경우 visited의 값을 반환
        # (시작지점을 1로 잡고 출발해서 도착 바로 전 값이 결과 값)
        # 시작지점을 방문처리안하고 풀면 결과 값을 +1 처리해줘야 함
        # (방문처리안해도 상관x)
        for _ in range(len(q_biber)):
            ib, jb = q_biber.popleft()
            for k in range(4):
                nib = ib + di[k]
                njb = jb + dj[k]
                if 0 <= nib < r and 0 <= njb < c:
                    if matrix[nib][njb] == '.' and not visited[nib][njb]:
                        q_biber.append([nib, njb])
                        visited[nib][njb] = visited[ib][jb] + 1
                    if matrix[nib][njb] == 'D':
                        return visited[ib][jb]

    result = 'KAKTUS'
    return result


# 입력 선언
r, c = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
water_pos = []
biber_pos = []

# 2중 for문을 돌려 물과 비버의 스타트 지점을 찾으면 각 리스트에 추가해 주고
# 스타트 지점에도 물이 도달할 수 있어서 방문처리하고 .처리
for i in range(r):
    for j in range(c):
        if matrix[i][j] == '*':
            water_pos.append([i, j])
        if matrix[i][j] == 'S':
            biber_pos.extend([i, j])
            matrix[i][j] = '.'
            visited[i][j] = 1

print(BFS())