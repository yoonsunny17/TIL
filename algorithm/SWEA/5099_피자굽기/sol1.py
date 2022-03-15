import sys
from collections import deque

sys.stdin = open('pizza.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    # 피자 번호와 Ci값 같이 받아 줄 q 생성해주기
    pizza = deque()
    for i in range(M):
        pizza.append([Ci[i], i+1]) # Ci, numb 순서로 받음

    # 오븐 q 생성해주기
    oven = deque()

    # 오븐 회전시키쟈
    for _ in range(N):
        oven.append(pizza.popleft())

    # 오븐에 남은 피자가 하나일 때까지 반복할거야
    while len(oven) > 1:
        # 오븐에 자리가 비어있고, 오븐에 넣지 않은 피자가 있는 경우라면 오븐에 넣어주자
        if len(oven) < N and pizza:
            oven.append(pizza.popleft())

        # 그리고 oven에서 cheese, numb을 꺼내서 얼마나 녹았는지 확인해봐
        cheese, numb = oven.popleft()
        # 치즈 양이 0이 되었으면 제거해줘
        if not cheese//2:
            continue
        # 치즈가 덜 녹았으면 다시 회전시켜줘
        else:
            oven.append([cheese//2, numb])

    # oven에 마지막으로 남은 피자의 번호를 출력해줘
    print(f'#{tc} {oven.popleft()[1]}')

