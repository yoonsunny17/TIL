import sys
from collections import deque

sys.stdin = open('rotation.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbs = list(map(int, sys.stdin.readline().split()))
    q = deque()
    for numb in numbs:
        q.append(numb)

    # 숫자 3개인 경우, 3번 반복하면 원상태 => 실질적인 회전 수 = M을 N으로 나눈 나머지
    # r가 stack에서 idx로 생각하면 될 듯
    r = M % N
    rlt = q[r]
    print(f'#{tc} {rlt}')

