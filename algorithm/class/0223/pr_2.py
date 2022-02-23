# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 의 powerset 중 원소의 합이 10인 부분집합 구하기

def f(i, N, s, t): # s => 이전까지 고려된 원소의 합, t => 목표값
    # 내가 원하는 목표값을 찾았어! (s == t)
    if s == t:
        my_subset = set()
        for j in range(N):
            if bit[j]: # target 값 만족하는 부분집합 찾아야 하니까, bit에 1이 들어있다면,
                my_subset.add(my_set[j]) # 부분집합 만들어서 요소 넣어주고,
        print(my_subset) # 출력해주자!

    # 아무리 찾아봐도 target number와 일치하는게 없어
    # 즉, 마지막까지 비교한 idx가 집합 길이 N과 동일한 경우..
    elif i == N:
        return # 앞으로 다시 가서 확인해봐

    # 더하고 비교해봤는데 목표값보다 커! (s > t)
    elif s > t:
        return # 그럼 다시 앞으로 돌아가서 확인해봐

    # 아직 목표값에 도달하지 못했어! (s < t)
    else:
        # 우선 i번째를 1로 만들고 다음번 idx에서 반복하자 (재귀)
        bit[i] = 1
        f(i+1, N, s + my_set[i], t)

        # 다했으면 0 넣고 위처럼 똑같이 반복해줘
        bit[i] = 0
        f(i+1, N, s, t)
    return

N = 10
my_set = [x for x in range(1, N+1)]
bit = [0] * N # 각 원소들이 부분집합에 포함되어있는지를 0 or 1 로 표현해줄 거야
t = 10 # target number = 10
f(0, N, 0, t)