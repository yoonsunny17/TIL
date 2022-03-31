from pprint import pprint

def f(r, c, N):
    global plus, minus, zero

    # 탐색 시작하는 숫자가 무엇인지 받아주자
    numb = matrix[r][c]

    # 그리고 다른 숫자들이 동일한지 아닌지 확인해줘
    for i in range(r, r+N):
        for j in range(c, c+N):
            # 만약 숫자가 다르다면 무한반복 시작... ! ! !
            if matrix[i][j] != numb:
                f(r, c, N//3)
                f(r, c+N//3, N//3)
                f(r, c+(N//3)*2, N//3)
                f(r+N//3, c, N//3)
                f(r+N//3, c+N//3, N//3)
                f(r+N//3, c+(N//3)*2, N//3)
                f(r+(N//3)*2, c, N//3)
                f(r+(N//3)*2, c+N//3, N//3)
                f(r+(N//3)*2, c+(N//3)*2, N//3)
                return

    # 개수 세어줄거야
    if numb == 1:
        plus += 1
    elif numb == -1:
        minus += 1
    else:
        zero += 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 종이의 개수 몇개인지 세어 줄 변수 초기화
plus = minus = zero = 0
# pprint(matrix)
f(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')