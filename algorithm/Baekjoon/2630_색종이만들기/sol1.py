from pprint import pprint


# 재귀함수 구현,, 구역이 나누어지지 않으면 N//2 해주자
def f(r, c, N):
    global white, blue
    color = matrix[r][c]  # 구역의 색이 무엇인지 받아 줄 변수 초기화
    for i in range(r, r+N):
        for j in range(c, c+N):
            if matrix[i][j] != color:  # 구역의 모든 색이 동일하지 않은 경우라면,
                # 재귀함수를 호출해 줄거야! 항상 한 구역은 네 구역으로 나뉘므로 함수도 4개 호출해줘
                f(r, c, N//2)
                f(r, c+N//2, N//2)
                f(r+N//2, c, N//2)
                f(r+N//2, c+N//2, N//2)
                return

    # 흰색인 경우,
    if color == 0:
        white += 1
    # 파란색인 경우,
    else:
        blue += 1


N = int(input())  # N = 2, 4, 8, 16, 32, 64, 128
matrix = [list(map(int, input().split())) for _ in range(N)]
# pprint(matrix)
white = blue = 0

f(0, 0, N)
print(white)
print(blue)
