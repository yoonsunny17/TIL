w, h = map(int, input().split()) # w = 가로, h = 세로
p, q = map(int, input().split()) # p = w축 현재 위치, q = h축 현재 위치
time = int(input()) # 개미 움직이는 시간

# 개미가 벽을 만났을 때 갈 수 있는 방향 delta 시계방향으로 나열
dp = [1, 1, -1, -1]
dq = [1, -1, -1, 1]
i = 0

while True:

    if time == 0:
        break

    x = p + dp[i]
    y = q + dq[i]
    time -= 1

    if x == 0 or y == 0 or x == w or y == h:
        while True:
            i += 1
            if 0 <= p + dp[i] <= w and 0 <= q + dq[i] <= h:
                x = p + dp[i]
                y = q + dq[i]
                break
            else:
                continue

        i += 1
        p, q = x, y

    else:
        p, q = x, y



