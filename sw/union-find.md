# union-find algorithm

> 수학에서의 서로소 집합

* **공통 원소가 없는 두 집합**
  * {1, 2}, {3, 4} => 서로소 관계이다

> 서로소 집합 자료구조

* 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
* 연산 : `union + find`
* `union` : 2개 원소로 이루어진 집합을 **하나의 집합**으로 합치기
* `find` : **특정 원소가 속한 집합이 뭔지** 알려주는 연산
* 서로소 집합 자료구조는 **union + find 연산으로 구성**되므로 **union-find 자료구조**라고 불리기도 함



## 서로소 집합 계산 알고리즘

> 동작 방법

1. union 연산 확인
   * 서로 연결된 두 노드를 확인한다
     * A의 루트 노드 A'와 B의 루트 노드 B'를 찾는다 (find)
     * A'를 B'의 부모 노드로 설정한다 (A' < B' 라고 가정)
2. 모든 union 연산을 처리할 때까지 1번을 반복 수행



> 문제점 : 비효율적인 find 함수

* 노드의 개수 V개, union 과 find 연산의 개수 M개라고 한다면, 최악의 경우 **O(VM)**의 시간이 소요된다
  * **경로 압축**을 이용하여 최적화를 할 수 있다

> 개선된 서로소 집합 알고리즘

* find 함수의 경로 압축 : return값을 `parent[x]`로 수정해주기

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
```

* 노드의 개수 V개, 최대 V-1개의 union 연산과 M개의 find 연산을 수행할 때 시간복잡도

![image-20220413105409219](union-find.assets/image-20220413105409219.png)

> 사이클 판별법

* union-find 알고리즘을 이용해서 **무방향 그래프 내에서 사이클을 판별**할 수 있다
  1. 각 간선을 확인하면서 두 노드의 루트노드를 확인한다
     * 루트 노드가 서로 **다르면** union 연산 수행
     * 루트 노드가 서로 **같으면** cycle 발생
  2. 모든 간선에 대해 1번 반복

```python
cycle = False  # 기본 default값은 False로 (사이클이 발생하지 않았다고 가정 후 시작)
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 연산 수행
    else:
        union_parent(parent, a, b)
```

