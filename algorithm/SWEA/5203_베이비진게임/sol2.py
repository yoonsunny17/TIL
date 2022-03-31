import sys

sys.stdin = open('baby_gin.txt')


# 이길 수 있는지 확인해보는 함수를 구현하자
def winner(player):
    # case 1. 같은 숫자 카드가 3장인 경우
    for i in range(10):
        if player[i] == 3:
            return True  # 이겼당

    # case 2. 연속된 숫자가 세장 나오는 경우
    for j in range(8):
        if player[j] and player[j+1] and player[j+2]:
            return True  # 이겼당

    return False  # 두가지 경우 다 돌았는데 안된다면 졌당..


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 각 플레이어들이 10장의 카드에서 각 숫자의 카드를 몇장씩 받았는지 체크해주자
    player_1 = [0]*10
    player_2 = [0]*10

    # 승부의 default 값은 무승부야
    win = 0

    # 이제 주어진 12장의 카드를 나누어 가져볼게
    for i in range(len(cards)):
        # idx 가 짝수 = 홀수번째 = player 1
        if not i % 2:
            player_1[cards[i]] += 1
            # 카드를 나누어 가질 때마다 이길 수 있는지 확인해줘
            if winner(player_1):
                win = 1
                break  # 먼저 외친 사람이 이김!
        # idx 홀수 = player 2
        else:
            player_2[cards[i]] += 1
            # 카드를 나누어 가질 때마다 이길 수 있는지 확인해줘
            if winner(player_2):
                win = 2
                break  # 먼저 외친 사람이 이김!

    print(f'#{tc} {win}')

