'''
주사위 개수를 첫번째 줄에 입력받고,
그 다음 줄부터 한 줄에 한 주사위의 번호 6개씩 입력된다
'''

'''
A, B, C, D, E, F면으로 이루어진 주사위라고 했고, 전개도에서 마주보는 면끼리 짝을 지어주면 될 듯
그리고 얘네가 KEY값, 입력값이 VALUE값인 딕셔너리 형식으로 받으면 될 듯

1번 주사위 value가 1인 면을 찾고, 2번 주사위 value가 1인 면을 찾고, 그 맞은편의 key:value쌍 찾고..
주사위가 n개면 (n-1)번 반복하면 된다

주사위를 다 쌓았으면, 각 주사위에서 옆면이 가능한 key:value 4쌍이 있을 것
각각의 dict에서 max값을 추출하고, n개의 max값을 더하면 되지 않을까?
'''

# (A, F) => B, C, D, E // (0, 5) => 1, 2, 3, 4
# (B, D) => A, C, E, F // (1, 3) => 0, 2, 4, 5
# (C, E) => A, B, D, F // (2, 4) => 0, 1, 3, 5

N = int(input()) # 주사위 개수
dice_side = ['A', 'B', 'C', 'D', 'E', 'F'] # 주사위 전개도 순서
for _ in range(N):
    dice_numb = list(map(int, input().split()))
    



# N = int(input())
# for _ in range(N):
#     numbers = list(map(int, input().split()))
#     for i in numbers:
#         dice_dict = dict(A=numbers[0], B=numbers[1], C=numbers[2], D=numbers[3], E=numbers[4], F=numbers[5])

