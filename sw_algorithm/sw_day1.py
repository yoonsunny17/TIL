# 겹치지 않게 숫자 나열하는 방법
numb = {1, 2, 3}

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i2 and i3 != i1:
                    print(i1, i2, i3)


########

#baby gin game; 완전검색 사용하지 않고!!

'''
arr = list(map(int, input().split()))
arr = list(map(int, input()))
arr = [int(x) for x in input()]
'''

