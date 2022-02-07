# 첫번째 수 받기
N = int(input())
# 리스트 받는 이차원 리스트 생성
cnt_lst = []
for N2 in range(N//2, N+1):
    lst = [N]
    lst.append(N2)
    # 이미 lst안에 N, N2 있으니까 세번째 수 idx는 2부터 시작
    for i in range(2, N+1):
        # 전전에서 전꺼 뺐을 때 양수면 numb에 저장하고 lst에 저장
        if lst[i-2] - lst[i-1] >= 0:
            numb = lst[i-2] - lst[i-1]
            lst.append(numb)
        # 음수 나오면 numb저장 그만하고 cnt_lst에 저장
        else:
            cnt_lst.append(lst)
            break

# cnt_lst에 있는 리스트들의 요소 개수 받는 리스트
max_numb = []
for lst in cnt_lst:
    max_numb.append(len(lst))
# 최대 요소 개수 출력
print(max(max_numb))

for i in range(len(cnt_lst)):
    # 최대 요소 개수와 동일한 cnt_lst의 리스트의 요소를 일렬로 출력
    if len(cnt_lst[i]) == max(max_numb):
        for j in cnt_lst[i]:
            print(j, end=' ')
            
    
