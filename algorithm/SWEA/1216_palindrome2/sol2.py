# success!!!!!!!!!

'''
my_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

**가로 reverse**
r_lst = []
for r in range(len(my_lst)):
    r_lst.append(my_lst[r][::-1])
print(r_lst)

**세로 reverse**
new_lst = list(zip(*my_lst))
print(new_lst)
'''

import sys

sys.stdin = open('palindrome2.txt')

T = 10

# 회문의 길이를 반환해주는 함수
def my_palindrome(arr):
    for i in range(len(arr), -1, -1): # 회문의 길이 100 일때부터 0이 될때까지
        for j in range(len(arr)):
            for k in range(len(arr)-i+1):
                word = arr[j][k:k+i]
                if word == word[::-1]: # 회문이라면
                    return i # 회문의 길이를 반환해줘!

for tc in range(1, T+1):
    n = int(input())
    lst = [list(map(str, input())) for _ in range(100)]
    cnt = 0 # 최종 최대 회문 길이 받을 변수

    # 가로 방향 회문 판별 먼저 해보자
    r_cnt = my_palindrome(lst)
    
    # 세로 방향 회문 판별
    # 먼저 transpose 해줘~ zip 함수 쓸래
    c_lst = list(zip(*lst))
    c_cnt = my_palindrome(c_lst)
    
    # 가로 회문 vs 세로 회문 => 누가 누가 더 긴가
    if r_cnt > c_cnt:
        cnt = r_cnt
    else:
        cnt = c_cnt

    print(f'#{tc} {cnt}')
        
















    # rlt = 0
    # # column 고정, row 역순 정렬 (transpose => zip!!)
    # c_lst = list(zip(*lst))
    # # row 고정, column 역순으로 정렬
    # r_lst = []
    # for r in range(100):
    #     r_lst.append(lst[r][::-1])
    #     for i in range(100, 1, -1): # 회문 길이를 100에서 1까지 -1씩 해주면서 탐색
    #         for j in range(100-i+1):
    #             if r_lst[j:j+i] == r_lst[j:j+i][::-1]: # 만약 회문이 맞다면
    #                 if len(r_lst[j:j+i]) > rlt: # 그리고 rlt 값보다 더 긴 길이의 회문이라면
    #                     rlt = len(r_lst[j:j+i])
    #
    #                 if c_lst[j:j + i] == c_lst[j:j + i][::-1]:  # 만약 회문이 맞다면
    #                     if len(c_lst[j:j + i]) > rlt:  # 그리고 rlt 값보다 더 긴 길이라면
    #                         rlt = len(c_lst[j:j + i])
    #
    #
    # # column 고정, row 역순 정렬 (transpose => zip!!)
    # # c_lst = list(zip(*lst))
    # # for i in range(100, 1, -1): # 회문 길이를 100에서 1까지 -1씩 해주면서 탐색
    # #     for j in range(100-i+1):
    # #         if c_lst[j:j+i] == c_lst[j:j+i][::-1]: # 만약 회문이 맞다면
    # #             if len(c_lst[j:j+i]) > rlt: # 그리고 rlt 값보다 더 긴 길이라면
    # #                 rlt = len(c_lst[j:j+i])
    # #                 break
    #
    # print(f'#{tc} {rlt}')
    #
    # # rlt = 0 # 회문 길이 받을 변수 선언
    # # max_v = 0
    #
    # # i = 100 # 최대 회문 길이를 100으로 설정
    # # while i > 0: # 회문 길이가 0이 아닐때까지 while문 반복
    # #     for r in range(100):
    # #         for c in range(100-i, 100):
    # #             r_pal = ''.join(r_lst[r][c]) # row 고정시켰을 때 찾은 회문
    # #             c_pal = ''.join(c_lst[r][c]) # column 고정시켰을 때 찾은 회문
    # #             if r_pal == r_pal[::-1] or c_pal == c_pal[::-1]: # 둘 중 하나라도 회문이라면
    # #                 rlt = i # rlt에 회문의 길이인 i를 저장해주자
    # #                 if rlt > max_v: # 근데 rlt가 max_v보다 크다면
    # #                     max_v = rlt # max_v 에 rlt를 넣어줘
    # #
    # #             else: # 회문이 아니야?
    # #                 i -= 1 # i에서 1을 빼주고
    # #                 rlt = 0 # rlt값을 초기화해
    #
    #
    #
    #
    #




