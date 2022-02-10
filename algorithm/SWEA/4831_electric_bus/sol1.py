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
    # print(electric)

    max_lst = [0] * (N+1) # 각 정류장 도착할 때마다 남은 버스의 수명
    max_lst[0] += K # 0번 정류장에서 충전 후 출발하므로 K만큼 수명 주고 시작해준다

'''
1. 무조건 충전 다 해주면서 간다
2. 
'''


    for i in range(1, N+1):
        max_lst[i] -= 1 # 일단 정류장 하나씩 이동할 때마다 수명 깎임
        if electric[i] == 1: # 근데 도착한 정류장에 충전기가 있으면 무조건 충전 ㄱㄱ




