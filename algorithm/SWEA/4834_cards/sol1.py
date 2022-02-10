import sys

sys.stdin = open('cards.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    cnt = [0] * 10 # 각 카드 개수 세줄 cnt 리스트 만들어 주기(0 ~ 9)

    # 해당 카드 개수를 cnt 리스트에 1씩 누적해서 세어주기
    for i in range(len(cards)):
        for j in range(len(cnt)):
            if cards[i] == j:
                cnt[j] += 1


    # 가장 많은 개수의 카드와 그 숫자카드를 구할거야
    max_card = 0
    for i in range(len(cnt)):
        if cnt[i] >= max_card:
            max_card = cnt[i]
            max_numb = i

    print(f'#{tc} {max_numb} {max_card}')


