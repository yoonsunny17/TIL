import sys

sys.stdin = open('sort.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 오름차순 정렬
    n = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f'#{tc}', end=' ')
    for number in numbers:
        print(f'{number}', end=' ')
    print()

