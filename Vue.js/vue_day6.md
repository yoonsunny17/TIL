## vue project with pair programming

**'vue-cli-service'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.** 라는 에러가 나는 경우??

*해결 방법*

1. npm cache를 삭제해준다
2. package.json에 정의된 모듈을 재설치 해준다

*******

```python
npm cache clean --force  # npm 캐시 삭제
npm install. # package.json 의존하는 모듈 설치
```



**!important**

현재 windows와 OS 운영체제를 동시에 사용중인데, 왜인지 모르겠지만 위의 명령어를 실행하였을 때 또 다른 라이브러리를 설치하라고 요구를 한다

그냥 말 잘 들으면 잘 실행되니 걱정할 필요 없다!

