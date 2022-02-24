infix = "(6 + 5 * (2 - 8) / 2)"
stack = [] # 변환을 위해 사용할 stack
rlt = [] # 결과 담길 stack

# 1. 중위 표현식을 순회
for token in infix:

    # 2. 만약에, 너 숫자면 결과에 push
    if token.isdigit():
        rlt.append(token)

    # 3. 연산자라면
    else:
        if not stack: # stack이 비어있는 경우에는
            stack.append(token)
        else: # 스택이 비어있지 않다면(icp, isp 비교 후 push)
            # icp = 3
            if token == '(':
                stack.append(token)
            elif token == ')':
                temp = stack.pop()
                while temp != '(':
                    rlt.append(temp)
                    temp = stack.pop()
            # icp = 2
            elif token == '*' or token == '/': # 이미 icp = 3인 경우를 걸렀으니까 icp = 2 가 가장 높은 우선순위
                while stack and (stack[-1] == '*' or stack[-1] == '/'): # stack이 비어있지 않고, top이 * 또는 / 인 경우,
                    rlt.append(stack.pop())
                stack.append(token)
            # icp = 1
            elif token == '+' or token == '-':
                while stack and stack[-1] != '(': # stack이 비어있지 않고, isp = 0인 열린 괄호인 경우가 아니라면!
                    rlt.append(stack.pop())
                stack.append(token)

# stack에 남아있다면, 모두 꺼내서 push!
for token in range(len(stack)):
    rlt.append(stack.pop())

print(infix)
print(''.join(rlt))