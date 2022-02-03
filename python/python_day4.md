## Review

### Module

**코드 => 함수 => 모듈 => 패키지(서브패키지) => 라이브러리**

* 모듈과 패키지 불러오기

  > `import module`  : 파일을 다 불러오는 것은 비효율적
  >
  >  `from module import var, function, Class` : 원하는 것만 불러오는것
  >
  > `from module import *`  : 첫번째랑 동일, *'\*' 자체가 all이라는 의미*를 뜻함

  

* 파이썬 표준 라이브러리 (python ver 3.9로 맞춰서 보기)

* 파이썬 패키지 관리자(pip) 

  * [PyPI](https://pypi.org/) (Python Package Index)에 저장된 **외부 패키지**들을 설치하도록 도와주는 패키지 관리 시스템

  * 패키지 설치

    | `pip install SomePackage`            | 최신버전     |
    | :----------------------------------- | ------------ |
    | **`pip install SomePackage==1.0.5`** | **특정버전** |
    | **`pip install SomePackage<=1.0.4`** | **최소버전** |

  * 모든 폴더에는 __init\_\_.py 파일을 만든다!



### 가상환경

* venv (virtual environment)
  * 가상 환경을 만들고 관리하는 데 사용되는 모듈
  * **특정 디렉토리에 가상 환경**을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  * `$python -m venv <폴더명>` : 가상환경이 들어가는 폴더 이름



*********

JSON: Data를 표현하는 방법 중 하나 (파이썬과 무관)

key, value 형식으로 되어 있음 (python의 딕셔너리 형식과 비슷)

