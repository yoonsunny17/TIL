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

    width = sorted(width) # L 기준으로 오름차순 정렬

# print(width) => L 기준 오름차순 정렬
# length, height 리스트는 다시 빈 리스트가 됨
# 이제 다시 width에 넣은 순서대로 length, height에 요소 넣어주기

# 기둥 위치 순서대로 정렬된 length, heigth list
for j in range(len(width)):
    length.append(width[j][0])
    height.append(width[j][1])

# print(length)
# print(height)


left_area = []
right_area = []
center_area = []


for k in range(N):
    if height[k] is max(height):
        center_area.append(height[k])

        # center_area += height[k]


# print(center_area)

# 왼쪽 기둥부터 max 기둥전까지

for l in range(N):
    if height[l] is max(height):
        break

    if height[l] <= height[l+1]:
        left_area.append(height[l] * (length[l+1] - length[l]))

    else:
        left_area.append(height[l] * (length[l+1] - length[l]))
        height[l+1] = height[l]

# print(left_area)

# length, height list에서 왼쪽 idx 제거 후 역순 sort (오른쪽 기둥부터 max 기둥 계산 위해)


# 오른쪽 기둥부터 max 기둥전까지 reverse idx
for r in range(N-1, 0, -1):
    if height[r] is max(height):
        break

    if height[r] <= height[r-1]:
        right_area.append(height[r] * (length[r] - length[r-1]))

    else:
        right_area.append(height[r] * (length[r] - length[r-1]))
        height[r-1] = height[r]

# print(right_area)
        
    rlt = sum(center_area) + sum(right_area) + sum(left_area)
print(rlt)



