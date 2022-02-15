'''
1. row 고정, column 0 ~ 99 탐색
start column 은 고정하고, end column을 하나씩 줄여 나가면서 회문 탐색
없으면 start column + 1

'''

import sys

sys.stdin = open('palindrome2.txt')

T = 10
for tc in range(1, 11):
    
    print(f'#{tc} ')

