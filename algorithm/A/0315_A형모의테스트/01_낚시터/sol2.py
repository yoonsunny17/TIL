import sys
from collections import deque
sys.stdin = open('fish.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(3)]
    lst[0].append('A')
    lst[1].append('B')
    lst[2].append('C')
    seat = [[0]*N]
    people = []
    turn = deque()

    # # 인원수가 중복되는지 확인해 줄 변수 초기화
    # cnt = 0
    for i in range(3):
        people.append(lst[i][1])

    for i in range(3):
        if people[i] is min(people):
            turn.append(lst[i])

    # 최소 인원이 중복되지 않는 경우,
    if len(turn) == 1:
        seat[lst[i][0]] = lst[i][2]



    print(len(turn))
    print(people)
    print(lst)

    # 차례 정하는 규칙
    # 1. 인원수가 가장 최소인 출입구부터 시작한다
    # 2. 만약 인원수가 동일한 경우, 출입구가 뒤쪽인 부분부터 시작한다
    # def turn(matrix):
    #     for i in range(3):
    #         if matrix[i][1] is min and

    # print(lst)


    
    print(f'#{tc} ')

