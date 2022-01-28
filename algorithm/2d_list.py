# 


dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
cnt = sum(dwarfs)
for i in range(9):
    for j in range(i+1, 9):
        if cnt - (dwarfs[j] + dwarfs[i]) == 100: #IndexError: list assignment index out of range
            del dwarfs[j]
            del dwarfs[i]
            
            print(dwarfs)