> tree structure data 순회 방법 3가지

1. Indorder traversal
2. Preorder traversal
3. Postorder traversal



> 계산기

* 중위표기식 => 사람이 사용하는 일반 순서
* 후위표기식 => 우선순위에 따라 연산자 표현

*********

> 부분집합

```python
# 합이 10 인 경우 찾기
def f(i, N, s, t): # s 이전까지 고려된 원소의 합, t 목표값
    global cnt
    cnt += 1
    
    if s == t: # 너가 찾는 목표에 도달했니? YES!
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()

    elif i == N: # 더이상 고려할 원소가 없는데..?
        return # 앞으로 되돌아가봐
    
    elif s > t: # 고려의 원소의 합이 목표값을 초과한 경우에도
        return # 앞으로 되돌아가봐

    else:
        bit[i] = 1
        f(i+1, N, s+a[i], t)
        bit[i] = 0
        f(i+1, N, s, t)
    return

N = 10
a = [x for x in range(1, N+1)]
bit = [0]*N
t = 10 # t가 되는 경우가 있어??
cnt = 0
f(0, N, 0, t)
print(f'{cnt = }')
# t가 최댓값이면 어쩔수 없이 다 돌게 되니까 cnt값이 최대로 나오겠지

'''
남은 원소 rs를 고려하는 경우 ==> target 값이 큰 경우일 때에는 전체 탐색하는 경우보다  rs를 고려하는 경우
순환하는 횟수가 상당히 많이 줄어들지만, target값이 중간 정도의 값일 경우일 때에는 큰 차이가 없다
'''
```

