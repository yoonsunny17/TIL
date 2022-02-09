import sys

sys.stdin = open('sol1.txt')

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input()))
    cnt = [0] * 12

    for i in range(len(cards)):
        for j in range(1, 10):
            if cards[i] == j:
                cnt[j] += 1

    tri = run = 0
    for i in range(len(cnt)):
        if cnt[i] >= 3: # tri
            tri += 1
            cnt[i] -= 3
            continue

        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1: # run
            run += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue



    if tri + run == 2:
        print(f'#{tc} {1}')

    else:
        print(f'#{tc} {0}')