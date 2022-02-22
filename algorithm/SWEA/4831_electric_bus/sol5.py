'''
DP 사용해서 풀어보기~~~
'''

import sys

sys.stdin = open('electric_bus.txt')

def check(life, last, arr):

    # empty stack 만들어주기
    memo = []

    # bus_stop = [x for x in range(last+1)]
    # for i in range(0, len(bus_stop), life):
    #     for j in range(len(arr)):
    #         if i == arr[j]:
    #             memo.append(arr[j])
    #         else:
    #             while True:
    #                 i -= 1
    #                 if i == arr[j]:
    #                     memo.append(arr[j])
    #                     break
    #

    # for i in range(len(bus_stop)):
    #     for j in range(len(arr)):
    #         if bus_stop[i] == arr[j]:
    #             memo.append(arr[j])
    #
    #     if i % life == 0 and i > 0:
    #         if memo[-1] == bus_stop[i]:
    #             memo.pop()







T = int(input())
for tc in range(1, T + 1):
    # K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 종점 정류장 번호
    # M: 충전기 설치된 정류장의 개수
    K, N, M = map(int, input().split())
    chargers = [map(int, input().split())]
    rlt = check(K, N, chargers) # check 함수 만들어서 rlt 반환하자

    # rlt => 최소 충전횟수 또는 0을 출력하도록!
    print(f'#{tc} {rlt}')

