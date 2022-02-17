'''
일단 가로로 가장 긴 길이 찾고
나머지 row 뒷부분에 최댓값 row 길이만큼 ''를 append 해주기
그다음에 세로로 한줄씩 읽어나가면서 새로운 리스트에 저장
join함수 써서 출력하면 될 듯 => 만약에 공백 처리 애매하면
또 다른 리스트 만든다음에 아까 만들어 둔 리스트에서 공백이 아닌 문자열을 리스트에 옮겨주고
그 문자열들을 join써서 출력하든가
'''

import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = []
    for _ in range(5):
        row_i = list(map(str, input()))
        lst.append(row_i)

    # 가장 긴 row 찾기
    max_r = 0
    for i in range(5):
        if len(lst[i]) > max_r:
            max_r = len(lst[i])

    # 가장 긴 row 가 아닌 row들의 뒤에 빈 문자열 append 해주기
    for i in range(5):
        if len(lst[i]) < max_r:
            for _ in range(max_r - len(lst[i])):
                lst[i].append('')
                
    # 이제 세로로 읽어주면서 새로운 리스트에 저장해주자
    c_lst = []
    for c in range(max_r):
        for r in range(5):
            c_lst.append(lst[r][c])

    # 그치만 c_lst에는 빈 문자열도 들어가 있을테니 빈 문자열을 빼준 새로운 리스트를 또 만들자
    new_lst = []
    for i in range(len(c_lst)):
        if c_lst[i] != '':
            new_lst.append(c_lst[i])

    # 이제 진짜 최종 출력 ㄱㄱ
    rlt = ''.join(new_lst)
    print(f'#{tc} {rlt}')
