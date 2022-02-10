# 교수님 풀이!
import sys

sys.stdin = open('gravity.txt')

'''
블록 하나하나를 움직인다기 보다는, 블록 탑을 움직인다고 생각하면 편하다
'''

T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    lst = list(map(int, input().split()))
    max_drop = 0

    for i in range(n):
        now = lst[i]
        temp_drop = 0

        for j in range(i+1, n):
            if now > lst[j]:
                temp_drop += 1

        if temp_drop > max_drop:
            max_drop = temp_drop
    
    print(f'#{tc} {max_drop}')

