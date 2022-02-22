'''
DP 사용해서 풀어보기~~~
'''

import sys

sys.stdin = open('electric_bus.txt')

T = int(input())
for tc in range(1, T + 1):
    # K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 종점 정류장 번호
    # M: 충전기 설치된 정류장의 개수
    K, N, M = map(int, input())

    print(f'#{tc} ')

