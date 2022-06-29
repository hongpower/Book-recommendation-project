import urllib.request
import requests
import json
from bs4 import BeautifulSoup
from xml.etree import ElementTree

# 참고 url : http://book.interpark.com/bookPark/html/bookpinion/api_booksearch.html
# https://book.interpark.com/api/search.api?key=645728B13A4958BA2A529B817B334E1F21BDE565472C0F5E8CA82186417603D9&query=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C&queryType=all&encoding=utf-8&maxResults=100

# 각 tr에 있는 input name이 book_chkID인 애의 value의 콤마로 구분한 첫번째 값이 query에 들어가면 됌.

query = "8956698074"
#isbn, productNumber
queryType = "isbn"
# 지수 :
key = "8802B6357C7CEC1DB36E8644E66A5228DD54ABDB8FABA587312F4B11C3014EB5"
# 성헌 :
key = "645728B13A4958BA2A529B817B334E1F21BDE565472C0F5E8CA82186417603D9"
# 낙원 :
key = "4DCD5F230BD3DA4D25FAE6956AF08A3B0567A759F8ED8BDB79E135B161060BF5"

url = "https://book.interpark.com/api/search.api?key="+key+"&query="+query+"&queryType="+queryType+"&encoding=utf-8&maxResults=100"

with open('data_rcm/isbn13_rcm_novel.json', 'r') as f:
    isbn13 = json.load(f)['isbn13']

lst = list()

for isbn in isbn13[-100:]:
    query = isbn
    url = "https://book.interpark.com/api/search.api?key=" + key + "&query=" + query + "&queryType=" + queryType + "&encoding=utf-8&maxResults=100"
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, 'xml')
    try:
        image = soup.find('coverLargeUrl').text
        lst.append([isbn, image])
    except:
        continue

print(lst)