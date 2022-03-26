'''dfs + backtracking 으로 풀어보기'''

### 중복된거 다나오는 경우 ###
# def dfs(i, N, M):
#     if i == M:
#         print(stack)
#     else:
#         for j in range(1, N+1):
#             stack.append(j)
#             dfs(i+1, N, M)
#             stack.pop()


def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start, N+1):
            if i not in stack:
                stack.append(i)
                dfs(i+1)  # 새로운 start 지점 = 방금 넣어준 것보다 큰 숫자!
                stack.pop()


N, M = map(int, input().split())
stack = []  # 수열 깊이우선탐색 받아줄 stack
dfs(1)