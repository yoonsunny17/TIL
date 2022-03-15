import sys
from collections import deque

sys.stdin = open('fish.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(3)]

    print(lst)

    seat = [[0]*N]
    # 최솟값이 하나만 존재하는 경우 (인원수가 중복되지 않는 경우)
    for i in range(3):
        if lst[i][1] is min:
            seat[lst[i][0]] = 1

    gate = deque()
    people = deque()

    # print(lst)
    # for i in range(3):
    #     gate.append(lst[i][0])
    #     people.append(lst[i][1])

    # people을 한명씩 빼면서 생각해보자
    # 그리고 사람이 가장 적게 줄서있는 출구부터 자리 배치를 시작하자
    # print(gate)
    # turn = min(gate)
    # print(turn)

    # # 가장 적은 인원이 있는 출구부터, 단 최소인원이 같은 출구가 존재하는 경우
    # while sum(people) != 0:
    #     for i in range(3):
    #         if people[i] is min:
    #             turn = people[i]

    # 인원 수가 중복되지 않는 경우 (최솟값이 단 하나만 존재하는 경우)
    # for i in range(3):





    # print(gate)
    # print(people)




    # print(f'#{tc} ')

