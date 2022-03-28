
def tree(r, c, N):
    # 쿼드트리 탐색 출발 지점 설정해주기
    start = matrix[r][c]

    for i in range(r, r+N):
        for j in range(c, c+N):
            if matrix[i][j] != start:  # 만약 start 지점과 같은 숫자가 아니면,
                stack.append('(')  # 일단 열린 괄호 추가해!
                tree(r, c, N//2)  # 좌상 탐색
                tree(r, c+N//2, N//2)  # 우상 탐색
                tree(r+N//2, c, N//2)  # 좌하 탐색
                tree(r+N//2, c+N//2, N//2)  # 우하 탐색
                stack.append(')')  # 탐색 끝나면 괄호 닫아줘
                return stack  # 탐색 끝난 stack 반환해줘

    # start에 해당하는 숫자를 stack에 넣어줘
    if start:
        stack.append(1)
    if start == 0:
        stack.append(0)

    return stack


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
stack = []
# pprint(matrix)
rlt = tree(0, 0, N)
print(''.join(map(str, rlt)))