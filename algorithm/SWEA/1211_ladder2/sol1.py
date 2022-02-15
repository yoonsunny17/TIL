'''
사다리 타기 => 세로로 이동하므로 j 고정, i 이동
idx 탐색 시 위 방향은 탐색 필요 없음

'''

from pprint import pprint
import sys

sys.stdin = open('ladder2.txt')

T = 10
for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] # 100 x 100 이차원 리스트 생성
    print(arr)

    
    # print(f'#{tc} {arr}')

