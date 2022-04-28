# DOM (Document Object Model)

**DOM**

* HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
* 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
* 문서가 구조화되어 있으며 각 요소는 **객체(object)**로 취급

* 프로그래밍 언어(JS)를 사용하여 조작

**DOM 조작**

* Document는 문서 한 장(HTML)에 해당하고 이를 조작
* DOM 조작 순서
  1. 선택 (Select)
  2. 변경 (Manipulation)

**DOM 관련 객체 상속 구조**

* EventTarget
* Node
  * 여러 가지 DOM 타입들이 상속하는 인터페이스

* **Element**
* **Document**
* **HTMLElement**



**DOM 선택 - 선택 관련 메서드**

* `document.querySelector`
  * 단일 element
* `document.querySelectorAll`
  * Node list

* id, class, tag 선택자 등을 모두 사용 가능함!

**DOM 변경 - 변경 관련 메서드**

* `document.createElement()`
  * 작성한 태그 명의 HTML 요소를 생성하여 반환
* `Element.append()`
  * 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
* `Node.appendChild()`
  * 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
  * 한번에 오직 하나의 Node만 추가 가능

**DOM 변경 - 변경 관련 속성**

* `Node.innerText`
  * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현
  * 모든것을 string 덩어리로 인지함 (꺽쇠고 뭐고 그냥 다 string임.)
* `Element.innerHTML`
  * 요소 내에 포함된 HTML 마크업을 반환
  * **XSS(Cross-site Scripting) 공격에 취약하므로 사용 시 주의**
    * XSS: 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
    * 피해자 (사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함
    * 결론 .. 쓰지 마 ...ㅠ

**DOM 삭제 - 삭제 관련 속성**

* ` ChildNode.remove()`
  * Node가 속한 트리에서 해당 Node를 제거
* `Node.removeChild()`
  * DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  * Node는 인자로 들어가는 자식 Node의 부모 Node

**DOM 속성 - 속성 관련 메서드**

* `Element.setAttribute(name, value)`
  * 지정된 요소의 값을 설정
  * 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
* `Element.getAttribute(attributeName)`
  * 해당 요소의 지정된 값(문자열)을 반환
  * 인자(attributeName)는 값을 얻고자 하는 속성의 이름



**Event(이벤트) 개념**

* 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
* 이벤트 발생
  * 마우스 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수 있음
  * 특정 메서드를 호출하여 프로그래밍적으로도 만들어낼 수 있음

**Event 기반 인터페이스**

* AnimationEvent, ClipboardEvent, DragEvent 등 ..
  * ClipboardEvent : 복사할 때 임시 저장되는 이벤트

**Event 역할**

* ~하면 ~한다

**Event handler - `addEventListner()`**

* 대상에 특정 이벤트가 발생하면, 할 일을 등록하자