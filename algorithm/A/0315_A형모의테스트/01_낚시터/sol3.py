import sys
from collections import deque

sys.stdin = open('fish.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(3)]
    visited = [0 for _ in range(N+1)]

    # delta column 만 고려
    dc = [-1, 1]

    def bfs():
        q = deque()
        turn = 100
        for i in range(3):
            if matrix[i][1] < turn:
                turn = matrix[i][1]
                seat = matrix[i][0]
                q.append([seat, turn])
                visited[seat] = 1

        # q가 빌 때까지 반복할거야
        while q:
            c, p = q.popleft()
            # column만 고려
            for i in range(2):
                cc = c + dc[i]
                # cc가 범위 내에 존재하고, 아직 방문기록이 없는 곳이라면
                if 1 <= cc <= N and not visited[cc]:
                    # 자리에 앉혀놓고, 사람 한명 빼고, q에 저장해줘
                    visited[cc] = visited[c] + 1
                    p -= 1
                    q.append([cc, p])

                # 사람을 다 앉혔다면 visited 를 반환해줘
                if 1 <= cc <= N and p == 0:
                    return visited

        return bfs()

    print(f'#{tc} {sum(bfs())}')
    # print(bfs())

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(3)]
#     visited = [[0]*(N+1)]
#     cnt = 0
#
#     # delta 좌 우만 고려하면 될듯 (c만 고려)
#     dc = [-1, 1]
#
#     q = deque()
#     turn = 100 # 낚시꾼 최솟값 구하기 위해 초기화하기
#     for i in range(3):
#         if lst[i][1] < turn:
#             turn = lst[i][1]
#             q.append([lst[i][0], lst[i][1]]) # [10, 2] 저장
#             visited[lst[i][0]] = 1 # 10번자리 방문기록 남김
#
#     def bfs():
#         # q가 빌 때까지
#         while q:
#             c, p = q.popleft()
#             for i in range(2):
#                 cc = c + dc[i]
#                 # idx가 범위 내에 존재하고, 아직 방문한 적이 없는 곳인 경우,
#                 if 1 <= cc <= N and not visited[cc]:
#                     # 거리를 누적시키고
#                     visited[cc] = visited[c] + 1
#                     # 사람 한명 빼주고
#                     pp = p - 1
#                     # 큐에 넣어줘
#                     q.append([cc, pp])
#                 # p가 0이 되는 경우,
#                 if p == 0:
#                     return visited
#
#     print(visited)

