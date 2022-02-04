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

> **시맨틱 태그** :star: 

* html5에서 *의미론적 요소*를 담은 태그
  * 기존 영역을 의미하는 div 태그를 대체하여 사용 (div: 하나의 구역을 의미, box라고 생각하면 됨)

* 대표적인 태그 목록
  * header
  * nav
  * article
  * section

* 시맨틱 태그를 잘 써야 검색엔진최적화(SEO)에서 효과적으로 활용 가능하다

* Non-sementic tag: div, span



> HTML 문서 구조화

* 인라인 / 블록 요소
* 텍스트 요소
  * ```<a></a>```
  * ```<b></b>```, ```<strong></strong>``` => strong 요소가 좀 더 시맨틱한 의미가 들어감
  * ```<i></i>```, ```<em></em>``` => em요소가 좀 더 시맨틱한 의미가 들어감
  * ``<img scr="url">`` 

* 그룹 컨텐츠
  * ```<pre></pre>``` 공백 문자를 유지하는 데에 유리
  * ```<p></p>``` 하나의 문단(paragraph), *인라인 요소*만 들어갈 수 있음
    * div 같은 애는 들어갈 수 없음
    * div tag 안에 p tag가 들어가는 것은 가능



> form

* <form\> 기본속성 :star:
  * **action** : form을 처리할 서버의 URL
  * **method** : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  * <form\> 안에 <input\> 을 통해 사용자의 data를 입력받는다
  * querystring

> input

* post, get
* form 안에 input을 통해 사용자의 데이터를 입력받는다
* name= querystring의 key 역할
* type = 입력받는 형태를 지정 (txt, email ...)

>input label

* label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  * 사용자가 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용 가능
* input에 id 속성을, label에는 for 속성을 활용하여 상호 연관을 시킴
  * for, id에 같은 속성을 입력해주어야 둘이 연동 된다는 뜻

> input 유형

* checkbox: 다중 선택 가능
* radio: 단일 선택만 가능

* [input 속성](