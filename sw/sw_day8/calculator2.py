# 계산하자~!
# 계산할 때에는 stack에 피연산자를 넣어주었다가, 연산자를 만나면 pop pop으로 숫자 두개 꺼내서 연산해주고, 다시 stack에 넣어준다
# 단!! 첫번째 pop 한 애를 연산자 왼쪽, 그 다음 pop 한 애를 연산자 오른쪽으로 배치 해주어야 한다!!
rlt = '6528-*2/+'
stack = []
for token in rlt:
    if token.isdecimal(): # 숫자라면
        stack.append(int(token))

    else: # 연산자라면
        p2 = stack.pop()
        p1 = stack.pop()

        if token == '+':
            result = p1 + p2
            stack.append(result)
        elif token == '-':
            result = p1 - p2
            stack.append(result)
        elif token == '*':
            result = p1 * p2
            stack.append(result)
        elif token == '/':
            result = p1 / p2
            stack.append(result)
ans = stack.pop()
print(ans)