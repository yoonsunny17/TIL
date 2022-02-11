> 관통 프로젝트_3: 반응형 웹 페이지 구성

관통 프로젝트 03- web README.md에 링크 => 이런게 있구나 참고



> **반응형 웹, media query**
>
> (과목평가 내용은 아님) web 분야에 대해 조금 더 deep 하게 알고싶다면 !!

>웹 페이지 디자인 형태

* 고정폭 레이아웃 => 브라우저 크기가 변화하더라도 컨텐츠가 변화하지 않음
* 유동적 레이아웃
* 별도의 사이트 => 디바이스에 따른 별도의 사이트(도메인)으로 구분됨
  * naver.com // m.naver.com

* 반응형 레이아웃 => 너비 조정함에 따라 컨텐츠가 유동적으로 줄어들기도 하고 구성 또는 레이아웃이 변화하는 레이아웃
* **media query** => css 활용하여 구성하는 방법 중 하나
  * @media 키워드 활용
  * landscape => 가로모드 (너비 > 높이)
  * portrait => 세로모드 (높이 > 너비)
  * media type : all, print, screen, speech
  * 특정 너비

> 반응형 웹 페이지 구성

* Favicon, Icon, Font
* Favicon(favorite icon)
  * 사이트를 대표하는 아이콘
  * <link> tag이므로 <head> 에 넣어준다!