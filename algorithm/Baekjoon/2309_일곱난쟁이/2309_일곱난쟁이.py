# '''
# 난쟁이..이놈의 난쟁이들..
# 9명 중에서 7명이 진짜 난쟁이고
# 2명은 이상한 놈들인데..
# 7명 난쟁이 키의 합이 100이라고 했으니
# 9명 키 합에서 2명 키 합을 뺐을 때 100이 나온다면
# 나머지 7명이 진짜 난쟁이겠구나
# '''

# dwarfs = []
# for _ in range(9):
#     dwarfs.append(int(input()))

# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(dwarfs) - (dwarfs[i] + dwarfs[j]):
#             num1 = dwarfs[i]
#             num2 = dwarfs[j]


dwarfs = [int(input()) for _ in range(9)]

dwarfs.sort()
cnt = sum(dwarfs)
num_1 = 0
num_2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if cnt - (dwarfs[i] + dwarfs[j]) == 100:
            num_1, num_2 = dwarfs[i], dwarfs[j]

            break

dwarfs.remove(num_1)
dwarfs.remove(num_2)

for i in dwarfs:
    print(i)



# dwarfs = []
# for _ in range(9):
#     dwarfs.append(int(input()))

# dwarfs.sort()
# cnt = sum(dwarfs)
# for i in range(len(dwarfs)):
#     for j in range(len(dwarfs)):
#         if dwarfs[i] == dwarfs[j]:
#             continue

#         elif cnt - (dwarfs[i] + dwarfs[j]) == 100: #IndexError: list assignment index out of range
            
#             del dwarfs[j]
#             del dwarfs[i]

#     if len(dwarfs) == 7:
#         break


# for dwarf in dwarfs:
#     print(dwarf)



    



