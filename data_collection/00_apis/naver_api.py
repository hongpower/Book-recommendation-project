import os
import sys
import urllib.request
import json
import re

client_id = "KKiYfv2vsBYGZ0PTUb3Z"
client_secret = "QiqvuyUvpn"

query = "%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C"
isbn = "9788954641630"
url = "https://openapi.naver.com/v1/search/book_adv.xml?d_isbn=" + isbn


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

response_all = response.read()
print(response_all.decode('utf-8'))

