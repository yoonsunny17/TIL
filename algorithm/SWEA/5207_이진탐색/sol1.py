'''fail'''
import sys
sys.stdin = open('binary_search.txt')


def binary(left, right, target):
    global cnt
    
    mid = (left+right)//2

    # case 1. left가 right를 넘어가면 끝!
    if left > right:
        return

    # case 2. target 값을 n_lst에서 찾은 경우 return
    if n_lst[mid] == target or n_lst[left] == target or n_lst[right] == target:
        cnt += 1  # 찾았으니 1 누적해주고 반환해줘
        return

    # case 3. target 값이 n_lst의 왼쪽에 있는 경우,
    if n_lst[left] < target < n_lst[mid]:
        n_visited[target] = 1  # 방문 처리 해주고
        right = mid - 1  # mid의 왼쪽 구간을 탐색해줘
        binary(left, right, target)

    # case 4. target 값이 n_lst의 오른쪽에 있는 경우,
    if n_lst[mid] < target < n_lst[right]:
        n_visited[target] = 1  # 방문 처리 해주고
        left = mid + 1  # mid의 오른쪽 구간을 탐색해줘
        binary(left, right, target)

    # case 5. 모두 방문했는데 못찾은 경우 return
    else:
        return
    

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    n_lst.sort()  # 정렬 시켜주기
    m_lst = list(map(int, input().split()))
    cnt = 0  # 결과 도출할 변수 초기화
    n_visited = [0] * M  # n_lst의 숫자들을 모두 탐색해봤는지 확인해주기 위한 방문 리스트 만들기

    for b in m_lst:
        binary(0, N-1, b)

    print(f'#{tc} {cnt}')

