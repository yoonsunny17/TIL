import sys

sys.stdin = open('sample_input.txt')

def game(pages, target): # pages = 전체 쪽 수 // target = 원하는 페이지 수
    left = 1 # 왼쪽 페이지 초기화
    right = pages # 오른쪽 페이지 초기화
    cnt = 0 # 이진탐색 횟수 누적해 줄 변수

    while True:
        avg = int((left + right) / 2) # 중간 페이지 탐색

        if avg == target: # 원하는 페이지가 나온다면 cnt 반환
            return cnt

        if avg < target: # 원하는 페이지가 더 큰 경우
            left = avg
            cnt += 1

        elif avg > target: # 원하는 페이지가 더 작은 경우
            right = avg
            cnt += 1

T = int(input())
for tc in range(1, T + 1):
    pages, A, B = map(int, input().split())

    # A, B에 대해 각각의 cnt 반환
    cnt_A = game(pages, A)
    cnt_B = game(pages, B)

    # 더 적은 횟수로 찾은 사람이 이김ㄲ
    if cnt_A > cnt_B:
        winner = 'B'
    elif cnt_A < cnt_B:
        winner = 'A'
    else:
        winner = 0

    print(f'#{tc} {winner}')