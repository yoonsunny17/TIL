import sys

sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T + 1):
    codes = input().split()

    stack = [] # 빈 stack 만들어주기
    ans = 0

    for code in codes:
        if code.isdecimal(): # code가 피연산자 (숫자) 인 경우에는,
            stack.append(int(code)) # stack 에 넣어줘

        else: # code가 연산자거나 마침표인 경우에는,
            try:
                numb2 = stack.pop()
                numb1 = stack.pop()

                if code == '+':
                    rlt = numb1 + numb2
                    stack.append(rlt)
                elif code == '-':
                    rlt = numb1 - numb2
                    stack.append(rlt)
                elif code == '*':
                    rlt = numb1 * numb2
                    stack.append(rlt)
                elif code == '/':
                    rlt = numb1 / numb2
                    stack.append(rlt)
            except:
                ans = -1

    if ans == 0 and len(stack) == 1:
        print(f'#{tc} {stack.pop()}')
    else:
        print(f'#{tc} error')






    # print(len(codes) - len(check) - 1)
    # print(len(check))

        # else:
        #     if code == '.': # code가 마침표인 경우라면,
        #         if len(stack) >= 2
        #     if code != '.': # 숫자도 아니고 연산자도 아닌 경우에는
        #         numb2 = stack.pop()
        #         numb1 = stack.pop()
        #

