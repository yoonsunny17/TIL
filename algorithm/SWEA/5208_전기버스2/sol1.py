import sys
sys.stdin = open('electric_bus.txt')


def charge(start, cnt):
    global min_rlt
    
    # 만약 현재 cnt 값이 min 보다 크거나 같으면 더이상 할 필요 없어! 반환해줘
    if cnt >= min_rlt:
        return
    
    # 도착 지점에 충분히 도착할 만큼 충전했다면,
    if start >= N:
        # 최솟값 갱신해주고 반환해줘
        if cnt < min_rlt:
            min_rlt = cnt
            return
    
    # 배터리 양 만큼 갈 수 있는 경우의 수 생각하고, 각 지점마다 충전 가능한 경우 보자
    for i in range(1, arr[start]+1):
        charge(start+i, cnt+1)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]  # 마지막 버스 정류장 번호 = 맨 처음에 받은 수
    min_rlt = 987654321  # 최솟값 초기화 시켜주자

    charge(1, 0)  # start idx = 1, cnt = 0

    print(f'#{tc} {min_rlt-1}')

