# JSON Server (API-Server) 활용하기
*별도의 서버가 없는 환경에서 프론트엔드 작업을 진행하고자 할 때, 최소한의 실무적인 환경을 제공 받을 수 있는 API-Server 중 하나*

1. Json Server 구축하기

    1. Node.js 설치

  2-1. 폴더에 Server 정보를 세팅 후 사용
  2-2. JSON Server를 전역으로 설치하여 별도의 세팅 없이 사용


2-1. 폴더에 Server 정보를 세팅 후 사용하는 경우

    1. CMD 에서 명령어를 순서대로 입력한다
      * 폴더 내에 node_modules 폴더와 pakage.json, pakagelock.json 파일이 생성됨

    2. Server를 생성하고 셋팅하기 위한 server.js와, DB로 사용할 JSON 파일인 db.json을 생성한다
      * server.js에는 아래와 같이 코드를 작성하여 서버 환경을 구축해준다
      * 만일 사용하고자 하는 data가 달라지면 db.json을 수정하거나, 해당 위치에 다른 JSON 파일명을 넣어준다
      * port 는 사용할 포트 넘버를 설정하는 부분으로, 본인 환경에 맞게 변경해서 사용이 가능하다

    3. `node server.js` 명령어를 통해 서버를 구동시킨다


2-2. JSON Server를 전역으로 설치하여, 별도의 세팅 없이 사용하는 경우
    1. CMD 에서 명령어를 순서대로 입력한다
   `npm install -g json-server`
  
    2. 설치 이후에는 DB로 사용할 JSON 파일이 있는 위치로 이동하여, 해당 data를 load할 수 있도록 명령어를 입력한다