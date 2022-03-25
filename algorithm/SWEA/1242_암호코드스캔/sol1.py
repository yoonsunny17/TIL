import sys

sys.stdin = open('scan.txt')

T = int(input())


for tc in range(1, T + 1):
    
    print(f'#{tc} ')

'''
import sys
sys.stdin = open('input.txt')
# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {
    '0001101': 0, 
    '0011001': 1, 
    '0010011': 2,
    '0111101': 3, 
    '0100011': 4, 
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
'''