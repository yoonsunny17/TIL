import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num_lst = list(map(int, input().split())) # 10개의 요소로 이루어진 리스트