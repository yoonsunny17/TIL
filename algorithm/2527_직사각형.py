
# R1, R2는 4개의 요소를 받을 것. [x y p q] 순서대로 받는다
R1 = [] # [x1, y1, p1, q1]
R2 = [] # [x2, y2, p2, q2]

# 4줄에 걸쳐 data 받음
for _ in range(4):
    n = list(map(int, input().split()))
    # 4개씩 잘라서 R1, R2 list에 넣기
    for i in range(8):
        if 0 <= i <=3:
            R1.append(n[i]) # [3, 10, 50, 60]
        else:
            R2.append(n[i]) # [100, 100, 200, 300]


'''
2. 직사각형인 경우 => a를 출력해라
한 axis만 만족해도 괜찮음
안만나는 경우와 정 반대라고 생각하면 된다. (각 변의 길이의 합) > (edge 좌표 거리) 이면 ok!
'''
'''
3. 선으로 만나는 경우 => b를 출력해라
1) x-axis; (edge 좌표 거리) = 각 변의 길이의 합 & y-axis; (각 변의 길이의 합) > (edge 좌표 거리) 이면 ok!
2) 위와 축만 반대인 경우 
'''
'''
4. 점으로 만나는 경우 => c를 출력해라
경우 3의 1)과 2)를 동시에 만족하면 ok!
'''


# if (R1[2]-R1[0]) + (R2[2]-R2[0]) == abs(R2[2]-R1[0]) and (R1[3]-R1[1]) + (R2[3]-R2[1]) == abs(R2[3]-R1[1]):
#     print(c)

# 간결하게 쓰기 위해..
# R1
x1 = R1[2] - R1[0]
y1 = R1[3] - R1[1]
# R2
x2 = R2[2] - R2[0]
y2 = R2[3] - R2[0]
#좌표 거리
x_distance = abs(R2[2] - R1[0])
y_distance = abs(R2[3] - R1[1])

if (x1 + x2 == x_distance) and (y1 + y2 == y_distance):
    print("c")

elif (x1 + x2 == x_distance) or (y1 + y2 == y_distance):
    print()

'''
1. 안만나는 경우 => d를 출력해라
x-axis or y-axis 중 하나라도 (각 변의 길이 합) < (각 직사각형 edge 좌표 거리) 이면 ok!
=> abs(q2-y1) or abs(p2-x1)
'''
(x1 + x2) 