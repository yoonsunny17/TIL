codes = input()

memo = []  # 연산자 저장해 둘 빈 stack 생성
check = list()  # 후위표기법으로 정리하여 저장할 list 생성

for code in codes:
    if code == '(':  # 열린 괄호인 경우에는,
        memo.append(code)  # stack에 저장해줘 (icp == 3)

    elif code == ')':  # 근데 만약에 닫힌 괄호를 만난 경우라면,
        temp = memo.pop()  # 일단 memo의 맨 위를 pop 해
        while temp != '(':  # temp가 열린괄호가 아닌 동안 반복해줘
            check.append(temp)
            temp = memo.pop()

    elif code == '*':  # 곱하기인 경우에는,
        memo.append(code)  # stack에 저장해줘 (icp == 2)

    elif code == '+':  # 더하기인 경우에는,
        while memo and memo[-1] != '(':  # stack이 비어있지 않고, 열린괄호 나오기 전까지는
            check.append(memo.pop())  # 연산자 꺼내서 check에 넣어줘
        memo.append(code)

    else:  # 피연산자인 경우에는,
        check.append(code)  # check에 바로 저장해줘

print(''.join(check))


# codes = input()
# rlt = list() # 최종 출력 list
# stack = [] # 연산자 모아둘 empty stack
#
# for code in codes:
#     if code.isalpha():
#         rlt.append(code)
#     else:
#         if code == '(':
#             stack.append('(')
#         elif code == '+':
#             stack.append('+')
#         elif code == '-':
#             stack.append('-')
#         elif code == '*':
#             stack.append('*')
#         elif code == '/':
#             stack.append('/')
#         elif code == ')':
#             while True:
#                 if stack[-1] == '(':
#                     stack.pop()
#                     break
#                 rlt.append(stack.pop())
#
# while True:
#     if not len(stack):
#         print(''.join(rlt))
#         break
#     rlt.append(stack.pop())