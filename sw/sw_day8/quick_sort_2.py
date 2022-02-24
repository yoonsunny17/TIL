'''
quick sort pythonic ver.
'''
def quicksort(arr):
    # 만약에 arr의 길이가 1보다 작거나 같아진다면, arr를 리턴해줘
    if len(arr) <= 1:
        return arr

    pivot, other = arr[0], arr[1:] # pivot을 맨 처음 원소로 잡아줘

    left = [x for x in other if x <= pivot] # other가 pivot보다 작거나 같으면 꺼내서 left로 두자
    right = [x for x in other if x > pivot]

    # 실행된 뒤 재귀호출 될 것이니까, pivot 이 들어있는 list를 더해주어서 return 해
    return quicksort(left) + [pivot] + quicksort(right)

lst = [69, 10, 30, 2, 16, 8, 31, 22]
print(lst)

sorted_lst = quicksort(arr=lst)
print(sorted_lst)