## Django Form

직접 사용자의 데이터를 받으면 **입력된 데이터의 유효성을 검증**하고, 필요시 입력된 데이터를 검증 결과와 함께 다시 표시해야 함

* 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 함
  * 사요자가 입력한 데이터를 검증하는 것 = **유효성 검증**
* Django Form = 과중한 작업과 반복 코드를 줄여줌으로써 작업을 훨씬 쉽게 만들어 줌

* HTML Form
* Django Form
* Model Form



> Django's forms

* Forms은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 **중요한 방어 수단**
* Django는 Form과 관련한 유효성 검사를 단순화 하고, 자동화 할 수 있는 기능을 제공하여 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있게 함
* 주요 역할 세가지
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



## Django Form Class

* Django Form 관리 시스템의 핵심
* 사용자 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요 시 입력된 데이터 검증 결과 재출력) 등의 반복적 작업을 줄여줌

> Form rendering options

* <label> & <input> 쌍에 대한 3가지 출력 옵션

  1. `as_p()`

     * 각 필드가 단락(<p>태그)으로 감싸져서 렌더링 됨

  2. `as_ul()`

     * 각 필드가 목록 항목(<li>태그)으로 감싸져서 렌더링 됨
     * (<ul>)태그는 직접 작성해야 함

  3. `as_table()`

     * 각 필드가 테이블(<tr>태그) 행으로 감싸져서 렌더링 됨

     * <table> 태그는 직접 작성해야 함

> Django의 HTML input 요소 표현 방법 2가지

1. Form fields
   * input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용됨
2. Widgets
   * 웹 페이지의 HTML input 요소 렌더링
   * GET/POST 딕셔너리에서 데이터 추출
   * widgets은 반드시 Form fields에 할당 됨

> Widgets

* Django의 HTML input element 표현
* HTML 렌더링 처리

* 주의사항
  * Form Fields와 혼동하면 안됨
  * Form Fields는 input 유효성 검사를 처리
  * widgets은 웹페이지에서 input element의 단순 raw한 렌더링 처리



## ModelForm

Django Form을 사용하다 보면 Model에 정의한 필드를 유저로부터 입력받기 위해 Form에서 Model 필드를 재정의하는 행위가 중복될 수 있음

따라서 Django는 Model을 통해 Form Class를 만들 수 있는 **ModelForm이라는 Helper를 제공**

> ModelForm Class

* Model을 통해 Form Class를 만들 수 있는 Helper
* 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능

* forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음
* 정의한 클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

> Meta Class

* Model의 정보를 작성하는 곳



## Form vs ModelForm

**누가 더 좋은거라고 단정지을 수 없다**: 상황에 따른 역할이 다르므로 그때그때 사용해야 하는 것이 달라진다

* Form : 사용자로부터 받아 단순히 데이터로서만 사용이 되는 경우 (로그인)

* ModelForm : 사용자로부터 받는 데이터가 DB의 구조와 동일하게 저장이 되는 경우 (회원가입)



*****

## 모델폼이 쉽게 해주는 것

1. 모델 필드 속성에 맞는 html element를 만들어주고
2. 이를 통해 받은 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함 