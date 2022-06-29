from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import json

import os

final_dict = dict()
total_review_list = list()

service = webdriver.chrome.service.Service('./driver/chromedriver')
driver = webdriver.Chrome(service=service)

isbn_path = "/Users/jisu/Desktop/project/book_recommendation_project/json/"
isbn_file_name = "novel_isbn.json"

url = "http://www.yes24.com/Product/Search?domain=BOOK"
driver.get(url)

print('시작 시간 : ',datetime.now())

memory_cnt = 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

restart = False

# 1. isbn으로 찾기
with open(isbn_path + isbn_file_name, 'r') as f:
    isbn_lst = json.load(f)['isbn13']

try:
    for isbn in isbn_lst[7231:]:
        print('시작하는 isbn : ', isbn)
        sleep(0.5)
        memory_cnt += 1

        if memory_cnt % 200 == 0 :
            restart = False
            url = driver.current_url
            driver.quit()
            sleep(1)
            driver = webdriver.Chrome(service=service)
            driver.get(url)
            sleep(1)

        if restart:
            restart = False
            driver.quit()
            driver = webdriver.Chrome(service=service)
            driver.get(url)
            sleep(1)

        temp_dict = dict()
        review_lst = list()

        review_cnt = 0

        # 2. 검색칸 클릭 후 isbn으로 검색
        try:
            search_box = driver.find_element(By.XPATH, '//*[@id="query"]')

        except:
            ### !! 여기도 수정
            restart=True

        #search_box.click()
        search_box.clear()
        search_box.send_keys(isbn)
        search_box.send_keys(Keys.ENTER)

        # 3. review 페이지 들어가기
        sleep(1)

        # 팝업페이지 종료 :
        try:
            popups = driver.find_elements(By.ID, 'chk_info')
            for pop in popups:
                pop.click()
        except:
            pass

        sleep(1)

        try:
            review_page = driver.find_element(By.CSS_SELECTOR, '.rating_rvCount > a > .txC_blue')
            #print(review_page)
            review_page.click()

            """
            detail_link = driver.find_element(By.CLASS_NAME, 'gd_name').get_attribute("href")
            print(detail_link)
            driver.get(detail_link)
            sleep(2)
            """

        except:
            print('실패')
            restart = True
            continue

        sleep(0.5)

        try:
            rcm_order = driver.find_element(By.ID, 'commit_recommend')
            rcm_order.click()

        except:
            pass

        sleep(0.5)

        # 4. 페이지 수 긁어오기 :
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        ## !! 여기 추가
        try :
            pages = soup.find('em', {'id' : "txtOneCommentCount"}).text.lstrip('(').rstrip('건)')
            pages = (int(pages)//6) + 1
        except :
            pages = 0
        #print(pages)

        page_cnt = 0

        while True:
            #페이지 수만큼 긁어오되 만약 20개가 넘으면 중단하기
            if review_cnt > 20:
                break

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            comments = soup.find_all('div', class_="cmt_cont")

            try:
                for comment in comments:
                    review = comment.find('span', {'class' : 'txt'}).text
                    review_lst.append(review)
                    review_cnt += 1

            except:
                pass

            try:
                new_pages = driver.find_elements(By.CSS_SELECTOR, '#infoset_oneCommentList > .rvCmt_sort:nth-child(2) > .rvCmt_sortLft > .yesUI_pagenS > .num')
                new_pages[page_cnt].click()

            except:
                break

            page_cnt +=1
            sleep(1)

        print(isbn, 'length_review : ', len(review_lst), '횟수' , memory_cnt)
        temp_dict['isbn13'] = isbn
        temp_dict['reviews'] = review_lst

        total_review_list.append(temp_dict)
        sleep(1)


except:
    print('강제종료이지만 여기까지는 저장할게')

final_dict['books'] = total_review_list
print('끝난 시간 : ', datetime.now())
print(final_dict)

with open('yes24_reviews/yes24_novel_reviews_7231_end.json', 'w') as f:
    json_dict = json.dumps(final_dict, indent='\t', ensure_ascii=False)
    f.write(json_dict)



# 5992에 시작해 329했고 시작하는건 9791160401066 <- 이거 못하고죽음
# 6321부터 6321+ 53개했으니까 6374까지
# 6374부터 6400까지 완료
# 6400부터 6442는 조금 고민해봐야할듯 아냐 일단 들고가자
# 6442부터 8000까지 practice라서 자유
# 6442 + 789 -> 7231부터 다시작작