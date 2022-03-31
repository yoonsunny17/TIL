from itertools import combinations
from pprint import pprint
# powerset 구하기

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
lst = []
for i in range(1<<n):
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])
    lst.append(temp)

for k in lst:
    if sum(k) == 10:
        print(' '.join(map(str, k)))