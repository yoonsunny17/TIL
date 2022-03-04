# A든 B든 stack 에 넣고, 그 다음꺼가 같은 문자열이면 pop, 아니면 push
N = int(input())
cnt = 0 # 좋은 단어 아닌 애들 세어 줄 변수
for n in range(N):
    codes = list(input())
    stack = [] # empty stack
    stack.append(codes[0]) # 첫번째 codes 문자열은 넣어주기
    for i in range(1, len(codes)):
        if not len(stack): # stack이 비어있고, 문자열이 남아있음 push해줘
            stack.append(codes[i])
        else: # stack이 비어있지 않다면,
            if codes[i] == stack[-1]: # stack의 맨 위의 문자열과 같은 경우에 pop해줘
                stack.pop()
            else:
                stack.append(codes[i]) # 아니면 push해줘

    if len(stack) != 0:
        cnt += 1 # stack이 다 비워지지 않으면 좋은 단어가 아니야

rlt = N - cnt
print(rlt)

# rstrip 사용하는 방법도 해보자..