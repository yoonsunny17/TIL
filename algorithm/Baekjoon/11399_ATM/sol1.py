# 내장함수 sum, append 빼서 최대한 빠르게 해보자!
N = int(input())
P = list(map(int, input().split()))
P.sort()  # 오름차순으로 정렬 후 시작하자
time = [0]*N  # 각 사람들이 기다려야 하는 시간 받을 리스트

# 각 사람들이 기다려야 하는 시간 구하기
cnt = 0
for i in range(N):
    cnt += P[i]
    time[i] = cnt

# 최종 시간 구하기
rlt = 0
for t in time:
    rlt += t

print(rlt)