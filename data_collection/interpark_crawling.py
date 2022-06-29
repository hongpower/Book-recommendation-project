from bs4 import BeautifulSoup
from selenium import webdriver

service = webdriver.chrome.service.Service('./driver/chromedriver')
driver = webdriver.Chrome(service=service)
url = "http://book.interpark.com/display/displaylist.do?_method=allListBook&sc.shopNo=0000400000&sc.dispNo=028005&query=%C7%D8%B8%AE%C6%F7%C5%CD"

# 각 tr에 있는 input name이 book_chkID인 애의 value의 콤마로 구분한 첫번째 값이 query에 들어가면 됌.

# 1. interpark 접속
driver.get(url)

# 2. 모든 국내도서-소설에 대한 productNumber 가져오기

# 3. 모든 국내도서-시/에세이 대한 productNumber 가져오기