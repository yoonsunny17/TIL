'''
     icp  isp
  )   -    -
 * /  2    2
 + -  1    1
  (   3    0

icp > isp 일때 push
) 오면 stack에서 ( 만날때까지 pop
'''

import sys

sys.stdin = open('calculator3.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    codes = input()
    
    memo = [] # 연산자 저장해 둘 빈 stack 생성
    check = list() # 후위표기법으로 정리하여 저장할 list 생성

    for code in codes:
        if code == '(': # 열린 괄호인 경우에는,
            memo.append(code) # stack에 저장해줘 (icp == 3)

        elif code == ')': # 근데 만약에 닫힌 괄호를 만난 경우라면,
            temp = memo.pop() # 일단 memo의 맨 위를 pop 해
            while temp != '(': # temp가 열린괄호가 아닌 동안 반복해줘
                check.append(temp)
                temp = memo.pop()

        elif code == '*': # 곱하기인 경우에는,
            memo.append(code) # stack에 저장해줘 (icp == 2)

        elif code == '+': # 더하기인 경우에는,
            while memo and memo[-1] != '(': # stack이 비어있지 않고, 열린괄호 나오기 전까지는
                check.append(memo.pop()) # 연산자 꺼내서 check에 넣어줘
            memo.append(code)

        else: # 피연산자인 경우에는,
            check.append(code) # check에 바로 저장해줘

    # 후위표기식 끝났으면, 계산을 시작하자
    rlt = [] # 계산한 값을 저장할 빈 stack 생성
    for i in check:
        if i.isdigit(): # 피연산자라면,
            rlt.append(int(i)) # rlt에 int형으로 저장해줘
        else: # 연산자라면,
            # 우선 두 숫자 꺼내줘
            p2 = rlt.pop()
            p1 = rlt.pop()
            if i == '*': # 그리고 연산자가 곱하기이면 곱해서 다시 넣어
                p = p1 * p2
                rlt.append(p)
            elif i == '+': # 더하기인 경우,
                p = p1 + p2
                rlt.append(p)

    print(f'#{tc} {rlt[-1]}')

