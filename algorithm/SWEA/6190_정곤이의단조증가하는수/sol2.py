import sys

sys.stdin = open('s_input.txt')

# 단조증가인지 확인하는 함수 만들기
# 단 한곳이라도 단조증가 성립하지 않는다면 끝!
def mono(number):
    numb = str(number) # str으로 형변환 해주기
    for i in range(len(numb) - 1):
        if numb[i] > numb[i + 1]: # 단조증가 하지 않는 경우
            return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    mono_lst = [] # 단조증가 성립하는 숫자를 받아 줄 리스트

    # N개의 숫자 중 2개 골라서 곱하기
    for i in range(N-1):
        for j in range(i+1, N):
            multi_sum = arr[i] * arr[j]
            if mono(multi_sum) == 0: # 단조증가가 아닌 경우
                mono_lst.append(-1) # 리스트에 -1을 넣어주자
            else:
                mono_lst.append(multi_sum) # 단조증가라면 그 값을 넣어주고..

    # 단조증가 최댓값 찾기
    max_mono = mono_lst[0]
    for i in range(len(mono_lst)):
        if mono_lst[i] >= max_mono:
            max_mono = mono_lst[i]

    # 어짜피 단조증가 없으면 -1 만 나올것..
    print(f'#{tc} {max_mono}')


