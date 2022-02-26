import sys

sys.stdin = open('input_2.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pattern = list(map(int, input().split())) # 원하는 패턴
    numb = [x for x in range(1, N+1)] # 각 조명 번호
    # print(pattern)
    # print(numb)
    i = 0
    cnt = 0 # 몇번 바꿔주었는지 세어 줄 변수
    while True: # 초기상태가 될 때까지 = 모두 0인 상태일 때까지 반복
        if sum(pattern) == 0:
            break

        if pattern[i] == 0: # 0이면 그냥 넘겨
            i += 1
        
        if pattern[i] == 1: # 1인 경우 여러 경우 생각할 수 있겠지 ,, 배수 고려
            for j in range(len(numb)):
                if numb[j] % numb[i] == 0: # 배수인 경우라면 반전시켜주고,
                    if pattern[j] == 1: pattern[j] = 0
                    else: pattern[j] = 1
            i += 1
            cnt += 1 # 몇번 반전했는지 세어줘

    print(f'#{tc} {cnt}')
