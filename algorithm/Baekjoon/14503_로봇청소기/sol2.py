import sys

sys.stdin = open('input.txt')

# 로봇 청소기
# N X M 행렬
# 청소한 구역은 2

# r = row, c = column
# d = 방향 0북(-1, 0) / 1동(0, 1) / 2남(1, 0) / 3서(0, -1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# robot_clean 함수
def robot_clean(x, y, d):
# global 변수로 둬서 함수 내에서 자유롭게 사용
    global ans
# 현재 위치 청소
    if data[x][y] == 0:
        data[x][y] = 2
        ans += 1
# 현재 방향 기준 왼쪽 방향부터 차례대로 탐색
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
# 탐색 도중 청소하지 않은 공간이 있을 시 재귀 함수로 호출
        if data[nx][ny] == 0:
            robot_clean(nx, ny, nd)
            return
            # 최종 리턴 위치 (아래 리턴을 하더라도 결국 여기를 리턴해야 맞는 함수)
            # 만약에 여기 리턴이 없다면 추가로 작동해서 원하던 작동보다 더 하게됨
        d = nd
# 네방향에 청소할 공간이 없으면 아래 코드 시작
# 후진 방향이 벽이 있는지 체크
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == 1:
        return # 벽이 있다면 함수 종료
# 후진 방향에 벽이 없다면 재귀함수 호출
    robot_clean(nx, ny, d)


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    ans = 0
    robot_clean(x, y, d)

    print(ans)