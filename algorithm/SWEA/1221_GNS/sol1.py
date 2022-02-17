import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())
# 행성 숫자 코드 => idx number와 일치하게 나열
space_numb = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for tc in range(1, T + 1):
    n = list(map(str, input().split()))
    codes = list(map(str, input().split()))

    # 일단 숫자로 바꿔주기
    for i in range(len(codes)):
        for j in range(len(space_numb)):
            if codes[i] == space_numb[j]:
                codes[i] = j

    # 버블정렬 오름차순
    for i in range(len(codes)):
        for j in range(len(codes)-i-1):
            if codes[j] > codes[j+1]:
                codes[j], codes[j+1] = codes[j+1], codes[j]

    # 다시 외계어로 바꿔주기
    for i in range(len(codes)):
        for j in range(len(space_numb)):
            if codes[i] == j:
                codes[i] = space_numb[j]

    print(f'#{tc}', end=' ')
    for code in codes:
        print(f'{code}', end=' ')
    print()

