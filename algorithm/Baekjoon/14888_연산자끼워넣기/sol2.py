# i = 연산자 몇번 썼는지 확인해주는 변수
# rlt = dfs 한번 할때마다 갱신되는 결과값
# add, sub, mul, div = 사칙연산 개수
def dfs(i, rlt, add, sub, mul, div):
    global max_rlt, min_rlt  # 전역변수로 최댓값, 최솟값 불러와줘

    # 종료 조건 = 연산 반복을 N-1 번 끝낸 경우, 그만 하고 결과값 갱신하고 반환해줘
    if i == N:
        max_rlt = max(max_rlt, rlt)
        min_rlt = min(min_rlt, rlt)
        return

    # 사칙연산에 대해 동일한 과정을 반복할거야
    # 만약 주어진 연산자의 개수가 1 이상이면 (0보다 크다면 = 아직 다 안썼다면)
    # 일단 하나 썼다는 것 표시해주고 (-1)
    # rlt 값 계산해주고 (연산자 우선순위 없으므로 그 다음 숫자와 계산 하면 돼!)
    # dfs 재귀 호출해서 다음 연산으로 넘어가자!!
    if add > 0:  # 더하기 연산자인 경우
        dfs(i+1, rlt+numbs[i], add-1, sub, mul, div)
    if sub > 0:  # 빼기 연산자인 경우
        dfs(i+1, rlt-numbs[i], add, sub-1, mul, div)
    if mul > 0:  # 곱하기 연산자인 경우
        dfs(i+1, rlt*numbs[i], add, sub, mul-1, div)
    if div > 0:  # 나누기 연산자인 경우 2가지 경우를 고려해야 해 !!
        dfs(i+1, -((-rlt)//numbs[i]) if rlt < 0 else (rlt//numbs[i]), add, sub, mul, div-1)


N = int(input())
numbs = list(map(int, input().split()))
op = list(map(int, input().split()))

# 최댓값, 최솟값 초기화 시켜주기
max_rlt = -10**9
min_rlt = 10**9

dfs(1, numbs[0], op[0], op[1], op[2], op[3])
print(f'{max_rlt}\n{min_rlt}')