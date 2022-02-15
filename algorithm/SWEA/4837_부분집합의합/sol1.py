import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N개의 원소를 가지는 부분집합, 원소의 합이 K인 부분집합
    arr = [x for x in range(1, 13)]  # 1~12 숫자 가지는 집합
    n = len(arr)

    sub_lst = []  # 부분집합 중 N개의 원소를 가지는 부분집합들을 저장하는 리스트
    for i in range(1 << n):
        num_lst = [] # 부분집합 구하기
        for j in range(n):
            if i & (1 << j):
                num_lst.append(arr[j])
        sub_lst.append(num_lst)

    # 개수가 N인 리스트들 모으기
    sum_lst = []
    for sub in sub_lst:
        if len(sub) == N:
            sum_lst.append(sub)

    # 개수가 N인 리스트들 중 합이 K인 리스트 있는지 확인
    cnt = 0 # 있다면 +1 해줄 변수
    for lst in sum_lst:
        rlt = 0 # for 문 안에 넣어주어야 한다는 거!! 위치 중요~~
        for i in range(len(lst)):
            rlt += lst[i]
        if rlt == K:
            cnt += 1

    print(f'#{tc} {cnt}')


