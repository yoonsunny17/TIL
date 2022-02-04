## CSS (Cascading Style Sheets)

>  스타일을 지정하기 위한 언어

1) 선택하고, 
2) 스타일을 지정한다

```py
h1 {
 color: blue;
 font-size: 15px;
}
```

> CSS 정의 방법

* 인라인(inline)
* 내부 참조(embedding) - <style>
* 외부 참조(link file) - 분리된 CSS 파일
  * 우리는 외부참조만 사용한다.....
  * 코드의 재사용성 높고, 유지보수가 쉬우므로

* 굉장한 것들..
  * [pure css picture gallery](https://css-art.com/pure-css-lace/)
  * [classlayout](https://csslayout.io/)
  * [색 그라데이션 생성기](https://mybrandnewlogo.com/ko/color-gradient-generator)



> 선택자(Selector)

* 기본 선택자

  * 전체 선택자(*), 요소 선택자(tag명으로 선택: h1, h2, div, span, strong...)
  * 클래스 선택자(.className { }), 아이디 선택자(#id_name {})

* 결합자

  * 자손 결합자, 자식 결합자 ?????????????
    * **div p(자손 결합자)**: 모든 자손 중에서 p 인 tag를 다 선택해서 바꿔줌
    * **div >p(자식 결합자)**
  * 일반 형제 결합자, 인접 형제 결합자
    * **A ~ B(일반 형제 결합자)**: A를 만족하는 형제 중에서 B를 만족하는 형제
    * **A + B(인접 형제 결합자)** : A형제 요소 중 바로 뒤에 위치하는 B 요소

  * 의사 클래스/요소
    * 링크, 동적 의사 클래스
    * 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

> **의사 클래스**

### 1. 동적 의사 클래스
- **:link** : 사용자가 아직 한 번도 해당 링크를 누르지 않은 상태 ( a요소 기본 )
- **:visited** : 사용자가 한 번이라도 해당 링크를 누른 상태
- **:hover** : 사용자의 마우스 커서가 위에 올라가 있는 상태
- **:active** : 사용자의 마우스 커서가 클릭중인 상태
- **:focus** : tab키로 focus가 맞춰진 상태
### 2. 상태 의사 클래스
- **:checked** : input의 checkbox나 raidobutton이 체크된 상태
- **:enabled** : input의 "type=text", select, option에서 사용자가 선택한 상태
- **:disabled** : input의 "type=text", select, option을 사용자가 선택할 수 없도록 만든 상태출처 - [https://aboooks.tistory.com/311](https://aboooks.tistory.com/311)
### 3. 구조 의사 클래스
- **:first-child** : 모든 자식 요소 중에서 첫 번째에 위치하는 자식을 선택
- **:nth-child(n)** : 모든 자식 요소 중에서 n번째에 위치하는 자식을 선택
- **:last-child** : 모든 자식 요소 중에서 마지막에 위치하는 자식을 선택
- **:first-of-type** : 모든 자식 요소 중에서 첫 번째에 등장하는 특정 요소를 선택
- **:nth-of-type(n)** : 모든 자식 요소 중에서 n번째로 등장하는 특정 요소를 선택
- **:last-of-type** : 모든 자식 요소 중에서 마지막으로 등장하는 특정 요소를 선택



> **의사 요소**

- **::first-letter** : 요소의 텍스트에서 첫 번째 글자에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::first-line** : 요소의 텍스트에서 첫 줄에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::before** : 요소의 콘텐츠 시작부분에 생성된 콘텐츠를 추가한다.
- **::after** : 요소의 콘텐츠 끝부분에 생성된 콘텐츠를 추가한다.



> CSS  선택자 정리

* id 선택자

  * #으로 시작

  * 일반적으로 하나의 문서에 1번만 사용 (여러번 사용해도 괜찮지만, 단일 id을 사용하는 것을 권장)

* class 선택자

  * 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택



> CSS 적용 우선순위 :star:

* 우선순위 무시하고 그냥 시키는거: ```!important``` => 얘는 웬만하면 쓰지 말아라..
* **인라인 > id > class > 요소(h1)**

* CSS 파일 로딩 순서: 가장 나중에 정의된 것을 따른다 (위에서 아래로 읽기 때문)



> CSS 상속

* 상속을 통해 부모 요소 속성을 자식에게 상속한다
* 속성 중에는 *상속되는 것*과 *상속되지 않는 것*이 있다
  * 상속되지 않는 것을 상속받게 하고 싶은 경우: ```inherit```을 쓰면 됨 (존재만 알고 있자)

>크기 단위 (가변 크기 단위 / 고정 크기 단위)

* 고정 크기 단위: 항상 일정한 크기를 나타내는 것

  * px (모니터 해상도의 한 화소인 '픽셀' 기준)
  * inch (고정단위긴 한데, 운영체제마다 다르긴 함)
  * pt (1pt = 1/72 in)

* 가변 크기 단위: device에 따라, 부모에 따라, 상황에 따라 가변적으로 바뀌는 크기

  * 일반적으로 가변 크기 단위를 자주 쓴다
  * % (백분율 단위)

  > em & rem

  * em (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    * **배수 단위**, 요소에 지정된 사이즈에 대한 상대적인 사이즈를 가짐
  * rem(바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
    * **최상위 요소(html)의 사이즈를 기준**으로 배수 단위를 가짐
  * viewport (디바이스 화면): 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
    * vw (1vw = width의 1/100), vh (1vh = height의 1/100), vmin&vmax(viewport가 작아지거나 커질 때 변경 가능한 최소, 최대 크기)

> 색상 단위

* 색상 키워드
  * 대소문자를 구분하지 않음
  * [색상 키워드](http://ielselog.blogspot.com/2013/10/css-color-keywords.html)

* RGB 색상
  * 16진수 표기법 or 함수형 표기법으로 사용
* a는 alpha(투명도)



> CSS Box Model

* 모든 요소는 **네모(박스모델)**이고, **위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다**
  * 좌측 상단에 배치

* 모든 HTML 요소는 box 형태로 되어있음
* 하나의 박스는 네 부분으로 이루어짐
  * content(내용 들어가는 자리)와 border(테두리 영역) 사이 거리 = padding
  * 요소와 요소 사이 거리 = margin

* Box model 구성
  * margin/padding (십자가, 나누기, 시계방향!!!!)



> CSS 원칙 2

* 모든 요소는 네모(박스모델)

> 대표적으로 활용되는 display (block, inline이 있다는 것만 알고있자 일단은!)

* display: **block**
  * 줄바꿈이 일어나는 요소
  * 화면 크기 전체의 가로 폭을 차지
  * 블록 레벨 요소 안에 인라인 레벨 요소 들어갈 수 있음
* display: **inline**
  * 줄 바꿈이 일어나지 않는 행의 일부 요소
  * content의 너비만큼 가로 폭을 차지한다
  * width, height, margin-top, margin-bottom을 지정할 수 없다



> 블록 레벨 요소와 인라인 레벨 요소

* 대표적인 블록 레벨 요소
  * div / ul, ol, li / p / hr / form 등

> CSS display

* 공간 부여 안됨
* visibility: hidden 요소는 해당 요소 공간 차지하나 화면 표시 하지 않음



> CSS position

* 문서 상에서 요소 위치를 지정
* static: 모든 태그의 기본 값
  * 일반적인 요소 배치 순서에 따름 (좌측 상단)
  * 부모 요소 내에서 배치될 때는 **부모 요소의 위치를 기준으로 배치됨**

* 좌표 프로퍼티(top, bottom, left, right) 사용하여 이동 가능

  * relative(상대위치)
    * 자기 자신의 static 위치를 기준으로 이동
    * normal flow 유지
    * 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
  * absolute(절대위치)
    * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    * normal flow에서 벗어남
    * static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
  * fixed(고정위치)
    * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    * normal flow에서 벗어남
    * 부모 요소 관계 없이 viewport 기준으로 이동 : 스크롤 시에도 항상 같은 곳에 위치

  * **absolute와 fixed는 자리를 붕 뜬다!!!!!!!!!**