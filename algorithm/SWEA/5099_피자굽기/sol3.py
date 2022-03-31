import sys

sys.stdin = open('pizza.txt')

def pizza():
    oven = []
    for i in range(1, N+1):
        oven.append(i)

        next_pizza = i + 1
        pizza_numb = 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    first_cheese = [0] + list(map(int, input().split()))


    print(f'#{tc} ')

