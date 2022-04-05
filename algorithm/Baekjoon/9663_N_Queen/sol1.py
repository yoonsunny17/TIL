# dfs는 재귀, 재귀는 탈출 조건!!!

def promising(v):
    # 내가 있는 위치 - 1 까지만 확인해주면 돼
    for i in range(v):
        # 위에 내가 두고싶은 자리에서 세로로 위쪽으로 퀸이 놓여져 있거나,
        # or
        # 내 위치의 row, col 에서 그 위에 있는 퀸들의 row, col의 차를 구했을 때 그 차가 동일하면 둘 수 없겠다! (대각선 조건 두개 한번에 처리한거)
        if row[v] == row[i] or abs(row[v] - row[i]) == (v-i):
            return False  # 둘 수 없엉~

    return True


def dfs(v):
    global cnt

    # 탈출 조건: 마지막 row까지 모든 퀸을 배치한 경우
    if v == N:
        cnt += 1  # 이거 +1 안하고 끝내면 답이랑 1 차이 날껄?
        return

    # 지금 두는 퀸이 마지막 row 에 두는 것이 아니라면,
    else:
        for i in range(N):
            # v 번째 row 에 i column 에 퀸을 두겠어
            row[v] = i
            # 그리고 밑에 다음번 퀸을 두기 전에,
            # 퀸을 둘 수 없는 경우/있는 경우를 체크한 뒤 말을 둘거야
            if promising(v):  # 밑에 줄에 퀸을 어느 자리에 둘 수 있는지 체크해 줄 함수!
                dfs(v+1)


N = int(input())  # 체스판의 크기


cnt = 0  # 결과값 받을 변수
row = [0] * N  # visit을 체크해줄거임!!

dfs(0)
print(cnt)