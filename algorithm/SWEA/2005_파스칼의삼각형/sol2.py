'''
교수님 solution
'''
import sys

sys.stdin = open('input.txt')

T = int(input())

memo = [[0 for _ in range(11)] for _ in range(11)]

for i in range(11):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

