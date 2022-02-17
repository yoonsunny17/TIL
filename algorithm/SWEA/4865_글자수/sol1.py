import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt = max_v = 0

    for i in str1: # str1에 있는 문자열이
        for j in str2: # str2 에 있는 문자열과 비교했을 때
            if i == j: # 두 문자열이 동일하다면
                cnt += 1 # cnt +1 해줘

        if max_v < cnt: # 최댓값 변수보다 cnt 변수의 값이 더 크다면
            max_v = cnt # 최댓값 변수에 값을 넣어줘
        cnt = 0 #cnt 변수를 초기화 하고 반복해주자

    print(f'#{tc} {max_v}')