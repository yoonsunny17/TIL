w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

dp = [1, 1, -1, -1]
dq = [1, -1, -1, 1]
i = 0

while time != 0: # 좌표 하나 이동할 때마다 time -= 1

    # 벽을 만날 때까지 한 방향으로 쭉 이동, time -= 1
    # p += dp[i]
    # q += dq[i]
    # time -= 1

    # 벽을 만나면 방향 틀기
    if p < 0 or q < 0 or p > w or q > h:
        p -= dp[i]
        q -= dq[i]

        for di in range(1, 4):
            p += dp[i+di]
            q += dq[i+di]
            if 0 <= p <= w and 0 <= q <= h:
                time -= 1
            else:
                p -= dp[i+di]
                q -= dq[i+di]
        # i = (i + 1) % 4
        # p += dp[i]
        # q += dq[i]
        # time -= 1
    # else:
    p += dp[i]
    q += dq[i]
    time -= 1

print(f'{p} {q}')