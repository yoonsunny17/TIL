from collections import deque

N, K = map(int, input().split())
max_numb = 100000
time = [0] * (max_numb+1)  # 방문기록 및 시간 기록할 리스트 (0 ~ 100000)


# def bfs():
q = deque()
q.append(N)  # 언니의 위치를 넣어줘

while q:
    x = q.popleft()  # q에서 언니가 움직일 위치 하나를 꺼내와
    lst = [x+1, x-1, x*2]  # 언니가 걷거나 순간이동 가능하니까
    if x == K:  # 언니가 동생이랑 만나게 된다면,
        print(time[x])
        break
    # 가능한 세 경우 모두 고려해보자
    for dx in lst:
        # 그 위치가 범위 내에 있고, 아직 방문한 적이 없으면,
        if 0 <= dx <= max_numb and not time[dx]:
            time[dx] = time[x] + 1  # 시간 누적해줘
            q.append(dx)  # 그리고 그 위치를 q에 추가해줘

'''
처음에는 if x == K 랑 for dx in lst랑 위치 반대로 했었는데
89%에서 틀림
왜그런걸까?????
'''

