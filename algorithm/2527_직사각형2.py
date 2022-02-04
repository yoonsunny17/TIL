for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # R1의 가로, 세로길이
    a1 = p1 - x1
    b1 = q1 - y1

    # R2의 가로, 세로길이
    a2 = p2 - x2
    b2 = q2 - y2

    # 점으로 만나는 경우
    if (a1 + a2) == (p2 - x1) and (b1 + b2) == (q2 - y1):
        print('c')

    # 아예 안만나는 경우
    elif (a1 + a2) < (p2 - x1) or (b1 + b2) < (q2 - y1):
        print('d')

    # 겹치는 경우
    elif (a1 + a2) > (p2 - x1) and (b1 + b2) > (q2 - y1):
        print('a')

    # 직선인 경우
    else:
        print('b')