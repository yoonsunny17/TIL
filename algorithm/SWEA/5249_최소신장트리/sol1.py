import sys

sys.stdin = open('tree.txt')


def union(x, y):
    a = find(x)
    b = find(y)

    parent[max(a, b)] = min(a, b)


# 경로압축 포함한 find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

'''
# 경로압축 포함하지 않은 find 함수
def find(x):
    while x != parent[x]:
        x = parent[x]
    
    return x
'''

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parent = [x for x in range(V+1)]  # 자기 자신을 부모로 가지도록 초기화
    # [0,1,2,3,4,5,6,7,8,9 ...]
    # union(1,2)
    # [0,1,1,3,4,5,6,7,8,9 ...]
    # union(1,3)
    # [0,1,1,1,4,5,6,7,8,9 ...]
    # union(2,4) ***find 함수에 경로압축 들어가있어서 바로 부모가 1로 바뀜~~***
    # [0,1,1,1,1,5,6,7,8,9 ...]
    '''
    parent[1] = 1
    parent[2] = 2
    parent[3] = 3
    '''
    graph = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph.append([u, v, w])

    graph.sort(key=lambda x:x[2])
    ans = 0
    for start,end,cost in graph:
        if find(start) != find(end):
            union(start, end)
            ans += cost

    print(f'#{tc} {ans}')
