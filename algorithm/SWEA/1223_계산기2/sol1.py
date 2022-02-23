'''
문자열에서 +를 만난다면 stack에 있는 모든 연산자들을 pop 해준 뒤 +를 push 해주고,
*를 만난다면 그냥 push 해줘어어
'''
import sys

sys.stdin = open('calculator2.txt')

T = 10
for tc in range(1, 11):
    L = int(input())
    codes = input()
    
    memo = [] # 연산자 저장할 빈 stack 생성
    answer = list() # 답 출력할 빈 list 생성

    for code in codes:
        if code == '*': # 곱하기 연산자인 경우
            memo.append(code) # stack 에 저장해줘

        elif code == '+': # 더하기 연산자인 경우
            while len(memo) != 0: # 기존 stack 에 저장되어 있던 연산자들을 모두 꺼내서 answer 에 넣어줘
                answer.append(memo.pop())
            memo.append(code) # stack이 다 비었다면 연산자 저장해줘
        
        else: # 피연산자인 경우에는
            answer.append(code) # answer 리스트에 저장해줘

    while len(memo) != 0: # stack에 있는 연산자가 다 꺼내지지 않았을거야
        answer.append(memo.pop()) # 남은애들 처리해줘

    # 후위표기식으로 표현 끝났으니까 이제 계산을 시작하자
    numb_memo = [] # 숫자를 저장할 빈 stack 생성
    for i in answer:
        if i == '*': # 곱하기 만나면 두 숫자 pop 해서 곱한다음 다시 stack에 저장해줘
            numb1 = numb_memo.pop()
            numb2 = numb_memo.pop()
            numb3 = numb1 * numb2
            numb_memo.append(numb3)
        elif i == '+': # 더하기 만나면 두 숫자 pop 해서 더한 다음 다시 stack에 저장해줘
            numb1 = numb_memo.pop()
            numb2 = numb_memo.pop()
            numb3 = numb1 + numb2
            numb_memo.append(numb3)
        else: # 피연산자면 stack 에 저장해줘 => int로!
            numb_memo.append(int(i))

    print(f'#{tc} {numb_memo[0]}')