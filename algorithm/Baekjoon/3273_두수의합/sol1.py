N = int(input())
numbs = list(map(int, input().split()))
numbs.sort()
x = int(input())
start = 0
end = N - 1
interval_cnt = 0  # 중간 합계 계산할 변수 초기화
cnt = 0  # x 만족하는 쌍 몇 개 있는지 세어줄 변수 초기화

# start와 end가 같은 숫자를 가리킬 때까지 반복할거야
while start < end:
    interval_cnt = numbs[start] + numbs[end]
    # 현재 구간 합이 목표 합보다 작다면, start를 밀어
    if interval_cnt < x:
        start += 1

    # 현재 구간 합이 목표 합보다 크다면, end를 땡겨
    elif interval_cnt > x:
        end -= 1

    # 현재 구간 합이 목표 합과 일치한다면, cnt +1 해줘
    else:
        cnt += 1
        start += 1

print(cnt)
'''
BOJ 3273
case 1. 두 수의 합

1. 받은 숫자를 정렬한다 (작은수 .. 큰수)

2. 포인터 i, j를 사용한다 ==> i는 왼쪽 끝, j는 오른쪽 끝에 두고 시작
i = 0, j = N-1

3-1. 합이 목표보다 큰 경우 => j를 땡겨
3-2. 합이 목표보다 작은 경우 => i를 밀어
3-3. 합이 목표와 일치해 => cnt +1, 그리고 i나 j중 무엇을 땡기고 밀든 상관이 없어
    원하는걸로 하나 설정해

언제까지 반복?? while i < j
서로 다른 두 수를 고르라고 했으므로, i와 j가 겹치기 전까지 반복!

시간 복잡도 O(N)
'''


'''
BOJ 2003
case 2. 수의 구간 합

1. 숫자를 정렬할 필요가 없다!
2. 투 포인터를 idx 제일 작은 아이들부터 i, j를 배치한다
i = 0, j = 1

***모두 미는 과정밖에 없다***
j를 밀면 구간합이 커지고, i를 밀면 구간합이 작아지겠지

3-1. 구간 합이 목표보다 작은 경우 => j를 밀어
3-2. 구간 합이 목표보다 큰 경우 => i를 밀어
3-3. 구간 합이 목표와 동일한 경우 => cnt +1, 둘다 밀어
    
언제까지 반복?? j가 구간을 나갈 때까지
작기때문에 j를 밀었는데, idx를 나가버렸고, 그러면 구간 합이 더이상 커질 수 없으니까 봐줄 필요가 없어
while True:
    if j == N:
        break

'''