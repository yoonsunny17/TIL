import sys

sys.stdin = open('heap.txt')

# 힙 삽입 함수를 정의해주자
def min_heap(number):
    global last
    last += 1
    tree[last] = number
    child = last
    parent = child // 2  # 부모 노드는 자식 노드의 절반

    # 부모 노드값이 1 이상이고, 자식노드보다 값이 더 큰 경우에는, 서로 자리를 교환해줘
    while parent >= 1 and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    tree = [0 for _ in range(N+1)]
    last = 0  # 트리의 가장 마지막 노드가 될 전역변수

    # 입력받은 숫자들을 최소힙 만족시키도록 넣어줘
    for numb in numbers:
        min_heap(numb)

    rlt = []  # 조상 노드 값들을 받을 리스트
    grand = last//2  # 가장 마지막 index의 절반부터 시작해

    # 조상 노드가 존재할 때까지 반복해줘
    while grand:
        rlt.append(tree[grand])
        grand = grand//2

    print(f'#{tc} {sum(rlt)}')


