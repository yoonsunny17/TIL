# 교수님 풀이!
import sys

sys.stdin = open('baby_gin.txt')


def check_babygin(numbers):
    counter = [0] * 10 # 각 숫자를 카운트 할 list
    is_babygin = 0 # 정답 여부 판단

    # 0 ~ 9 의 카드 개수 세기
    for number in numbers:
        counter[number] += 1

    # while은 idx를 언제 증가시켜줄지 내가 정할 수 있음

    idx = 0
    while idx < len(counter): # 모든 카드를 돌겠다
        # check triplet
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        # check run
        if idx < len(counter) - 2: # idx가 맨 끝자리 or 끝에서 두번째면 run이 안되므로!
            if counter[idx] and counter[idx+1] and counter[idx+2]: # 1이상이다 = True이다
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue

        # 결과 체크
        if is_babygin == 2:
            return 1
        
        idx += 1 # 다음 카드 보기
    
    return 0 # 만약 모든 카드를 다 돌았는데도 2 가 안되면 0을 반환하기

T = int(input())
for tc in range(1, T + 1):

    numbers = list(map(int, input()))
    result = check_babygin(numbers) #check-babygin이라는 함수 만들것임
    
    print(f'#{tc} {result}')
