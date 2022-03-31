import sys

sys.stdin = open('cart.txt')

def f(i, cnt):
    global min_rlt  # 전역변수 가져오구

    # cnt 값이 더 작은 경우에만 고려해주는게 효율적이지!
    if cnt < min_rlt:
        # 근데 만약에 cart 자리가 꽉 찼다면, 최솟값 갱신해주고 반환해줘
        if len(cart) == N-1:
            min_rlt = min(min_rlt, cnt + matrix[i][0])
            return

    # 위의 경우가 아니라면, 다음 j값을 찾아 떠날래
    for j in range(1, N):
        # 만약 j가 stack 안에 없고, 행렬의 값이 0이 아니라면,
        if j not in cart and matrix[i][j] != 0:
            cart.append(j)  # stack에 j값 넣어주고
            f(j, cnt + matrix[i][j])  # i에 j를 넣고, cnt 값을 갱신해준다음에 재귀 돌려줘
            cart.pop()  # 그리고 return 문 걸렸다가 돌아오면 cart에서 숫자 빼줘


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 최솟값 받아줄 변수 초기화
    min_rlt = 987654321

    # 1부터 N-1까지의 값에 대해서 차례대로 재귀를 진행해볼게
    for i in range(1, N):
        cart = []  # 우선 i 값이 바뀔 때마다 stack은 초기화 시켜줘야해
        cart.append(i)  # 그리고 stack에 i값을 넣어줘
        f(i, matrix[0][i])  # 그담에 재귀함수 돌려돌려

    print(f'#{tc} {min_rlt}')

