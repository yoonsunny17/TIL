import sys

R, S = map(int, sys.stdin.readline().split())

# 충돌 전 유성 사진
before_collision = [sys.stdin.readline().rstrip() for _ in range(R)]
# 유성과 땅 사이 거리 갱신해 줄 변수
distance = float('inf')

for j in range(S):
    low_meteor = 0
    high_ground = float('inf')
    check = False  # 유성이 있는지 확인해주기 (처음에는 없음으로 설정)

    for i in range(R):
        # 만약 유성이고, 최솟값 갱신 가능하면 갱신해주기
        if before_collision[i][j] == 'X':
            if i > low_meteor:
                low_meteor = i
                check = True  # 유성 발견했음을 체크!

        # 만약 땅이고, 최댓값 갱신 가능하면 갱신해주기
        elif before_collision[i][j] == '#':
            if i < high_ground:
                high_ground = i

    # 유성이 있다면, 가장 낮은 유성과, 가장 높은 땅의 차이를 계산하고 갱신해줘
    if check:
        distance = min(abs(high_ground - low_meteor) - 1, distance)
        
# 충돌 후의 사진을 출력할거야
# 충돌 후 배열 받아주기
after_collision = [list('.' for _ in range(S)) for _ in range(R)]
for i in range(R):
    for j in range(S):
        if before_collision[i][j] == 'X':
            after_collision[i+distance][j] = 'X'
        if before_collision[i][j] == '#':
            after_collision[i][j] = '#'

for i in range(R):
    for j in range(S):
        sys.stdout.write(after_collision[i][j])
    sys.stdout.write('\n')