'''
test case 10개 중 2개 맞음... fail!!!
'''
import sys

sys.stdin = open('myroom.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 학생 수
    room_lst = [list(map(int, input().split())) for _ in range(N)] # N명의 학생에 대해, 현재 방과 돌아갈 방을 받음
    time = 1 # 기본 단위시간 => 하나도 겹치지 않는 경우는 1이 출력되도록!

    # 만약 현재 방 번호보다 돌아가야 할 방 번호가 큰 경우가 있을 수 있음
    # 계산의 편의를 위해 오름차순으로 모두 정리해줄 것 (현재 tc에는 없지만..)
    for r in range(len(room_lst)):
        for c in range(len(room_lst[0]) - 1):
            if room_lst[r][c] > room_lst[r][c+1]:
                room_lst[r][c], room_lst[r][c+1] = room_lst[r][c+1], room_lst[r][c]

    # [r][1]번째 값이 [r+1][0]번째 값보다 크다면 time += 1
    for r in range(len(room_lst) - 1):
        for c in range(len(room_lst[0]) - 1):
            if room_lst[r][c+1] > room_lst[r+1][c]:
                time += 1

    print(f'#{tc} {time}')


