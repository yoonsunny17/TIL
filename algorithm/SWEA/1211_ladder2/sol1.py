'''
ladder 1 처럼 역방향 탐색하는 것이 편할 듯 (어차피 답 도출이 출발 column value이므로..)
'''

import sys

sys.stdin = open('ladder2.txt')

T = 10
for tc in range(1, 11):
    N = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)] # 100 x 100 이차원 리스트 생성
    min_cnt = []  # 결과값 넣어줄 리스트 초기화

    # delta 탐색 방향 지정 및 처음 시작 지점 초기화
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    idx = 0 # 0 = up, 1 = left, 2 = right
    
    # 도착점에서 출발점으로 역탐색
    # row = 99 시작, arr[99][c] == 1 인 경우 모두 반복
    for j in range(100):
        if arr[99][j] == 1:
            c = j
    r = 99

    cnt = 0
    while True:
        # 종료조건 설정
        if r == 0:
            break

        # 왼쪽에 1 있는 경우 왼쪽으로 방향 틀고, 0 나오면 stop
        if array





    cnt = 0
    min_cnt = [] # 최솟값 구해줄 리스트 만들기

    while True:
        # 종료조건 설정
        if r >= 100:
            break

        # 왼쪽에 1 있으면 왼쪽으로 방향 틀고, 0 나오면 stop
        if arr[r][c-1] and 0 <= c-1 < 100:
            idx = 1
            while True:
                r += dr[idx]
                c += dc[idx]
                cnt += 1
                if arr[r][c-1] == 0 or c <= 0:
                    break

        # 오른쪽에 1 있으면 오른쪽으로 방향 틀고, 0 나오면 stop
        elif arr[r][c+1] and 0 <= c+1 < 100:
            idx = 2
            while True:
                r += dr[idx]
                c += dc[idx]
                cnt += 1
                if arr[r][c+1] == 0 or c >= 100:
                    break

        #  왼쪽, 오른쪽에 1 발견 못했으면 아래로 직진
        idx = 0
        r += dr[idx]
        c += dc[idx]
        cnt += 1

    min_cnt.append([c, cnt]) # column, cnt 값을 같이 append 해주기

    for i in min_cnt:
        print(i)
