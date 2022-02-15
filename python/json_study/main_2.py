import json

file_stream = open('data/data_2.json', 'r', encoding ='UTF-8')

data = json.load(file_stream)

print(data)
print(type(data))

print('========')

print(data[0])
print(type(data[0]))

print('========')

for i in range(len(data)):
    print(data[i])

print('')