import sys

sys.stdin = open('subtree.txt')

def postorder(node):
    global cnt

    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        cnt += 1
        return cnt


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))

    tree = [[0 for _ in range(3)] for _ in range(E+2)]

    # 2칸씩 건너뛰면서 입력받기!
    for i in range(0, len(nodes)-1, 2):
        parent_node = nodes[i]  # 부모 노드
        child_node = nodes[i+1]  # 자식 노드

        # 왼쪽 자식 자리가 비어있으면 자식 노드를 넣어줘
        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node

        # 비어있지 않다면 오른쪽에 자식 노드를 넣어줘
        else:
            tree[parent_node][1] = child_node

    # 부모 노드가 누구인지 적어주자
    for i in range(1, E+2):
        tree[i][2] = i

    # for i in range(E+2):
    #     print(tree[i])

    cnt = 0 # 최종 반환해줄 변수 초기화
    print(f'#{tc} {postorder(N)}')

