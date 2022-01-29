A, B, C = map(int, input().split())
D = int(input())

hours = list()
for h in range(24):
    hours.append(h)

minutes = list()
for m in range(60):
    minutes.append(m)

seconds = list()
for s in range(60):
    seconds.appned(s)

'''
0 <= A <= 23
0 <= B <= 59
0 <= C <= 59
'''
'''
1시간 = 60분
1분 = 60초
'''
'''
C + D 기준으로 생각을 해야할 것 같음
분 단위를 바꿀 수 있는 범위인지
시 단위를 바꿀 수 있는 범위인지

리스트로 해서 하는 게 나을려나
'''