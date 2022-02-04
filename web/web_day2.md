## HTML (Hyper Text Markup Language)

> HTML 기본 구조

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

> DOM(Document Object Model) 트리

* parent-children
* sibling

> Element

* 내용이 없는 태그들 :star: 
  * hr, br, img, input, link, meta

* 텍스트 요소

  ![image-20220204104604777](web_day2.assets/image-20220204104604777.png)

  * strong, em 이 좀 더 시맨틱한 의미를 가지고 있다

    => 개발자들을 위해 강조/기울임 글씨 하는 것



>  CSS Display

**블록 레벨 요소와 인라인 요소**



> CSS position

* Absolute : 집을 나감 (normal flow 유지 안함)
* Relative : 자리는 이동했지만, 집은 유지함 (normal flow 유지함)
  * => 없는 경우 body 기준



> 실습_practice 1

* big-box의 position: relative가 왜 적혀있는지?
  * big-box의 position을 설정하지 않으면, body 기준으로 돌아다니므로 absolute인 애들의 위치가 난장판이 되어버린다

> 실습_practice 2

* 