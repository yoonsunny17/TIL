'''
에라토스테네스의 채

입력보다 작은 소수 리스트를 만들고,
구간합을 구하면 돼

'''

N = int(input())
numbs = [True] * (N+1)
arr = []

for i in range(2, N+1):
    for j in range(i, N+1, i):
        # 아직 True == 지워지지 않음 => 지워주고, 리스트에 담아주기
        if numbs[j]:
            arr.append(j)
            numbs[j] = False

print(arr)


# N = int(input())
# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# matrix.sort(key=lambda x:(x[1], x[0]))
#
# for lst in matrix:
#     print(f'{lst[0]} {lst[1]}')
