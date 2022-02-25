'''
success!!!!
sol 1이랑 똑같은데.. sol 1은 runtime error 나고.. 왜 얘는 안나는거징 ..
'''
import sys

sys.stdin = open('tournament.txt')

def winner(i, j):
    # 최종 승자가 나온 경우
    if i == j:
        return i

    # 최종 승자를 가리지 못한 경우 => left, right partition을 나누어 재귀함수 호출!
    left = winner(i, (i+j)//2)
    right = winner((i+j)//2+1, j)

    # 1 = 가위, 2 = 바위, 3 = 보
    if cards[left] == 1: # left가 가위를 낸 경우,
        if cards[right] == 1: return left # draw
        elif cards[right] == 2: return right # lose
        else: return left # win
    if cards[left] == 2: # left가 바위를 낸 경우,
        if cards[right] == 1: return left # win
        elif cards[right] == 2: return left # draw
        else: return right # lose
    if cards[left] == 3: # left가 보를 낸 경우,
        if cards[right] == 1: return right # lose
        elif cards[right] == 2: return left # win
        else: return left # draw


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split())) # idx 고려해서 앞에 0 넣어줘
    win = winner(i=1, j=N)

    print(f'#{tc} {win}')

