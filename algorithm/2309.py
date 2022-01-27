# '''
# 난쟁이..이놈의 난쟁이들..
# 9명 중에서 7명이 진짜 난쟁이고
# 2명은 이상한 놈들인데..
# 7명 난쟁이 키의 합이 100이라고 했으니
# 9명 키 합에서 2명 키 합을 뺐을 때 100이 나온다면
# 나머지 7명이 진짜 난쟁이겠구나
# '''


dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
cnt = sum(dwarfs)
for i in range(9):
    for j in range(i+1, 9):
        if cnt - (dwarfs[j] + dwarfs[i]) == 100: #IndexError: list assignment index out of range
            del dwarfs[j]
            del dwarfs[i]
            
            print(dwarfs)
    



