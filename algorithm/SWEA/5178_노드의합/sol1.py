import sys
from pprint import pprint

sys.stdin = open('node_sum.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    # parent, left, right, node value 순으로 저장
    tree = [[0 for _ in range(4)] for _ in range(N+1)]

    # 각 리프노드에 저장된 값을 받아줘
    for _ in range(M):
        data = list(map(int, input().split()))
        tree[data[0]][3] = data[1]
    # 우선 리프 노드에 idx(현재 노드 = 부모 노드) 표시를 해주자
    for i in range(1, len(tree)):
        tree[i][0] = i
        parent_node = tree[i][0]
        if tree[i][3] == 0:
            tree[i][1] = parent_node*2
            tree[i][2] = parent_node*2 + 1
    for i in range(M, 0, -1):
        if tree[i][3] == 0:
            tree[i][3] = tree[tree[i][1]][3] + tree[tree[i][2]][3]

    pprint(tree)
