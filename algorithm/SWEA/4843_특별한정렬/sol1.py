'''
특별한 정렬 결과
idx 짝수인 경우: 내림차순
idx 홀수인 경우: 오름차순
'''

import sys

sys.stdin = open('sample_input.txt')

# 버블정렬을 사용해서 내림차순 정렬 시키자
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = bubblesort(lst) # 정렬된 리스트 반환받기

    rlt = [] # 특별한 정렬 받을 리스트 초기화
    # 10개까지만 출력하라고 했으니까 5번 반복
    for i in range(5):
        # 제일 큰 수 맨 앞에 넣고
        rlt.append(lst[i])
        # 그 다음에 제일 작은 수 들어온다
        rlt.append(lst[len(lst)-i-1])

    print(f'#{tc}', end=' ')
    for r in rlt:
        print(f'{r}', end=' ')
    print()
