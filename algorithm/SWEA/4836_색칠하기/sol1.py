import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # red_lst = []
    # blue_lst = []
    # purple_lst = []
    cnt = 0
    for i in range(N): # N 개수만큼
        colors = list(map(int, input().split())) # r1 c1 r2 c2 color 순서대로 입력받기

        # RED color 면적과 BLUE color 면적 구분해서 받기 & slicing 사용해서 좌표 정보만 입력 받기
        # 마지막 자리가 1인 경우 red
        red_lst = []
        if colors[-1] == 1:
            colors = colors[0:4] # r1, c1, r2, c2
            dr = colors[2] - colors[0] + 1 # dr = r2 - r1 + 1
            dc = colors[3] - colors[1] + 1 # dc = c2 - c1 + 1
            # red_lst = []
            for ir in range(dr):
                for ic in range(dc):
                    red_r = colors[0] + ir
                    red_c = colors[1] + ic
                    red = [red_r, red_c]
                    red_lst.append(red)

        # 마지막 자리가 2인 경우 blue
        blue_lst = []
        if colors[-1] == 2:
            colors = colors[0:4]
            dr = colors[2] - colors[0] + 1  # dr = r2 - r1 + 1
            dc = colors[3] - colors[1] + 1  # dc = c2 - c1 + 1

            for ir in range(dr):
                for ic in range(dc):
                    blue_r = colors[0] + ir
                    blue_c = colors[1] + ic
                    blue = [blue_r, blue_c]
                    blue_lst.append(blue)

        # red_lst, blue_lst 공통 부분 있으면 cnt + 1

    for i in range(len(red_lst)):
        for j in range(len(blue_lst)):
            if red_lst[i] == blue_lst[j]:
                cnt += 1

    print(f'#{tc} {cnt}')



