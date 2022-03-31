import sys
sys.stdin = open('min_cost.txt')


def factory(col, cnt):
    global min_cost

    # 만약 현재 값이 최솟값보다 크면 해줄 필요 없어! 그냥 종료시켜
    if cnt > min_cost:
        return

    # 만약 제품별 공장을 다 선택했다면, cnt 값과 min 값을 비교해보고, 갱신해줘
    if col == N:
        if cnt < min_cost:
            min_cost = cnt
            return

    # 각 제품에 대해서, 아직 공장을 정하지 않았다면,
    for row in range(N):
        if not visited[row]:
            visited[row] = 1  # 공장 정했다는 방문 기록 남겨주고,
            factory(col + 1, cnt + matrix[row][col])  # col + 1, cnt 갱신 후 다시 반복해줘
            visited[row] = 0  # 그리고 그 방문기록은 지워줘 (백트래킹)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N  # 각 제품별 공장 골랐는지 체크해줄 리스트! (row 만 체크)
    min_cost = 987654312  # 최솟값 초기화 시켜주어어어

    factory(0, 0)
    print(f'#{tc} {min_cost}')

