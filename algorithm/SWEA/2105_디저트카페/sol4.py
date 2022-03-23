import sys

sys.stdin = open('cafe.txt')

# delta 대각선 우하, 좌하, 좌상, 우상 (clockwise)
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# DFS 함수 구현
def dfs(r, c, d, cnt):
    global rlt

    for i in range(2):
        # 방향 설정
        temp = (d + i) % 4
        rr = r + dr[temp]
        cc = c + dc[temp]

        if start_r <= rr < N and 0 <= cc < N:
            if cnt != 0 and rr == start_r and cc == start_c:
                rlt = max(rlt, cnt + 1)
                return
            # 만약 다음칸의 디저트를 먹지 않았다면
            if matrix[rr][cc] not in cafe:
                # 디저트 리스트에 추가
                cafe.append(matrix[rr][cc])
                # DFS 재귀 호출
                dfs(rr, cc, temp, cnt + 1)
                # 백트래킹 해야하므로
                # 리스트에 넣어주었던 디저트 제거
                # 스택이므로 마지막 원소를 빼주면 됨
                cafe.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최종 출력해줄 변수 초기화
    rlt = 0

    # 출발하는 지점의 범위를 지정해주자: 굳이 다 돌 필요가 없음!
    for r in range(N-1):
        for c in range(1, N-1):
            # 방문 스택 만들어주고, 처음 다녀온 카페 넣어주자
            cafe = [matrix[r][c]]
            # 출발하는 위치 변수 저장
            start_r, start_c = r, c
            # DFS 수행해주기
            dfs(r, c, 0, 0)

    print(f'#{tc} {rlt if rlt != 0 else -1}')

