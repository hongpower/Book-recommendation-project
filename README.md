# 📚책itUp📚 - 맞춤별 도서 추천 서비스

- 프로젝트 주제: 도서 데이터 수집 및 분석 후 컨텐츠 기반 도서 추천 서비스 개발

- 팀명: 오벤져스
  - 데이터 엔지니어링 팀(2인), 데이터 사이언스 팀(3인)

- 개발기간: 2022/04/04 ~ 2022/05/13 (약 5주)



## 서비스 소개
- 책itUp은 도서 선택에 어려움을 갖는 사용자를 대상으로 한 도서추천 서비스입니다. 
- 총 249,650권의 도서 데이터를 가지고 있습니다. 이중 특정 조건을 만족하는 도서들만 선별해서 최종적으로 사용자에게 추천할 도서(분석을 진행할 도서)는 8,553권입니다. 

- 유사도 분석을 활용한 컨텐츠 기반 추천 서비스 : 사용자가 도서에 대한 선호도를 선택하면 해당 책들과 유사도가 높은 책들을 사용자에게 추천합니다.
- 토픽모델링을 기반으로한 추천 서비스 : 토픽 모델링을 통해 직접 레이블링한 키워드를 기반으로 사용자에게 도서를 추천합니다.
- 이외에도 시간대에 따른 추천, 가벼운 책 추천 등 다양한 추천 서비스도 제공하고 있으며 도서 노트 작성, 커뮤니티 서비스 등 각종 부가 서비스도 포함하고 있습니다.



## 팀원 소개

| 팀원명       | 역할                                                         |
| ------------ | ------------------------------------------------------------ |
| 홍지수(팀장) | WEB 기능구현(BE), FE, 데이터 파이프라인 구축, DB구축         |
| 임지윤       | 유사도 분석 및 토픽 모델링                                   |
| 조성헌       | WEB 기능구현(BE), DB구축, 데이터 파이프라인 구축, 서비스 배포 |
| 조완제       | 텍스트 분석 및 토픽 모델링                                   |
| 홍동수       | 텍스트 전처리, 유사도 분석, 토픽 모델링                      |
|              |                                                              |



## 프로젝트 구조

### 프로젝트 세부자료

- [WBS]()
- [추천용 도서 선정기준]()



### 프로젝트 발표자료

- [책itUp 도서 추천서비스-ppt]()



### 기술 스택

- **Front** : HTML, CSS, Javascript
- **Back** : Hadoop, Spark SQL, Elasticsearch, Django
- **Server** : AWS
- **DB** : MySQL, MongoDB, Elasticsearch



### ERD

<img width="849" alt="image" src="https://user-images.githubusercontent.com/96896873/176119994-7779cab9-83bf-480b-b7f0-ab4cd75e1e9c.png">



### 시스템 아키텍쳐

<img width="750" alt="image" src="https://user-images.githubusercontent.com/96896873/176119485-66992963-b1a9-4714-83c5-de583a8eeccc.png">



### 서비스 플로우

<img width="888" alt="image" src="https://user-images.githubusercontent.com/96896873/176119646-69f302f0-41bf-45ea-87a6-0157f73d77f1.png">



## 	서비스 화면

### 메인 페이지

> 모든 사용자에게 추천하는 도서를 보여주는 페이지

- 책itUp 도서 랭킹, 로맨스 도서 추천, 가볍게 읽기 좋은 도서 추천, 시간대(낮/밤)별 도서 추천

![mainpage_whole_view](https://user-images.githubusercontent.com/96896873/176129039-e56b6116-771c-4c5d-acac-f09b51b4160c.gif)



- 도서 이미지 클릭 시 세부 정보 확인 가능

![detail_whole_view_real2](https://user-images.githubusercontent.com/96896873/176134682-8ca0182e-38bf-4964-be6a-7ee9d69eff0a.gif)



### 검색 페이지

- 저자나 도서 이름으로 검색 후 도서 세부정보 확인 가능
- 자동 완성 기능 포함

![search](https://user-images.githubusercontent.com/96896873/176148185-d3a68897-a23e-4d9a-bc44-a93d2a5634f4.gif)



### 선호도 측정 페이지

> 사용자가 랜덤으로 주어지는 도서에 대해 선호도를 표시하면 이를 바탕으로 후에 맞춤형 추천 서비스 제공

- 좋아요/싫어요/찜기능 
  - 싫어요/좋아요는 하나만 선택 가능, 찜기능은 무관


![like_dislike_function](https://user-images.githubusercontent.com/96896873/176140630-887196f3-bb86-48c5-ba04-e59419227c90.gif)



### 추천 페이지

> 사용자가 선호하는 도서, 선호하지 않는 도서, 찜한 도서들을 기반으로 사용자에게 도서를 추천하는 페이지

- 선호도 기반 추천
  - 사용자 선호 도서와 유사도가 높은 도서 추천
  - 사용자 선호 도서와 같은 장르 내 유사도가 가장 다른 도서 추천

- 스릴러 도서 선호 유저에게 추천된 도서:

![rcm_iamjoker](https://user-images.githubusercontent.com/96896873/176136492-2c87810e-0a6e-42be-964b-ed477fa5fb2e.gif)



- 자기관리, 개발서, 수필 선호 유저에게 추천된 도서:

<img src="https://user-images.githubusercontent.com/96896873/176138062-8d68f349-aa90-4d01-885f-48b791ebed6c.gif" alt="rcm_neighbor" style="zoom: 43%;" />



- 토픽 기반 추천
  - 랜덤으로 나오는 10개의 토픽을 선택하면 해당 토픽 기반으로 추천

![rcm_keyword](https://user-images.githubusercontent.com/96896873/176138759-f8e98091-0cb3-4ce7-876f-60ff1fbd6be3.gif)



### 유저 페이지

>사용자 기본정보, 책itUp에서 활동 내역, 좋아요/찜한 책보기 등 다양한 정보를 한눈에 확인할 수 있는 페이지

- 마이페이지

![my_page](https://user-images.githubusercontent.com/96896873/176139644-bb09aca8-9e9f-4233-a5c3-d1f752cf0883.gif)



### 부가 페이지

> 각종 도서에 대한 의견을 자유롭게 공유함으로써 독서 문화를 장려하고 건강한 독서습관을 기르는 데 도움을 주기 위해 포함된 부가 페이지

- 내 서재 서비스
- 서재 도서 등록 : 읽은 도서를 선택 후 해당 도서에 대한 별점 및 독서시작/종료 날짜 기록 가능

![library_post](https://user-images.githubusercontent.com/96896873/176143463-1b6af8f5-b6ff-47a8-8a08-462bb73a348d.gif)

- 서재 조회/수정/삭제

![library_edit_delete](https://user-images.githubusercontent.com/96896873/176143476-20a714a6-0a4b-482a-b64c-b0fa72f82da5.gif)



- 커뮤니티
- 도서 노트 조회 및 작성

![write_note](https://user-images.githubusercontent.com/96896873/176144011-8ea045fb-1417-48d6-812e-c23266565517.gif)

- 도서 노트 수정 및 삭제

![edit_delete_note](https://user-images.githubusercontent.com/96896873/176144002-1b911c9f-fbbd-43c1-9d42-f4c59abaa791.gif)
