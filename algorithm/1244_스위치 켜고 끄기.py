'''
1 = switch on
0 = switch off

학생들에게 1 이상, switch 개수 이하의 자연수 하나씩 나누어 줌

boy: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
girl: 자기가 받은 수를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간에서,
그 구간에 속한 스위치의 상태를 모두 바꿔준다 => 항상 홀수개의 switch 상태를 바꾼다

'''

switch_numb = int(input()) # 스위치 개수
switches = list(map(int, input().split())) # 각 스위치 상태 리스트로 받기
students = int(input()) # 학생 수
for i in range(students):
    gender_and_number = list(map(int, input().split())) # 각 학생 성별 및 부여받은 번호 리스트로 받기

    if gender_and_number[0] == 1: # 남자인 경우
        for n in range(1, switch_numb+1):
            if n % gender_and_number[1] == 0: # 번호의 배수에 해당되는 스위치 조작
                switches[n-1] = int(not switches[n-1])

            else:
                continue


    elif gender_and_number[0] == 2: # 여자인 경우
        for n in range(1, switch_numb+1):
            if n == gender_and_number[1]: # 번호에 해당되는 스위치 조작
                switches[n-1] = int(not switches[n-1])
                x = n-1
                while True:
                    for k in range(1, x+1):
                        if (x-k < 0) or (x+k > len(switches) - 1):
                            if switches[x-k] == switches[x+k]: # 좌우대칭 스위치 상태 같은 경우 조작
                                switches[x-k] = int(not switches[x-k])
                                switches[x+k] = int(not switches[x+k])

                            else:
                                break

                        
# 20개씩 끊어서 출력, join 함수 사용
for length in range(len(switches)//20 + 1):
    switch = switches[:20]
    switches = switches[20:] 
    print(' '.join(map(str, switch)))
  

                # # if switches[x-1] == switches[x+1]:

                # # 해당 번호 스위치 상태 우선 조작
                # switches[i-1] = int(not switches[i-1])
                # x = i-1
                # # 좌우대칭 스위치 조작 => 최대 반복 가능한 수 len(switches)//2
                # for n in range(1, len(switches)//2):
                #     if switches[x-n] == switches[x+n]:
                #         switches[x-n] = int(not switches[x-n])
                #         switches[x+n] = int(not switches[x+n])
                #     # 좌우대칭 스위치 상태 다른 경우 stop
                #     else:
                #         continue





                # if switches[n-2] == switches[n]:
                #     switches[n-2] = int(not switches[n-2])
                #     switches[n] = int(not switches[n])
                # x = n - 2
                # y = n
                # if switches[x] == switches[y]:
                #     switches[x] = int(not switches[x])
                #     switches[y] = int(not switches[y])
                #     x -= 1
                #     y += 1
                
                # if x <= 0 or y >= switch_numb:
                #     break
        



          

                # for k in range(1, (switch_numb - n)):
                #     if switches[x-k] == switches[x+k]:
                #         switches[x-k] = int(not switches[x-k])
                #         switches[x+k] = int(not switches[x+k])

                #         if (x-k) == -1 or (x+k) >= (len(switches)+1):
                #             break


# for switch in switches:
#     print(switch, end=' ')

# for switch in switches:
#     for length in range(len(switches)//20 + 1):
#         switch = swi

# for switch in switches:
#     if (len(switches) // 20) == 0:
#         print(switch, end=' ')

#     elif 1<= (len(switches) // 20) <= 5:
#         for m in
#         while len(switches) != 0:
#             rlts = switches[:20]
#             for rlt in rlts:
#                 print(rlt, end=' ')
#                 rlts = switches[20:]
            
#             break


# for student in range(1, students+1): 
#     gender, numb = list(map(int, input().split())) # 각 학생의 성별 및 부여받은 번호

# print(gender, numb)
# # switch_on = True
# # switch_off = False


# # 학생 수만큼 스위치 조작 반복
# for student in range(1, students+1):
#     # 남학생인 경우
#     if gender == 1:
#         # 스위치 개수(번호)만큼 반복
#         for i in range(1, switch_numb+1):
#             # 스위치 번호가 할당받은 번호의 배수인 경우 스위치 상태 변환
#             if i % numb == 0:
#                 switches[i-1] = int(not switches[i-1])
#             else:
#                 continue

#     # 여학생인 경우: 부여받은 숫자 중심으로 좌우 대칭 스위치들 모두 조작
#     elif gender == 2:
#         # 스위치 개수(번호)만큼 반복
#         for i in range(1, switch_numb+1):
#             # 할당받은 번호 = 스위치 번호 ///번호 기준으로 좌우대칭 스위치 상태 같은 경우 둘 다 변환 및 반복
#             if i == numb:
#                 # 해당 번호 스위치 상태 우선 조작
#                 switches[i-1] = int(not switches[i-1])
#                 x = i-1
#                 # 좌우대칭 스위치 조작 => 최대 반복 가능한 수 len(switches)//2
#                 for n in range(1, len(switches)//2):
#                     if switches[x-n] == switches[x+n]:
#                         switches[x-n] = int(not switches[x-n])
#                         switches[x+n] = int(not switches[x+n])
#                     # 좌우대칭 스위치 상태 다른 경우 stop
#                     else:
#                         continue

# for switch in switches:
#     if (len(switches) // 20) == 0:
#         print(switch, end=' ')

#     elif 1<= (len(switches) // 20) <= 5:
#         while len(switches) != 0:
#             rlts = switches[:20]
#             for rlt in rlts:
#                 print(rlt, end=' ')
#                 break
#             switches.remove(rlts)


# # 20개씩 끊어서 출력 => while문 돌리기
# while len(switches) != 0:
#     for switch in range(switches[20]):
#         print(switch, end=' ')
#         print('')
# switches.remove(switches[:20])

        





    



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