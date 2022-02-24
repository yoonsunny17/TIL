'''
pivot을 정하는 것이 가장 중요!
pivot 기준으로 왼쪽에는 pivot보다 작은 숫자들을,
오른쪽에는 pivot보다 큰 숫자들을 정렬하고,
pivot을 기준으로 왼쪽, 오른쪽 숫자들을 partition으로 나누어 다시 한번
각각의 quicksort를 진행한다
'''

def partition(arr, start, end):
    # pivot은 어느 곳을 잡아도 상관은 없지만, 보통은 가운데 숫자로 잡는다
    pivot = arr[(start + end) // 2]

    while start <= end:

        # start
        while arr[start] < pivot:
            start += 1

        # end
        while arr[end] > pivot:
            end -= 1

        if start <= end: # 만약 너희가 엇갈리지 않았다면,
            arr[start], arr[end] = arr[end], arr[start] # swap 으로 자리바꿔줘
            # 이제 다음꺼 찾아야 되니까 움직여줘
            start += 1
            end -= 1
    return start # 다음 part2의 시작 idx를 return할거니까

def quickSort(arr, start, end):
    part2_idx = partition(arr, start, end)
    if start < end:
        quickSort(arr, start, part2_idx-1)
        quickSort(arr, part2_idx, end)


lst = [69, 10, 30, 2, 16, 8, 31, 22]
print(lst)

quickSort(arr=lst, start=0, end=len(lst) - 1)
print(lst)