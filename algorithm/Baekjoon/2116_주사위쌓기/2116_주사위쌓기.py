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

N = int(input()) # 주사위 개수
dice_lst = [] # 이중 리스트 만들기위해 빈 리스트 생성
for _ in range(N):
    dice_lst.append(list(map(int, input().split()))) # 각 주사위 수 리스트로 받아서 리스트에 추가

# 윗면 아랫면 짝지어주기
bottom_and_top = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
} 

# 가능한 옆면을 value로 받는 딕셔너리 설정
sides = {
    0: [1, 2, 3, 4],
    1: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    4: [0, 1, 3, 5],
    5: [1, 2, 3, 4]
}

# 최종 출력할 값 초기화
max_result = 0

# 첫번째 주사위 먼저 시작 => 윗면만 고려
for i in range(6):
    top_idx = bottom_and_top[i] # i = 0 인 경우, top_idx = 5
    top_numb = dice_lst[0][top_idx] # top_numb = 4
    side_idx = sides[i] # side_idx = [1,2,3,4]

    result = max(dice_lst[0][idx] for idx in side_idx) # 윗면 아랫면 제외한 나머지 중 max값을 result에 저장

    # 두번째 ~ 마지막 주사위 반복 => 아랫면, 윗면 둘 다 고려
    for j in range(1, len(dice_lst)):
        bottom_idx = dice_lst[j].index(top_numb) # 두번째 주사위 아랫면 = 첫번째 주사위 윗면
        top_idx = bottom_and_top[bottom_idx] # bottom_and_top으로 쌍을 찾기
        top_numb = dice_lst[j][top_idx] # top_idx에 부합하는 top_numb 찾기
        side_idx = sides[bottom_idx] # sides_idx 리스트 뽑기

        result += max(dice_lst[j][idx] for idx in side_idx) # 옆면 중 max값을 result에 합산

    # max_result에 result값을 할당
    if max_result < result: 
        max_result = result

print(max_result)



