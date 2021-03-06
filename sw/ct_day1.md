## Computational Thinking

> 이산수학 (Discrete mathematics)

* 이산적인 수학 구조에 대해 연구하는 학문; 연속되지 않는 공간을 다룬다

* 연속된 수를 다루는 미적분학(Calculus)과 반대의 개념

> CT_ 중요한 것 :star:

* 재귀
* 동적 프로그래밍

> Hard Logic vs Soft Logic

* 논리적으로 푸는 경우, 직관적으로 푸는 경우

> 명제

* 참, 거짓을 판별할 수 있는 문장

* 명제가 참 또는 거짓의 값을 가질 때 그 값을 **진리값 (truth value)** 이라고 함
* 이진 논리라고도 말함
* 논리: 참, 거짓을 판별할 수 있는 법칙

> 논리 연산자

* 단순한 명제를 연결시켜주는 연산자
* 부정 NOT
  * ~ p (not p 또는 p의 부정)
* 논리합 OR
  * P v Q (합집합 느낌)
* 논리곱 AND
  * P ^ Q (교집합 느낌)
* 배타적 논리합 (exclusive or)  XOR
  * p, q 중 하나만 참일 때 참이 되는 명제
  * **거짓을 가정하고 시작하면, 결론은 항상 참!**
  * = **전제가 거짓이면, 그 명제는 항상 참이다** :star2::star2:
* 합성
  * 연산자 우선 순위
    * ~ > v, ^ > ->, <->
  * 항진명제: 진리값이 항상 참
  * 모순명제: 진리값이 항상 거짓
  * 사건명제: 항진명제도 모순명제도 아닌 명제

> 증명 (proof)

* 연역법
  * 일반적인 사실을 나타내는 명제를 전제로 하여 개별명제의 특수한 결론을 추론해 내는 것
  * 사람은 동물이다. 모든 동물은 죽는다. 모든 사람은 죽는다
* 귀납법
  * 특수사실로부터 일반진리를 이끌어내는 추론 방법으로 일반화 방법이라고도 함
  * 가설이 존재함
  * 이순신 장군은 죽었다. 세종대왕은 죽었다. 모든 사람은 죽는다.

* 수학적 귀납법 (3단계)
  1. **basis**
  2. **hypothesis (가설)**
  3. **step (검증)**

* 모순 증명법
* 직접 증명법, 존재 증명법, 대우 증명법, 반례 증명법, 필요충분조건 증명법