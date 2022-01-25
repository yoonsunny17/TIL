### 2차원 배열 ###

``` python
def student_score(score_lst):
    for j in range(len(score_lst[0])):
        total = 0
        for i in range(len(score_lst)):
            # print(score_lst[i][j])
            total += score_lst[i][j]
        # print("-----")
        print(total)
students = [
 [100, 80, 100, 10],
 [90, 90, 60, 10],
 [80, 80, 80, 10]
]
student_score(students)
```

종이에 직접 그려보고, 많이 찍어보고 합시당~