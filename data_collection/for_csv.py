import csv
import json

with open('/book_recommendation_project/data/all_essay_data.json', 'r') as f:
    lst = json.load(f)['all_books']
print(len(lst))

keys = lst[0].keys()
with open('/book_recommendation_project/data/all_essay_data.csv', 'w', newline='') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(lst)


