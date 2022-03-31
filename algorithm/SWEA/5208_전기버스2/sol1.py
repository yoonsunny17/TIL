import sys
sys.stdin = open('electric_bus.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    
    print(f'#{tc} ')

