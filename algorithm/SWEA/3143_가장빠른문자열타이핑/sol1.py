import sys

sys.stdin = open('typing.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())
    cnt = 0 # 글자수 세어 줄 변수 초기화
    i = 0

    while i < len(A): # i가 A의 길이보다 작을 때까지 반복
        if A[i] == B[0]: # 만약 A의 i번째 글자와 B의 첫번째 글자가 동일하다면
            if A[i:i+len(B)] == B: # 두근대면서 혹시 나머지도 다 비슷한지 체크
                cnt += 1 # 동일하다면 글자수 cnt +1 해주고
                i += len(B) # i는 B의 글자수만큼 건너뛰자
            else:
                cnt += 1 # 실망했다면 cnt +1 하고
                i += 1 # i는 하나만 증가시키고
        else: # 만약 B의 첫번째 글자와 동일한 경우가 없으면
            cnt += 1
            i += 1

    print(f'#{tc} {cnt}')

