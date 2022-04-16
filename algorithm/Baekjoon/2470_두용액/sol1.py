'''
BOJ 두 수의 합
음수의 합이여도 피곤해지지 않는다

정렬하고 

가장 왼쪽 // 가장 오른쪽 포인터 두고 시작

value = float('inf')
sol1, sol2 = 0, 0

0에 제일 가장 가까운 두 수의 합을 구해야 함
abs(numbers[i] + numbers[j]) < value:
    value = abs(numbers[i] + numbers[j])
    sol1 = numbers[i]
    sol2 = numbers[j]
'''
import sys

N = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))
info.sort()  # 일단 정렬해주자

# 두 수의 합이니까 스타트는 맨 왼쪽, 엔드는 맨 오른쪽 시작이야
start = 0
end = N - 1

# 최솟값이니까 초기값은 무한대로 초기화해주기
min_cnt = float('inf')
# 용액 받을 변수 초기화
sol1, sol2 = 0, 0

# 두 인덱스가 같은 수를 가리키기 전까지 반복해줘
while start < end:
    # 만약 두 수의 합의 절댓값이 최솟값을 갱신할 수 있다면 갱신해줘
    if abs(info[start] + info[end]) < min_cnt:
        min_cnt = abs(info[start] + info[end])
        sol1 = info[start]
        sol2 = info[end]

    # 그렇지 않다면,
    else:
        # 만약 두 수의 합이 음수인 경우에는 start 인덱스를 오른쪽으로 밀어
        if info[start] + info[end] < 0:
            start += 1
        # 만약 두 수의 합이 양수라면 end 인덱스를 외쪽으로 땡겨
        else:
            end -= 1

print(f'{sol1} {sol2}')






''' 시간 초과 ...?!?!!!???'''
# start = 0
# end = N - 1
#
# min_cnt = float('inf')
# cnt = 0
# sol1, sol2 = 0, 0
#
# while start < end:
#     cnt = info[start] + info[end]
#
#     if abs(cnt) < min_cnt:
#         min_cnt = abs(cnt)
#         sol1 = info[start]
#         sol2 = info[end]
#
#     if cnt < 0:
#         start += 1
#     elif cnt > 0:
#         end -= 1
#
# print(f'{sol1} {sol2}')