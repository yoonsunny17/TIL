### Review

> Display 속성 3가지

* block, inline, inline-block, none



> border box vs content box

* ```css
  box-sizing: content-box;
  ```

  * 이걸 써주지 않아도 content box가 default다
  * 그래서 padding값을 설정해주면 같은 height와 width를 가지는 box라도 다른 크기로 보이게 됨

* ```css
  box-sizing: border-box;
  ```

  * 이걸 해주면 width, height 값을 padding까지 알아서 계산

* 

> Emmit

- `>`  태그를 만들고 들여쓰기
- `*n` 반복
- `+` 줄바꿈 + 다음 태그 추가
- `.` class 지정
- `#` id 지정
- `{content}` 내용 입력

```html
div.box>div*3#hello{hola}
```

