def quick_sort(arr, start, end):
    # 원소가 1개밖에 없는 경우라면 바로 종료해줘
    if start >= end:
        return

    pivot = start  # pivot 은 첫번째 원소로 지정해주고,
    left = start + 1  # left는 pivot의 바로 옆 원소
    right = end  # right는 맨 오른쪽 (맨 끝) 원소로 지정해줘

    # left와 right가 엇갈리지 않는 동안,
    while left <= right:
        # pivot 숫자보다 더 큰 숫자를 찾을 동안 left를 왼쪽에서 오른쪽으로 하나씩 옮겨줘
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot 숫자보다 더 작은 숫자를 찾을 동안 right를 오른쪽에서 왼쪽으로 하나씩 옮겨줘
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 만약 left, right가 엇갈렸다면 pivot과 right 값을 swap해줘
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 left, right 값을 swap 해줘
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 왼쪽 부분, 오른쪽 부분 partition 나누어 각각 정렬을 수행하자
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right+1, end)


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, len(lst) - 1)
    print(f'#{tc} {lst}')