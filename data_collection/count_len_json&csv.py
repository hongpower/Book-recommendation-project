import json
import pandas as pd

## json
with open('json/final_novel_keyword.json', 'r') as f:
    lst = json.load(f)['keyword']
    print('json 중복 제거 후 길이 :', len(lst))
"""
with open('./data/test_result.json', 'r') as f:
    lst = json.load(f)['all_books']
    print('json 중복 제거 전 길이 :', len(lst))
"""

## pandas
# csv파일 내에 개행문자인 '\r'을 기준으로 줄을 나눠서 오류가 생기기 때문에 lineterminator 작성해줌
df = pd.read_csv('/book_recommendation_project/data/all_essay_data.csv', encoding='utf-8', low_memory=False, lineterminator='\n')
print('csv 중복 제거 후 길이 :', len(df))


df = pd.read_csv('/Users/jisu/Desktop/project/book_recommendation_project/data_rcm/size_temp_novel.csv', encoding='utf-8', low_memory=False, lineterminator='\n')
print('csv 중복 제거 후 길이 :', len(df))

"""
df = pd.read_csv('/Users/jisu/Desktop/project/book_recommendation_project/data/all_document_info2.csv', encoding='utf-8', low_memory=False, lineterminator='\n')
print('csv 중복 제거 후 길이 :', len(df))

df2 = pd.read_csv('/Users/jisu/Desktop/project/book_recommendation_project/data/test.csv', encoding='utf-8', low_memory=False)
print('csv 중복 제거 전 길이 : ', len(df2))
"""
