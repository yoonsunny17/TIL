'''
1 = switch on
0 = switch off

학생들에게 1 이상, switch 개수 이하의 자연수 하나씩 나누어 줌

boy: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
girl: 자기가 받은 수를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간에서,
그 구간에 속한 스위치의 상태를 모두 바꿔준다 => 항상 홀수개의 switch 상태를 바꾼다

'''

from re import X


switch_numb = int(input()) # 스위치 개수
switches = list(map(int, input().split())) # 각 스위치 상태
students = int(input()) # 학생 수
for _ in range(students): 
    student, numb = list(map(int, input().split)) # 각 학생의 성별 및 부여받은 번호

# switch_on = True
# switch_off = False

# 학생 수만큼 스위치 조작 반복
for student in students:
    # 남학생인 경우: 부여받은 숫자의 배수에 해당되는 스위치 조작
    if student == 1:
        # 스위치 개수만큼 반복
        for i in range(1, switch_numb+1):
            if i % numb == 0:
                switches[i-1] = int(not switches[i-1])


    # 여학생인 경우: 부여받은 숫자 중심으로 좌우 대칭 스위치들 모두 조작
    elif student == 2:
        for i in range(1, switch_numb+1):
            if i == numb:
                switches[i-1] = int(not switches[i-1])
                x = i-1
                for n in range(1, x+1):
                    if switches[x-n] == switches[x+n]:
                        switches[x-n] = int(not switches[x-n])
                        switches[x+n] = int(not switches[x+n])



for switch in switches:
    print
                # #좌우대칭
                # if switches[x-1] == switches[x+1]:


    



    # 학생 성별에 따라 스위치 조작 방법이 다르므로 성별 조건문 설정
    # 남학생일 경우, 부여받은 번호의 배수에 해당되는 스위치들을 조작
    # if student == 1:
    #     for i in range(1, len(switches)+1):
    #         if i % numb == 0:
    #             not switches[i-1]


    # # 여학생일 경우, 부여받은 번호 중심으로 좌우 대칭인 스위치들을 모두 조작
    # if student == 2:
    #     for i in range(1, len(switches)+1):
    #         if i == numb:

    #         if switches[i-1] == switches[i+1]: