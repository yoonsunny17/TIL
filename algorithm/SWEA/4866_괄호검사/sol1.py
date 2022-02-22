import sys

sys.stdin = open('bracket.txt')

def pair(words):

    check = [] # 빈 stack 생성

    # 문자에 괄호 있는지 체크하기
    for word in words:
        if word == '(' or word == '{':
            check.append(word)
        elif word == ')': # 닫는 괄호 나온 경우 => 짝이 맞는지, 개수가 맞는지 확인
            if len(check) != 0 and check[-1] == '(':
                check.pop()

            elif len(check) == 0:
                return False

            elif check[-1] == '{':
                return False

        elif word == '}':
            if len(check) != 0 and check[-1] == '{':
                check.pop()

            elif len(check) == 0:
                return False

            elif check[-1] == '{':
                return False

    if not len(check):
        return True

T = int(input())
for tc in range(1, T + 1):
    codes = input() # 한 문장의 코드 받기
    rlt = pair(codes) # 짝 여부 판별하는 pair 함수 사용하기 => 0 또는 1 반환

    if rlt is True:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

