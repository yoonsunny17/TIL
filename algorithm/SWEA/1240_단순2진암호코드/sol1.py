import sys
from collections import deque
from pprint import pprint

sys.stdin = open('secret.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 어차피 1이 있는 행 한줄만 필요한 것 같은데..?
    for n in range(N):
        if sum(matrix[n]) != 0:
            codes = matrix[n]
            break

    # 그 다음에는 보니까.. 모든 코드의 맨 뒷자리가 무조건 1로 끝나니까
    # 리스트 역순으로 검사하다가 1 나오면 그걸 기준으로 56개 따오자
    # silcing 해서 리스트 초기화 해주는 식으로 가자!
    codes = codes[::-1]
    for i in range(len(codes)):
        if codes[i]:
            codes = codes[i:i+56]
            codes = codes[::-1]
            break

    new = []
    # 코드를 만들 수 있도록 7개씩 묶어서 다시 리스트에 저장해주자
    for i in range(0, 56, 7):
        numb = ''.join(map(str, codes[i:i+7]))
        new.append(numb)

    # print(new)
    real = []
    for numb in new:
        if numb == '0001101':
            real.append(0)
        elif numb == '0011001':
            real.append(1)
        elif numb == '0010011':
            real.append(2)
        elif numb == '0111101':
            real.append(3)
        elif numb == '0100011':
            real.append(4)
        elif numb == '0110001':
            real.append(5)
        elif numb == '0101111':
            real.append(6)
        elif numb == '0111011':
            real.append(7)
        elif numb == '0110111':
            real.append(8)
        elif numb == '0001011':
            real.append(9)
    # print(real)

    # 홀수번째 숫자 계산 결과값 받을 변수 = cnt1
    # 짝수번째 = cnt2
    # 최종 결과값 = rlt
    cnt1 = cnt2 = rlt = 0
    for i in range(len(real)):
        if not i % 2:
            cnt1 += real[i]
        else:
            if i != 7:  # cnt2 에는 마지막 자리 빼고 더해줘야해
                cnt2 += real[i]
        rlt += real[i]
    final = cnt1 * 3 + cnt2 + real[-1]
    # print(rlt, final)
    print(f'#{tc} {rlt if not (final % 10) else 0}')

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