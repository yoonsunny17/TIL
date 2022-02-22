import sys

sys.stdin = open('remove_words.txt')

def repeat(words):

    check = [] # 빈 stack 생성

    for i in range(len(words)):
        # stack이 비어있거나(or) 마지막에 나와 동일하지 않은 문자가 저장되어 있는 경우
        if len(check) == 0 or check[-1] != words[i]:
            check.append(words[i]) # stack 에 문자를 저장해줘

        # stack에 문자들이 저장되어 있는데(and), 마지막에 나와 동일한 문자가 저장되어 있는 경우
        elif len(check) != 0 and check[-1] == s[i]:
            check.pop() # stack 마지막 문자를 제거 후 반환해줘

    return len(check) # stack 안에 남은 문자열 길이 반환

T = int(input())

for tc in range(1, T + 1):
    s = input()
    rlt = repeat(s)

    print(f'#{tc} {rlt}')

