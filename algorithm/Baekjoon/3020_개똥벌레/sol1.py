import sys

# 석순 = 아래, 홀수번째 // 종유석 = 위, 짝수번째
N, H = map(int, input().split())

data = []  # input 받기

barrier = [0] * (H + 1)  # 석순 + 종유석
down = [0] * (H+1)  # 석순만
up = [0] * (H+1)  # 종유석만

for _ in range(N):
    data.append(int(input()))

cnt = 0
for i in data:
    # 종유석 만난 경우
    if cnt % 2 == 0:
        cnt += 1
        up[i] += 1
    # 석순 만난 경우
    else:
        cnt += 1
        down[H - i + 1] += 1

# 종유석 => 위에서 아래로 자라니까 거꾸로 범위 생각
for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]

# 석순 => 아래에서 위로 자람
for j in range(1, H + 1):
    down[j] += down[j - 1]

# 종유석 + 석순
for k in range(1, H + 1):
    barrier[k] = up[k] + down[k]


# print(barrier)
# index 0 제외해주기
print(min(barrier[1:]), barrier[1:].count(min(barrier[1:])))