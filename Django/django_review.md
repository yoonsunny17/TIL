# Django = python web framework

## web framework

> static web page

* 서버가 클라이언트로부터 정적 웹 페이지에 대한 요청을 받은 경우, 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄
* **모든 상황에서 모든 사용자들에게 동일한 정보를 표시**

> dynamic web page

* 웹 페이지에 대한 요청을 받은 경우 서버는 **추가적인 처리 과정 이후 클라이언트에게 응답을 보냄**
* 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
* 서버 사이드 프로그래밍 언어(python, java, c++)

> Framework 

* 일종의 환경 및 툴을 제공, 클래스 및 라이브러리 모임 (재사용할 수 있는 수많은 코드)

> web framework

* **웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적**

> Framework architecture

* Django: **MTV pattern**
  * M(model), T(template), V(view)
  * M = 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리 (추가, 수정, 삭제)
  * T = 파일의 구조나 레이아웃을 정의, 실제 내용을 보여주는 데 사용
  * V :star: = HTTP 요청을 수신하고 응답을 반환, model을 통해 요청을 충족시키는데 필요한 데이터에 접근, template에게 응답 서식 설정을 맡김 

> Django intro

1. 가상환경 생성 및 활성화 `python -m venv venv`, `source venv/Scripts/activate`
2. django 설치 `pip install django==3.2.12`
3. 프로젝트 생성 `django-admin startproject <projectname> .`
4. 서버 켜서 로켓 확인하기 `python manage.py runserver`
5. 애플리케이션 생성 `python manage.py startapp <appname>`
6. 애플리케이션 등록 => project/settings.py `INSTALLED_APPS`에 등록 진행
7. templates 생성  => application 내부에 sandwich 구조로 폴더 생성 후, html 파일 생성

> 프로젝트 구조

* settings.py : 애플리케이션의 모든 설정을 포함 :star:

* urls.py : 사이트의 url과 적절한 views의 연결을 지정 :star: 
* wsgi.py : web server gateway interface, 배포할 때 사용(X)
* manage.py : 서버킬 때 사용 `python manage.py <command> [options]` :star:

> Application 구조

* admin.py : 관리자용 페이지를 설정하는 곳 :star:
* apps.py : 앱의 정보가 작성된 곳 (X)
* models.py : 앱에서 사용하는 Model을 정의하는 곳 :star:
* tests.py : 프로젝트의 테스트 코드를 작성하는 곳 (X)
* views.py : view 함수들이 정의되는 곳 :star:

> Project & Application

* 프로젝트에는 여러 앱이 포함될 수 있음
* 앱은 여러 프로젝트에 있을 수 있음
* 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
* 하나의 프로젝트는 여러 앱을 가짐
* 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

> Django template

* 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
* 사용하는 built-in system
  * django template languate (DTL)

> DTL

* 조건, 반복, 변수 치환, 필터 등의 기능을 제공
* 단순히 Python이 HTML에 포함된 것이 아니며, 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것

> DTL Syntax

* variable `{{ variable }}`
  * render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
  * render()의 세번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨줌
    * key로 접근하는 것!!

* filter `{{ variable|filter }}`
  * 표시할 변수를 수정할 때 사용
  * chained가 가능하며 일부 필터는 인자를 받기도 함 `{{ variable|join:' ,' }}`

* tags `{% tag %} `:star:
  * 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  * 일부 태그는 시작과 종료 태그가 필요 `{% if %}{% endif %}`

> Template inheritance (템플릿 상속)

* 코드의 재사용성에 초점을 맞춤
* 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 skeleton template을 만들 수 있음

`{% extends '<base.html>'%}` & `{% block content %} {% endblock content %}`

****************

## Django Model (review)

> Model

* 단일 데이터에 대한 정보를 가짐

> Database

* 체계화된 데이터의 모임
* 쿼리(Query)
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  * query를 날린다 = data를 보낸다
* 기본 구조
  * 스키마(schema)
  * 테이블(table)

> ORM

* Object-Relational-Mapping (객체 지향 매핑)
* 장점
  * SQL을 잘 알지 못해도 DB 조작이 가능함
  * 생산성이 좋음



## Migrations

> Migrations Commands

1. `python manage.py makemigrations`

2. `migrate`

3. `sqlmigrate`
4. `showmigrations`



## CRUD

> Create

1. 인스턴스 생성 후 인스턴스 변수 설정

2. 초기 값과 함께 인스턴스 생성
3. QuerySet API - creat() 사용; save 과정이 포함되어 있음
   * `save() method`
   * 객체를 데이터베이스에 저장함