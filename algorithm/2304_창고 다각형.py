N = int(input()) # 기둥의 개수
length = [] # L(기둥의 왼쪽 면의 위치) 리스트
height = [] # H(기둥의 높이) 리스트
width = [] # [L, H] 받을 이차원 리스트
for _ in range(N):
    L, H = map(int, input().split()) # 각 기둥의 왼쪽 면의 위치 및 높이
    length.append(L)
    height.append(H)

    # # 가로길이: length (max - min) + 1
    # l = (max(length) - min(length)) + 1

    # # 최대 면적
    # max_width = l * max(height)

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
    pillars = [width[0],width[-1]]

    # 가장 높은 기둥 찾기
    for i in range(N):
        if width[i][1] == max(width[i][1]):
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

    # 기둥 위치로 정렬, 최종 면적 값 설정
    pillars = sorted(pillars)
    rlt = 0
    for p in range(len(pillars)):
        if pillars[p][1] <= pillars[p+1][1]:
            rlt += pillars[p][1] * (pillars[p+1][0] - pillars[p][0])

        elif pillars[p][1] == max(pillars[p][1]):
            rlt += pillars[p][1]

        elif max(pillars[p][1]) > pillars[p+1][1]:
            rlt += pillars[p+1][1] * (pillars[p+1][0] - pillars[p][0])

            if pillars[p] == pillars(len(pillars)):
                break

    print(rlt)

