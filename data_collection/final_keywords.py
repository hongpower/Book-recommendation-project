## 최종 isbn으로 필요한 키워드만 추출
# isbn13 final만 있으면됌.

import json

genre = "essay"
path_final_isbn = "/Users/jisu/Desktop/project/book_recommendation_project/json/"
final_isbn_name = "isbn13_"+genre+".json"
keyword_name = "kyobo_"+genre+"_keyword.json"

with open(path_final_isbn + final_isbn_name, 'r') as f:
    temp = json.load(f)['isbn13']

with open(path_final_isbn + keyword_name, 'r') as f:
    keywords = json.load(f)['books']

final_lst = list()
final_dict = dict()

for isbn in temp:
    for keyword in keywords:
        if keyword['isbn13'] == isbn:
            final_lst.append(keyword)

final_dict['keyword'] = final_lst

with open(path_final_isbn + 'final_' + genre + '_keyword.json', 'w') as f:
    json_dict = json.dumps(final_dict, ensure_ascii=False, indent="\t")
    f.write(json_dict)






