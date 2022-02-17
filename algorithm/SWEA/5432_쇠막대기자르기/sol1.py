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
    lst = list(input())
    iron = 0 # 쌓여있는 쇠막대기 개수
    cnt = 0 # 잘린 쇠막대기 개수

    i = 0
    while True:
        # 종료조건 설정
        if i == len(lst):
            break

    # i = 0
    # while i < len(lst): # input 개수보다 i가 작은 동안 while문 반복


    print(f'#{tc} ')
