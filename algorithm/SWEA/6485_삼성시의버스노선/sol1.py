import sys

sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 버스 노선 개수
    cnt = [0] * 5001 # 각 버스 정류장에 지나다니는 버스 몇개인지 세어줄 리스트 (1~5000 해주기 위해 맨 앞에 idx = 0 포함)
    bus_stop = [] # 각 정류장에 몇 개의 버스 노선 다니는지 받을 최종 리스트
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1): # A 이상, B 이하의 정류장을 지나다니므로
            cnt[i] += 1 # 해당 정류장에 버스 개수 누적해주기
    P = int(input()) # 버스 정류장 개수
    for _ in range(P):
        C = int(input()) # 버스 정류장 번호 = cnt lst의 idx 번호
        bus_stop.append(cnt[C])

    rlt = ' '.join(map(str, bus_stop))

    print(f'#{tc} {rlt}')

