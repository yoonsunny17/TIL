from collections import deque

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

'''
dfs (깊이 우선 탐색) : 리스트의 가장 끝에 잇는 데이터를 기준으로 추출
'''
def dfs(graph, start_node):
    visited = [] # 방문 기록 남겨줄 곳
    stack = deque([start_node]) # 1. stack 만들고 시작 노드 설정해주기

    # 2. 방문하지 않은 곳이 아직 존재한다면, (stack이 아직 비어있지 않음 = 아직 dfs 끝내지 않음)
    while stack:
        # 3-1. 시작 노드를 지정해줘
        node = stack.pop()

        # 3-2. 만약 방문기록에 아직 없는 곳이라면,
        if node not in visited:
            # 방문 기록을 남겨주고,
            visited.append(node)
            # 인접 노드들을 stack에 추가해주자
            stack.extend(graph[node])

    return visited


a = dfs(graph, 'A')
print(a)

#############

'''
bfs (너비 우선 탐색) : 리스트의 가장 처음에 있는 인자를 받음
'''
def bfs(graph, start_node):
    visited = []
    stack = deque([start_node])

    while stack:
        node = stack.popleft()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

b = bfs(graph, 'A')
print(b)