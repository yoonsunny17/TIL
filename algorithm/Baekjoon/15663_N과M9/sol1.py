'''
다시 풀 것 !!!
'''

# def dfs(i):
#
#     if len(stack) == M:
#         print(' '.join(map(str, stack)))
#     else:
#         not_same = 0  # 중복된 숫자 방지
#
#         for i in range(len(numbs)):
#             # 방문한 기록이 없으면서, 중복된 숫자가 아닌 경우
#             if not visited[numbs[i]] and numbs[i] != not_same:
#                 visited[numbs[i]] = 1  # 방문 기록을 남겨주고
#                 stack.append(numbs[i])  # stack에 넣어주고
#                 not_same = numbs[i]  # 중복 가능성 있는 숫자라고 표시해줘
#                 dfs(i+1)  # 그리고 재귀를 돌고,
#                 visited[numbs[i]] = 0  # 다시 방문 기록을 삭제해줘
#                 stack.pop()  # backtracking
#
#
# N, M = map(int, input().split())
# numbs = list(map(int, input().split()))
# numbs.sort()
# stack = []
# visited = [0]*1000  # 방문 기록 남길 리스트
# dfs(0)
