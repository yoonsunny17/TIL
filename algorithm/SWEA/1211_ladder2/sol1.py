'''
ladder 1 처럼 역방향 탐색하는 것이 편할 듯 (어차피 답 도출이 출발 column value이므로..)
'''

import sys

sys.stdin = open('ladder2.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 100 x 100 이차원 리스트 생성
    rlt = []  # 시작 column 값, cnt 값 넣어줄 리스트

    # delta 탐색 방향 지정 및 처음 시작 지점 초기화
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    idx = 0 # 0 = up, 1 = left, 2 = right
    
    for j in range(102): # indexError 방지 !!
        if arr[99][j] == 1:
            c = j
            r = 99
            cnt = 0 # 사다리 한칸 이동할 때마다 +1 누적해주기!

            while True:
                # 무한루프 종료조건
                if r == 0:
                    break

                # 왼쪽에 1 발견한 경우 왼쪽으로 가다가 0 만나면 stop
                if arr[r][c-1]:
                    idx = 1
                    while True:
                        r += dr[idx]
                        c += dc[idx]
                        cnt += 1
                        if arr[r][c-1] == 0:
                            break

                # 오른쪽에 1 발견한 경우 오른쪽으로 가다가 0 만나면 stop
                elif arr[r][c+1]:
                    idx = 2
                    while True:
                        r += dr[idx]
                        c += dc[idx]
                        cnt += 1
                        if arr[r][c+1] == 0:
                            break
                
                # 왼쪽, 오른쪽 1 없으면 위로 직진
                idx = 0
                r += dr[idx]
                c += dc[idx]
                cnt += 1

            rlt.append([c-1, cnt])

    # 최단거리인 경우일 때의 col값 구하기
    min_cnt = rlt[0][1]
    min_col = rlt[0][0]
    for i in range(len(rlt)):
        if rlt[i][1] <= min_cnt:
            min_cnt = rlt[i][1]
            min_col = rlt[i][0]
    print(f'#{tc} {min_col}')

