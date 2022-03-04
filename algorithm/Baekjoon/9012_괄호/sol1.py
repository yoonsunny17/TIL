T = int(input())
for tc in range(1, T+1):
    vps = list(input())
    rlt = 'YES'

    open_stack = [] # 여는 괄호 받을 empty stack 생성
    for v in vps:
        if v == '(': # 여는 괄호라면, stack에 넣어줘
            open_stack.append(v)
        else: # 닫는 괄호인 경우는 2가지를 고려해줘
            if not len(open_stack): # stack에 여는 괄호가 없으면 짝이 안맞는거니까 NO 출력하고 끝이야
                rlt = 'NO'
                break
            else: # 여는 괄호 있으면 pop 해줘
                open_stack.pop()

    # 다 끝났는데 stack에 여는 괄호 남아있는 것도 NO야
    if len(open_stack) >= 1:
        rlt = 'NO'

    print(f'{rlt}')