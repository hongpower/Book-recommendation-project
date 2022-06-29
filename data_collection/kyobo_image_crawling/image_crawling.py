import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

print("시작 시간 :", datetime.now())
genre_lst = ['essay']
img_urls = []
cnt = 0
cnt2 = 0
# img id CoverMainImage 의 src 가져오면댐

try:
    for genre in genre_lst:
        with open('../data/all_' + genre + '_ids.json') as f:
            books = json.load(f)['all_books']
            print(len(books))
            for book in books :
                if cnt%700 == 0:
                    time.sleep(100)
                    print("1000개째 하는중")
                if cnt2 == 300:
                    print('100개', datetime.now())
                    print(book)
                temp = dict()
                url = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + book['item_id'] + "&start=wz&ptid=9&utm_source=aladin&utm_medium=wizard&utm_campaign=choice&utm_content=welcome"
                resp = requests.get(url)
                soup = BeautifulSoup(resp.text, 'html.parser')
                try:
                    img_url = soup.find('img', {'id' : 'CoverMainImage'})['src']
                    if img_url == "https://image.aladin.co.kr/img/shop/2018/img_no.jpg":
                        continue
                except:
                    continue
                temp['item_id'] = book['item_id']
                temp['cover'] = img_url
                cnt += 1
                cnt2 += 1
                img_urls.append(temp)

except Exception as e:
    print('실패')
    print(e)

final_dict = dict()
final_dict['all_books'] = img_urls
final_json = json.dumps(final_dict, ensure_ascii=False, indent="\t")

print("끝난 시간 :", datetime.now())
with open('./all_books_cover_urls.json', 'w') as f:
    f.write(final_json)



