# Promise와 async/await 차이점



> js에는 비동기 처리를 다룰 수 있는 방법이 여러가지가 존재하는데, 주로 `callback`, `Promise`, `async/await`를 활용함
>
> 그 중에서도, 최근 많이 사용하는 `Promise`, `async/await`에 대해 공부하고자 함



### Promise

* js 비동기 처리에 사용되는 객체
  * 내용은 실행되었지만 **결과를 아직 반환하지 않은 객체**
* 3가지 상태
  * `Pending` (대기)
    * 비동기 처리가 완료되지 않은 경우
  * `Fulfilled` (이행)
    * 완료된 경우
  * `Rejected` (실패)
    * 실패하였거나 오류가 발생한 경우

**Promise 사용 예시**

```javascript
const condition = true;
const promise = new Promise((resolve, reject) => {
    if (condition) {
        resolve('resolved');
    } else {
        reject('rejected');
    }
});
promise
	.then((res) => {
      console.log(res);
	})
	.catch((error) => {
      console.error(error);
	});
```

`condition`의 값에 따라 `promise`의 반환 값이 결정되어짐

* 값이 참인 경우 `resolve`를 호출하고, 참이 아닌 경우 `reject`를 호출한다
* `resolve`한 반환 값에 대해서는 `then()`을 통해 결과 값을 반환 받을 수 있고, `reject`의 반환 값에 대해서는 `catch()`를 통해 반환 받는다
* `then()`과 `catch()`문의 체이닝을 통해 비동기 로직의 성공 여부에 따른 분기 처리 가능

*****

### async / await

* 가장 최근에 나온 비동기 처리 문법
* 기존의 `callback`이나 `Promise`의 단점을 해소하고자 만들어짐
  * `callback`이나 `Promise`의 경우, 꼬리에 꼬리를 무는 코드가 나올 수 있으며, 이를 *콜백 지옥* 이라고 부른다
* `await`를 통해 `Promise` 반환 값을 받아올 수 있다

```javascript
const variable = await promise; // promise의 반환 값을 받을 variable
```

* 그러나 `async/await`를 사용하기 위해서는 선행되어야 하는 조건이 있는데, `await`는 `async` 함수 안에서만 동작한다.

**async/await 사용예시**

```javascript
(async() => {
    const condition = true;
    const promise = new Promise((resolve, reject) => {
        if (condition) {
            resolve('resolved');
        } else {
            reject('rejected');
        }
    });
    
    try {
      const result = await promise;
        console.log(result);
    } catch(err) {
        console.error(err);
    }
})();
```

* `Promise` 사용 코드를 `async/await` 사용하여 코드를 변경함
* 익명 함수 패턴을 사용
* `async` 함수 내의 `await`를 통해 `Promise`의 반환 값을 `result` 변수에 담에 콘솔에 출력하는 코드임
* 주의할 점은, `async/await`은 `Promise`와는 다르게 에러를 핸들링 할 수 있는 기능이 없으므로, `try-catch()`문을 활용하여 에러를 핸들링 해주어야 한다.

*****

### 차이점

**에러 핸들링**

* `Promise`를 활용할 시에는 `.catch()` 문을 통해 에러 핸들링이 가능하지만, `async/await`는 에러 핸들링할 수 있는 기능이 없으므로 `try-catch()`문을 활용해야 한다

**코드 가독성**

* `Promise`의 `.then()` 지옥의 가능성
* 코드 길이가 길어질수록 `async/await`를 활용한 코드의 가독성이 좋다
* `async/await`는 비동기 코드가 동기 코드처럼 읽히게 해준다. 코드 흐름을 이해하기 쉽다