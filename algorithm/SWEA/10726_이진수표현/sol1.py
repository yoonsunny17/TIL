'''
TimeError 인 듯?
'''
from collections import deque
import sys

sys.stdin = open('binary_onoff.txt')


def f(numb):
    # 종료조건 2가지 경우: numb이 1 또는 0이 되었을 때!
    if numb == 1 or numb == 0:
        q.appendleft(numb)
        return

    # 나머지가 1이 나오면 q에 1 저장해줘
    if numb % 2:
        q.appendleft(1)
        numb = numb//2
        f(numb)  # 다음 숫자는 2로 나누어주었을 때의 몫이겠지!
    # 나머지가 0이면 0 저장해줘
    else:
        q.appendleft(0)
        numb = numb//2
        f(numb)  # 다음 숫자는 2로 나누어주었을 때의 몫이겠지!


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque()  # 2진수로 변환해준 숫자 저장해줄 q 만들기

    # 처음 주어진 수 M 이 짝수거나 0이라면, 마지막 비트는 무조건 0이 나오므로 OFF 출력해줘
    if not M % 2:
        print(f'#{tc} OFF')

    else:
        f(M)
        print(f'#{tc} ON')

    # print(q)
    # # 그게 아니라면, 2진수로 바꾸는 작업을 시작해보자
    # else:
    #     # 재귀 함수 사용해보자!
    #     for _ in range(N):
    #         f(M)
    #         if 0 in q:
    #             print(f'#{tc} OFF')
    #         else:
    #             print(f'#{tc} ON')


        # 나는 지금 q에 뒷자리부터 append를 해주었으니까 popleft하면 뒷자리부터 나올거야
        # N개를 꺼내서 모두 1인지 확인해볼건데, 하나라도 0이 나온다면 곱했을 때 0이 되겠지
        # N개의 비트를 곱해 볼 변수 초기화해주자
        # rlt = 1
        # for i in range(N):
        #     rlt *= q.popleft()
        #
        # if rlt:
        #     print(f'#{tc} ON')
        # else:
        #     print(f'#{tc} OFF')



    # def f(numb):
    #     # 나머지가 1이 나오면 q에 1 저장해줘
    #     if numb % 2:
    #         q.append(1)
    #         f(numb//2)  # 다음 숫자는 2로 나누어주었을 때의 몫이겠지!
    #     # 나머지가 0이면 0 저장해줘
    #     else:
    #         q.append(0)
    #         f(numb//2)  # 다음 숫자는 2로 나누어주었을 때의 몫이겠지!

