# Model relationship 2

**1:N의 한계**

* 새로운 예약을 생성하는 것이 불가능
* 중개 모델 (중개 테이블)



**ManyToManyField**

* 다대다(M:N, many-to-many) 관계 설정 시 사용하는 모델 필드

* 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요

* `ManyToManyField` 작성 (중개 모델 삭제)

  * 필드 작성 위치는 Doctor 또는 Patient 모두 작성 가능

* 모델 필드의 `RelatedManager`를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음

  * `add(), remove(), ... `

  

**related_name**

* target model(관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 사용할 manager의 이름을 설정 = **역참조**
* 즉, 역참조 시에 사용하는 manager의 이름을 설정
* ForeignKey의 related_name과 동일



**중개 모델(테이블) in Django**

* django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성
* 그렇다면 중개 테이블을 직접 작성하는 경우는 없을까?
  * 중개 테이블을 수동으로 지정하려는 경우, `through` 옵션을 사용하여, 중개 테이블을 나타내는 django 모델을 지정할 수 있음
  * 가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려는 경우에 사용



**Summary**

* 실제 Doctor와 Patient 테이블이 변하는 것은 없음
* 1 : N  관계는 완전한 종속 관례이지만, M : N 관계는 **의사에게 진찰받는 환자, 환자를 진찰하는 의사**의 두 가지 형태로 모두 표현이 가능한 것!



**ManyToManyField's Arguments**

1. `related_name`
2. `through`
3. `symmetrical`



**Related Manager**

* 1 : N 또는 M : N 관련 컨텍스트에서 사용되는 매니저
* 같은 이름의 메서드여도 각 관계에 따라 다르게 사용 및 동작함
  * 1:N 에서는 target 모델 인스턴스만 사용 가능
  * M:N 관계에서는 관련된 두 객체에서 모두 사용 가능
* `add()`
  * 지정된 객체를 관련 객체 집합에 추가
  * 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  * 모델 인스턴스, 필드값을 인자로 허용
* `remove()`
  * 관련 객체 집합에서 지정된 모델 객체를 제거
  * 내부적으로 `QuerySet.delete()`를 사용하여 관계가 삭제됨
  * 모델 인스턴스, 필드값을 인자로 허용

* `through`
  * 모델 관계 설정



**중개 테이블의 필드 생성 규칙**

1. source model 및 target model이 다른 경우
   * id
   * `<containing_model>_id`
   * `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   * id
   * `from_<model>_id`
   * `to_<model>_id`





### LIKE 구현하기

* 에러 발생 원인
  * `like_users` 필드 생성 시 자동으로 역참조는 `.article_set` 매니저를 생성
  * 그러나 이전 1 : N (User:Article) 관계에서 이미 해당 매니저 이름을 사용 중이기 때문
  * User와 관계된 ForeignKey 또는 ManyToManyField 중 하나에 related_name 추가 필요

* 현재 `User-Article` 간 사용 가능한 DB API
  * `article.user`
  * `articles.like_users`
  * `user.article_set`
  * `user.like_articles`



**QuerySet API - `exists()`**

* QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
* 특히 규모가 큰 QuerySet의 컨텍스트에서 특정 개체 존재 여부와 관련된 검색에 유용
* 고유한 필드(예: PK)가 있는 모델이 QuerySet의 구성원인지 여부를 찾는 가장 효율적인 방법
  * 동작에는 차이가 없음





### Profile Page

* 자연스러운 follow 흐름을 위한 회원 프로필 페이지 작성하기
* `symmetrical`
  * `symmetrical=True (default)`일 경우 Django는 person_set 매니저를 추가하지 않음