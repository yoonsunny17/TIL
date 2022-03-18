from collections import deque
import sys

sys.stdin = open('contact.txt')

# s = start 시작지점
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        # matrix[from][to]에서 start=from 이므로 matrix[s][j] == 1 이면 전화 걸 수 있음
        for j in range(101):
            if matrix[i][j] == 1 and not visited[j]:  # from - to 이어져 있고, 아직 전화 건 기록이 없다면,
                q.append(j)  # 경로를 추가해주고
                visited[j] = visited[i] + 1  # 전화 걸었다는 기록을 남겨줘

    return visited  # 방문기록을 반환하자


T = 10
for tc in range(1, T + 1):
    length, start = map(int, input().split())
    lst = list(map(int, input().split()))
    # from to 체크해줄 이중 리스트 만들기
    # row = from, column = to
    matrix = [[0]*101 for _ in range(101)]
    # 연락받는 사람들 기록 남길 리스트 만들기; 일차원리스트
    visited = [0]*101

    # matrix에 lst data 넣기
    for i in range(0, len(lst), 2):
        matrix[lst[i]][lst[i+1]] = 1


    bfs(start)
    # 마지막에 연락받은 번호들 저장할 리스트
    rlt = []
    for k in range(101):
        if visited[k] == max(visited):
            rlt.append(k)
    print(f'#{tc} {max(rlt)}')