import sys

sys.stdin = open('binary_search.txt')

# 중위순회를 사용하자 left => root => right
def inorder(node):
    global cnt
    # 최대 idx 범위 내에서 순회할거야
    if node <= N:
        inorder(node*2)  # 왼쪽 자식이라면 인덱스 두배 되겠지
        tree[node] = cnt  # 더이상 자식이 없다면 tree에 값을 저장해줘
        cnt += 1  # 그리고 값을 증가시켜줘
        inorder(node*2 + 1)  # 오른쪽 자식이라면 왼쪽 자식보다 + 1 해줘

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree= [0 for _ in range(N+1)]
    cnt = 1  # 1부터 N까지 순차적으로 tree에 넣을거니까 1로 초기화
    inorder(1)  # node가 1일 때부터 시작해줘

    print(f'#{tc} {tree[1]} {tree[N//2]}')

