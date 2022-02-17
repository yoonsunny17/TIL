'''
교수님 solution
ord() function 사용~!
'''

def itoa(my_int):

    my_str = "" # return 값

    while my_int != 0:
        # 나머지를 구해서
        r = my_int % 10
        # 나머지를 문자열로 만들고, my_str에 더해줌 chr, ord 함수 사용
        # ord('0') => 숫자 0에 대한 ASCII code 값을 받는 함수
        my_str = chr(ord('0') + r) + my_str
        # my_str = my_str + chr(ord('0') + r) 이렇게 하면 순서가 뒤집힌다는 것 유의
        
        # 나눈 몫을 다시 my_int에 저장

    return my_str


# ord() 사용
user_number = int(input()) # 정수
print(type(itoa(user_number))) # class_str