import sys

sys.stdin = open('string_input.txt', 'rt', encoding='UTF-8')

T = 10
for tc in range(1, 11):
    N = int(input())
    target = input()
    chars = input()
    cnt = 0
    for i in range(len(chars)):
        if chars[i] == target[0]:
            if chars[i:i+len(target)] == target:
                cnt += 1

    print(f'#{tc} {cnt}')

