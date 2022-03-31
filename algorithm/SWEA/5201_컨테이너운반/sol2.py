import sys

sys.stdin = open('container.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 최댓값 출력해야 하니까 내림차순으로 정렬해주고 시작해
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    # 최대 옮길 수 있는 상자 개수 = 트럭의 개수
    move = [0 for _ in range(M)]

    # 각 상자들 및 각 트럭들을 하나씩 매칭시켜볼거야
    for i in range(N):
        for j in range(M):
            # 만약 트럭이 옮길 수 있는 무게인 경우,
            if weight[i] <= truck[j]:
                # 그리고 아직 트럭에 자리가 있는 경우라면,
                if move[j] == 0:
                    # 트럭에 상자 넣어주고, 그 자리는 이미 찼으니까 break해줘
                    move[j] = weight[i]
                    break

    print(f'#{tc} {sum(move)}')

