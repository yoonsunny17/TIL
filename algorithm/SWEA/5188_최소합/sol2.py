import sys

sys.stdin = open('min_sum.txt')


def f(r, c, cnt):
    global min_sum
    
    # 함수 호출하면 일단 값부터 갱신해줘
    cnt += matrix[r][c]

    # 만약에 오른쪽 아래에 도착했다면, 최솟값 갱신해주자
    if r == N-1 and c == N-1:
        if cnt < min_sum:
            min_sum = cnt
            return

    # 만약 갱신된 최솟값보다 현재 돌고있는 cnt 값이 더 크면 그만해.. 안돌아도 돼!
    if cnt > min_sum:
        return

    # 우/하 두 방향에 대해서 탐색해봐
    for i in range(2):
        rr = r + dr[i]
        cc = c + dc[i]
        # 탐색 지점이 범위 내에 존재한다면, 재귀함수 호출해!
        if 0 <= rr < N and 0 <= cc < N:
            f(rr, cc, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 987654321

    # 왼쪽 위에서 오른쪽 아래로 탐색하는 것이므로, 우/하 방향만 탐색하면 된다
    dr = [0, 1]
    dc = [1, 0]
    
    # 시작지점 row = 0, col = 0, cnt = 0
    f(0, 0, 0)
    print(f'#{tc} {min_sum}')

