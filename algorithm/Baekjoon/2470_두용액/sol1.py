'''
BOJ 두 수의 합
음수의 합이여도 피곤해지지 않는다

정렬하고 

가장 왼쪽 // 가장 오른쪽 포인터 두고 시작

value = float('inf')
sol1, sol2 = 0, 0

0에 제일 가장 가까운 두 수의 합을 구해야 함
abs(numbers[i] + numbers[j]) < value:
    value = abs(numbers[i] + numbers[j])
    sol1 = numbers[i]
    sol2 = numbers[j]
'''

