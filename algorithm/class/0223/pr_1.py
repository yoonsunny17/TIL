# output이 이상해요...
T = int(input())
for tc in range(1, T + 1):
    codes = input()  # 수식문자열 입력받을 변수
    memo = []  # 연산자 받을 빈 stack 생성
    rlt = list()  # 결과 받을 빈 list 만들기

    for code in codes:
        # 만약 연산자라면 스택에 저장해줘
        if code == '-' or code == '+' or code == '*' or code == '*':
            memo.append(code)

        # 피연산자라면, rlt 리스트에 저장해줘
        else:
            rlt.append(code)

        # input 길이 = stack 길이 + rlt 길이 => 한 문장 순회 끝났다!
        # 그럼 memo에서 pop을 통해 rlt에 하나씩 저장해주자
    if len(codes) == len(memo) + len(rlt):
        rlt.append(memo.pop())

    # 리스트로 받았으니까 join 써서 출력해
    answer = ''.join(rlt)
    print(f'#{tc} {answer}')