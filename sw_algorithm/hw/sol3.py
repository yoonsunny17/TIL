import sys

sys.stdin = open('gravity.txt')

T = int(input())
for tc in range(1, T + 1):
    cnt = int(input()) # 상자 기둥 개수
    boxes = list(map(int, input().split())) # 각 기둥 상자 몇개씩인지 입력받기

    cnt_lst = [0] * cnt # 그냥 각 기둥의 낙차값 다 구해버리자
    for i in range(len(boxes)): #왼쪽에서 오른쪽 순서대로 높이 비교하면서 낙차 계산
        for j in range(i+1, len(boxes)):
            if boxes[i] > boxes[j]: # 오른쪽의 높이가 더 낮다면 낙차 +1
                cnt_lst[i] += 1

    # 모든 상자들에 대해 반복이 끝나면 최대값을 출력
    # max 내장함수 사용 금지..?
    rlt = 0
    for cnt in cnt_lst:
        if cnt > rlt:
            rlt = cnt

    print(f'#{tc} {rlt}')





