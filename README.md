# jangpanzi

- 신발 전문 가격 정보 사이트
 
 -> 국내외 신발 판매 사이트의 정보를 크롤링으로 모아와 모델별로 가격비교를 해 소비자가 같은 제품을 더 싼 가격으로 살 수 있도록 돕는데에 주력
 
 -> 응모 이벤트 데이터도 구해 와 현 날짜에서 응모 할 수 있는 아이템들만 보여주도록 설정
 
 -> 북마크 기능을 추가하여 소비자가 같은 제품을 마이페이지에서 한번에 볼 수 있도록 로직 구현

- 백엔드 : Django(python)

- 프론트엔드 : html / css

- DB : mysql

# url

 - / [GET] : 로그인 여부에 따른 메인 페이지 이동  
 - login [GET] : 로그인 화면이동
         [POST] : 로그인 요청
 - logout [GET] : 로그아웃 기능
 - sign_up [GET] : 회원가입 화면이동
           [POST] : 회원가입 요청
 - search [GET] : 검색 결과 출력
 - datecom [GET] : 한정판 응모 페이지 이동
 - howto [GET] : 사이트 이용방법 페이지 이동
 - bookmard<int:id> [GET] : 신발 위시리스트 추가

# ERD MODEL

![캡처](https://user-images.githubusercontent.com/23503161/149621629-5d7b8b98-03b6-42c7-9444-727bf67f5e55.PNG)
