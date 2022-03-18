from collections import deque
import sys

sys.stdin = open('square.txt')

# delta
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(si, sj):
    q = deque()
    room = deque()
    q.append([si, sj])
    visited[si][sj] = 1
    room.append(matrix[si][sj])

    while q:
        r, c = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 탐색 지점이 범위 내에 존재하고, 아직 방문한 적이 없으며, 원래 지점과 값 차이가 -1 또는 +1 인 경우라면
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and abs(matrix[rr][cc] - matrix[r][c]):
                q.append([rr, cc])
                visited[rr][cc] = 1
                room.append(matrix[rr][cc])

    # 출발했던 가장 작은 방 번호와, 이동한 방의 개수를 반환해줘
    return min(room), len(room)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    num = N*N  # 들어갈 수 있는 최대 숫자
    cnt = 0  # 방 몇번 이동했는지 세어 줄 변수 초기화
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                temp_num, temp_cnt = bfs(i, j)  # 재귀!
                # 이동한 방의 최대 개수와, 최소 방 번호 구하자
                if cnt < temp_cnt or cnt == temp_cnt and num > temp_num:
                    cnt = temp_cnt
                    num = temp_num

    print(f'#{tc} {num} {cnt}')
