import sys

sys.stdin = open('inorder.txt')

# 중위순회 함수 정의해주기
def inorder(node):
    if node <= N:  # 노드가 N 보다 작다면,
        inorder(node * 2)  # 왼쪽 자식 먼저 방문해서
        print(tree[node], end='')  # 처리해주고,
        inorder(node * 2 + 1)  # 오른쪽 자식 방문해서 처리해줘 (반복)


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)  # 트리구조 만들거야 idx값 보기 쉽게하려고 N+1 개 만듦

    for i in range(N):
        codes = list(input().split())
        idx = int(codes[0])  # codes[0] = tree의 idx
        tree[idx] = codes[1]  # 각 node 안에 알파벳을 넣어주자

    print(f'#{tc}', end=' ')
    inorder(node=1) # root는 항상 1
    print()



