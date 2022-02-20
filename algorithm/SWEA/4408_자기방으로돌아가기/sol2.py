'''
success!!!

********important!!!*********
처음에 이런 식으로 풀었는데 tc 10개 중 7개 맞았다고 나옴
start = room[1] // 2 는 안되는걸까
end = room[0] // 2
==> [1, 5], [6, 10] 인 경우 고려해볼 것!!!!!
==> 5 < 6 이지만, 이것도 중복으로 간주하기 때문에 몫 구하기 전에 +1을 해주어야 한다
'''
import sys

sys.stdin = open('myroom.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 학생 수
    room_lst = [list(map(int, input().split())) for _ in range(N)]  #현재 방과 돌아갈 방에 대한 이차원 리스트
    time = [0] * 201 # idx = 1 ~ 200, 복도의 중복되는 수 만큼 time이 증가한다


    # 계산의 편의를 위해 오름차순 (출발방 번호 < 도착방 번호) 로 정리해줌
    # 방 번호는 400까지 있지만, 1 ~ 200의 구간에서 중복되는 구간이 있는지를 체크해주는 것과 동일!
    for room in room_lst:
        if room[0] > room[1]:
            start = (room[1] + 1) // 2 # start = room[1] // 2 는 안되는걸까 ==> [1, 5] , [6, 10] 인 경우 고려해볼 것~!!
            end = (room[0] + 1) // 2
        else:
            start = (room[0] + 1) // 2
            end = (room[1] + 1) // 2

        for i in range(start, end+1):
            time[i] += 1
            
    # time 에서 최댓값 도출
    rlt = time[0]
    for t in time:
        if t >= rlt:
            rlt = t

    print(f'#{tc} {rlt}')


