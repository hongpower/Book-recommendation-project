import json
import glob



reviews_path = "/Users/jisu/Desktop/project/book_recommendation_project/yes24_reviews/"
file_name = "yes24_all_essay_reviews.json"

all_data_list = list()
final_dict = dict()

# 1) 합칠 json 파일 이름 다 가져오기
name_lst = list(glob.glob(reviews_path + "yes24_essay_reviews*.json"))

# 2) all_data_list에 추가하기 (중복제거까지)
for name in name_lst:
    with open(name, 'r') as f:
        temp_list = json.load(f)['books']
        all_data_list += temp_list

# 3) all_data_list를 통합해서 가져오기
final_dict['books'] = all_data_list
print(final_dict)

final_json = json.dumps(final_dict, ensure_ascii=False, indent="\t")
with open(reviews_path + file_name, 'w') as f:
    f.write(final_json)
