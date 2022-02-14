import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split())) # 10개의 요소로 이루어진 리스트
    n = len(arr)

    sub_lst = [] # 각 tc에 대한 모든 부분집합 저장할 리스트 => 이차원리스트
    cnt_lst = [] # 각 부분집합 원소 합 받을 리스트 => 일차원리스트
    cnt = 0 # 합이 0인 부분집합 개수 받을 변수

    for i in range(1<<n):
        num_lst = [] # 모든 부분집합의 경우 받을 리스트 => 일차원리스트
        for j in range(n):
            if i & (1<<j):
                num_lst.append(arr[j])
        sub_lst.append(num_lst)
        
    for sub in sub_lst:
        rlt = 0 # 각 부분집합 합 구하기
        for k in sub:
            rlt += k
        cnt_lst.append(rlt)

    # 부분집합의 원소의 합이 0인 경우 cnt에 1씩 누적 합해주기
    for numb in cnt_lst:
        if numb == 0:
            cnt += 1

    # 공집합을 제외하고 부분집합의 합이 0인 경우를 고려해야함
    if cnt >= 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
