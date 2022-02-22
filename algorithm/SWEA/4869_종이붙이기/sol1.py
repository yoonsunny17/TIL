import sys

sys.stdin = open('paper.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 10의 배수
    rlt = 0
    memo = [1, 3] # N = 10일 때 1가지 경우, N = 30일 때 3가지 경우 저장

    for i in range(2, N // 10): # N = 30; i = 2, N = 40; i = 3, N = 50; i = 4 ...

        # 모두 그려본 결과 memo[i] = memo[i - 1] + 2 * memo[i - 2] 라는 규칙 발견!
        memo.append(memo[i - 1] + 2 * memo[i - 2])

        # 최댓값 구하기 = 모든 경우의 수 구하기
        if rlt < memo[i]:
            rlt = memo[i]

    print(f'#{tc} {rlt}')

