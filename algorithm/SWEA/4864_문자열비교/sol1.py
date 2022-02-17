'''
Brute force로 풀자~~
'''

import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input() # 찾을 문자열
    str2 = input() # 전체 문자열
    s1 = len(str1) # 찾을 문자열의 길이
    s2 = len(str2) # 전체 문자열의 길이

    i = j = 0 # i는 s1의 idx, j는 s2의 idx
    while i < s1 and j < s2:
        if str1[i] != str2[j]: # 찾을 문자열과 전체 문자열이 일치하지 않는다면
            j = j - i
            i = -1
        i += 1
        j += 1

    if i == s1: # 찾을 문자열의 idx와 그 길이가 동일하다면 검색 성공한 것이므로
        print(f'#{tc} {1}')

    else: # 그렇지 않다면 실패
        print(f'#{tc} {0}')

