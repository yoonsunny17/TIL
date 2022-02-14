import sys

sys.stdin = open('electric_bus.txt')

T = int(input())

def charging(N, K, chargers):
    i = 0
    num = 0 # 충전 횟수
    d = K # 최대 이동 정류장 수 => 수명
    while True:
        if chargers[i+d] == 1: # K 범위부터 안으로 탐색, 그 안에 충전기가 있으면 이동하고 충전횟수 +1
            num += 1
            i += d # 수명 풀 충전
            d = K
        else:
            d = d-1 # 충전기 못만나면 수명 하나 깎임

        if d == 0: # K 범위 내에서 충전기 못만난 경우 0 리턴
            return 0

        if i >= N-K: # 종점 도착할때까지 수명 다 안깎인 경우
            return num


for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    chargers = [0]*(N+1) # 전체 정류장 개수만큼 요소를 만들고
    for numb in numbers:
        chargers[numb] = 1 # idx numb = charging station
    
    print(f'#{tc} {charging(N, K, chargers)}')

