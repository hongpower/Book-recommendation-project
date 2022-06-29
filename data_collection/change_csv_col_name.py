import pandas as pd

df = pd.read_csv('/book_recommendation_project/data/all_essay_data.csv', encoding='utf-8', low_memory=False, lineterminator='\n')
print(df)
print(df.dtypes)

df = df.rename(columns={'categoryName' : 'category_name', 'authorInfo' : 'author_info', 'authorPhoto' : 'author_photo'})
df = df.rename(columns={'author_info\r' : 'author_info'})
df = df.rename(columns={'author_photo\r' : 'author_photo'})
df = df.rename(columns={'review_cnt\r' : 'review_cnt'})
print(df.dtypes)
df.to_csv("/Users/jisu/Desktop/project/book_recommendation_project/data/all_essay_data.csv", header=True, index=False)

