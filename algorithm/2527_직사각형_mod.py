# R1 = []
# R2 = []
# codes = '' # 문자열로 코드 받기

for _ in range(4):
    # R1 = []
    # R2 = []
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    # R1 += [x1, y1, p1, q1]
    # R2 += [x2, y2, p2, q2]

    # R1의 가로, 세로길이
    a1 = p1 - x1
    b1 = q1 - y1

    # R2의 가로, 세로길이
    a2 = p2 - x2
    b2 = q2 - y2

    # R1, R2의 수직, 수평 좌표 거리
    x_dis = [abs(p2 - x1), abs(p1 - x2)]
    y_dis = [abs(q2 - y1), abs(q1 - y2)]    
    # x_dis = abs(p2 - x1)
    # y_dis = abs(q2 - y1)

    # 점으로 만나는 경우
    if max(x_dis) == (a1 + a2) and max(y_dis) == (b1 + b2):
        # codes += 'c'
        print('c')

    # 아예 만나지 않는 경우
    if max(x_dis) > (a1 + a2) or max(y_dis) > (b1 + b2):
        # codes += 'd'
        print('d')

    # 직사각형인 경우
    if max(x_dis) < (a1 + a2) and max(y_dis) < (b1 + b2):
        # codes += 'a'
        print('a')

    # 선으로 만나는 경우
    if (max(x_dis) == (a1 + a2) and max(y_dis) < (b1 + b2)) or (max(y_dis) == (b1 + b2) and x_dis < (a1 + a2)):
        print('b')
        # codes += 'b'
    # else:

# for code in codes:
#     print(code)

# for _ in range(4):
#     n = list(map(int, input().split()))
#     for i in range(8):
#         if 0 <= i <=3:
#             R1.append(n[i])
#         else:
#             R2.append(n[i])
