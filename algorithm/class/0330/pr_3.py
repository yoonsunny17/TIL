# case 1. 전위 순회 (preorder)
# root - left - right
def preorder(edge):
    if edge:
        rlt1.append(edge)
        preorder(graph[edge][0])
        preorder(graph[edge][1])


# case 2. 중위 순회 (inorder)
# left - root - right
def inorder(edge):
    if edge:
        inorder(graph[edge][0])
        rlt2.append(edge)
        inorder(graph[edge][1])


# case 3. 후위 순회 (postorder)
# left - right - root
def postorder(edge):
    if edge:
        postorder(graph[edge][0])
        postorder(graph[edge][1])
        rlt3.append(edge)


V, E = map(int, input().split())
nodes = list(map(int, input().split()))
graph = [[0 for _ in range(3)] for _ in range(V+1)]
for i in range(0, len(nodes)-1, 2):
    parent = nodes[i]
    child = nodes[i+1]

    # 부모의 왼쪽 자식 자리 비어있으면 자리 채워줘
    if graph[parent][0] == 0:
        graph[parent][0] = child

    # 아니면 오른쪽 자식으로 데려오자
    else:
        graph[parent][1] = child

    # 자식 노드의 부모가 누구인지 적어주세요
    graph[child][2] = parent

    start = 1
    rlt1, rlt2, rlt3 = [], [], []
    preorder(start)
    if len(rlt1) == V:
        print(' '.join(map(str, rlt1)))
    inorder(start)
    if len(rlt2) == V:
        print(' '.join(map(str, rlt2)))
    postorder(start)
    if len(rlt3) == V:
        print(' '.join(map(str, rlt3)))



"""
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""