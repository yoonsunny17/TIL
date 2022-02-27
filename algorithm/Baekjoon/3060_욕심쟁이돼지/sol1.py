T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 하루에 배달되는 사료의 양
    pig = [0] + list(map(int, input().split())) # idx 보기 편하게 하려고 앞에 0 붙임
    day = 1 # 사료 언제 못주는지 세어 줄 변수 설정, 초기값을 1로 잡기

    while True: # 일단 무한루프
        # 종료조건 설정
        if sum(pig[1:]) > N:
            break

        odd = pig[1] + pig[3] + pig[5]
        even = pig[2] + pig[4] + pig[6]
        
        for i in range(1, 7):
            if i % 2 == 0: # even이면
                pig[i] += odd # odd를 더해
            else: # odd이면
                pig[i] += even # even을 더해

        odd = even = 0
        day += 1

    print(day)

