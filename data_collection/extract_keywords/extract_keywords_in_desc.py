import csv
import json

isbn_lst = list()
cnt = 0
final_lst = list()
final_dict = dict()
genre = "novel"

# 1. desc의 isbn13만 가져온다
with open("desc.csv", 'r') as f:
    desc = csv.reader(f)
    for row in desc:
        cnt += 1
        if cnt == 1:
            continue
        isbn_lst.append(row[0])

# 2. 있는 isbn만 추가한다
with open("final_"+genre+"_keyword.json", "r") as f:
    keywords =  json.load(f)['keyword']

for keyword in keywords:
    if keyword['isbn13'] in isbn_lst:
        final_lst.append(keyword)
        isbn_lst.remove(keyword['isbn13'])

print(len(final_lst))
# json 파일로저장
final_dict['keyword'] = final_lst

final_dict = json.dumps(final_dict, ensure_ascii=False, indent='\t')
with open('keyword_' + genre + ".json", 'w') as f:
    f.write(final_dict)