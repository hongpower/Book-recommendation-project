import pandas as pd

df = pd.read_csv('/Users/jisu/Desktop/project/book_recommendation_project/data/test.csv', encoding='utf-8', low_memory=False)
print(df)

## 1. row 이름에 isbn13 들어가있는경우 삭제
position = df[df['isbn13'].str.contains('isbn13', na=False)].index
print(position)
df = df.drop(position)
print(df)

## 2. 중복제거
# 특정 컬럼 기준으로 중복제거 :
df2 = df.drop_duplicates(subset="item_id",keep='first',inplace=False, ignore_index=True)
print(df2)

# 모든 컬럼이 같을 때 중복제거 :
df = df.drop_duplicates(subset=None, keep='first',inplace=False, ignore_index=True)
print(df)

## 3. 저장
df.to_csv("/Users/jisu/Desktop/project/book_recommendation_project/data/all_novels_data.csv", header=True, index=False)

