import sys

sys.stdin = open('quick_sort.txt')

def quick_sort(arr, start, end):
    # 만약 원소가 하나라면, 바로 리턴해줘
    if start >= end:
        return

    pivot = start  # pivot은 arr의 첫 번째(가장 왼쪽)로 잡자
    left = start + 1  # pivot의 바로 오른쪽이 left
    right = end  # arr의 가장 끝쪽이 right

    # 엇갈리기 전까지 계속 반복해줘
    while left <= right:
        # pivot 보다 값이 작으면 그냥 냅두고 left += 1 해줘
        while left <= right and arr[left] <= arr[pivot]:
            left += 1
        # pivot 보다 값이 크면 냅두고 right -=1 해줘
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        # 만약에 둘이 엇갈리면, pivot을 중간으로 보내줘
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        # 그게 아니면 왼쪽, 오른쪽 값의 자리를 바꿔줘
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # pivot을 중심(partition)으로 퀵정렬 반복해줘
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick_sort(lst, 0, len(lst)-1)
    # print(lst)
    print(f'#{tc} {lst[N//2]}')

