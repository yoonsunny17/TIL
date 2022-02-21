import sys

sys.stdin = open('input_prob_1.txt')

T = int(input())
for tc in range(1, T + 1):

    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]  # N x N 2차원 리스트로 받기
    max_lst = []  # 각 행에서의 구간 합 받을 리스트

    for r in range(N):  # 열 고정, 행 우선탐색
        rlt = 0  # 각 행에서의 구간 합을 받을 변수 (매 행마다 초기화)
        if r + K <= N:  # indexError 를 넘지 않는 경우
            for c in range(r, r + K):
                rlt += lst[r][c]
                max_lst.append(rlt)
        else:  # r + K > N 이 되어 indexError 가 발생하는 경우 고려
            for c in range(r, N):
                rlt += lst[r][c]
                max_lst.append(rlt)

    # 최댓값 구하기: max_lst의 첫번째 원소를 임시의 최댓값으로 설정 후 진짜 최댓값 찾기
    max_rlt = max_lst[0]
    for i in range(len(max_lst)):
        if max_lst[i] >= max_rlt:
            max_rlt = max_lst[i]

    print(f'#{tc} {max_rlt}')
