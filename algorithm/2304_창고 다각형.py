N = int(input()) # 기둥의 개수
length = [] # L(기둥의 왼쪽 면의 위치) 리스트
height = [] # H(기둥의 높이) 리스트
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

    # center_area = 0 # 최종 면적 받을 변수
    # left_area = 0 
    # right_area = 0 
    
    # 넓이 면적 구하는데에 필요한 기둥에 대한 원소들만 받을 리스트
    pillars = list(width[0],width[-1])

    # 가장 높은 기둥 찾기
    for i in range(N):
        if width[i][1] is max(height):
            pillars.append(width[i])

        # 왼쪽 기둥에서 가장 높은 기둥까지
        left_pillar = width[0]
        for j in range(1, i):
            if width[0][1] <= width[j][1]:
                pillars.append(width[j])

        # 오른쪽 기둥에서 가장 높은 기둥까지
        right_pillar = width[-1]
        for k in range(-1, -i-N):
            if width[-1][1] <= width[k][1]:
                pillars.append(width[k])

    pillars = sorted(pillars)


    # 가장자리 두개의 기둥은 무조건 포함
    # right_pillar = width[N] or width[-1]





    # # 첫번째 기둥과 맨 마지막 기둥은 필수로 포함되어야 함
    # # 가장 높은 기둥의 넓이 먼저 더하기
    # for i in range(N):
    #     if width[i][1] is max(height):
    #         center_area += width[i][1]

    # j = 0
    # while j == i:
    #     if width[j][1] <= width[j+1][1]:
    #         left_area += width[j][1] * (width[j+1][0] - width[j][0])
    #         j += 1

            



    for j in range(i):
        if width[j][1] <= width[j+1][1]:
            left_area += width[j][1] * (width[j+1][0] - width[j][0])

        elif width[j][1] > width[j+1][1]:
            
        
            

        if width[i][0] < width[i+1][0]:
            total_area += width[i][0] * (width[i+1][0] - width[i][0])



    for i in range(N):
        if width[i][0] < width






 


# for i in range(N):
#     if length[i] is min(length):
#         width.append([length[i], height[i]])







# # 가로길이: length (max - min) + 1
# l = (max(length) - min(length)) + 1

# # 최대 면적
# max_width = l * max(height)

