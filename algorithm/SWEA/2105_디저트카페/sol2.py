### 진환이 코드 보면서 연습...! ###
import sys

sys.stdin = open('cafe.txt')

# delta 대각선 우하, 좌하, 좌상, 우상 (clockwise)
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


# DFS 함수 구현
def dfs(r, c, d, cnt):
    global rlt

    # 현재 노드에서 우하단 방향으로 시작해서
    # 시계방향으로 탐색한다고 가정하면,탐색 방향은 두 가지로 고정됨
    # 예를들어 우하단으로 시작 -> 다음 탐색 방향은 우하단 or 좌하단
    # 이렇게 해도 모든 탐색의 경우의 수를 체크할 수 있음이 보장됨
    for i in range(2):
        # 방향 설정
        temp = (d + i) % 4
        # 다음칸
        rr, cc = r + dr[temp], c + dc[temp]
        # 우하단 방향으로 시작해서 시계방향으로
        # 시작 칸으로 돌아온다고 가정했으므로
        # 시작 칸의 행의 위쪽은 탐색할 필요 없음
        if start_r <= rr < N and 0 <= cc < N:
            # 종료 조건
            # 2개 이상의 디저트를 먹고 시작칸으로 돌아왔을 경우
            if cnt != 0 and rr == start_r and cc == start_c:
                rlt = max(rlt, cnt + 1)
                return
            # 다음칸 탐색
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