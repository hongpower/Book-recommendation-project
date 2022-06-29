# 자기계발 아닌 애들은 다빼라
import json


with open('data/all_document_data.json', 'r') as f:
    temp = json.load(f)['all_books']

new_lst = []

# 9998까지 포함시키기
for book in temp[:9999]:
    new_lst.append(book)

final_dict = dict()
final_dict['all_books'] = new_lst

final_json = json.dumps(final_dict, ensure_ascii=False)

with open('./data/all_document_info2.json', 'w') as f:
    f.write(final_json)

