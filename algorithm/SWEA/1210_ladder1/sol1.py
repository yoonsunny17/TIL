'''
도착 지점 = 2
i = 99일 때 2의 값을 가지는 위치를 찾자
'''

import sys

sys.stdin = open('ladder1.txt')

T = 10
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # r, c값 초기화
    r = c = 0
    # 사다리 타기는 down, left, right 방향만 고민하면 된다 // default 값이 down
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    idx = 0 # dr, dc의 idx 0: down, 1: left, 2: right

    # 냅다 무한루프
    while True:
        # 왼쪽에 1 발견하면
        if arr[r][c-1] == 1:
            idx = 1
            


    
    # print(f'#{tc} ')

