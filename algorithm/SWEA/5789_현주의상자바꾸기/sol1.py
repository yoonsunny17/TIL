import sys

sys.stdin = open('changing_box.txt')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    boxes = [0] * (N+1) # i 값 만큼 더해줄 리스트. 앞에 idx= 0을 만들어 주어서 idx numb = box numb 되도록 설정
    for i in range(1, Q+1): # 1부터 Q까지
        L, R = map(int, input().split()) # 우선 L, R 값을 받아줘
        for j in range(L, R+1): # L ~ R 범위동안 Q의 i값을 boxes값에 넣어줘
            boxes[j] = i

    rlt = ' '.join(map(str, boxes[1:N+1]))
    print(f'#{tc} {rlt}')


