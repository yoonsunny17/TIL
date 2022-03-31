import sys

sys.stdin = open('work.txt')


def worker(j, success):
    global max_rlt

    # 만약 확률이 최댓값보다 작거나 같으면 계산 하지 말자
    if success <= max_rlt:
        return

    # 모든 사람들에 대한 일 분배가 끝났으면 최댓값 갱신해줘
    if j == N:
        if success > max_rlt:
            max_rlt = success
            return

    # 아직 일 분배 받지 못한 직원들한테 일 분배 시키고, 각자 해낼 확률을 누적해서 곱해주자
    for i in range(N):
        if not check[i]:
            check[i] = 1
            worker(j+1, success*matrix[i][j]*0.01)  # 곱해줄 때마다 확률로 바꿔서 곱해주자
            check[i] = 0

    ## 이것도 가능.
    # if success > max_rlt:
    #     if j == N:
    #         max_rlt = success
    #         return
    #
    # for i in range(N):
    #     if not check[i]:
    #         check[i] = 1
    #         worker(j+1, success*matrix[i][j]*0.01)
    #         check[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N  # 직원들이 어떤 일을 맡았는지 기록할 리스트!
    max_rlt = 0  # 최댓값 갱신해줄 변수 초기화 해주기

    worker(0, 1)  # col idx = 0, success = 1 초기화! (success는 곱해야하니까)
    max_rlt *= 100  # 마지막에 확률을 퍼센트로 변경해줘야해

    print(f'#{tc} {max_rlt:.6f}')

