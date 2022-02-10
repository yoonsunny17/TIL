import sys

sys.stdin = open('electric_bus.txt')

T = int(input()) # 노선 수
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # K = 최대 갈 수 있는 정류장, N = 종점, M = 충전기 설치된 정류장 번호
    numbers = list(map(int, input().split()))

    electric = [0] * (N+1) # 충전기 설치되어 있으면 1, 아니면 0으로 표시
    for number in numbers:
        if number != 0:
            electric[number] = 1

    max_lst = [0] * (N+1) # 각 정류장 도착할 때마다 남은 버스의 수명
    max_lst[0] += K # 0번 정류장에서 충전 후 출발하니까 K 수명 더해주고 시작하기
    for i in range(1, N+1):
        max_lst[i] -= 1
        if electric[i] == 1 and numbers[i+1] - numbers[i] <= K: #다음 충전소보다 내 수명 충분히 남아잇으니까 그냥 지나치기
            continue

        if electric[i] == 1 and numbers[i+1] - numbers[i] > K: # 다음 충전소 거리보다 내 수명이 짧으니까 충전해주기
            max_lst[i] == K
            continue
        
        if electric[i] == 0 and K != 0: # 충전소 가는중
            continue
        
        if electric[i] == 0 and numbers[i+1] - numbers[i] == 0: # 도착 실패!
            max_lst[i] *= -1 # 실패라는 것을 표현하기 위해 음수로 표현


    print((max_lst))



    # max_lst = [0] * (N+1) # 각 정류장 도착할 때마다 남은 버스의 수명
    # max_lst[0] += K # 0번 정류장에서 충전 후 출발하므로 K만큼 수명 주고 시작해준다
    #
    #
    # for i in range(1, N):
    #     max_lst[i] -= 1 # 일단 정류장 하나씩 이동할 때마다 수명 깎임
    #     if electric[i] == 1 and max_lst[i] < :# 도착한 정류장이 충전기가 있는 경우일 때
    #         max_lst[i] == K # 다시 K 로 수명 충전




