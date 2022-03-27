'''
얘는 왜 안되는걸까..??
'''

# rlt = 첫번재 숫자
def dfs(i, rlt, op):
    global max_rlt, min_rlt

    # 종료 조건 = 연산 반복을 N번으로 넘어가는 경우, 그만하고 결과값 갱신해주기
    if i == N:
        max_rlt = max(max_rlt, rlt)
        min_rlt = min(min_rlt, rlt)
        return

    # 사칙연산에 대해 동일한 과정을 반복할거야
    # 만약 주어진 연산자의 개수가 1 이상이면 (0보다 크다면 = 아직 다 안썼다면)
    # 일단 하나 썼다는 것 표시해주고 (-1)
    # rlt값 계산해주고 (연산자 우선순위 없으므로 그 다음 숫자와 계산 하면 돼!)
    # dfs 재귀 호출해서 다음 연산으로 넘어가자!!
    if op[0] > 0:  # 더하기 연산자인 경우
        op[0] -= 1
        rlt += numbs[i]
        dfs(i+1, rlt, op)
    if op[1] > 0:  # 빼기 연산자인 경우
        op[1] -= 1
        rlt -= numbs[i]
        dfs(i+1, rlt, op)
    if op[2] > 0:  # 곱하기 연산자인 경우
        op[2] -= 1
        rlt *= numbs[i]
        dfs(i+1, rlt, op)
    if op[3] > 0:  # 나누기 연산자인 경우 2가지 경우를 고려해야 해 !!
        op[3] -= 1
        if rlt < 0:
            rlt = -((-rlt) // numbs[i])
        else:
            rlt = rlt // numbs[i]
        dfs(i+1, rlt, op)


N = int(input())
numbs = list(map(int, input().split()))
op = list(map(int, input().split()))

# 최댓값, 최솟값 초기화 시켜주자!
# 재귀함수 돌면서 계속 갱신 시켜줄거야
max_rlt = -10**9
min_rlt = 10**9

dfs(1, numbs[0], op)
print(f'{max_rlt}\n{min_rlt}')
