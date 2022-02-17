import sys

sys.stdin = open('practice1.txt')

T = int(input())
for tc in range(1, T + 1):

    # slicing method
    my_words = input()
    my_words = my_words[::-1]
    print(f'#{tc} {my_words}')

    # list reverse method
    my_words = list(input())
    my_words.reverse()
    my_words = "".join(my_words)
    print(f'#{tc} {my_words}')


'''
# 문자열 뒤집기
# 1. 슬라이싱 사용
my_str = "abc"
my_str = my_str[::-1]
print(my_str)

# 2. reverse 메소드를 사용하고싶다
my_str = "abc"
my_str = list(my_str)
my_str.reverse()
my_str = "".join(my_str)
print(my_str)

# 3. 새로운 문자열 생성
new_str = ""
my_str = "abc"
for ch in my_str:
    new_str = ch + new_str
print(new_str)
'''