# for j in range(5): #=> 세로
#     for i in range(3): #=> 가로
#         print('*', end='')
#     print('')

'''
solution) 0이 아닌 요소 찾으면서 나아가기, 0 만나면 아래 또는 좌우로 이동
만약 상하좌우에 0이 아닌 값이 존재하지 않는다면 사각형이 없는 것으로 간주 가능
이중 리스트 만들어서 for문 두번 반복
'''

# 행(가로)를 i, 열(세로)를 j
def width(i, j): #가로길이 측정
    cnt = 1
    del_x = j 
    while True:
        del_x += 1
        if del_x >= N: # 범위를 초과하는 경우
            break

        if lst[i][del_x] != 0: # 0이 아닌 경우 계속 가로길이 continue
            cnt += 1
        else:
            break
    return cnt

def height(i, j): #세로길이 측정
    cnt = 1
    del_y = i
    while True:
        del_y += 1
        if del_y >= N:
            break
        
        if lst[del_y][j] != 0: # 0이 아닌 경우 세로길이 continue
            cnt += 1
        else:
            break
    return cnt

# 중복 검사 방지
def dup(sy, sx, ey, ex):
    for i in range(sy, ey):
        for j in range(sx, ex):
            lst[i][j] = 0
    
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) 
    lst = [list(map(int, input().split())) for _ in range(N)] # 이중리스트 생성
    rlt = [] # 최종 결과 받을 리스트

    for i in range(N):
        for j in range(N):
            if lst[i][j] != 0: 
                w = width(i, j)
                h = height(i, j)
                dup(i, j, i+h, j+w)
                rlt.append([h, w, w*h])
    
    # 출력 우선순위 => 열 행 순서로 출력하되, 크기가 작은 순서대로 출력. 만약 크기가 같으면 행이 작은 값부터 출력 (오름차순)
    rlt = rlt.sort(key= lambda x: (x[2], x[0]))
    print('#{} {}'.format(test_case, len()), end=' ')
    for x, y, z in rlt:
        print("{} {}".format(x, y), end='')
    print()