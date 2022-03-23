import sys
from collections import deque

sys.stdin = open('node.txt')

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        n = q.popleft()
        for i in range(E):
            # 어느 노드가 먼저인지 몰라서 다 검사해줘야해요
            # case 1. 입력받은 노드 중 왼쪽 노드부터 시작이고, 그 다음 노드에 아직 방문한 적이 없다면,
            if pair[i][0] == n and not visited[pair[i][1]]:
                # 그 다음 노드를 경로에 추가해주고, 방문기록 남기고, 이동거리 + 1 해줘요
                q.append(pair[i][1])
                distance[pair[i][1]] = distance[n] + 1
                visited[pair[i][1]] = 1

            # case 2. 입력받은 노드 중 오른쪽 노드부터 시작이고, 왼쪽 노드에 아직 방문한 적이 없다면,
            if pair[i][1] == n and not visited[pair[i][0]]:
                # 그 다음 노드를 경로에 추가해주고, 방문기록 남기고, 이동거리 + 1 해줘요
                q.append(pair[i][0])
                distance[pair[i][0]] = distance[n] + 1
                visited[pair[i][0]] = 1


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    pair = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())

    # 방문 기록 남길 리스트
    visited = [0] * (V+1)
    # 각 노드 별 도달거리
    distance = [0] * (V+1)

    bfs(start)
    print(f'#{tc} {distance[end]}')