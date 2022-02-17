'''
ord() : 특정 한 문자를 아스키 코드 값으로 변환해 주는 함수
chr() : 아스키 코드 값을 문자로 변환해 주는 함수
ASCII CODE => 48 ~ 57; 0 ~ 9
'''

import sys

sys.stdin = open('practice2.txt')

# 숫자를 문자열로 변환하는 함수를 구현하자
def my_itoa(number):
    
    # idx_lst 만들어주기
    idx_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # idx 자리와 숫자가 동일하도록 리스트 만들어주었음

    # 양수인 경우,
    if number >= 0:
        code = number # 그대로 가져가자
        is_minus = False # 마이너스니? 아니
    # 음수인 경우,
    else:
        code = -1 * number # - 붙여줘
        is_minus = True # 마이너스니? 응

    code_lst = [] # 문자열 받을 리스트 초기화
    while True:
        # 종료조건 => 한자리 수 남았을 때
        if 1 <= code <= 9:
            code_lst.append(code % 10)
            break
        # 우선 code를 10으로 나누었을때의 나머지를 저장해주자
        code_lst.append(code % 10)
        code = code // 10 # 그리고 10으로 나누었을 때의 몫을 새로 할당해주자

    # code_lst에 거꾸로 들어갔을테니 다시 역으로 정렬
    code_lst = code_lst[::-1]
    rlt = [] # 문자 받아줄 리스트를 선언해주고,
    for i in code_lst:
        rlt.append(idx_lst[i])
        
    answer = ''.join(rlt) # join 함수 써주자

    # 근데 맨 처음 number가 음수였다면 다시 마이너스 돌려주고 반환하자
    if is_minus:
        answer = '-' + answer

    return answer

T = 6
for tc in range(1, 1 + T):
    numb = int(input())
    print(f'#{tc} {my_itoa(numb)} {type(my_itoa(numb))}')

