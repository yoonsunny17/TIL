from collections import deque
from pprint import pprint


def dfs(start):
    # 시작하는 노드 방문기록 적어주기
    visited[start] = 1
    global cnt
    # start와 연결된 노드에 대해서,
    for i in graph[start]:
        # 만약 그 노드에 아직 방문한 적이 없다면,
        if not visited[i]:
            # dfs 재귀호출; i 노드를 start 지점으로 다시 탐색해
            dfs(i)
            cnt += 1


N = int(input())
M = int(input())
# node 들의 연결 관계를 확인해 줄 그래프 생성! index 숫자 맞추기 위해 N+1 개 만듦
graph = [[] for _ in range(N+1)]
# 방문 기록 남길 리스트 생성
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 바이러스 몇 대 걸렸는지 세어 줄 변수 초기화
cnt = 0

# 1번 컴퓨터부터 시작해줘
dfs(start=1)
print(cnt)