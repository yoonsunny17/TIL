''' success code !! '''
import sys

N, S = map(int, sys.stdin.readline().split())
numbs = list(map(int, sys.stdin.readline().split()))

# 투 포인터 초기화 시켜주기
start = 0
end = 1
# 구간합 받을 변수 초기화
# numbs[start:end]
interval_sum = numbs[0]
# 최솟값 받을 변수 초기화
min_rlt = float('inf')

while True:
    # 구간합이 목표값보다 크거나 같은 경우, start를 밀어!
    if interval_sum >= S:
        # 일단 최솟값 갱신 가능하면 갱신해주자
        if end - start < min_rlt:
            min_rlt = end - start
        interval_sum -= numbs[start]
        start += 1

    # 종료조건 numbs 맨 끝 숫자의 인덱스가 N-1이니까!
    elif end == N:
        break

    # 구간합이 목표값보다 작은 경우라면, end를 밀어!
    else:
        interval_sum += numbs[end]
        end += 1

if min_rlt == float('inf'):
    print(0)
else:
    print(min_rlt)




# while True:
#
#     # 구간 합이 목표값보다 크거나 같은 경우라면, start를 밀어!
#     if interval_sum >= S:
#         # 최소길이 갱신 가능하면 갱신하기
#         if end - start + 1 < min_rlt:
#             min_rlt = end - start + 1
#         interval_sum -= numbs[start]
#         start += 1
#
#     # end idx가 범위 나가면 종료!
#     elif end == N:
#         break
#
#     # 구간 합이 목표값보다 작은 경우라면, end를 밀어!
#     else:
#         interval_sum += numbs[end]
#         end += 1
#
#
# if min_rlt == float('inf'):
#     print(0)
# else:
#     print(min_rlt - 1)