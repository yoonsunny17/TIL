# 첫번째 주어지는 수 N <= 30000
# N = int(input())

# 두번째 주어지는 수의 범위 설정이 중요
'''
if N = 100일 때 n < 50 인 경우 빨리 최대 개수가 나오지 않음
100 30 70 -40 //  100 60 40 20 20 0 20 -20
 '''
# 즉, 두번째 주어지는 수의 범위는 첫번째 수의 절반보다 커야 함
# => range(N//2, N)

#일단 무한루프
# while True:
#     for numb in range(N//2, N):
#         if N - numb >= 0:

# numb = []
# numb_list=[]
# for N2 in range(N//2, N):
#     numb.append(N2)
#     n = N - N2
#     numb.append(n) # numb = [N2, n]; 세번째 숫자가 numb[1]이 되도록 설정

import numbers


cnt_lst=[]
N = int(input())
lst = []

for N2 in range(N//2, N):
    lst.append(N)
    lst.append(N2)
    for i in range(2, N//2): #범위 정확 ㄴ
        if lst[i-2] - lst[i-1] >= 0:
            numb = lst[i-2] - lst[i-1]
            lst.append(numb)
        else:
            break
cnt_lst.append(lst)
print(cnt_lst)

    

