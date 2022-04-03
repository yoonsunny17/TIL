''' success code '''
from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸 , 1 = 집, 2 = 치킨집
stores = []  # 가게 위치 받을 리스트
house = []  # 집 위치 받을 리스트
# 일단 치킨집 위치가 어디에 있는지 찾아줘야지
# 집 위치가 어딘지도 찾아줘
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            stores.append([i, j])
        if matrix[i][j] == 1:
            house.append([i, j])

# print(stores)
# print(house)

min_rlt = 987654321
distance = 0
# 치킨집에서 M개의 가게를 살려두는 경우를 생각해볼게
for store in combinations(stores, M):
    chicken_street = []
    # 각 집에서 치킨가게까지 최단 거리를 생각해보자
    for home in house:
        # 치킨가게가 여러개니까 일단 거리들 받을 리스트 만들고,
        min_d = []
        # 각 치킨가게에 대해서, 거리를 구하고 리스트에 담아줘
        for kfc in store:
            distance = abs(home[0]-kfc[0]) + abs(home[1]-kfc[1])
            min_d.append(distance)

            # chicken_street.append(distance)
            # print(distance)

        # 다 담았으면, 그 중 최솟값을 치킨 거리 리스트에 담아줘
        chicken_street.append(min(min_d))

    # print(chicken_street)
    # print(sum(chicken_street))
    # print()

    # 여러 경우의 M개 가게 살려두는 경우 중에서, 치킨 거리가 제일 적은 경우를 출력하자
    min_rlt = min(min_rlt, sum(chicken_street))

print(min_rlt)
