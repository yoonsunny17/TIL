import sys

sys.stdin = open('merge_sort.txt')


def partition(arr):
    # 원소 하나 남았으면 반환해줘
    if len(arr) <= 1:
        return arr
    # 계속 쪼개줄거야!
    mid = len(arr)//2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    l = len(left)
    r = len(right)
    result = [0]*(l+r)
    left_i, right_i = 0, 0
    i = 0
    if left[-1] > right[-1]:
        cnt += 1

    while left_i < l or right_i < r:
        if left_i < l and right_i < r:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1

        elif left_i < l:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < r:
            result[i] = right[right_i]
            i += 1
            right_i += 1
    return result


T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))
    answer = partition(lst)

    print(f'#{tc} {answer[N//2]} {cnt}')