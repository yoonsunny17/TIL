for _ in range(4):

    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # R1의 가로, 세로길이
    a1 = p1 - x1
    b1 = q1 - y1

    # R2의 가로, 세로길이
    a2 = p2 - x2
    b2 = q2 - y2

    # R1, R2의 수직, 수평 좌표 거리
    x_dis = [p2 - x1, p1 - x2]
    y_dis = [q2 - y1, q1 - y2]    

    for xdis, ydis in x_dis, y_dis:
        xdis = max(x_dis)
        ydis = max(y_dis)

    # 점으로 만나는 경우
        if (xdis == (a1 + a2)) and (ydis == (b1 + b2)):
            print('c')
            break

    # 직사각형인 경우
        if (xdis < (a1 + a2)) and (ydis < (b1 + b2)):
            print('a')
            break

    # 선으로 만나는 경우
        if (xdis == (a1 + a2) and ydis < (b1 + b2)) or (ydis == (b1 + b2) and xdis < (a1 + a2)):
            print('b')
            break
    
    # 아예 만나지 않는 경우
        else:
            print('d')
            break