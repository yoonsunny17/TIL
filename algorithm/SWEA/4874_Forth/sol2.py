import sys

sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T + 1):
    codes = input().split()
    
    numb_stack = [] # 피연산자 넣어 줄 빈 stack 만들기
    
    # error 나는 경우: 피연산자 개수 <= 연산자 개수
    numb_lst = list()
    op_lst = list()

    i = 0
    while codes[i] != '.':
        if codes[i].isdecimal():
            numb_lst.append(codes[i])
            numb_stack.append(int(codes[i]))
            i += 1
        else:
            op_lst.append(codes[i])
            i += 1

    if len(numb_lst) <= len(op_lst):
        print(f'#{tc} error')

    else:
        for code in codes:
            if code == '+' or code == '-' or code == '*' or code == '/':
                numb1 = numb_stack.pop()
                numb2 = numb_stack.pop()

            # 그 다음엔, 사칙연산 각각의 경우를 모두 고려해줘
            if codes[i] == '+':
                rlt = numb1 + numb2
                numb_stack.append(rlt)

            elif codes[i] == '-':
                rlt = numb1 - numb2
                numb_stack.append(rlt)

            elif codes[i] == '*':
                rlt = numb1 * numb2
                numb_stack.append(rlt)

            elif codes[i] == '/':
                rlt = numb1 / numb2
                numb_stack.append(rlt)

            else:
                ans = numb_stack.pop()
                print(f'#{tc} {ans}')

