''' success code  '''

N, K = map(int, input().split())  # 행렬의 크기 N, 세균의 개수 1 ~ K개
matrix = [list(map(int, input().split())) for _ in range(N)]
virus = []  # 바이러스 번호 낮은애들부터 퍼뜨릴거야
S, X, Y = map(int, input().split())  # S초 뒤 위치 (X, Y) 의 세균 종류

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            virus.append([matrix[i][j], i, j])  # virus num, row, col,

virus.sort()  # virus numb 순서대로 오름차순 정렬 필수!!!!

# delta 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 주어진 시간만큼 반복할거야
while S:
    # 그리고 바이러스 하나씩 반복해줄거지
    for _ in range(len(virus)):
        v, r, c = virus.pop(0)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            # 만약 탐색 지점이 범위 내에 있고, 아직 바이러스가 퍼지지 않은 곳이라면 퍼뜨리자
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc]:
                visited[rr][cc] = v
                virus.append([v, rr, cc])
    # 한 사이클 돌았으면 1초 차감해줘
    S -= 1

print(visited[X-1][Y-1])