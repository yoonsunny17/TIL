import json

file_stream = open('data/data.json', 'r', encoding='UTF-8')
data = json.load(file_stream)
file_stream.close()

for each_dict in data:

    title = each_dict['title']
    year = each_dict['year']
    print(f'제목: {title} 개봉연도: {year}')


# print(data)
# print(type(data))
# print('========')
# print(data[0])
# print(type(data[0]))
# print('========')
# for i in range(len(data)):
#     print(data[i])
# print('')

#with open을 같이 쓴다! 위와 똑같은 결과값 도출
with open('data/data.json', 'r', encoding='UTF-8') as file_stream: 
    data = json.load(file_stream)
    for each_dict in data:

        title = each_dict['title']
        year = each_dict['year']
        print(f'제목: {title} 개봉연도: {year}')
    