

# 📚책itUp📚 - 도서 추천 서비스



- 프로젝트 주제: 도서 데이터 수집 및 분석 후 컨텐츠 기반 도서 추천 서비스 개발
- 팀명: 오벤져스
  - 데이터 엔지니어링 팀(2인), 데이터 사이언스 팀(3인)
- 개발기간: 2022/04/04 ~ 2022/05/13 (약 5주)



<br>


## 서비스 소개
- 책itUp은 도서 선택에 어려움을 갖는 사용자를 대상으로 한 도서추천 서비스입니다. 
- 총 249,650권의 도서 데이터를 가지고 있습니다. 이중 특정 조건을 만족하는 도서들만 선별해서 최종적으로 사용자에게 추천할 도서(분석을 진행할 도서)는 8,553권입니다. 

- 유사도 분석을 활용한 컨텐츠 기반 추천 서비스 : 사용자가 도서에 대한 선호도를 선택하면 해당 책들과 유사도가 높은 책들을 사용자에게 추천합니다.
- 토픽모델링을 기반으로한 추천 서비스 : 토픽 모델링을 통해 직접 레이블링한 키워드를 기반으로 사용자에게 도서를 추천합니다.
- 이외에도 시간대에 따른 추천, 가벼운 책 추천 등 다양한 추천 서비스도 제공하고 있으며 도서 노트 작성, 커뮤니티 서비스 등 각종 부가 서비스도 포함하고 있습니다.



<br>

## 팀원 소개

| 팀원명       | 역할                                                         |
| ------------ | ------------------------------------------------------------ |
| 홍지수(팀장) | WEB 기능구현(BE), FE, 데이터 파이프라인 구축, DB구축         |
| 임지윤       | 유사도 분석 및 토픽 모델링                                   |
| 조성헌       | WEB 기능구현(BE), DB구축, 데이터 파이프라인 구축, 서비스 배포 |
| 조완제       | 텍스트 분석 및 토픽 모델링                                   |
| 홍동수       | 텍스트 전처리, 유사도 분석, 토픽 모델링                      |
|              |                                                              |

<br>

## 프로젝트 구조

### 프로젝트 세부자료

- [WBS]()
- [추천용 도서 선정기준](https://github.com/hongpower/Book-recommendation-project/blob/master/Documents/filtering_conditions.md)

<br>

### 프로젝트 발표자료

- [책itUp 도서 추천서비스-ppt](https://github.com/hongpower/Book-recommendation-project/blob/master/Documents/%EC%B1%85itUp%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf)

<br>

### 기술 스택
|        | 사용 기술                                |
| ------ | ---------------------------------------- |
| Front  | HTML, CSS, Javascript                    |
| Back   | Hadoop, Spark SQL, Elasticsearch, Django |
| Server | AWS                                      |
| DB     | MySQL, MongoDB, Elasticsearch            |
| <br/>  |                                          |

### ERD

<img width="849" alt="image" src="https://user-images.githubusercontent.com/96896873/176119994-7779cab9-83bf-480b-b7f0-ab4cd75e1e9c.png">

<br>

### 시스템 아키텍쳐

<img width="750" alt="image" src="https://user-images.githubusercontent.com/96896873/176119485-66992963-b1a9-4714-83c5-de583a8eeccc.png">

<br>

### 서비스 플로우

<img width="888" alt="image" src="https://user-images.githubusercontent.com/96896873/176119646-69f302f0-41bf-45ea-87a6-0157f73d77f1.png">



<br>

## 	서비스 화면

### 메인 페이지

> 모든 사용자에게 추천하는 도서를 보여주는 페이지

- 책itUp 도서 랭킹, 로맨스 도서 추천, 가볍게 읽기 좋은 도서 추천, 시간대(낮/밤)별 도서 추천

![01_main_page-min](https://user-images.githubusercontent.com/96896873/176346172-fb55ab01-d1b5-49e1-b305-cfd40a189d19.gif)

<br>

- 도서 이미지 클릭 시 세부 정보 확인 가능

![02_book_detail](https://user-images.githubusercontent.com/96896873/176345264-12b122c3-c939-43e3-a51e-e80282499278.gif)

<br>

### 검색 페이지

- 저자나 도서 이름으로 검색 후 도서 세부정보 확인 가능
- 자동 완성 기능 포함

![03_search](https://user-images.githubusercontent.com/96896873/176345691-5fd3bcab-1867-42e2-92c7-db28b9eff5c1.gif)

<br>

### 선호도 측정 페이지

> 사용자가 랜덤으로 주어지는 도서에 대해 선호도를 표시하면 이를 바탕으로 후에 맞춤형 추천 서비스 제공

- 좋아요/싫어요/찜기능 
  - 싫어요/좋아요는 하나만 선택 가능, 찜기능은 무관

![04_like_dislike_wish](https://user-images.githubusercontent.com/96896873/176345275-bdda71b1-2584-42e0-adcd-1aaff7bb0aae.gif)



<br>

### 추천 페이지

> 사용자가 선호하는 도서, 선호하지 않는 도서, 찜한 도서들을 기반으로 사용자에게 도서를 추천하는 페이지

- 선호도 기반 추천
  - 사용자 선호 도서와 유사도가 높은 도서 추천
  - 사용자 선호 도서와 같은 장르 내 유사도가 가장 다른 도서 추천

- 스릴러 장르 선호 유저에게 추천된 도서:

![06_rcm_thriller](https://user-images.githubusercontent.com/96896873/176345696-c6cca40b-9d95-40db-bb4e-ee794fe5ab0e.gif)

<br>

- 자기관리, 자기개발서, 수필 선호 유저에게 추천된 도서:

![05_rcm_neighbor](https://user-images.githubusercontent.com/96896873/176345279-e140fdca-7a4a-4da5-a574-f4614c814cb3.gif)

<br>

- 토픽 기반 추천
  - 랜덤으로 나오는 10개의 토픽을 선택하면 해당 토픽 기반으로 추천

![07_rcm_keyword](https://user-images.githubusercontent.com/96896873/176345285-85e5dfec-fd58-4a3e-b86a-0fd81d4c9936.gif)

<br>

### 유저 페이지

>사용자 기본정보, 책itUp에서 활동 내역, 좋아요/찜한 책보기 등 다양한 정보를 한눈에 확인할 수 있는 페이지

- 마이페이지

![08_mypage](https://user-images.githubusercontent.com/96896873/176345704-fb7b4bfb-1910-429d-8d4c-99b341568d8a.gif)

<br>

### 부가 페이지

> 각종 도서에 대한 의견을 자유롭게 공유함으로써 독서 문화를 장려하고 건강한 독서습관을 기르는 데 도움을 주기 위해 포함된 부가 페이지

- 내 서재 서비스
- 서재 도서 등록 : 읽은 도서를 선택 후 해당 도서에 대한 별점 및 독서시작/종료 날짜 기록 가능

![09_library_post](https://user-images.githubusercontent.com/96896873/176345294-dc9f5e02-6b9f-414a-9b28-a6d43c910797.gif)

<br>

- 서재 조회/수정/삭제

![10_library_edit](https://user-images.githubusercontent.com/96896873/176345303-329ac31f-e75e-45a7-afe2-1d76cd56ba95.gif)

<br>

- 커뮤니티
- 도서 노트 조회 및 작성

![11_community_post](https://user-images.githubusercontent.com/96896873/176345306-bbb0b016-f85d-413f-96ab-a2d830456675.gif)

<br>

- 도서 노트 수정 및 삭제

![12_community_delete_edit](https://user-images.githubusercontent.com/96896873/176345308-4e927f5e-345e-467a-9835-3b4c206e0c26.gif)

<br>
