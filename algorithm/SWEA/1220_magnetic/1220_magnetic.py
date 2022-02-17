'''
위에가 N극, 아래가 S극
자성체 N극 = 1, S극 = 2

100*100 테이블이므로 이중 리스트 만들어서
세로로 반복 탐색 하면 될 듯
N극 쪽에 2먼저 나오면 끝나는거고
1 나오면 교착 가능성 있으니까 다음 번호로 넘어가고~ 반복하다가
2 나오면 교착 시키고, 교착 초기화 (세로로 한쌍만 가능하니까 초기화 무조건)
'''

for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)] # 이중리스트

    rlt = 0
    for j in range(n): # row 고정
        cnt = 0
        for i in range(n): # column 먼저 탐색
            if arr[i][j] == 1: # 위에가 N극, 위부터 탐색
                cnt = 1 # N 자성체 발견하면 교착 가능성 발견 = 1 !!
            
            elif arr[i][j] == 2: # S극이 나오는 경우 2가지 경우 발생
                if cnt != 0: # 가능성 있는 애를 발견했으니 교착하자!!
                    rlt += 1 # 교착 총 개수에 누적
                    cnt = 0 # 다시 가능성 초기화
                # else:
                #     continue # 가능성 없는애 발견했으면 그냥 지나치기..
    
    print(f'#{test_case} {rlt}')