import sys
from pprint import pprint

sys.stdin = open('arithmetic.txt')


T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = [0] + [list(input().split()) for _ in range(N)]
    # 아래에서 위로 보면서 연산자를 만나면 계산하자!
    for i in range(len(data)-1, 0, -1):
        # 만약 연산자가 주어졌다면 4개의 data가 주어졌겠지
        if len(data[i]) == 4:
            # 사칙연산 4가지 경우에 대해 각각 계산해줘
            # 계산한 다음에 연산자가 있던 자리에 저장해줘! (피연산자만 있던 노드들과 동일하게 맞춰야하니까)
            if data[i][1] == '-':
                data[i][1] = int(data[int(data[i][2])][1]) - int(data[int(data[i][3])][1])
            elif data[i][1] == '+':
                data[i][1] = int(data[int(data[i][2])][1]) + int(data[int(data[i][3])][1])
            elif data[i][1] == '*':
                data[i][1] = int(data[int(data[i][2])][1]) * int(data[int(data[i][3])][1])
            else:
                data[i][1] = int(data[int(data[i][2])][1]) / int(data[int(data[i][3])][1])

    # 최종 값 = 루트 노드의 1번 idx 값! (정수형으로 출력하자)
    print(f'#{tc} {int(data[1][1])}')

