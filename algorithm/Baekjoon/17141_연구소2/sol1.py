from itertools import combinations
from collections import deque
from pprint import pprint

N, M = map(int, input().split())  # N = 연구소의 크기, M = 바이러스 개수
matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 놓을 수 있는 곳
# pprint(matrix)

start = deque()
# 벽인 부분은 숫자가 아닌 다른 문자열로 변환해주자
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = -1
        if matrix[i][j] == 2:
            start.append([i, j])

print(start)



# pprint(matrix)

# matrix에서 2가 몇개인지 세어보자 = 바이러스가 시작할 수 있는 위치의 개수
# 그럼 그 개수에서 M개만큼 위치를 골라서 bfs 돌리고, 최단 시간 걸리는 것 출력하면 될 것 같음
# M개 고를 때 순서는 중요하지 않으므로 combination(조합)이다!