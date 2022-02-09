# bubble sort

# lst = [55, 7, 78, 12, 42]
#
# for i in range(len(lst)-1, 0, -1):
#     for j in range(0, i):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(lst)

#######

# SWEA bubble sort solution

def bubble_sort(a, N): # 오름차순
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return

T = int(input()) # tc 개수
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr, N)
    print(f'#{tc}', end=' ')
    # for x in arr:
    #     print(x, end=' ')
    # print()
    print(*arr) #=> unpacking!!

##########

# counting sort
