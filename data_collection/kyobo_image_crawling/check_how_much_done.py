# 크롤링한 img 중에 얼마나 안됐는지 보기

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

genre_lst = ['novels', 'document', 'essay']
isbn_lst = []
item_id_lst = []

final_isbn_lst = []
final_item_id_lst = []
cnt = 1
cnt2 = 1

final_lst = list()
final_dict = dict()

# 2. 크롤링한 isbn13만 가져온다

with open('./rcm_books_cover_urls.json') as f:
    books = json.load(f)['all_books']
    print(len(books))
    print(books[-1])

print(len(final_isbn_lst))
print(len(final_item_id_lst))

