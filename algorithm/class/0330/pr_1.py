def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1

        if left == right:
            done = True

        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:  # 교차하지 않는 경우라면,
        pivot = partition(arr, start, end)  # pivot 설정하고
        quick_sort(arr, start, pivot-1)  # 왼쪽 정렬
        quick_sort(arr, pivot+1, end)

    return arr


T = int(input())
for tc in range(1, T + 1):
    numbs = list(map(int, input().split()))
    quick_sort(numbs, 0, len(numbs)-1)  # 정렬할 배열, 시작 ~ 끝 idx
    print(f'#{tc} {numbs}')