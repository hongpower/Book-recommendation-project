import json

# yes24 reviews의 yes24_all_장르_reviews.json 불러오기

genre_name = "essay"
reviews_path = "/Users/jisu/Desktop/project/book_recommendation_project/yes24_reviews/"
file_name = "yes24_all_" + genre_name + "_reviews.json"

with open(reviews_path + file_name, 'r') as f:
    data = json.load(f)['books']

print(genre_name + ' isbn 개수 : ', len(data))