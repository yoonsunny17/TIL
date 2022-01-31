N = int(input()) # 기둥의 개수
length = [] # L 리스트
height = [] # H 리스트
width = [] # [L, H] 받을 이차원 리스트
for _ in range(N):
    L, H = map(int, input().split()) # 각 기둥의 왼쪽 면의 위치 및 높이
    length.append(L)
    height.append(H)

    # 가로길이: length (max - min) + 1
    l = (max(length) - min(length)) + 1

    # 최대 면적
    max_width = l * max(height)

    # length 오름차순으로 이차원 리스트 요소 정렬
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

    for i in range(N):
        





 


# for i in range(N):
#     if length[i] is min(length):
#         width.append([length[i], height[i]])







# # 가로길이: length (max - min) + 1
# l = (max(length) - min(length)) + 1

# # 최대 면적
# max_width = l * max(height)

