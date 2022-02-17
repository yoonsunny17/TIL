import sys

sys.stdin = open('simple_factorization.txt')

def my_factorization(number):
    lst = [] # 소인수 받을 리스트
    rlt = [0] * 5 # 결과 반환할 리스트 idx 0~4 == a ~ e
    i = 2 # 소인수 중 가장 작은 숫자

    while number != 1:
        if number % i == 0: # 주어진 숫자가 나누어 떨어진다면
            lst.append(i)
            number = number // i
        else: # 나누어 떨어지지 않는 경우에는
            i += 1
    
    for j in range(len(lst)):
        if lst[j] == 2:
            rlt[0] += 1
        elif lst[j] == 3:
            rlt[1] += 1
        elif lst[j] == 5:
            rlt[2] += 1
        elif lst[j] == 7:
            rlt[3] += 1
        elif lst[j] == 11:
            rlt[4] += 1

    return rlt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = ' '.join(map(str, my_factorization(N)))
    
    print(f'#{tc} {result}')

