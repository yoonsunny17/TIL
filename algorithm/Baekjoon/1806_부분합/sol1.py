'''
투포인터 구간 합
i=0, j=1
interval_sum = 0

'''
import sys

N, S = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))

# 투 포인터 초기값 설정해주자
start = 0
end = 1

# 구간 길이 최솟값 받을 변수 초기화
min_rlt = float('inf')

# 구간합 반복은 end 인덱스가 범위를 나갈 때까지 반복한다
while True:
    # 종료조건 설정!
    if end == N-1:
        break

    interval_sum = sum(numbs[start:end])

    # 구간 합이 목표 값보다 크거나 같은 경우, start를 밀자
    if interval_sum >= S:
        # 그리고 최솟값 갱신 가능하면 갱신하기
        if end - start + 1 < min_rlt:
            min_rlt = end - start + 1
        interval_sum -= numbs[start]
        start += 1

    # 구간 합이 목표 값보다 작은 경우, end를 밀자
    else:
        end += 1
        interval_sum += numbs[end]


if min_rlt == float('inf'):
    print(0)
else:
    print(min_rlt)