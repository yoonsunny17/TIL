from itertools import combinations
from pprint import pprint
from collections import deque
'''
나보다 큰 물고기가 있으면 : 못먹고 못지나가
나랑 같은 크기 물고기라면 : 못먹고 지나갈수 있어
나보다 작은 크기 물고기라면 : 먹고 지나갈 수 있어

아기상어의 현재 크기만큼 물고기 마릿수 먹으면 상어 크기 + 1 증가
가장 가까운 물고기부터 섭취
여러마리라면, 윗쪽부터 섭취, 위에 여러마리인 경우 왼쪽부터 섭취
'''

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 아기상어 초기 위치 및 크기 변수 초기화
x, y = 0, 0
size = 2
# 실제로 몇마리 먹었는지 세어 줄 변수 초기화
eat = 0

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 물고기들 일단 다 세어주고 시작해보자
all_fish = []
for i in range(N):
    for j in range(N):
        if 0 < matrix[i][j] <= 6:
            all_fish.append([i, j])
        if matrix[i][j] == 9:
            x = i
            y = j
# 상어 출발 위치 0으로 초기화 해주자!
matrix[x][y] = 0