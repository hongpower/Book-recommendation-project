## 크롤링 한 파일을 기준으로
import json
import csv

import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

import pandas as pd

## 조심할 것 :
# 1. json은 쌍따옴표
# 2. json할 때 같은 키끼리 합치기 x
# 3. csv는 header빼기
# 항상 test하고 진행하기!

import sys, os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from etc.keys import get_aladin_keys

aladin_key_lst = get_aladin_keys()

## !! 추가
temp_cnt = 0

# 1) id 있는 파일
path_id = "/book_recommendation_project/data/"
id_file_name = "all_document_ids.json"

# 2) 저장할 기존 json파일 / append할 json 파일
path_save_json = "/book_recommendation_project/data/"
json_file_name = "all_document_data.json"

# 3) 저장할 기존 csv파일
path_save_csv = "/book_recommendation_project/data/"
csv_file_name = "all_document_data.csv"

# 4) 컬럼 지정파일
path_meta = "/book_recommendation_project/etc/"
meta_name = "all_meta.csv"

def call_api(item_id, review_cnt):

    # item_id로 api 요청하기
    temp_dict = {}

    key = aladin_key_lst[1]

    item_type = "ItemId"
    options = "FullDescription,FullDescription2,categoryIdList,Toc,ebookList,packing,Story,authors,phraseList"
    url = "https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey=" + key + "&itemIdType=" + item_type + "&ItemId=" + item_id + "&output=xml&" + "Version=20131101&OptResult=" + options
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, 'xml')
    try:
        totalResults = soup.find('totalResults').text

    except:
        print('pass1', item_id)
        return "pass"

    if totalResults == "1":

        # isbn13이 없는 경우는 "0000000000000"으로 대체
        try:
            temp_dict["isbn13"] = soup.find('isbn13').text

        except:
            temp_dict["isbn13"] = '0000000000000'

        temp_dict["isbn"] = soup.find('isbn').text
        temp_dict["item_id"] = item_id
        temp_dict["title"] = soup.select_one('item > title').text

        # category 등록이 안된 경우는 None(오류나서) -> 0으로 대체
        try:
            temp_dict["category_name"] = soup.select_one('item > categoryName').text

        except:
            temp_dict["category_name"] = "Not described"

        temp_dict["cover"] = soup.find('cover').text
        temp_dict["publisher"] = soup.find('publisher').text
        temp_dict["pubdate"] = soup.select_one('item > pubDate').text
        temp_dict["price"] = soup.select_one('priceStandard').text

        # authors라는 하나의 태그 안에 여러 author 태그가 포함되어있음
        try:
            authors = soup.find('authors').find_all('author')
        except:
            print('pass2', item_id)
            return "pass"

        # 작가만 있다면 :
        if len(authors) == 1:
            temp_dict["author"] = authors[0].find('authorName').text
            temp_dict["author_info"] = authors[0].find('authorInfo').string
            temp_dict["author_photo"] = authors[0].find('authorPhoto').text
            temp_dict["translator"] = None

        # 작가가 여러명이거나 번역가가 있는 경우 :
        else:
            # 번역가는 여러명일 수 있기 때문에 리스트로 작성
            translator = []

            for person in authors:
                identity = person.find('authorType').text

                if identity == "author":
                    temp_dict["author"] = person.find('authorName').text
                    ## author_info
                    temp_dict["author_info"] = person.find('authorInfo').string
                    ## author_photo
                    temp_dict["author_photo"] = person.find('authorPhoto').text

                elif identity == "translator":
                    translator.append(person.find('authorName').text)

            temp_dict['translator'] = translator

        temp_dict["adult"] = soup.find('adult').text
        temp_dict["score"] = soup.find('customerReviewRank').text
        temp_dict["review_cnt"] = review_cnt
        return temp_dict

    else:
        print('결과 중복', item_id)
        return "pass"

def make_json(dic):
    final_json = json.dumps(dic, ensure_ascii=False, indent='\t')
    with open(path_save_json + json_file_name, 'w') as f:
        f.write(final_json)

def make_csv(dic):
    global temp_cnt
    temp_cnt += 1
    with open(path_save_csv + csv_file_name, 'a', newline='') as f:
        global cols
        dict_writer = csv.DictWriter(f, cols)
        #dict_writer.writeheader()
        dict_writer.writerows(dic['all_books'])

# api 시작 날짜 출력 :
print(datetime.now())

final_list = list()
final_dict = dict()
recent_dict = dict()

with open(path_id + id_file_name, 'r') as f:
    all_books = json.load(f)['all_books']

with open(path_save_json + json_file_name, 'r') as f:
    new_books = json.load(f)['all_books']

cols = pd.read_csv(path_meta + meta_name, low_memory=False).columns

# 몇 개의 책을 등록했는지 확인하기 위함 :
cnt = 0

# id 자체의 오류인데 result가 나와서 오류 뜨는 아이디는 여기에 작성해서 후에 제외시킴 :
error_ids = ['668478']

for i in range(0,30000, 10000):
    final_list = list()
    for book in all_books[i:i+10000]:
        cnt += 1

        ## 1) all_books의 value를 가져와서 하나씩 돌며 item_id를 가져온다. (error id에 포함돼있으면 loop stop)
        book_id = book['item_id']

        if book_id in error_ids:
            continue

        print(cnt, book_id)
        # 리뷰가 없는 책은 0으로
        try:
            review_cnt = book['review_cnt']
        except:
            review_cnt = 0

        ## 2) item_id를 기준으로 open api 요청한다
        temp_dict = call_api(book_id,review_cnt)

        # 결과값이 2개 또는 pass인 경우엔:
        if temp_dict == "pass":
            continue

        ## 3) 임시 list에 저장한다 -> 변경해서 바로 기존 list에 저장
        ### !!!
        final_list.append(temp_dict)
        new_books.append(temp_dict)

    ## 4) json & csv 파일로 만든다

    # new_books는 새로운 책이 들어올 때마다 거기에 append 해야하기 때문에 킵하고, temp_books라는 이름으로 새로 정렬해서 value로 지정
    # json으로 변환해서 중복값 삭제 :
    set_of_jsons = {json.dumps(d) for d in new_books}
    # json 다시 리스트로 변환 :
    temp_books = [json.loads(d) for d in set_of_jsons]
    # 중복값 제거 :
    temp_books = sorted(temp_books, key=lambda k: int(k['item_id']), reverse=False)

    final_dict['all_books'] = temp_books
    recent_dict['all_books'] = final_list

    make_json(final_dict)
    make_csv(recent_dict)

    # 만번당 1번씩 api 호출 시간 출력:
    print(datetime.now())




