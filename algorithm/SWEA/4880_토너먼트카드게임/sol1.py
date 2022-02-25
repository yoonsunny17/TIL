'''
**교수님의 hint**

def f(i, j):   # i~j 사이의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾아 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현
'''

import sys

sys.stdin = open('tournament.txt')


# 토너먼트 반복하는 함수
def tournament(i, j):
    if i == j: # 최종 승자가 나왔다면,
        return i # return 해줘

    else: # i != j 즉, 아직 두 그룹으로 나뉘어 있다면, 재귀함수 호출해서 반복해줘야 해
        left = tournament(i, (i+j)//2) # 왼쪽 그룹을 다시 두 그룹으로 나눠줘
        right = tournament((i+j)//2 + 1, j) # 오른쪽 그룹을 다시 두 그룹으로 나눠줘

        # 가위 = 1, 바위 = 2, 보 = 3 승자를 가려보자
        if cards[left] == 1:
            if cards[right] == 1:
                return left  # draw
            elif cards[right] == 2:
                return right  # right win
            elif cards[j] == 3:
                return left  # left win

        if cards[left] == 2:
            if cards[right] == 1:
                return left  # left win
            elif cards[right] == 2:
                return left  # draw
            elif cards[right] == 3:
                return right  # b win

        if cards[left] == 3:
            if cards[right] == 1:
                return right  # right win
            elif cards[right] == 2:
                return left  # left win
            elif cards[right] == 3:
                return left  # draw

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    winner = tournament(1, N)
    print(f'#{tc} {winner}')
