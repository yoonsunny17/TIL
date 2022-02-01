from turtle import left, right


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

total = 0
left_area = 0
right_area = 0
center_area = 0

# 진짜 조금만 고치면 될듯... 지금 width[j][1] is max 라고 하니까 j가 max일때로 하는거같기도
for j in range(len(width)):
    if (width[j][1] is max) or (j+1 == len(width)):
        center_area = width[j][1]
        break
    else:
        left_area += width[j][1] * (width[j+1][0]- width[j][0])
    # left 부터 max까지   
        

# 진짜 조금만 고치면 될듯... 지금 width[k][1] is max 라고 하니까 k가 max일때로 하는거같기도
for k in range(-1, -len(width)):
    if (width[k][1] is max) or (k-1 == -len(width)):
        break
    else:
        right_area += width[k][1] * (width[k-1][0]- width[k][0])
    # right 부터 max까지 reverse idx

# total = left_area + right_area + center_area

print(total)


# right_area = 0  # while문으로 하는게 나을 것 같기도 하고...
# for i in range(len(width)):
#     if width[i][1] <= width[i+1][1]:
#         right_area += width[i][1] * (width[i+1][0] - width[i][0])
#     else:
#         right_area += width[i][1] * (width[i+1][0] - width[i][0])
#         if width[i][1] is max in range(len(width)):
#             break
#         else:
#             width[i+1][1] = width[i][1]
#             continue


# left_area = 0
# for j in range(-1, len(width)):
#     if width[j][1] <= width[j-1][1]:
#         left_area += width[j][1] * (width[j-1][0] - width[j][0])
#     else:
#         left_area += width[j][1] * (width[j-1][0] - width[j][0])
#         if width[j][1] is max in range(len(width)):
#             break
#         else:
#             width[j-1][1] = width[j][1]
#             continue

# total = right_area + left_area

# print(total)

    



