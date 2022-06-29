import json

new_list = list()
new_dict = dict()

with open('data/all_document_data.json', 'r') as f:
    all_books = json.load(f)['all_books']

"""
for book in all_books:
    book["category_name"] = book.pop("categoryName")
    try:
        book["author_info"] = book.pop("authorInfo")
        book["author_photo"] = book.pop("authorPhoto")
    except:
        pass
    new_list.append(book)
"""

for book in all_books:
    try:
        book["author_info"] = book.pop("author_info'")
    except:
        pass
    new_list.append(book)

new_dict['all_books'] = new_list
new_json = json.dumps(new_dict, ensure_ascii=False, indent='\t')
with open('data/all_document_data.json', 'w', encoding='utf-8') as f:
    f.write(new_json)