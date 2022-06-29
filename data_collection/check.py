from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep
from datetime import datetime
import json

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

print(len(isbn_lst))