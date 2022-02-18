import sys

sys.stdin = open('myroom.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 돌아가야 할 학생 수
    room = [list(map(int, input().split())) for _ in range(N)]
    time = 1 # 기본 단위시간
    
    for r in range(N-1):
        if room[r][1] > room[r+1][0] or room[r][0] > room[r+1][1]:
            time += 1
            continue

        else:
            break

    print(f'#{tc} {time}')

