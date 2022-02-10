import sys

sys.stdin = open('electric_bus.txt')

T = int(input()) # 노선 수
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # K = 한번 충전에 이동 가능한 최대 정류장 수 / N = 종점 정류장 / M = 충전기 있는 정류장
    numbers = list(map(int, input().split())) # M개의 정류장의 번호

    electric = [0] * (N + 1)  # 전체 정류장에서 충전기 설치되어 있으면 1, 아니면 0으로 표시
    limit = [0] * (M - 1) # 충전소 간 거리 받을 리스트
    # bus_life = [0] * (N+1) # 각 정류장에 도착했을 때 남은 버스의 수명
    # bus_life[0] += K
    # cnt = 0 # 충전 횟수 카운트

    for number in numbers: # 충전소가 있는 곳을 1, 없는 곳을 0으로 표시
        if number: electric[number] += 1 # [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0]

    for i in range(M-1): # 충전소 간 거리 차를 계산
        limit[i] += numbers[i+1] - numbers[i] # [2, 4, 1, 1]

    for i in range(len(limit)): # 충전소가 너무 멀어서 종점에 갈 수 없는 경우
        if K < limit[i]:
            print(f'#{tc} {0}')
    
    bus_life = [0] * (N+1) # 각 정류장에 도착했을 때 남은 버스의 수명
    bus_life[0] += K # 0번 정류장에서 출발할 때 full life로 시작
    cnt = 0 # 충전 횟수 카운트
    
    for i in range(1, N+1): # 최대 경우의 수부터 생각을 해보자 (무조건 많이 충전하는 경우)
        bus_life[i] -= 1 # 정류장 하나 이동할 때마다 수명 하나씩 깎임
        if electric[i] == 1: # 충전소가 있는 곳에 도착했을 때
            bus_life[i] = K # 충전을 하고
            cnt += 1 # 충전 횟수 1을 더해준다
