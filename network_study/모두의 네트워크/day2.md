# 03 물리 계층 : 데이터를 전기 신호로 변환하기

> 물리 계층이란?

* OSI 모델의 1 계층
* 데이터 전송을 위해 시스템 간 물리적인 연결
* 데이터를 전기 신호로 변환하는 역할 및 전기 신호를 제어하는 역할
* 간단히 말해서 물리계층이란,
  * 컴퓨터와 네트워크 장비를 연결하고 >> 전송매체(케이블)
  * 전송되는 데이터를 전기 신호로 변환하는 계층 >> 전기신호, 랜카드, 리피터, 허브



> 전송매체

* 데이터가 흐르는 물리적인 선로
* 유선/무선으로 나뉨
  * 유선: **트위스트 페어 케이블**, 광 케이블
  * 무선: 라디오파, 마이크로파, 적외선



>  트위스트 페어 케이블 (랜 케이블, 랜선)

* UTP 케이블, STP 케이블로 나뉨
* UTP 케이블은 shield로 보호 받지 않기 때문에 noise 영향이 크지만, 저렴하기 때문에 많이 사용함
  * 데이터 전송 품질에 따라 Cat3, Cat5, Cat3e, 등등 다르게 나뉨
    * 속도 및 규격에 따라 분류함 (4장에서 공부!)
* STP 케이블은 shield로 보호 하기 때문에 noise 영향을 거의 받지 않지만, 그만큼 많이 비쌈
* RJ-45 : 랜선의 양쪽 커넥터



> 노이즈

* 케이블에 전기 신호가 흐를 때 발생하는데, 노이즈가 발생하면 전기 신호의 형태가 왜곡됨
* 꼭 소리만을 의미하는 것이 아니라, 열 신호 간섭 등 다양한 신호들의 노이즈를 포함함



> 다이렉트 케이블, 크로스 케이블

* 랜선 속의 케이블 배열에 따른 구분
* 다이렉트 케이블 : 1, 2번이 1, 2번에 순서대로 연결되어 있음
  * 컴퓨터와 스위치를 연결할 때 사용
  * OSI 7계층에서 서로 다른 계층에 있는 장비끼리 연결할 때 사용 (블로그 자료..?)
  * MDI(Media Department Interface) 컴퓨터나 라우터의 인터페이스
  * MDI-X(Media Dependent Interface crossover) 스위치나 허브의 인터페이스
  * MDI == MDI-X
* 크로스 케이블 : 1, 2번이 3, 6번에 교차되어 연결되어 있음
  * 컴퓨터와 컴퓨터를 연결 시 사용, 컴퓨터 두대가 같은 번호로 데이터를 보낼 때 충돌이 일어나지 않도록 1, 2번 케이블을 의도적으로 교차시켜 연결하여 만듦
  * MDI == MDI



> 랜 카드

* 0과 1의 정보를 전기 신호로 변환하는 역할
* 별도의 랜 카드를 가지고 있는 경우도 있고, 메인보드에 랜 카드의 기능이 탑재된 경우도 있음



> 전기 신호의 종류

* 아날로그 신호
* 디지털 신호



> 리피터

* 전기 신호를 정형(일그러진 신호를 복원)하고 증폭하는 기능을 가진 네트워크 중계 장비
* 거리가 너무 멀면 신호가 약해질 수 있으므로, 리피터를 통해 신호 증폭시켜 먼 거리의 장비와도 통신할 수 있음
* 최근에는 잘 사용하지 않음



> 허브

* 리피터와 마찬가지로 전기 신호를 정형하고 증폭하는 기능을 함
* 여러 개의 리피터가 모여 있는 장비, 그래서 리피터 허브라고도 불림
* 허브에 연결된 모든 컴퓨터에 데이터가 전송되므로 비효율적
  * 이를 해결하는 장비가 **스위치**
  * 스위치는 고유한 주소값을 가지고 있으므로 데이터 전송에 있어서 선별하여 데이터 전송을 가능하게 함 (4장에서 공부!)



> 관련 면접 예상 질문

*  OSI 모형 7계층에서 각 계층에 대해 설명

* 허브 리피터 비교

* 허브 라우터 스위치 비교



************

> 궁금한 점

* 케이블에 전기 신호가 흐를 때 노이즈의 영향을 적게 받도록 구리 선 두개를 비틀어 꼬아 케이블을 만든다고 했는데, **비틀어 꼬아** 만드는 것이 구체적으로 노이즈 줄이는 데 어떻게 작용을 하는지 궁금합니다.
  * https://blog.naver.com/PostView.nhn?blogId=kwshop89&logNo=220019277267 참고하자

* 100메가 정도의 속도를 사용하는 경우에는 1, 2, 3, 6만을 실질적으로 사용하고, 나머지 네개는 임시 방편? 으로 냅두는 것
  * 기가 인터넷 (10기가 이더넷) 사용 시 8개의 선을 다 사용해서 데이터를 주고 받음