# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

arr = [[1,2,3], [4,5,6], [7,8,9]]
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]: # 우 하 좌 상 순서
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N: #유효 인덱스
                print(i, j, arr[ni][nj])

        print()