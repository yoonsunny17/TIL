'''
Runtime Error...!!!
'''

import sys

sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    sub_set = []

    # 비트 연산을 통한 부분집합 받기
    for i in range(1 << len(numbers)):
        lst = []
        for j in range(len(numbers)):
            if i & (1 << j):
                lst.append(numbers[j])

        # print(lst) => 입력받은 집합에 대한 모든 부분집합 출력
        # 부분집합 중 원소의 개수가 두개인 부분집합만 가져오기
        if len(lst) == 2:
            sub_set.append(lst)


    max_rlt = []
    for r in range(len(sub_set)):
        multi_sum = sub_set[r][0] * sub_set[r][1]
        multi_sum = str(multi_sum)

        for i in range(len(multi_sum) - 1):
            if multi_sum[i] <= multi_sum[i+1]:
                max_rlt.append(multi_sum)

    max_rlt = list(map(int, max_rlt))
    max_v = max_rlt[0]
    for i in range(len(max_rlt)):
        if max_rlt[i] >= max_v:
            max_v = max_rlt[i]
        else:
            max_v = -1

    print(f'#{tc} {max_v}')

