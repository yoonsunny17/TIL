# powerset (재귀호출(DFS)을 통한 완전탐색!!)
def powerset(idx, arr):
    global cnt
    cnt += 1

    # 만약에 이번에 들어왔는데, 부분집합의 합이 10이야 => RETURN
    each_sum = 0
    for each in zip(bit, lst): # bit value가 1인 lst 원소들만 더해주기~
        each_sum += each[0] * each[1]

    if each_sum == 10:
        for each in zip(bit, lst):
            if each[0]:
                print(f'{each[1]}', end=' ')
        print()
        return

    if idx == N:
        # print(bit)
        return

    bit[idx] = 0
    powerset(idx = idx + 1, arr=arr)

    bit[idx] = 1
    powerset(idx = idx + 1, arr=arr)



lst = [x for x in range(1, 11)]
N = len(lst)
bit = [0] * N

cnt = 0 # global에 할당된 값을 변경, 즉 재할당 해줄거야! 그럼 함수 내에 global임을 알려주자

powerset(idx=0, arr=lst)
print(f'count {cnt}') #=> cnt = 2047