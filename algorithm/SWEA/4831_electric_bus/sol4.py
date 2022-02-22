'''
교수님의 logic
일단 수명 k 만큼 넘어감
갔을 때 충전기가 있다면 충전 후 다시 넘어가면 됨

근데 만약 없는 경우, -1 하고 뒤로 back 함
있음 충전하고 다시 k 만큼 넘어가기
=> 근데 만약 또 없으면 또 -1 하고 뒤로 back 함
=> 뒤로 계속 갔는데 충전기를 만나긴 만났지만, 내가 마지막으로 충전했던 곳이라면 fail~~~

'''

import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    
    # K: 한 번 충전으로 이동할 수 있는 최대 정류장 수
    # N: 종점 정류장 번호
    # M: 충전기 설치된 정류장의 개수
    K, N, M = map(int, input())

    
    print(f'#{tc} ')

