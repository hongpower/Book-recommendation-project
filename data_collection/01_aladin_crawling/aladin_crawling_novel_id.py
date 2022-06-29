## 알라딘에서 책아이디(알라딘고유), 책제목, 리뷰갯수 크롤링하는 코드

# 최종 결과 모습 :
# json : {'all_books' : [{'item_id' : "값"}, {'title' : "값"}, {"review_cnt" : "값"}]}

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from time import sleep
from datetime import datetime
import json

import os

# 크롤링 끝나면 알림음 울리기:
def beepsound():
    for _ in range(5):
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')

final_dict = dict()
final_list = list()

service = webdriver.chrome.service.Service('./driver/chromedriver')
driver = webdriver.Chrome(service=service)

print('시작시간 : ', datetime.now())
## 리뷰순 url :
#url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=4&page=1&Stockstatus=1&PublishDay=84&CID=1&SearchOption=#"

## 등록일순 url :
#url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=6&page=1&Stockstatus=1&PublishDay=84&CID=1&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#"

## 등록일순 1000개씩 보여주는 url :
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=1000&ViewType=Detail&PublishMonth=0&SortOrder=6&page=1&Stockstatus=1&PublishDay=84&CID=1&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#"
driver.get(url)

## 모든 책에 대한 정보 크롤링하기(국내도서-소설/시/희곡에서 등록일 순으로 정렬한 후에 모든 책 크롤링)
driver.implicitly_wait(0.5)
sleep(0.5)

# 마지막 페이지로 이동하기
driver.find_element(By.CSS_SELECTOR, '.numbox_last > .numoff').click()
soup = BeautifulSoup(driver.page_source, 'html.parser')

call_cnt = 1
cnt = 1

while True:
    # 메모리를 비우기 위해 매 페이지마다 드라이버 reboot:
    if cnt % 1 == 0:
        url = driver.current_url
        driver.quit()
        sleep(1)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        sleep(1)

    # 페이지바의 페이지 길이만큼 반복 (페이지바가 2개라서 2로 나눔)
    page_length = int(len(driver.find_elements(By.CSS_SELECTOR, '.numbox'))/2)

    # 페이지 하나로 들어가기 :
    for j in range(page_length-1, -1, -1):

        page = driver.find_elements(By.CSS_SELECTOR, '.numbox')[j]
        page.click()

        # class이름이 ss_book_box인 div 태그의 itemid 속성값 가져오기
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result = soup.find_all('div', class_='ss_book_box')

        for book in reversed(result):
            temp = dict()

            # 책 id 추가 :
            temp['item_id'] = book.attrs['itemid']

            # 책 이름 추가 :
            temp['title'] = book.find('a', class_='bo3').text

            # ul의 마지막 li의 a태그는 리뷰수를 지칭(리뷰가 없으면 해당 태그 없음)
            review_cnt = book.find('ul').find_all('li')[-1].find('a')

            # 리뷰가 있을 때는 :
            if review_cnt != None:
                temp['review_cnt'] = int(review_cnt.text)

            call_cnt += 1
            final_list.append(temp)
        print(call_cnt, datetime.now())
        sleep(0.3)
    cnt += 1
    print(datetime.now(), cnt)
    print('------------------------------------------')

    # 페이지바의 모든 페이지를 건너갔으면 10 페이지 전으로 이동
    try:
        driver.find_element(By.CSS_SELECTOR, '.numbox_pre > .numoff').click()

    except:
        break

# 끝나면 소리 출력 :
beepsound()
sleep(60)
#pkill chrome

driver.quit()

final_dict['all_books'] = final_list
json_dict = json.dumps(final_dict, ensure_ascii=False)

print('루프 종료시간 : ', datetime.now())
print('총 건너간 책 수 : ', call_cnt)

with open('../data/all_novel_ids.json', 'w', encoding='utf-8') as f:
    f.write(json_dict)

print('종료시간 : ', datetime.now())


