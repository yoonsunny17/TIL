N = int(input()) # 정수 N의 값을 입력 받음
numb = N # 입력받은 수를 numb로 할당
cnt = 0 # 사이클 수
while True: 
    # i번째 수의 일의 자리 수 = (i+1)번째 수의 십의 자리 수
    # i번째 수의 각 자리수의 합 = (i+1)번째 수의 일의 자리 수
    # 단, 10 이상일 경우 존재하므로 % 연산자 사용하여 나머지만을 더한다

    x = (numb % 10)
    y = (numb // 10)
    z = (x + y) % 10

    numb = (x * 10) + z
    cnt += 1
    if numb == N:   # while 무한루프 종료조건
        break  

print(cnt)





##########종현님과 매우 매우 매우 동일한 풀이방법#########










##################현진님####################

N = int(input())
rlt = N
a = 0

while True:
    # 10의 자리수
    x = N // 10
    # 1의 자리수
    y = N % 10

    # string으로 바꿔서 이어붙인 후 int로 변환
    N = int('%d'%y + '%d'%((x+y)%10))
    a += 1

    if rlt == N:
        print(a)
        break




##################숙경님######################



# string으로 변환해서 int로 재변환 하는것이 소름!













######## 지훈님 ###########

# 데이터 입력
N = int(input())

# 계산
list_nums = [N]
while True:
    if N < 10:
        N = int(str(N)[-1] + str(int(str(N * 10)[0]) + int(str(N * 10)[-1]))[-1])
    else:
        N = int(str(N)[-1] + str(int(str(N)[0]) + int(str(N)[-1]))[-1])
    if N in list_nums:
        break
    list_nums.append(N)

print(len(list_nums))
