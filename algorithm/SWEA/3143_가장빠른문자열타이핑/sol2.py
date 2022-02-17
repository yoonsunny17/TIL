'''
교수님 solution **respect....
B 기준으로 A를 나누면 어떨까?
=> B로 A를 split해주고, 빈 문자열에 특정 문자 하나를 넣어주고, 다시 문자열의 수를 센다
'''
import sys

sys.stdin = open('typing.txt')

T = int(input())
for tc in range(1, T + 1):
    a_str, b_str = input().split()
    typing = a_str.split(b_str)
    typing = 'x'.join(typing)
    print(f'#{tc} {len(typing)}')

