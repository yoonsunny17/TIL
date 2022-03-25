# itertools 사용하여 순열과 조합 구하기

> itertools 사용하는 방법

1. `from itertools import permutations, combinations` 로 처음부터 지정해주어도 좋고,

2. `from itertools` 로만 지정 후 아래 코딩에서 순열, 조합을 import 해주어도 된다



> example

* **A, B, C, D 라는 네 개의 문자가 주어졌을 때, 무작위 두 개를 뽑았을 때의 순열과 조합을 구해라**

```python
from itertools import combinations, permutations

chars = ['A', 'B', 'C', 'D']

per = list(permutations(chars, 2))
com = list(combinations(chars, 2))

print('=====permutations=====')
for p in per:
    print(p)

print('=====combinations=====')
for c in com:
    print(c)
```

* result (각각 튜플 형식으로 출력됨!)

```python
=====permutations=====
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
=====combinations=====
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
```

