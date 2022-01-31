switches = list(map(int, input().split()))
students = int(input())

print(switches)

for i in range(students):
    gender_and_number = list(map(int, input().split()))
    
    if gender_and_number[0] == 1:
        print("이거맞나")

    elif gender_and_number[0] == 2:
        print("여자")



# for i in range(1, len(switches)+1):
#     if i % 3 == 0:
#         switches[i-1] = int(not switches[i-1])





# # if len(switches) <= 20:
# #     print(switch, end=' ')

# # for switch in switches:
# #     if (len(switches) // 20) == 0:
# #         print(switch, end=' ')

# #     else:
# length = (len(switches) // 20)
# for l in range(length):
#     for switch in switches:
#         print(switch, end=' ')
#         if len(switches) >20:
#             print('')
            




# for switch in switches:
#     if len(switches) >= 20:
#         print(switch, end=' ')
# print('')
    





# n = 5 가로
# m = 9 세로

# for j in range(m):
#     for i in range(n):
#         print('*', end=' ')
    # print('') #가로개수 만큼 출력 후 줄바꿈