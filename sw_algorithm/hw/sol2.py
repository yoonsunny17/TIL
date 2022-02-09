import sys

sys.stdin = open('baby_gin.txt')

T = int(input())
for tc in range(1, T + 1):

    cards = list(map(int, input())) # 카드 6장 받기
    cnt = [0] * 12 # 뽑은 카드에 적힌 숫자만큼 누적할 cnt list 생성

    for i in range(6):
        for j in range(1, 10):
            if cards[i] == j:
                cnt[j] += 1
            else:
                continue

    run = tri = 0
    i = 0
    while i < 10:
        if cnt[i] >= 3: # triplet인 경우
            cnt[i] -= 3
            tri += 1
            continue

        if cnt[i] * cnt[i+1] * cnt[i+2] != 0: # run인 경우 연속인 숫자 중 하나라도 0이 있으면 run이 성립 안됨
            cnt[i] -= 1
            cnt[i-1] -= 1
            cnt[i-2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')


