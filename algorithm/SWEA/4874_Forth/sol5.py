'''
pass!!!!!!!!
'''
import sys

sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T + 1):
    codes = input().split()

    stack = [] # empty stack
    for code in codes:
        if code == '.': # 마침표인 경우
            if len(stack) == 1: # 그리고 stack에 피연산자 1개 들어있다면,
                print(f'#{tc} {stack.pop()}') # pop 해줘
            else: # 나머지는 error 날껄
                print(f'#{tc} error')

        elif code.isdigit(): # 피연산자인 경우
            stack.append(int(code)) # int형으로 바꿔서 stack에 저장해줘

        else: # 연산자라면,
            if len(stack) < 2: # 근데 stack 안에 피연산자가 2개가 안된다면,
                print(f'#{tc} error') # error난다~
                break
            else: # 그게 아니라면, 우선 stack에서 두개 꺼내
                p2 = stack.pop()
                p1 = stack.pop()
                if code == '+':
                    stack.append(p1+p2)
                elif code == '-':
                    stack.append(p1-p2)
                elif code == '*':
                    stack.append(p1*p2)
                elif code == '/':
                    stack.append(p1//p2) # 정수..출력....으앙...


