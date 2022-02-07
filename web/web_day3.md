### CSS Layout

* Float, **Flexbox** 

>Float

* CSS 원칙: Normal Flow
* 어떤 요소를 감싸는 형태로 배치는? 혹은 좌/우측에 배치는?? => *Float*

* Float => 둥둥 떠있는 느낌으로
  * 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping하도록 함
  * 요소가 Normal flow를 벗어나도록 함

* Float 속성
  * none:기본값
  * left: 요소를 왼쪽으로 띄움
  * right: 요소를 오른쪽으로 띄움

* .clearfix
  * float 요소의 부모로 div!
  * 부모에게 .clearfix 클래스 부여
  * ::after : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
    * 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가 시 사용
  * clear 속성 요소 => 부모에게 부여!!
  * 부모 요소에 clearing float해서 이후 요소부터 normal flow를 유지할 수 있도록 해주어야 함



> Flexbox

* CSS Flexible Box Layout :star: 
  * 행과 열 형태로 아이템들을 배치하는 *1차원 레이아웃 모델*

* 축
  * main axis
  * cross axis

* 구성 요소
  * flex container (부모요소)
  * flex item (자식요소)

* 수동 값 부여 없이
  * 수직 정렬 가능하고
  * 아이템의 너비와 높이 혹은 간격을 동일하게 배치 가능

* flex-direction
  * row/ row-reverse
  * column/ column-reverse

* flex-wrap
  * 아이템이 컨테이너를 벗어나는 겨우 해당 영역 내에 배치되도록 설정
  * 기본적으로 컨테이너 영역을 벗어나지 않도록 함

* justify-content
* align-content
* align-items
* align-self : 개별 아이템을 cross axis 기준으로 정렬 => container에 적용하는 것이 아니라 개별 아이템에 적용하는 것!!!

* main-axis, cross-axis : 어떤 것을 기준으로 정렬하냐에 따라 방법이 매우 다양함 (mdn 참고)
* flex grow, order.. 



> **Bootstrap**

* 넷플릭스, SSAFY 도 Bootstrap 기반으로 만들어짐
* 기존 html에 비해 margin-top이 없어지고, margin-bottom이 줄어듦을 확인할 수 있음

> spacing

* .mt-1 : margin-top{0.25rem} => 4px
  * m-1부터 m-5까지

* .mx-0 : margin right, left 0px
* .mx-auto
* .my-0 : margin top, bottom 0px

* .my-auto

* **t b s e x y** 