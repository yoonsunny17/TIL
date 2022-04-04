''' success code '''
''' BFS 변형 '''
''' 최소 가중치를 갱신해 나가는 방향으로 풀어나가자! '''
import sys

sys.stdin = open('supply.txt')


def bfs(si, sj, ei, ej):
    q = []  # q 생성해주기
    # 방문 기록 남길 리스트 만들고, 초기값은 충분히 큰 값으로 지정!
    # 최솟값 갱신 해야 하기 때문에!
    visited = [[float('inf')]*N for _ in range(N)]

    q.append((si, sj))
    visited[si][sj] = matrix[si][sj]
    # delta 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        ci, cj = q.pop(0)
        # 네방향, 8방향, 숫자차이가 일정값 이하
        for i in range(4):
            ni = ci + dr[i]
            nj = cj + dc[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[ci][cj] + matrix[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + matrix[ni][nj]

    return visited[ei][ej]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0, 0, N-1, N-1)

    print(f'#{tc} {ans}')