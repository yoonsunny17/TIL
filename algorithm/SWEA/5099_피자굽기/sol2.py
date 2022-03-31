from collections import deque
import sys

sys.stdin = open('pizza.txt')

def pizza():
    oven = deque()
    for i in range(1, N+1):
        oven.append(i)

    idx = N + 1
    pizza_num = 0

    while oven:
        pizza_num = oven.popleft()

        if first_cheese[pizza_num] // 2 != 0:
            first_cheese[pizza_num] //= 2
            oven.append(pizza_num)

        elif idx <= M:
            oven.append(idx)
            idx += 1

    return pizza_num


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    first_cheese = [0] + list(map(int, input().split()))

    check = pizza()
    print(f'#{tc} {check}')
