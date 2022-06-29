import pandas as pd
import json

path_all_data = "/Users/jisu/Desktop/project/book_recommendation_project/data/"
all_data_file_name = "all_essay_data.csv"

path_save_isbn = "/Users/jisu/Desktop/project/book_recommendation_project/rcm/"
isbn_file_name = "isbn13_rcm_essay.json"

pd.set_option('display.max_rows',20)
pd.set_option('display.max_columns',30)
# 변수 생성:
isbn13_dict = dict()

df = pd.read_csv(path_all_data + all_data_file_name, encoding='utf-8', low_memory=False, lineterminator='\n')

print(df.dtypes)
print(len(df))
print()

df = df.astype({'review_cnt': int})
print(df.dtypes)

# isbn13이 0 * 13개인 책 + review가 5개 이상이고 별점이 8점이상인 책은 21권
print(df[(df['isbn13'] == "0000000000000") & (df['review_cnt'] >= 5) & (df['score'] >= 8)])

# 성인물 개수 : 12만개 기준 2745개
condition2 = (df[(df['adult'] == True)])

# categoryName이 null인 것들 count : 5개
null_category = df[df['category_name'].isnull()]

# category_name이 Not described인 것들 : 6개
not_described_category = df[df['category_name'].str.contains('Not described', na=False)]

# categoryName중 라이트노벨 들어가있으면 제외 : 171개
lightnovel = df[df['category_name'].str.contains('라이트노벨', na=False)]

print('=====================================')

# 조건들 총합
# 1) categoryName이 null or Not described이 아니고 '라이트노벨'은 제외 ( ->119807)
categories = ['라이트노벨', 'Not described']
categories = '|'.join(categories)
condition_category = df['category_name'].str.contains(categories, na=False)

condition_null_category = df['category_name'].isnull()

df = df.drop(df[(condition_category) | (condition_null_category)].index)
print(df)

# 2) 리뷰수가 5개 이상일 것 (119807 -> 17150으로 변환)
condition_review = (df['review_cnt'] >= 5)
df = df[condition_review]
print(df)

# 3) 성인물은 제외하기 (17150 -> 17159으로 변환)
condition_adult = (df['adult'] == False)
df = df[condition_adult]
print(df)

# 4) 평점은 8점 이상 (17159 -> 15381으로 변환)
condition_score = (df['score'] >= 8)
df = df[condition_score]
print(df)

# 5) ISBN13이 0 * 13이면 빼기 (15381 -> 15360으로 변환)
condition_isbn = df[(df['isbn13'] == "0000000000000")]
df = df.drop(condition_isbn.index)
print(df)

# 6) ISBN13이 nan인 경우 빼기 ( 15360 -> 15274으로 변환)
df = df.dropna(axis='index', subset="isbn13")
print(df)

# 7) pubdate가 1973년부터있는데 어떻게하지?
"""
condition_pubdate = (df['pubdate'])
df = df.sort_values(by=['pubdate'])
print(df['pubdate'])
"""

# 번외 : translator의 개수
#print(df[df['translator'].str.contains(',', na=False)]['translator'])

isbn13_rcm = list(df['isbn13'])

# 최종 : 15274
print(len(isbn13_rcm))

isbn13_dict['isbn13'] = isbn13_rcm
json_isbn13 = json.dumps(isbn13_dict, ensure_ascii=False)

#with open(path_save_isbn + isbn_file_name, 'w') as f:
#    f.write(json_isbn13)



