# print("Hello")
#
# n = int(input()) # 정수 한개 입력받기
#
# a, b = map(int, input().split()) # 정수 사이에 공백 한칸 가지고 입력받기





# lst = list(map(int, input().split())) # 정수 형태를 일차원 리스트로 입력 받기
# lst_2 = [map(int, input().split())] # 얘는 안됨

# cnt = list(map(int, list(input())))
#
# print(cnt)

# matrix = [] # 이차원리스트 만들기
# for _ in range(2):
#     lst = list(map(int, input().split()))
#     matrix.append(lst)
# print(matrix)

# matrix_2 = [x for x in range(10)]
# print(matrix_2)

# matrix = [list(map(int, input().split())) for _ in range(2)]
# print(matrix)

# # shallow copy
# lst = [1, 2, 3, 4]
# temp = []
# temp.append(lst)
#
# lst.pop()
# lst.insert(0, 5)
#
# print(temp)
#
# # deep copy
# lst = [1, 2, 3, 4]
# temp = []
# temp.append(lst[:])
#
# lst.pop()
# lst.insert(0, 5)
#
# print(temp)
#
# # deep copy => 이차원 이상일 때는 적용 ㄴㄴㄴㄴ => copy.deepcopy() 사용하자~~
# lst = [[1, 2], [3, 4]]
# temp = []
# temp.append[:]
#
# lst[0][0] = 5
#
# print(temp)

# matrix = []
# for _ in range(5):
#     row = [0] * 5
#     matrix.append(row)
#
# matrix[0][0] = 99
# print(matrix)

# 리스트 사이에 리스트 넣기
lst = [1, 2, 3, 4]
# lst[2:2] = ['a', 'b', 'c']
# lst[1:3] = ['a', 'b']
lst[1:3] = ['a', 'b', 'c', 'd', 'e'] #개수 달라도 가능~
print(lst)
