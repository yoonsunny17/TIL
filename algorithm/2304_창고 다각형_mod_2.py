# # N = int(input())
# # length = []
# # height = []
# # width = []

# # for _ in range(N):
# #     L, H = map(int, input().split())
# #     length.append(L)
# #     height.append(H)

# #     while len(length) != 0:
# #         i = 0
# #         if length[i] is min(length):
# #             width.append([length[i], height[i]])
# #             del length[i]
# #             del height[i]

# #         else:
# #             i += 1

# #     width = sorted(width)

# # for j in range(len(width)):
# #     length.append(width[j][0])
# #     height.append(width[j][1])

# # result = []

# # for k in range(N):
# #     while height[k] is not max(height):
# #         result.append(height[k] * (length[k+1] - length[k]))
# #         if height[k] > height[k+1]:
# #             height[k+1] = height[k]

        
# from turtle import heading


# N = int(input())
# length = []
# height = []
# width = []

# for _ in range(N):
#     L, H = map(int, input().split())
#     length.append(L)
#     height.append(H)

#     while len(length) != 0:
#         i = 0
#         if length[i] is min(length):
#             width.append([length[i], height[i]])
#             del length[i]
#             del height[i]

#         else:
#             i += 1

#     width = sorted(width)

# for j in range(len(width)):
#     length.append(width[j][0])
#     height.append(width[j][1])

# max_H = 1 # 최소 높이 1
# max_L = 0 # 최소 시작지점 0

# # 최고 높이 기둥을 기준으로
# if height[j] is max(height):
#     max_H = height[j]
#     max_L = length[j]

# left = []
# right = [] 

# # 왼쪽 => 0부터 최고 기둥까지
# for k in range(N):
#     if height[k] is max(height):
#         break

#     if height[k] > height[k+1]:
#         height[k+1] = height[k]
    
#     left.append(height[k] * (length[k+1] - length[k]))

# for k in range(N-1, 0, -1):
#     if height[k] is max(height):
#         break

#     if height[k-1] < height[k]:
#         height[k-1] = height[k]

#     right.append(height[k] * (length[k] - length[k-1]))

# rlt = sum(left) + sum(right) + max(height)

# print(rlt)
        
# # for k in range

# # for k in range(max(length)+1):
# #     if left < height[k]:
# #         left = height[k]
# #     total += left

# # # 오른쪽 => reverse idx로 맨 끝부터 최고 기둥까지
# # for k in range(max(length), max_L, -1):
# #     if right < height[k]:
# #         right = height[k]
# #     total += right

# # print(total)

# # for k in range(max_L+1):
# #     if left < height[k]:
# #         left = height[k]
# #     total += left

# # for k in range(length[N], max_L, -1):
# #     if right < height[k]:
# #         right = height[k]
# #     total += right

# # print(total)



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

for j in range(len(width)):
    length.append(width[j][0])
    height.append(width[j][1])

max_L = 0 # 최소 시작지점 0
# 최고 높이 기둥을 기준으로
if height[j] is max(height):
    max_L = length[j]

 
# 왼쪽 => 0부터 최고 기둥까지
total = 0
left = 0
for k in range(max_L+1):
    if height[k] is max(height):
        break

    if height[k] > left:
        left = height[k]
    
    total += left
    #left.append(height[k] * (length[k+1] - length[k]))

right = 0
for k in range(max(length), 0, -1):
    if height[k] is max(height):
        break

    if right < height[k]:
        right = height[k]
    
    total += right
    #right.append(height[k] * (length[k] - length[k-1]))

# rlt = sum(left) + sum(right) + max(height)
print(total)    

#print(rlt)


