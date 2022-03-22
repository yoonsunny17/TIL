from collections import deque

N, K = map(int, input().split())

# bfs를 위한 empty 큐 생성
q = deque()
q.append(K)
# 최단 시간 세어 줄 변수 초기화
cnt = 0

# delta
move = [-1, 1]

while q:
    now = q.popleft()
    cnt += 1
    for i in range(2):
        new = now + move[i]  # -1 or +1
        # 동생의 현위치가 홀수인 경우
        if new % 2:
            q.append(new)
            cnt += 1

        # 동생의 현위치가 짝수인 경우
        if not new % 2:
            new = new // 2
            q.append(new)
            cnt += 1
    cnt += 1

    break

print(cnt)


# while q:
#     move = q.popleft()
#     # 동생이 있는 위치의 숫자가 홀수인 경우 2가지로 나누어 고려
#     if move % 2:
#
#     # 동생 위치가 짝수인 경우 2로 나누기
#     if not move % 2:
#         move = move // 2
#         cnt += 1
