import sys

sys.stdin = open('baby_gin.txt')

T = int(input())
for tc in range(1, T + 1):
    
    cards = list(map(int, input()))
    cnt = [0] * 12 # 뽑은 카드에 적힌 수에 해당되는 idx에 그 수의 개수를 누적시킬 것임
    
    for i in range(6): # 카드 개수만큼 반복할거야
        for j in range(len(cnt)): # 해당 idx에 카드 수 누적을!
            if cards[i] == j: # cards[0] == 1이면
                cnt[j] += 1 # cnt[1] 에 1을 더할거야!! 이거를 6번 반복할거야

    # cnt 리스트 맨 마지막 요소는 무조건 0,0 일 것인데 이는 백스트레이트? 그거때문에 설정한거라 값 넣어줌
    cnt[10] += cnt[0]
    cnt[11] += cnt[1]
                
    run = tri = 0 # run, triplet 변수 초기화
    i = 0
    while i < 10:
        # triplet인 경우 먼저 생각해볼까
        if cnt[i] >= 3: # 해당 숫자의 카드 개수가 3개 이상이면 triplet!
            tri += 1
            cnt[i] -= 3 # triplet으로 간주했으니까 제거해줘야지
            continue # 333333인 경우 333. 333 반복

        # run인 경우 생각해보자
        if cnt[i] * cnt[i+1] * cnt[i+2] != 0: # 연속되는 수 중에 하나라도 카드가 없으면 곱했을 때 0 나오겠지
            run += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue

        i += 1

    # baby-gin
    if run + tri == 2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')


