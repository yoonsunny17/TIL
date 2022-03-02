### Django (python web framework)

> Web framework

* Web : World Wide Web

> Static web page

* 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

* 요청을 받은 경우 추가적인 처리과정 없이 클라이언트에게 응답을 보냄
* **모든 상황에서 모든 사용자에게 동일한 정보를 표시**
* HTML, CSS, JS로 작성됨
* flat page라고도 함

> Dynamic web page

* 요청을 받은 경우 **추가적인 처리 과정 이후** 클라이언트에게 응답을 보냄
* 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
* 서버 사이드 프로그래밍 언어(Python, Java, C++등)가 사용되며, 파일 처리하고 데이터베이스와의 상호작용이 이루어짐

> Framework

* 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임
  * 일종의 환경 및 tool을 제공해줌

> Django를 사용하는 이유?

* 검증된 파이썬 언어 기반 web framework
* 대규모 서비스에도 안저적이며 오랫동안 세계들인 기업들에 의해 사용됨
  * spotify, instaram, dropbox, delivery hero...

> Framework Architecture

* MVC Design Pattern (model-view-controller)

* Django는 **MTV pattern**이라고 함

> MTV pattern (Model-Template-View)

* model
  * 응용 프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
* template
  * 파일의 구조나 레이아웃을 정의
  * 실제 내용을 보여주는 데 사용(presentation)
* **view (controller)** :star:
  * HTTP 요청을 수신하고 HTTP 응답을 반환
  * model을 통해 요청을 충족시키는 데 필요한 데이터에 접근
  * template에게 응답의 서식 설정을 맡김 

> Project & Application

* Project
  * 프로젝트에는 여러 앱이 포함될 수 있음
  * 앱은 여러 프로젝트에 있을 수 있음

* Application :star:
  * 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
  * 하나의 프로젝트는 여러 앱을 가짐
  * 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
  * **앱은 생성 후 등록!!!**
* 앱 등록 시 주의사항
  * `# Local apps` => `# Third party apps` => `# Django apps` 
  * 위의 순서로 정리하기!



********

1. 가상환경 생성 및 활성화
2. django 설치
3. 프로젝트 생성
4. 서버 켜서 로켓 활성화 확인

5. 앱 생성
6. 앱 등록