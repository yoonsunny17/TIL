import sys

sys.stdin = open('baby_gin.txt')


def winner(player):
    for i in range(10):
        if player[i] == 3:
            return True

    for j in range(8):
        if player[j] and player[j+1] and player[j+2]:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 각 플레이어들이 몇번 카드를 몇 장 가지고 있는지 체크해주자
    player_1 = [0]*10
    player_2 = [0]*10

    # default 값은 비긴걸로 하자
    win = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            player_1[cards[i]] += 1
            if winner(player_1):
                win = 1
                break
        else:
            player_2[cards[i]] += 1
            if winner(player_2):
                win = 2
                break

    print(f'#{tc} {win}')


