import json
import csv

import urllib.request
from bs4 import BeautifulSoup

## csv/json 파일 저장 부분 자세히보기!! 특히 csv는 writeheader, append 부분!!!
# 처음할 때는 write, 인터파크 일일제한 때문에 append하는게 좋은나까 writeheader 삭제하고, append로 변경해주기
# 9000개 수정하기 !!!!!
## 인터파크는 일일 요청제한 꼭!!!!!!!!!! ㅇ
## 알라딘은 요청했을 때 제대로 이렇게 뜨는지 확인하기! ㅇ
## 책제목도 추가해야하지 않을까? ㅇ

import sys, os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from etc.keys import get_aladin_keys, get_interpark_keys

aladin_key_lst = get_aladin_keys()
interpark_key_lst = get_interpark_keys()

path_to_save = "/Users/jisu/Desktop/project/book_recommendation_project/data_rcm/"
save_file_name = "rcm_document_data"


## 함수 :
def get_total(isbn):
    global cnt
    print(cnt, isbn)
    ## 알라딘 :
    global key, item_type, options
    url = "https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey=" + key + "&itemIdType=" + item_type + "&ItemId=" + isbn + "&output=xml&" + "Version=20131101&OptResult=" + options
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, 'xml')

    if cnt%100 == 0:
        print(soup)

    dict1 = get_description(soup, isbn)
    dict2 = get_long_description(soup, isbn)
    dict3 = get_phrase(soup, isbn)
    dict4 = get_size(soup, isbn)

    ## 인터파크 키 :
    key2 = interpark_key_lst[1]

    queryType = "isbn"
    url = "https://book.interpark.com/api/search.api?key=" + key2 + "&query=" + isbn + "&queryType=" + queryType + "&encoding=utf-8&maxResults=100"
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, 'xml')

    dict5 = get_cover(soup, isbn)

    # 하나라도 pass라면 빼야할지 고민중.
    if "pass" in (dict1, dict2, dict3, dict4):
        return

    if "pass" == dict5:
        description_list_temp.append(dict1)
        long_description_list_temp.append(dict2)
        phrase_list_temp.append(dict3)
        size_list_temp.append(dict4)
        return

    # ===================================
    description_list_temp.append(dict1)
    long_description_list_temp.append(dict2)
    phrase_list_temp.append(dict3)
    size_list_temp.append(dict4)
    # ===================================

    description_list.append(dict1)
    long_description_list.append(dict2)
    phrase_list.append(dict3)
    size_list.append(dict4)
    cover_list.append(dict5)

    return

def get_description(soup, isbn):
    desc = soup.find('fullDescription').text.strip()
    contents = soup.find('toc').text.strip()
    title = soup.select_one('item > title').text

    temp = dict()
    temp['isbn13'] = isbn
    temp['title'] = title
    if desc != "":
        temp['description'] = desc
    if contents != "":
        temp['contents'] = contents
    if len(temp.keys()) == 2:
        return "pass"
    return temp

def get_long_description(soup, isbn):
    desc = soup.find('fullDescription2').text.strip()
    title = soup.select_one('item > title').text

    temp = dict()
    temp['isbn13'] = isbn
    temp['title'] = title
    if desc != "":
        temp['description2'] = desc

    if len(temp.keys()) == 2:
        return "pass"

    return temp

def get_phrase(soup, isbn):
    # phraseList의 phrase
    lst = list()
    temp = dict()
    title = soup.select_one('item > title').text

    phrases = soup.find_all('phrase')
    for p in phrases:
        lst.append(p.text.strip())

    temp['isbn13'] = isbn
    temp['title'] = title
    if len(lst) == 0:
        return "pass"
    temp['phrases'] = lst

    return temp

def get_size(soup, isbn):
    title = soup.select_one('item > title').text
    try:
        pages = soup.find('itemPage').text
    except:
        pages = ""
    try:
        weight = soup.find('weight').text
    except:
        weight = ""
    try:
        height = soup.find('sizeHeight').text
    except:
        height = ""
    try:
        width = soup.find('sizeWidth').text
    except:
        width = ""

    temp = dict()
    temp['isbn13'] = isbn
    temp['title'] = title
    """
    if pages != "":
        temp['pages'] = pages
    if weight != "":
        temp['weight'] = weight
    if height != "":
        temp['height'] = height
    if width != "":
        temp['width'] = width
    
    if len(temp.keys()) == 2:
        return "pass"
    """
    temp['pages'] = pages
    temp['weight'] = weight
    temp['height'] = height
    temp['width'] = width

    return temp

def get_cover(soup, isbn):
    ## 얘는 다른거 잊지말기!
    temp = dict()

    try:
        cover = soup.find('coverLargeUrl').text
        title = soup.select_one('item > title').text
        temp['isbn13'] = isbn
        temp['title'] = title
        temp['cover'] = cover
        return temp

    except:
        return "pass"

# ======================================================================================================================

## 알라딘 api 기본 정보 :
key = aladin_key_lst[1]

item_type = "ISBN13"
options = "FullDescription,FullDescription2,categoryIdList,Toc,ebookList,packing,Story,authors,phraseList"

##### !!!!!!!!!! 기존꺼에다가 append하고 다시 write해야하기 때문에, json만 작성
with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/description_novel.json', 'r') as f:
    prev_des_list = json.load(f)['books']

with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/long_description_novel.json', 'r') as f:
    prev_long_des_list = json.load(f)['books']

with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/phrase_novel.json', 'r') as f:
    prev_phrase_list = json.load(f)['books']

with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/description_temp_novel.json', 'r') as f:
    prev_des_temp_list = json.load(f)['books']

with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/long_description_temp_novel.json', 'r') as f:
    prev_long_des_temp_list = json.load(f)['books']

with open('/Users/jisu/Desktop/project/book_recommendation_project/data_document/phrase_temp_novel.json', 'r') as f:
    prev_phrase_temp_list = json.load(f)['books']


## aladin :
# 책 내용 가져오기(description) : isbn, isbn13, toc, Fulldescription1
# mongoDB
description_dict = dict()
description_dict_temp = dict()
description_list = prev_des_list
description_list_temp = prev_des_temp_list

# 책 내용 가져오기(full description) : isbn, isbn13, Fulldescription2
# mongoDB
long_description_dict = dict()
long_description_dict_temp = dict()
long_description_list = prev_long_des_list
long_description_list_temp = prev_long_des_temp_list

# 명언 : isbn, isbn13, phraseList
# mongoDB
phrase_dict = dict()
phrase_dict_temp = dict()
phrase_list = prev_phrase_list
phrase_list_temp = prev_phrase_temp_list

# 무게/사이즈 가져오기 : isbn, isbn13, itemPage, weight, sizeHeight, sizeWidth
# mySQL
size_dict = dict()
size_dict_temp = dict()
size_list = list()
size_list_temp = list()

## interpark :
# mySQL
cover_dict = dict()
cover_list = list()

## 1) isbn13 가져오기
### !!!!!!!!
with open('./data/document_isbn.json', 'r') as f:
    isbn13 = json.load(f)['isbn13']

#with open('./data/isbn13_rcm_document.json', 'r') as f:
#    isbn13 = json.load(f)['isbn13']

cnt = 6000
## 2) isbn13으로 검색해서 정보 추가하기

# 인터파크 : 동수 6000가능
# ~1000: 인터파크-동수, 알라딘-지수
# ~3000 : 동일

for isbn in isbn13[6000:]:
    cnt += 1
    get_total(isbn)

## 3) dict 파일로 만들기
description_dict['books'] = description_list
description_dict_temp['books'] = description_list_temp

long_description_dict['books'] = long_description_list
long_description_dict_temp['books'] = long_description_list_temp

phrase_dict['books'] = phrase_list
phrase_dict_temp['books'] = phrase_list_temp

size_dict['books'] = size_list
size_dict_temp['books'] = size_list_temp

try:
    cover_dict['books'] = cover_list
except:
    pass

var_name_lst = ['description', 'long_description', 'phrase']

var_lst = [description_dict, long_description_dict, phrase_dict]
var_temp_lst = [description_dict_temp, long_description_dict_temp, phrase_dict_temp]

csv_name_lst = ['size', 'cover']

csv_lst = [size_list, cover_list]
csv_temp_lst = [size_list_temp, cover_list]

key_lst = [('isbn13', 'title', 'pages', 'weight', 'height', 'width'), ('isbn13', 'title', 'cover')]

## 4) json, csv 파일로 만들기
# json :
for i in range(len(var_lst)):
    with open(f'./data_document/{var_name_lst[i]}_novel.json', 'w') as f:
        f.write(json.dumps(var_lst[i], ensure_ascii=False, indent='\t'))

for i in range(len(var_lst)):
    with open(f'./data_document/{var_name_lst[i]}_temp_novel.json', 'w') as f:
        f.write(json.dumps(var_temp_lst[i], ensure_ascii=False, indent='\t'))

# csv :
for i in range(len(csv_lst)):
    with open(f'./data_document/{csv_name_lst[i]}_novel.csv', 'a') as f:
        tmp_lst = csv_lst[i]
        keys = key_lst[i]
        dict_writer = csv.DictWriter(f, keys)
        #dict_writer.writeheader()
        dict_writer.writerows(tmp_lst)

for i in range(len(csv_lst)-1):
    with open(f'./data_document/{csv_name_lst[i]}_temp_novel.csv', 'a') as f:
        tmp_lst = csv_temp_lst[i]
        keys = key_lst[i]
        dict_writer = csv.DictWriter(f, keys)
        #dict_writer.writeheader()
        dict_writer.writerows(tmp_lst)
