### 런타임에러 조심해야 함! ###
import sys

sys.stdin = open('binary_onoff.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 출력해줄 결과 초기값을 ON 으로 설정해주자!
    # 0 안만나면 ON을 그대로 출력하겠징
    rlt = 'ON'
    # 시간 단축을 위해 N 개의 비트 자리수만 확인해주자
    for _ in range(N):
        # M이 0 으로 나누어 떨어진다면 OFF !
        if not M % 2:
            rlt = 'OFF'
        # 아니라면 계속 2진수로 바꿔줘
        else:
            M = M // 2

    print(f'#{tc} {rlt}')


