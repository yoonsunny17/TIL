import sys

sys.stdin = open('min_max.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 각 tc마다 입력받을 양수 개수
    numbers = list(map(int, input().split())) # 각 넘버를 리스트로 받자

    # max numb 찾자
    max_numb = numbers[0] # 일단 리스트 맨 첫값을 max numb이라고 가정해보자
    for i in range(len(numbers)):
        if numbers[i] >= max_numb:
            max_numb = numbers[i]
            continue

    # min numb 찾자 (위랑 동일하게)
    min_numb = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] <= min_numb:
            min_numb = numbers[i]
            continue

    rlt = max_numb - min_numb

    print(f'#{tc} {rlt}')




