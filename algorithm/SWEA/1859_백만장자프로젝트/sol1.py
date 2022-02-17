'''
거꾸로 보자
뒤에서부터 max_v 찾고, cnt 에 max_v 에서 그 다음 value를 빼준 값 누적하다가,
max_v 더 큰 값 만나면 갱신하고, (cnt 는 그대로 냅둔다)
다시 반복.. idx = 0 이 될때까지
'''
import sys

sys.stdin = open('rich_project.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    idx = len(arr) # 역탐색 할거야
    max_v = 0 # 매매가 가장 큰 날 할당해줄 변수
    cnt = 0 # 매매가 누적해줄 변수

    for i in range(idx-1, -1, -1): # 맨 뒤에서부터 역탐색 시작
        if arr[i] >= max_v: # 최대 매매값 찾으면 max_v값 갱신해주자
            max_v = arr[i] 
        cnt += max_v - arr[i] # 평소에는 계속 판매 누적 반복

    print(f'#{tc} {cnt}')

