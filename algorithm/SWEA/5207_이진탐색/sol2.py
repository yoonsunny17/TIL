import sys

sys.stdin = open('binary_search.txt')


def binary(left, right, target, d):
    global cnt

    # case 1. left가 right 보다 커지는 경우 종료!
    if left > right:
        return

    # mid 값 설정해줘 (case 1에서 걸리지 않는 경우에만 해주는걸로~!)
    mid = (left+right) // 2

    # case 2. target 값이 mid idx 값보다 작거나 같은 경우,
    if target <= n_lst[mid]:
        # 만약 내가 찾는 값이라면, cnt 해주고 리턴해줘
        if target == n_lst[mid]:
            cnt += 1
            return
        # 그게 아니라면, right idx를 mid 왼편으로 이동하고, 좀전에 왼쪽을 탐색한 것이 아니라면 왼쪽을 탐색해
        elif target < n_lst[mid] and d != -1:
            right = mid - 1
            d = -1
            binary(left, right, target, d)

    # case 3. target 값이 mid idx 값보다 큰 경우,
    if target > n_lst[mid] and d != 1:
        # left idx를 mid 오른편으로 이동하고, 좀전에 오른쪽을 탐색한 것이 아니라면 오른쪽을 탐색해
        left = mid + 1
        d = 1
        binary(left, right, target, d)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    n_lst.sort()  # 정렬 시켜주기
    m_lst = list(map(int, input().split()))
    cnt = 0  # 결과 도출할 변수 초기화
    d = 0  # 왼쪽, 오른쪽 번갈아 가면서 탐색하는지 확인해 줄 변수! 왼쪽 = -1, 오른쪽 = +1

    for b in m_lst:
        binary(0, N-1, b, 0)
    
    print(f'#{tc} {cnt}')

