import sys

sys.stdin = open('group.txt')


# 짝을 찾아보자!
def find_pair(x):
    if x == arr[x]:
        return x

    else:
        return find_pair(arr[x])


# 짝지어주는 함수를 구현하자
def pair(x, y):
    arr[find_pair(y)] = find_pair(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nodes = list(map(int, input().split()))
    
    # 인덱스가 노드의 번호와 동일하도록 N+1 개의 칸을 가진 리스트를 만들어줘
    arr = [x for x in range(N+1)]  # idx numb = node numb

    # 두명씩 짝 지어주기!
    for i in range(0, len(nodes), 2):
        pair(nodes[i], nodes[i+1])
    
    # 중복되는 것 다 없애야 하니까 set type으로 만들자
    rlt = set()

    for i in range(1, N+1):
        rlt.add(find_pair(i))

    # print(rlt)
    print(f'#{tc} {len(rlt)}')

