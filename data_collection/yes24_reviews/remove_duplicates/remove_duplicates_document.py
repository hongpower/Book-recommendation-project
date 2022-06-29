import json

def remove_duplicates(lst):
    seen = set()
    new_lst = []
    for book in lst:
        if book['isbn13'] not in seen:
            seen.add(book['isbn13'])
            new_lst.append(book)
    return new_lst
    
genre_name = "document"
reviews_path = "/Users/jisu/Desktop/project/book_recommendation_project/yes24_reviews/"
file_name = "yes24_all_" + genre_name + "_reviews.json"
new_file_name = "yes24_all_" + genre_name + "_reviews_no_duplicates.json"

final_dict = dict()

with open(reviews_path + file_name, 'r') as f:
    data = json.load(f)['books']

print(genre_name + ' isbn 개수 : ', len(data))

no_duplicate_data = remove_duplicates(data)

print(genre_name, " 중복 제거 후 isbn 개수 : ", len(no_duplicate_data))

final_dict['books'] = no_duplicate_data

final_json = json.dumps(final_dict, ensure_ascii=False, indent="\t")
with open(reviews_path + new_file_name, 'w') as f:
    f.write(final_json)