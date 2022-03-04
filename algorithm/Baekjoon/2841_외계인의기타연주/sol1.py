'''
N = 1 ~ 6
** cnt 변수 만들어주기 => stack에 push하거나 pop을 할 때마다 항상 +1 해주기 **
1. 각 줄 수 마다 stack을 따로 만들어야 함 (minimum 1개, maximum 6개)
2. 각 N stack에서, P를 stack에 push하는데 stack 맨위에 숫자가 나보다 작은 동안 계속 push해주기
3. 맨 위의 숫자가 나보다 크다면, 나보다 작거나 stack이 빌 때까지 pop 해준 뒤 append 해주기
'''
N, P = map(int, input().split())
my_set = set()
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    my_set.add(N)


# for i in range(len(my_set)): # N의 개수만큼 stack을 만들거야
#     stack = [] # 프렛 받을 empty stack
# print(my_set, len(my_set))
    # lst[0] = 1 ~ 6 ; stack 개수를 결정해줘어
    # lst[1] = stack에 넣어줄 애들!