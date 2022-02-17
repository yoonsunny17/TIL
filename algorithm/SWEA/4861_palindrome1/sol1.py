'''
이것도 brute force로 풀어볼까?
'''

import sys

sys.stdin = open('palindrome1.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N = 행 또는 열 길이, M = 찾을 회문의 길이
    lst = [list(map(str, input())) for _ in range(N)]
    rlt = [] # 최종 단어 받을 리스트 선언

    # row 고정, column 이동하면서 찾아보기
    for r in range(N):
        for c in range(N-M+1):
            r_lst = [] # row 고정했을 때 회문 단어 받을 리스트
            for i in range(M):
                r_lst.append(lst[r][c+i]) # column 을 하나씩 이동시키면서 값을 저장
            if r_lst == r_lst[::-1]: # 저장한 리스트와, 역으로 정렬한 리스트가 동일하다면
                rlt.append(''.join(r_lst)) # 회문 ㅇㅈ! join함수 써서 rlt 함수에 넣어주기

    # column 고정, row 이동하면서 찾아보기
    for c in range(N):
        for r in range(N-M+1): 
            c_lst = [] # column 고정했을 때 회문 단어 받을 리스트
            for i in range(M):
                c_lst.append(lst[r+i][c]) # row 를 하나씩 이동시키면서 값을 저장
            if c_lst == c_lst[::-1]: #저장한 리스트와, 역으로 정렬한 리스트가 동일하다면
                rlt.append(''.join(c_lst)) # 회문 ㅇㅈ! join 함수 써서 rlt 함수에 넣어주기

    # 어짜피 답은 하나! rlt[0]을 출력하면 된다
    print(f'#{tc} {rlt[0]}')
