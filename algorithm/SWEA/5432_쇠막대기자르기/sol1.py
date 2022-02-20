'''
() 이렇게 바로 나오면 얘는 레이저
레이저 만나면 막대기 잘림  ==> 잘린 막대기 +1
( 다음에 ( 가 나온다는것은 쇠막대기라는 뜻
( = 쇠막대기 첫부분 ==> 쌓인 막대기 +1
) = 쇠막대기 끝부분 ==> 잘린 막대기 +1, 쌓인 막대기 -1
'''

import sys

sys.stdin = open('iron.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = input()
    cnt = rlt = 0

    for i in range(len(lst)):
        if lst[i] == '(': # 열린 괄호
            cnt += 1 # 막대기 개수 +1 누적해주기
        else: # 닫힌 괄호
            if lst[i-1] == '(': # 그 전에 열린괄호가 나온 경우라면 레이저이므로
                cnt -= 1
                rlt += cnt # 막대기 개수 -1 해주고 누적 막대기 개수 rlt 더해주기
            else: # ')' 가 나왔다면 막대기가 끝났다는 표시이므로
                cnt -= 1
                rlt += 1 # 막대기 하나 끝날 때마다 누적되는 막대기 수 +1

    print(f'#{tc} {rlt}')

