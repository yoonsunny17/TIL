w, h = map(int, input().split()) # w = col, h = row
p, q = map(int, input().split()) # p = w-axis, q = h-axis
time = int(input()) # 개미 움직이는 시간

# 개미가 벽을 만났을 때 갈 수 있는 방향 delta 시계방향으로 나열
dp = [1, 1, -1, -1]
dq = [1, -1, -1, 1]
i = 0
while time != 0: # 좌표 하나 이동할 때마다 time -= 1

    # 벽을 만날 때까지 한 방향으로 쭉 이동, time -= 1
    p += dp[i]
    q += dq[i]
    time -= 1

    # 벽을 만나면 방향 틀기 (뺑뺑이 코드)
    if p == 0 or q == 0 or p == w or q == h:
        p -= dp[i]
        q -= dq[i]

        i = (i + 1) % 4
        p += dp[i]
        q += dq[i]
        time -= 1

print(f'{p} {q}')

