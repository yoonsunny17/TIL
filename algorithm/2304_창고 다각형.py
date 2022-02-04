N = int(input())
length = []
height = []
width = []

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

    width = sorted(width)

# print(width)

# 위치 기반으로 정렬된 length, height list
for j in range(len(width)):
    length.append(width[j][0])
    height.append(width[j][1])

# 가장 높은 기둥을 중심으로 왼쪽, 오른쪽 면적 구하기
center_idx = 0
total = 0
# print(length)
# print(height)

for i in range(len(height)):
    if height[i] is max(height):
        center_idx = i
        break

total += height[center_idx]

# print(center_idx)
# print(height[center_idx])
# print(total)

# 왼쪽 면적 구하기 전 정리
for i in range(center_idx):
    if height[i] >= height[i+1]:
        height[i+1] = height[i]
    total += height[i] * (length[i+1] - length[i])

# 오른쪽 면적 reverse idx 사용해서 정리
for i in range(len(height)-1, center_idx, -1):
    if height[i] >= height[i-1]:
        height[i-1] = height[i]
    total += height[i] * (length[i] - length[i-1])

print(total)



# # 최종 면적 값 받을 total값 초기화
# total = 0

# # 왼쪽 면적 합산
# for i in range(center_idx):
#     total += height[i] * (length[i+1] - length[i])

# # 오른쪽 면적 합산 reverse idx
# for i in range(len(height)-1, center_idx, -1):
#     total += height[i] * (length[i] - length[i-1])

# # center pillar 값을 더해주면서 최종 면적 정리
# total += height[center_idx]

# print(total)






# ################################
# # max_L = 0 # 최소 시작지점 0
# # # 최고 높이 기둥을 기준으로
# # if height[j] is max(height):
# #     max_L = length[j]

 
# # # 왼쪽 => 0부터 최고 기둥까지
# # total = 0
# # left = 0
# # for k in range(max_L+1):
# #     if height[k] is max(height):
# #         break

# #     if height[k] > left:
# #         left = height[k]
    
# #     total += left
# #     #left.append(height[k] * (length[k+1] - length[k]))

# # right = 0
# # for k in range(max(length), 0, -1):
# #     if height[k] is max(height):
# #         break

# #     if right < height[k]:
# #         right = height[k]
    
# #     total += right
# #     #right.append(height[k] * (length[k] - length[k-1]))

# # # rlt = sum(left) + sum(right) + max(height)
# # print(total)    

# # #print(rlt)


