from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))

# 숫자 넣어줄 큐 생성
q = deque()
for i in range(1, N+1):
    q.append(i)

# 2, 3번 연산 수행 횟수 세어줄 변수 초기화
cnt = 0
for numb in target:
    while True:
        # 1번 연산: 첫 번째 원소를 뽑아낸다
        # 가능한 경우 = 타겟 리스트의 첫 번째 원소와, 큐의 가장 왼쪽 원소가 일치하는 경우
        if q[0] == numb:
            q.popleft()
            break

        # 일치하지 않는 경우 = 2 또는 3번 연산 수행해야 함
        else:
            # 2번 연산: 왼쪽으로 한 칸 이동시킨다
            # 2번 연산이 효율적인 경우 = 뽑아내려는 수의 위치가 큐 길이의 반보다 작은 곳에 위치해 있는 경우!
            if q.index(numb) <= len(q) // 2:
                # 큐 왼쪽의 요소가 내가 원하는 숫자와 일치할 때까지
                while q[0] != numb:
                    # popleft 한것을 다시 더해주기를 반복해
                    q.append(q.popleft())
                    cnt += 1

            # 3번 연산: 오른쪽으로 한 칸 이동시킨다
            # 3번 연산이 효율적인 경우 = 뽑아내려는 수의 위치가 큐 길이의 반보다 큰 곳에 위치해 있는 경우
            else:
                while q[0] != numb:
                    # 오른쪽 숫자를 빼서 왼쪽에 넣어줘
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)
