## WEB

### HTML/ CSS

> HTML

* 웹페이지를 작성하는 도구
* HTML 소스코드를 웹 브라우저가 읽어서 우리에게 이쁘게 보여주는 것
* **마크업**을 이용해서 만들어진 문법 중 하나 (마크다운, HTML)
* [caniuse](https://caniuse.com/) : 각 웹페이지에서 HTML 문법 쓸 수 있는지 알려주는 사이트
* HTML, CSS 관련해서 모르는 것 구글링 할 때
  * [mdn](https://developer.mozilla.org/ko/docs/Web/HTML) 을 무조건 앞에 쓰고 검색하기

* [w3school](https://www.w3schools.com/) 여기도 많이 참고하기~~

* 도구 더보기 => 개발자 도구 (ctrl + shift + i) or (F12)



> Front-end 개발자 // Back-end 개발자

* front-end : 눈에 보이는 화면을 만든다
* back-end : 데이터와 로직을 담당한다



> front-end

* HTML: 웹 페이지 구조 생성
* CSS: 웹 페이지 스타일링
* JS: 웹 페이지 기능추가 (웹 페이지 조작)



> HTML (*Hyper Text Markup Language*)

* hyper link 
* tag로 **데이터**와 **문서의 구조**를 표현 (= markup language)
* markdown은 markup언어의 일종
  * markdown: 문서 작성시에 구조와 내용을 함께 적기 위해 만들어진 마크업 언어

* HTML로 웹페이지 구조를 작성할 거야 :smile: 



> HTML 기본 구조

* html : 문서의 최상위(root) 요소
* head :
* body :
* meta data = 데이터의 데이터

> DOM(Document Object Model) 트리

* 텍스트 파일인 html 문서를 브라우저에서 렌더링 하기 위한 구조
  * html 문서 내의 각 요소에 접근 및 수정에 매우 용이함
  * html 문서에 대한 모델을 구성함 

> 요소(element)

* ```<h1>contents</h1>``` : tag와 contents(내용)로 구성되어 있음

* **내용**이 없는 태그들
  * br(개행; ```\n``` 같은거), hr, img, input, link, meta => 닫는tag가 없어서 내용이 없는 태그들이 있다

> 속성(attribute)

* ```< a href="https://google.com"></a>``` 
  * *herf = 속성명, " " = 속성값*
  * 쌍따옴표 사용, 공백은 NO!!

* 속성을 통해 태그의 부가적인 정보를 설정 가능
  * ```<a href="https://www.google.co.kr">구글 바로가기</a>```
* 태그와 상관 없이 사용 가능한 속성(HTML Global Attribute)들도 있음