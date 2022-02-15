# 교수님 풀이~~

import sys
from pprint import pprint

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input()) # 종이 장수
    data_set = [list(map(int, input().split())) for _ in range(n)]

    # 각각의 범위에서 좌표를 구해서, set 에 담는다
    # 미리 set 정의해주기
    red = set()
    blue = set()

    for data in data_set:
        r1, c1, r2, c2, color = data

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1): # 범위는 항상 조심!!
                if color == 1:
                    red.add((r, c))
                else:
                    blue.add((r, c))

    # print(red & blue) # red이면서 blue인 애들이 출력

    rlt = len(red & blue) # red.intersection(blue) => 교집합
    print(f'#{tc} {rlt}')


'''
    합집합
    red | blue
    red.union(blue)
    
    차집합
    red - blue
    red.difference(blue)
    
    대칭차집합 (둘 모두에게 공통적으로 없는 것)
    red ^ blue
'''

