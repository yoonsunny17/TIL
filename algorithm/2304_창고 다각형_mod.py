N = int(input()) # 기둥 개수
length = [] # 기둥 왼쪽 면 위치 L list
height = [] # 기둥 높이 H list
width = [] # L, H 이차원 list

for _ in range(N):
    L, H = map(int, input().split())
    length.append(L)
    height.append(H)

    while len(length) != 0:
        i = 0
        if length[i] is min(length):
            width.append([length[i], height[i]])
            del length[i]
            del height[i]

        else:
            i += 1

    width = sorted(width) # L 기준 오름차순으로 정렬

print(width)





