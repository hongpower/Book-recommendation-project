# 개발표준안

### 작성형식

| 폴더/파일명  | 세부내용                        |
| ------------ | ------------------------------- |
| *(모든 폴더) | snake(언더바 활용), 소문자 작성 |
| 크롤링       | _crawling.py                    |
| api          | _api.py                         |
|              |                                 |
|              |                                 |
|              |                                 |
|              |                                 |
|              |                                 |
|              |                                 |

- 작성순서
  - 동사 + 플랫폼 + 메인기능 + 부가기능
    - 없는 기능은 생략해서 순서대로 작성
  - 예) interpark_api_temp.py : 임시적인 api 파일
  - 예2) get_data_interpark.py : interpark에서 데이터 가져오는 파일
- 데이터 수집하는 파일은 왠만하면 어디서 수집했는지 파악 가능하게 작성
  - 예) interpark_api.py



### 영어 관련

| 영어         | 한국어   |
| ------------ | -------- |
| 소설/시/희곡 | novel    |
| 에세이       | essay    |
| 자기계발     | document |
| 추천         | rcm      |
| 임시         | Temp     |
|              |          |
|              |          |
|              |          |
|              |          |

## 가상환경

1. 가상환경 이름 : book_project
   - 아나콘다 가상환경 사용(Python 3.9버전) -> 후에 스파크때문에 3.7/3.8로 내려야할듯

2. 가상환경에 설치한 것들 : pip freeze로 확인가능
   1. selenium
   2. lxml
   3. bs4
   4. Pandas
   5. Django -4.0.4

## 프로젝트 

1. 파이썬 프로젝트 이름 : book_recommendation_project

2. 폴더 구조 : 

   1. `01_data_collection` 폴더 - data폴더, driver폴더, 각종 크롤링 및 api 파일 => 데이터 수집 관련 파일 다 이곳에 작성
      1. driver폴더- chromedriver
      2. data폴더 : api 및 crawling으로 수집한 데이터
      3. rcm_data폴더 : 추천책에 한해서 제공할 데이터
   2. 미정

   

   

