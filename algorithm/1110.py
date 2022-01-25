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





