import sys

sys.stdin = open('container.txt')


# def f(x, y, cnt):
#     # 박스 > 트럭
#     if len(x) > len(y):
#         for i in range(len(y)):
#             cnt += x[i]
#
#     # 박스 <= 트럭
#     else:
#         for i in range(len(x)):
#             cnt += x[i]
#
#     return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 최댓값 출력해야 하니까 내림차순으로 정렬해주고 시작해
    wi.sort(reverse=True)
    truck.sort(reverse=True)

    print(wi, truck)
    # boxes = []
    # # 만약에 트럭이 옮길 수 있는 최대 무게보다 더 큰 짐이 있다면, 일단 제외해줘!
    # for w in wi:
    #     if w <= max(truck):
    #         boxes.append(w)

    # print(f(boxes, truck, 0))

    # 박스 개수가 트럭보다 많은 경우: 트럭 개수만큼 박스를 골라줘
    # 트럭이 박스 개수보다 많은 경우: 박스 개수에 맞추어 트럭 빼줘, 대신 작은 트럭들 순서로 빼자






    
    # print(boxes)

    # print(wi, truck)
    # print(f'#{tc} ')

