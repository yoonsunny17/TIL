## HOW TO USE 'JSON'

> json file을 먼저 생성. data를 입력 후 .py file생성

```python
import json
with open('data/data.json', 'r', encoding='UTF-8') as file_stream: 
    data = json.load(file_stream)
    for each_dict in data:

        title = each_dict['title']
        year = each_dict['year']
        print(f'제목: {title} 개봉연도: {year}')
```

