'''
DFS, 가지치기
'''
import sys
from pprint import pprint

sys.stdin = open('min_sum.txt')

def dfs(idx, rlt):
    global min_rlt
    # 종료조건
    if idx == N: # 모든 row를 다 돌고, 최솟값 찾았으면 반환해줘
        if rlt < min_rlt:
            min_rlt = rlt
        return

    # pruning
    if rlt >= min_rlt: # rlt가 min_rlt보다 크면 중단! 더 볼 필요 없어
        return

    # 각 행에 대해서 순차적으로 돌건데,
    for r in range(N):
        if not visited[r]: # 내가 방문하지 않은 행이라면
            visited[r] = 1 # 방문 기록을 남겨줘
            dfs(idx + 1, rlt + matrix[idx][r]) # 그리고 idx 증가시킴과 동시에 rlt 값을 갱신해줘
            visited[r] = 0 # 재귀함수 호출했으니까 방문기록 초기화 해줘야해



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)] # 방문기록 남길 리스트
    min_rlt = 987654321 # 충분히 큰 값을 넣어주자

    dfs(0, 0) # idx = 0, rlt = 0
    print(f'#{tc} {min_rlt}')
