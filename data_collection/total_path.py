### 파이썬 파일 이름은 항상 각 py파일 맨 위에
### 경로는 여기에
## loss 될 것을 대비해서 각 단계마다 백업 파일 만들기

## 0) 모든 api 요청 파일
# 00_apis ㅇ
# aladin_api ㅇ
# interpark_api ㅇ
# naver_api ㅇ
# kakao_api ㅇ

## 1) 알라딘 api에서 [책id, 책제목, 리뷰수] 크롤링
# 01_aladin_crawling ㅇ
# aladin_crawling_novel_id.py ㅇ -> all_novel_ids.json ㅇ
# aladin_crawling_document_id.py ㅇ -> all_document_ids.json ㅇ
# aladin_crawling_essay_id.py ㅇ -> all_essay_ids.json ㅇ

## 2) 책id로 api 요청
# 02_get_all_api ㅇ
# 표준 컬럼 만들어주자 : all_meta.csv ㅇ
# get_all_novel_api.py ㅇ -> all_novel_data.json, all_novel_data.csv ㅇ
# get_all_document_api.py ㅇ-> all_document_data.json, all_document_data.csv ㅇ
# get_all_essay_api.py ㅇ -> all_essay_data.json, all_essay_data.csv ㅇ

## ==============위까지 모든 책에 대한 정보===================

## 3) 필터링 해서 isbn만 저장하기 (임시)
# 03_filter_all_books ㅇ
# filter_novel_for_rcm.py.py ㅇ -> isbn13_rcm_novel.json
# filter_document_for_rcm.py ㅇ -> isbn13_rcm_document.json
# filter_essay_for_rcm.py ㅇ -> isbn13_rcm_essay.json

## 4) 부가 정보 요청 (사진, 사이즈, 요약 등)
# 04_get_rcm_api ㅇ
# isbn은 업데이트
# get_rcm_novel_api -> rcm_novel_data.json X, isbn13_rcm_novel.json ㅇ <- data_rcm
# get_rcm_document_api.py -> rcm_document_data.json X, isbn13_rcm_document.json ㅇ <- data_rcm
# get_rcm_essay_api.py -> rcm_essay_data.json X, isbn13_rcm_essay.json ㅇ <- data_rcm

## 5) 4번에서 가져온 isbn13으로 리뷰 데이터 및 키워드 가져오기
# 리뷰 1
# kyobo_crawling_novel_review.py -> rcm_novel_review.json
# kyobo_crawling_document_review.py -> rcm_document_review.json
# kyobo_crawling_essay_review.py -> rcm_essay_review.json

# 리뷰 2 -> 기존 리뷰에 append
# yes24_crawling_document_review.py -> rcm_novel_review.json
# yes24_crawling_document_review.py -> rcm_document_review.json
# yes24_crawling_essay_review.py -> rcm_essay_review.json

# 키워드
# kyobo_crawling_novel_review.py -> rcm_novel_keyword.json
# kyobo_crawling_document_review.py -> rcm_document_keyword.json
# kyobo_crawling_essay_review.py -> rcm_essay_keyword.json

## 4번과 5번은 스파크에서 조인한다?

## 기타 :
# 1) json -> csv 변환

# 2) 중복제거 (csv & json)

# 3)