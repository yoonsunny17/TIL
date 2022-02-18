import sys

sys.stdin = open('rotate.txt')

T = int(input())

# 90도 회전할 때 생성되는 행렬을 만드는 함수
def rotation(N, arr):
    # 90도 회전한 행렬을 받을 빈 이차원 리스트 생성
    arr_90 = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            arr_90[c][r] = arr[N-1-r][c]
    
    return arr_90

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    m_90 = rotation(N, matrix) # 90도 회전
    m_180 = rotation(N, m_90) # 180도 회전
    m_270 = rotation(N, m_180) # 270도 회전

    print(f'#{tc}')
    for i in range(N):
        print(f''.join(map(str, m_90[i])), end=' ')
        print(f''.join(map(str, m_180[i])), end=' ')
        print(f''.join(map(str, m_270[i])), end=' ')
        print()

