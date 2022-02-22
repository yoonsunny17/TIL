'''
새로운 접근 방법으로 풀어보자...!
w축 h축 각각 나누어 생각해보자
t 시간동안 개미가 이동한 거리 = t
t 시간 이후의 개미의 변위 = (x, y)
'''

w, h = map(int, input().split()) # w = 가로축, h = 세로축
p, q = map(int, input().split()) # 개미의 현재 위치 (p = w의 좌표, q = h의 좌표)
time = int(input()) # 개미가 움직이는 시간

'''
좌표가 아닌 수평선에서 움직인다고 생각해보자.
초기 위치는 각각 p, q 이고 t 시간 후 (p+t), (q+t) 가 되어있을 것이다.
그러나 실제로 문제에서는 w, h라는 boundary condition 을 주었으므로 고려해야 함!
'''
# dp, dq는 실제 좌표계 내에서 개미가 몇번 왔다갔다 했는지 (순환했는지) 체크 가능
# dp, dq 값이 짝수인지, 홀수인지에 따라 나누어서 x, y값 계산된다!
dp = (p + time) // w 
dq = (q + time) // h

# x 좌표 구하기
# 짝수인 경우
if dp % 2 == 0:
    x = (p + time) % w

# 홀수인 경우
else:
    x = w - (p + time) % w

# y 좌표 구하기
# 짝수인 경우
if dq % 2 == 0:
    y = (q + time) % h
# 홀수인 경우
else:
    y = h - (q + time) % h

print(f'{x} {y}')