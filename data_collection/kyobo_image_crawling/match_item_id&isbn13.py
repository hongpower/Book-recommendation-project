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

# 1. all_essay_data에서 item_id와 isbn13을 가져온다
for genre in genre_lst:
    with open('./all_' + genre + '_data.json') as f:
        books = json.load(f)['all_books']
        for book in books:
            isbn_lst.append(book['isbn13'])
            item_id_lst.append(book['item_id'])



# 2. rcm_isbn13에 포함되는 isbn13만 가져온다
genre_lst2 = ['essay']
for genre in genre_lst2:
    break_point = True
    with open('./phrase_novel.json') as f:
        books = json.load(f)['books']
        print(len(books))
        for book in books:
            temp = dict()
            isbn13 = book['isbn13']
            if break_point:
                if isbn13 != "9791157526369":
                    cnt += 1
                    continue
                break_point = False
                cnt2 += 1

            isbn_idx = isbn_lst.index(isbn13)
            if isbn_idx == -1:
                continue
            final_isbn_lst.append(isbn_lst[isbn_idx])
            final_item_id_lst.append(item_id_lst[isbn_idx])

print(len(final_isbn_lst))
print(len(final_item_id_lst))

# 3. 해당 item_id만 request를 보내고 저장할 때는 isbn과 img로 저장한다
try:
    for i in range(len(final_isbn_lst)):
        if cnt == 5000:
            time.sleep(300)
        if cnt%500 == 0:
            time.sleep(100)
            print(isbn13)
            print('500번째 달성')
        if cnt2%20 == 0:
            print('제외된거 20개째')
        temp_dict = dict()
        isbn13 = final_isbn_lst[i]
        item_id = final_item_id_lst[i]
        url = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + item_id + "&start=wz&ptid=9&utm_source=aladin&utm_medium=wizard&utm_campaign=choice&utm_content=welcome"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        try:
            img_url = soup.find('img', {'id': 'CoverMainImage'})['src']
            if img_url == "https://image.aladin.co.kr/img/shop/2018/img_no.jpg":
                continue
        except:
            cnt2 += 1
            continue
            print(cnt2)

        temp_dict['isbn13'] = isbn13
        temp_dict['item_id'] = item_id
        temp_dict['large_cover'] = img_url
        final_lst.append(temp_dict)
        cnt += 1

except Exception as e:
    print('실패')
    print(e)


final_dict['all_books'] = final_lst
final_json = json.dumps(final_dict, ensure_ascii=False, indent="\t")

print("끝난 시간 :", datetime.now())
with open('./rcm_books_cover_urls_4123.json', 'w') as f:
    f.write(final_json)
