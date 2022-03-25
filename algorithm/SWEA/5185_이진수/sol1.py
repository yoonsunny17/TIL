from collections import deque
import sys

sys.stdin = open('binary_numb.txt')

T = int(input())
for tc in range(1, T + 1):
    N, numbs = input().split()
    # 문자열을 숫자로 바꿔줘야해~~
    change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # queue 를 만들어서 뒤에서부터 2진수 변환한 후 appendleft 해주자
    rlt = deque()
    
    # 16진수 - 10진수 - 2진수 순서로 바꿔주자
    # input type = str
    for numb in numbs[::-1]:
        # 알파벳으로 받은 애들은 change dict 안에 있는 숫자로 바꿔주고,
        if numb in change:
            numb = change[numb]
        # 아닌 애들은 int 로만 변환해줘
        else:
            numb = int(numb)
        # print(numb)
        # 4자리수로 표현하라고 했으니까!
        for _ in range(4):
            rlt.appendleft(numb % 2)
            numb = numb // 2

    changed = ''.join(map(str, rlt))
    print(f'#{tc} {changed}')

