import sys
from collections import deque

sys.stdin = open('calculation.txt')


def bfs(numb):
    q = deque()
    # 큐에 현재 숫자와, 계산 갱신할 변수 넣어줘 (처음에는 0번)
    q.append([numb, 0])
    visited = [0] * (max_numb+1)  # 중복되면서 계산하지 않도록 방문 기록도 만들어주자
    visited[numb] = 1  # 일단 현재 숫자 방문 기록 남겨줘

    while q:
        now, cnt = q.popleft()
        # 계산 가능한 경우 4가지
        calc = [now+1, now-1, now*2, now-10]
        for new in calc:
            # 만약 새로 계산된 수가 최댓값을 넘지 않고, 아직 나온 적 없는 숫자라면,
            if new <= max_numb and not visited[new]:
                visited[new] = 1  # 이번에 나왔음을 표시해주고
                q.append([new, cnt+1])  # 큐에 넣어줘, 그리고 횟수 + 1 해줘
                if new == M:  # 근데 만약에 새로운 수가 원하는 수랑 일치한다면
                    return cnt+1  # cnt+1 을 반환하자


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # boundary condition 지정해주자!
    max_numb = 1000000
    print(f'#{tc} {bfs(N)}')