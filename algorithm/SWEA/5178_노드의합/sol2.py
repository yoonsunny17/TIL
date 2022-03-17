import sys
from pprint import pprint

sys.stdin = open('node_sum.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    
    # 각 노드의 값들을 받을 tree를 만들어줘
    tree = [0 for _ in range(N+1)]

    # 각 리프노드에 해당하는 값을 넣어주자
    for _ in range(M):
        leaf, numb = map(int, input().split())
        tree[leaf] = numb

    # 리프 노드부터 거꾸로 올라갈거야
    for j in range(N, 0, -1):
        # 거꾸로 올라가는 거니까 노드값은 절반으로 줄어들겠지
        if j//2 > 0:
            # idx가 0, 1일 때를 제외하고 값이 더해질거야
            tree[j//2] += tree[j]

    rlt = tree[L]
    print(f'#{tc} {rlt}')
