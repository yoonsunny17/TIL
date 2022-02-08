> Review (시험나올확률 높은거.. 강조 많이 하시는거)

**********

> Float

* float 언제 사용? 
  * 뉴스 레이아웃: 인라인 요소로 블록 요소를 감쌀 때

* normal flow를 벗어남
  * normal flow? 왼쪽 상단에 붙으려고 하는 원칙

* default = float none
* <p\> lorem(원하는 글자 수) => 임의의 ()글자 (*lorem ipsum*; 실제 문구를 넣기 전 구조 보기위해 사용하는  예시 문구)

* float를 사용했을 때, 다음 요소들의 정렬되는 순서를 지워주겠다  =>  **float clearing**
  * clear를 적용하는 애부터 float 정렬요소를 없앤다

* 의사요소 생성자 (: or ::을 앞에 붙여준다 => :는 클래스, ::는 )
* ::after 



*********

> Flexbox

* flex container, flex item으로 이루어져 있음

* 수평 구조를 손쉽게 만들어줌

  ```html
  .container {
  	display: flex;
  }
  ```

* 속성들이 container에 주어야 하는지, item에 주어야 하는지 구분이 중요!

  * container에 줄 수 있는 속성

    * display, flex-flow, justify content

    - `display` - Flex Container를 정의
    - `flex-flow` - `flex-direction` 과 `flex-wrap` 을 줄여서 쓸 수 있음
    - `flex-direction` - item들의 주 축(main-axis) 설정
    - `flex-wrap` - item들의 줄 바꿈 설정
    - `justify-content` - 주 축(main-axis)의 정렬  방법 설정
    - `align-content` - 교차 축(cross-axis)의 정렬 방법 설정 (2줄 이상)
    - `align-items` - 교차 축(cross-axis)의 정렬 방법 설정 (1줄)

  * item에 줄 수 있는 속성

    * order, flex, aling-self

*****

#### container에 줄 수 있는 속성들

* display => flex, flex-inline ; flexbox 의 display에 들어갈 수 있는 속성

  * block/inline방식의 container를 쌓는다

* flex-direction => main axis, cross axis 설정

  * default값이 row

  * row/row-reverse, column/column-reverse

* flex-wrap => 창이 줄어들 때 item들의 줄바꿈이 어떻게 될지 설정

  * nowrap(default) => 한줄로 모든 아이템을 표시
  * wrap => viewport 크기에 따라 아이템을 여러줄로 묶어서 표시
  * warp-reverse => viewport 크기가 줄어들면 가장 마지막 item부터 윗줄에 남음

* flex-flow => **flex-direction & flex-wrap**을 줄여서 쓰는 것

  * 사용 시 ```flex-flow: flex-direction flex-wrap``` 이 순서로 사용

* **justify-content** :star::star::star:
  * flex-start, flex-end, center => main-axis 기준으로
  * space-between, space-around, space-evenly
    * space-between =>start 지점의 item과 end 지점의 item 지점 *사이의* item들의 간격을 동일하게
    * space-around =>균등한 여백을 만들어서 정렬 (0.5:1:0.5)
    * space-evenly => **모든** 여백을 균등하게 만들어서 정렬

* align-content => cross-axis의 정렬 방법 설정 (2줄 이상)
  * flex-wrap이 nowrap이면 align-content를 주는 것은 의미가 없음!!
    * stretch(default) => 교차축을 꽉 채우기 위해 늘리는 것
    * flex-start, flex-end, **center**(중앙정렬 쉬워짐)
    * space-between, space-around 
* align-items => cross-axis의 정렬 방법 설정(1줄)
  * 문자들의 크기가 다 다름 => 문자를 담은 box들의 크기가 다 다름

![img](https://cdn.discordapp.com/attachments/940161636713500683/940426318829457469/unknown.png)

*****

#### item에 줄 수 있는 속성들

*  `order` - Item의 순서를 설정(default가 0) :star:

* `flex` - `flex-grow` , `flex-shrink` , `flex-basis` 에 대한 단축 속성!

  => 세개를 한줄로! 단, flex 사용 시 flex-grow 는 생략 불가!

  => flex-basis의 default는 auto이지만, flex 사용 시 flex-basis를 적어주지 않으면 자동적으로 0 이 들어감 (*시험에는 안나오지만 알아두면 좋음*)

- `flex-grow` (default가 1) - Item의 너비 증가(grow) 비율 설정 
- `flex-shrink` (default가 1)- Item의 너비 감소(shrink) 비율 설정 (*시험은 안나옴ㅎ*) 
  * 단, flex-wrap이 nowrap상태인 경우에는 flex-grow, -shrink는 노의미~
  * 아이템에 영향을 끼치는 시점부터 viewport가 줄어드는 distance 에 따라 각 item의 shink 비율에 따라 줄어듦
- `flex-basis` (default가 auto) - Item의 기본 너비 설정 (*얘도 뭐ㅎ*)
  * width를 줄 수 없던 요소들에도 너비를 줄 수 있다는 장점을 가지고 있다

* `align-self` (default가 auto) - cross axis 기준으로 item을 정렬하는 방법을 설정
  * vs `align-items` : 각각의 item들에 대해 설정해주는 `align-self`가 더 우선순위를 차지한다!!

*********

#### Bootstrap

> How to use?

1. file을 다운받아서 사용
2. CDN: Content Delivery(Distribution) Network 시스템 사용

> 기본 요소

* **container, rows, column** :star:

  * **12개의 column을 기준으로 동작한다 (12의 약수가 많아서)**:star:

  * **6개의 grid breakpoints**:star:

* container => container/ container-fluid/ container-{BreakingPoint}

  * 세가지의 class 가 있음
  * container => 안에 있는 item들이 반응형이 됨
  * container-fluid => width를 항상 100%로 지정해 주는 것
  * container-{BP} => viewport크기에 도달할 때마다 width가 100%가 되도록 지정해주는 것
    * BP: xs, sm(스마트폰), md(태블릿), lg(데스크탑), xl, xxl

*****

**CSS 데이터 주고, margin, padding 계산하는 문제 무조건 나옴, 개발자 도구 못씀** 