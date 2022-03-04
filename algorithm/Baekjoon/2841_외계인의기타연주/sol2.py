N, P = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
pressed = [[] for _ in range(7)] # 프렛 숫자 저장해 줄 빈 리스트 index 0 ~ 6 잡고 0 버리자
cnt = 0

