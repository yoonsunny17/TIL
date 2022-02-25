import sys

sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T + 1):
    codes = input().split()
    answer = 0 # error 날 때 받을 변수
    numb_stack = [] # 피연산자 넣어 줄 빈 stack 만들자

    for code in codes:
        if code.isdecimal(): # 피연산자를 만났다면,
            numb_stack.append(int(code))

        else: # 피연산자가 아니라면,
            try: # try & except 사용해주자
                numb2 = int(numb_stack.pop())
                numb1 = int(numb_stack.pop())
                # 우선, 연산자를 만났으면, 각각 처리하고 stack 에 피연산자 넣어줘
                if code == '+':
                    rlt = numb1 + numb2
                    numb_stack.append(rlt)
                elif code == '-':
                    rlt = numb1 - numb2
                    numb_stack.append(rlt)
                elif code == '*':
                    rlt = numb1 * numb2
                    numb_stack.append(rlt)
                elif code == '/':
                    rlt = numb1 / numb2
                    numb_stack.append(rlt)

            except: # error 나는 경우
                answer = -1
    
    if answer == -1 or len(numb_stack) >= 2:
        print(f'#{tc} error')

    else:
        print(f'#{tc} {numb_stack.pop()}')
            


