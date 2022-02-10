import sys

sys.stdin = open('sumofintervals.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 정수의 개수와 구간의 개수
    numbers = list(map(int, input().split())) # N개의 숫자 리스트
    # N개의 숫자에서 이웃한 M개를 골라 합 계산하는 것 몇 번 가능? => N - M + 1 번!!
    # ex, 1 .. 10 에서 3개씩일 때 마지막 가능한게 8 9 10 => 10 - 3 + 1 = 8
    # 가능한 마지막 idx = 7 (8번자리) : 마지막 idx range = N - M

    max_idx = N - M + 1
    cnt = [0] * max_idx

    m_sum = 0
    for i in range(M): # M개 더해주어 첫번째 변수 할당
        m_sum += numbers[i]

    max_sum = min_sum = m_sum # 최소 최대값 구해주기 위해 첫번째 값을 최대 최소값 변수에 할당
    # 그 다음 M개 연속 숫자의 합은 m_sum에 맨 처음 값을 빼고, 새로운 값 하나를 더해준 것과 같다
    for j in range(max_idx-1):
        m_sum = m_sum - numbers[j] + numbers[j+M]

        # 최대값 구하기
        if m_sum >= max_sum:
            max_sum = m_sum

        # 최소값 구하기
        if m_sum <= min_sum:
            min_sum = m_sum

    # 최대값 최소값 차이
    rlt = max_sum - min_sum

    print(f'#{tc} {rlt}')