import sys
from collections import deque

sys.stdin = open('binary_numb2.txt')


def f(numb):
    numb = numb * 2
    # 종료조건 case 1. 숫자가 1로 떨어지는 경우, stack에 1 더해주고 끝내줘
    if numb == 1:
        stack.append(1)
        return
    # 종료조건 case 2. 자리수가 13자리 이상이 되는 경우, 실패야ㅠ
    elif len(stack) >= 13:
        return

    # 종료 조건이 아닌 경우에는 2진수로 만들어주자
    else:
        if numb > 1:
            stack.append(1)
            f(numb - 1)
        else:
            stack.append(0)
            f(numb)


T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    # 2진수로 변환해준 숫자 저장해 줄 stack
    stack = deque()

    f(N)
    rlt = ''.join(map(str, stack))
    fail = 'overflow'
    print(f'#{tc} {rlt if len(stack) <= 12 else fail}')
