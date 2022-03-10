# DFS 와 BFS

* 그래프의 탐색 방법
* 목적 : 한 정점에서 시작하여 연결되어 있는 모든 정점을 1번씩 방문하는 것



> **DFS** 깊이 우선 탐색

```python
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
print(a) # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
```



> **BFS** 너비 우선 탐색

```python
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
print(b) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
```



**다 똑같은데, while문에서 DFS는 `node = stack.pop()`를, BFS는 `node = stack.popleft()`를 사용한다**

즉, DFS는 stack을 사용하고, BFS는 queue를 사용한다!!!!