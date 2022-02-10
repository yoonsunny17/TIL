import sys

sys.stdin = open('1206.txt')

# 총 10개의 test case
for tc in range(1, 11):
    T = int(input()) # 각 tc에 따른 건물 개수
    lst = list(map(int, input().split())) # 각 건물의 높이
    cnt = 0 # 조망권 획득한 세대 세는 변수

    for i in range(2, len(lst)-2): # 좌 우로 두개씩 0 0 이니까 idx range 설정 조심
        if lst[i] > lst[i-1] and lst[i] > lst[i-2] and lst[i] > lst[i+1] and lst[i] > lst[i+2]: # 전망권 획득
            rlt = 0 # max 함수 못쓸것 같아서.. 주변 전망 가리는 건물 중 최대 높이 구하는 변수
            for j in [lst[i-1], lst[i-2], lst[i+1], lst[i+2]]:
                if j > rlt:
                    rlt = j # 최대 건물 층 수 도출

            cnt += lst[i] - rlt # 각 건물에서 조망권 획득한 세대 수

    print(f'#{tc} {cnt}')

