import sys

sys.stdin = open('test_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # matrix 에 존재하는 전체 0의 개수
    total = 0 # 전체 0 개수 받을 변수
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 0:
                total += 1

    # 경비원이 감시할 수 있는 통로 개수 세어 줄 변수
    danger = 0
    for r in range(N):
        for c in range(N):
            # 경비원의 위치를 파악하자!
            if matrix[r][c] == 2:
                # delta 상 하 좌 우 순서로 표시
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]
                for i in range(4):
                    for j in range(1, N): # 경비원이 확인 가능한 통로 최대 개수 = N-1
                        rr = r + dr[i] * j
                        cc = c + dc[i] * j
                        # idx가 range 안에 포함되어 계산 가능한 경우,
                        if 0 <= rr < N and 0 <= cc < N:
                            # 그리고 그 대상이 통로인 경우 cnt +1 해줘
                            if matrix[rr][cc] == 0:
                                danger += 1
                            # 그러다가 벽을 만난다면, 멈춰!
                            elif matrix[rr][cc] == 1:
                                break

    # 전체 0의 개수 - 경비가 감시하는 0의 개수 = 사각지대
    safe = total - danger
    print(f'#{tc} {safe}')

