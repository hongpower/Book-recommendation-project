import json
import pandas as pd

keyword_isbn = []
all_isbn = []
common_isbn = []
null_isbn = []

# keyword의 isbn만 뽑는다
with open('./keyword_novel_final.json', 'r') as f:
    keywords = json.load(f)['keyword']
    for keyword in keywords:
        keyword_isbn.append(keyword['isbn13'])
        

# csv 파일의 isbn만 뽑는다
df = pd.read_csv('./all_novels_data.csv', encoding='utf-8', low_memory=False, lineterminator='\n')
for row in df['isbn13']:
    all_isbn.append(row)

# 공통열만 뽑는다
for row in keyword_isbn:
    if row == None:
    if row in all_isbn:
        common_isbn.append(row)
        

print(common_isbn)
print(len(common_isbn))
