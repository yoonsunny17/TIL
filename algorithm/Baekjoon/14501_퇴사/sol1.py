''' Dynamic Programming Algorithm 사용!!! 한번 계산한 것은 다시 계산하지 않는다! '''
''' N번째 날은 N+1 번째 날 기준 수익과 N번째 날 수익 +T 만큼 지난 후 수익 중 큰 값을 골라서 갱신한다 '''

N = int(input())
time, profit = [], []
dp = [0]*(N+1)
for j in range(1, N+1):
    Ti, Pi = map(int, input().split())
    time.append(Ti)
    profit.append(Pi)

# 마지막 날부터 계산해주자
for i in range(N-1, -1, -1):
    # 상담이 끝나는 날이 N을 초과한다면 일을 할 수 없으므로, 일을 맡을 수 없으니까 그 전날의 스케쥴을 맡을 수 있는지 확인해보자
    if time[i] + i > N:
        dp[i] = dp[i+1]
    # N을 초과하지 않는 경우라면,
    # case 1. profit[i] + dp[i+time[i]] = 그 날 일을 하고 일이 끝나는 다음날 일을 할 수 있다고 가정했을 때 받을 수 있는 보상값
    # case 2. dp[i+1] = 다음날 일했을 때 얻을 수 있는 보상 
    # case 1, 2 중 max 값으로 갱신하자
    else:
        dp[i] = max(profit[i] + dp[i+time[i]], dp[i+1])

print(dp[0])