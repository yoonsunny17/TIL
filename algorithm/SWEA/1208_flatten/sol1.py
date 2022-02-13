import sys

sys.stdin = open('flatten.txt')

T = 10
for tc in range(1, T + 1):
    dump = int(input()) # dump 횟수
    boxes = list(map(int, input().split())) # 각 상자의 높이값

    # dump 횟수만큼 while 문 돌리기
    while dump != 0:

        # 가장 높은 박스와 가장 낮은 박스 찾기
        max_box = min_box = boxes[0]
        max_idx = min_idx = 0
        for i in range(len(boxes)):
            if boxes[i] >= max_box:
                max_box = boxes[i]
                max_idx = i

            if boxes[i] <= min_box:
                min_box = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # dump 1회 진행 후 dump 횟수 차감
        dump -= 1

    # 다 하고 나면 평탄화 완료된 boxes 리스트 구한거니까 여기서 최고점 최저점 차이값 구하면 됨
    max_box = min_box = boxes[0]
    for i in range(len(boxes)):
        if boxes[i] >= max_box:
            max_box = boxes[i]

        if boxes[i] <= min_box:
            min_box = boxes[i]

    # 최고점에서 최저점 빼주기
    rlt = max_box - min_box

    print(f'#{tc} {rlt}')
