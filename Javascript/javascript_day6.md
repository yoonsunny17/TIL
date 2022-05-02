# AJAX

* Asynchronous JavaScript And XML (비동기식 JS와 XML)
* JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고 받을 수 있음

* 특징
  * 페이지 전체를 reload(새로고침)를 하지 않고서도 수행되는 **비동기성**
  * AJAX의 주요 두 가지 특징을 통해 아래의 작업이 가능함
    1. 페이지 새로 고침 없이 서버에 요청
    2. 서버로부터 데이터를 받고 작업을 수행



**Asynchronous JavaScript**

* 동기식(synchronous)
  * 순차적, 직렬적 task 수행
  * 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐 (blocking)
  * 버튼 클릭 후 alert 메세지의 확인 버튼을 누를 때까지 문장이 만들어 지지 않음
    * alert 이후 코드는 alert의 처리가 끝날 때까지 실행되지 않음

* 비동기식(asynchronous)
  * 병렬적 task 수행
  * 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐 (non-blocking)
  * 요청을 보낸 후 응답을 기다리지 않고 다음 코드가 실행됨



**JavaScript는 single threaded 이다**

* 컴퓨터가 어려 개의 CPU를 가지고 있어도 main thread라 불리는 단일 스레드에서만 작업 수행
* 즉, 이벤트를 처리하는 call stack이 하나인 언어라는 뜻
* 이 문제를 해결하기 위해 JS는
  1. 즉시 처리하지 못하는 이벤트들을 다른 곳(Web API)으로 보내서 처리하도록 하고
  2. 처리된 이벤트들은 처리된 순서대로 대기실(Task queue)에 줄을 세워두고
  3. Call Stack이 비면 담당자(Event Loop)가 대기 줄에서 가장 오래된(제일 앞의) 이벤트를 Call Stack으로 보냄



**순차적인 비동기 처리하기**

1. Async callbacks
2. promise-style :star:



**Callback Function**

