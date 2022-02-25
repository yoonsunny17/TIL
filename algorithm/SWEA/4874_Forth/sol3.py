import sys

sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T + 1):
    codes = input().split()

    numb_stack = [] # 피연산자 넣어 줄 빈 stack 만들어주자

    for i in range(len(codes)):
        if codes[i].isdecimal(): # 피연산자를 만났다면,
            numb_stack.append(int(codes[i])) # stack에 넣어줘

        else: # 피연산자가 아니라면, 두가지 경우가 있을거야 => 연산자거나, '.' 이거나
            # case.1 마침표인 경우
            if codes[i] == '.': # 만약 . 인데,
                if len(numb_stack) == 1: # stack에 피연산자 1개 있다면
                    print(f'#{tc} {numb_stack.pop()}') # 그대로 출력해줘
                    break
                else: # 1개가 아니라면,
                    print(f'#{tc} error') # error를 출력해줘
                    break

            # case.2 연산자인 경우
            else:
                if len(numb_stack) >= 2: # stack에 두 개 이상의 수가 들어있다면,
                    # stack에서 숫자 두개 꺼내줘
                    numb1 = numb_stack.pop()
                    numb2 = numb_stack.pop()

                    # 사칙연산에 대해 각각 계산하고, 다시 stack에 넣어줘
                    if codes[i] == '+':
                        numb3 = numb1 + numb2
                        numb_stack.append(numb3)

                    elif codes[i] == '-':
                        numb3 = numb1 - numb2
                        numb_stack.append(numb3)

                    elif codes[i] == '*':
                        numb3 = numb1 * numb2
                        numb_stack.append(numb3)

                    elif codes[i] == '/':
                        numb3 = numb1 / numb2
                        numb_stack.append(numb3)
            
                else: # stack에 문자 1개 이하가 들어있는데 연산자 만난거면 error나겠지
                    print(f'#{tc} error')
                    break

