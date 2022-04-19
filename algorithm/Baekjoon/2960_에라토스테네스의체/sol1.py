N, K = map(int, input().split())
numbs = [True] * (N+1)
rlt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        # True = 아직 지워지지 않았다는 뜻이니까, 소수의 배수에 해당된다면 지워주기
        if numbs[j]:
            numbs[j] = False
            rlt += 1
            # K번째 지워지는 수 찾으면 출력하고 끝내줘
            if rlt == K:
                print(j)
                break