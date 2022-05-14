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



**Vue.js에 Bootstrap 적용하는 방법** (3 step!)

1. 패키지 설치
2. main.js에 추가
3. Bootstrap-vue 사용

*******

```python
npm install vue bootstrap-vue bootstrap  # 패키지 설치
```

```javascript
// main.js에 추가
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
```

```html
<!-- bootstrap.vue 사용 -->
<!-- 대부분의 component는 b-로 시작한다! 외우는거 x 공식문서 참고하자 -->
<template>
  <div id="app">
    <b-button>Button</b-button>
    <b-button variant="danger">Button</b-button>
    <b-button variant="success">Button</b-button>
    <b-button variant="outline-primary">Button</b-button>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  margin: 20px;
}
</style>
```

