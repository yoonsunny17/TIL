# 교수님 풀이!
import sys

sys.stdin = open('1206.txt')


for tc in range(1, 11):

    cnt = int(input()) # 빌딩 수
    buildings = list(map(int, input().split())) # 각 빌딩 높이
    ans = 0 # 조망권 확보된 세대

    for i in range(2, cnt-2):
        curr_height = buildings[i]

        if not curr_height: # building이 안지어진 곳이라면.. if not = false
            continue # 다음 빌딩 나오세요
        
        else:
            max_height = 0 # 이번 빌딩을 기준으로 한 양옆 빌딩들 중 가장 높은 높이
            
            # 양옆 두칸씩의 빌딩 높이를 구하기
            d_row = [-2, -1, 1, 2] # i 기준 변화량
            for d in d_row:
                check_idx = i + d # 양옆 두 칸 빌딩의 idx
                if buildings[check_idx] > max_height:
                    max_height = buildings[check_idx] # 최대 높이 갱신

            if curr_height > max_height: # 조망권이 확보된 경우
                ans += curr_height - max_height

    print(f'#{tc} {ans}')

