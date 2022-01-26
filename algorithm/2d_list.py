lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#1) 1, 5, 9 반환

def play(lst):
    for i in range(len(lst)):
        new = 0
        for j in range(len(lst)):
            if i == j:
                new += lst[i][j]
                print(new)
    
    return ''

result = lst
print(play(lst))

#2) 3, 5, 7 반환

# def play(lst):
#     for i in range(len(lst)):
#         if i == len(lst) - 1:

#     for i in range(len(lst)):
#         new = 0
#         for j in range(len(lst), -1):
#             if i + j == 2:
#                 new += lst[i][j]
#                 print(new)
     
#     return ''

result = lst
print(play(lst))





#################
lst2=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

for i in range(len(lst2)):
    for j in range(len(lst2[i])):
        if i % 2 == 0 :
            print(lst2[i][j], end = ' ')
        else:
            print(lst2[i][-j-1], end = ' ')
        
