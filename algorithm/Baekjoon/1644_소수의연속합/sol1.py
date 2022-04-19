'''
에라토스테네스의 채

입력보다 작은 소수 리스트를 만들고,
구간합을 구하면 돼

'''
import sys

N = int(sys.stdin.readline())
check = [True] * (N+1)
check[0], check[1] = 0, 0

prime_lst = []

if N == 1:
    print(0)
    exit()

for i in range(2, N+1):
    if check[i]:
        prime_lst.append(i)
    for j in range(i*i, N+1, i):
        check[j] = False

# print(prime_lst)

# 가능한 구간합 경우의 수 세어주자
start = 0
end = 1
interval_sum = prime_lst[0]
cnt = 0

while True:
    # 만약 구간 합이 N보다 크거나 같은 경우라면,
    if interval_sum >= N:
        # 근데 구간합이 N과 동일한 경우라면 경우의 수 하나 +1 증가해줘
        if interval_sum == N:
            cnt += 1
        interval_sum -= prime_lst[start]
        start += 1

    # 종료조건 설정; prime_lst 인덱스가 end 인덱스와 동일해지면 종료!
    elif end == len(prime_lst):
        break

    # 구간합이 목표값보다 작으면 end를 밀자
    else:
        interval_sum += prime_lst[end]
        end += 1

print(cnt)

# N = int(input())
# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# matrix.sort(key=lambda x:(x[1], x[0]))
#
# for lst in matrix:
#     print(f'{lst[0]} {lst[1]}')
