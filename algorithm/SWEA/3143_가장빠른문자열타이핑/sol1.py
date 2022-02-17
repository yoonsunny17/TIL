import sys

sys.stdin = open('typing.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = map(str, input().split())
    cnt = 0
    i = 0

    while i < len(A):
        if A[i] == B[0]:
            if A[i:i+len(B)] == B:
                cnt += 1
                i += len(B)
            else:
                cnt += 1
                i += 1
        else:
            cnt += 1
            i += 1

    print(f'#{tc} {cnt}')

