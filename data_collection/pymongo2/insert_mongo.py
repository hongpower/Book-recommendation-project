from pymongo import MongoClient
import json

client = MongoClient("mongodb://seongheon:%40cshun1006@59.6.7.229:27018")

db = client.book


final_lst = list()

with open("DOC2VEC_SIM_NOVEL_FINAL.json", 'r') as f:
    books = json.load(f)['books']
    key_lst = list(books.keys())
    for i in range(len(books)):
        temp = dict()
        temp['isbn13'] = key_lst[i]
        values = books[key_lst[i]]
        temp_lst = list()
        for val in values:
            temp_lst.append(val[0])
        temp['books'] = temp_lst
        final_lst.append(temp)

print(final_lst)
print(len(final_lst))
#for book in final_lst:
#    db.relative_book.insert_one(book)

#print(len(db.relative_book.find()))