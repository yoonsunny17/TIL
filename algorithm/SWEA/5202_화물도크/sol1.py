from pprint import pprint
import sys

sys.stdin = open('dock.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    # 잡힌 시간표에서, 종료 시간이 늦은 순서대로 다시 정렬시켜주자
    time.sort(key=lambda x:x[1])
    # pprint(time)

    # 운행 가능한 애들을 stack에 넣어줄거야
    stack = []
    # 첫 스타트는 0시부터라고 생각해보자
    start = 0
    for i in range(N):
        # 작업 시간이 겹치지 않는 경우에만 가능해
        # 즉, A 작업의 종료시간이 다음 B 작업의 시작시간과 같거나 이전이어야 해
        if start <= time[i][0]:
            stack.append(time)
            start = time[i][1]  # 다음 작업 시작이 가능한 시간 = 지금 내가 끝낸 시간

    print(f'#{tc} {len(stack)}')

