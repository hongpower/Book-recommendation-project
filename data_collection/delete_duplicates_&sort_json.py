import json
from json import JSONDecoder
from collections import OrderedDict

## 로우 순서도 바꼈고, 컬럼순서도 바꼈다


# 2) 같은 key끼리 sort한 후에 중복은 제거하고 다시 list로 변경해서 item_id기준으로 정렬한 후 return
def remove_dup_dicts(lst):
    """기존방식
    temp = [json.dumps(d, sort_keys=True) for d in lst]
    final = set(temp)
    return [json.loads(s) for s in final]
    """
    set_of_jsons = {json.dumps(d) for d in lst}
    arr = [json.loads(d) for d in set_of_jsons]
    arr = sorted(arr, key=lambda k: int(k['item_id']), reverse=False)
    return arr
    """ 수정됐지만 믹스돼서 취소 :
    set_of_jsons = {json.dumps(d) for d in lst}
    arr = [json.loads(d, object_pairs_hook=OrderedDict) for d in set_of_jsons]
    arr = sorted(arr, key=lambda k: int(k['item_id']), reverse=False)
    return arr
    """

# 1) all_books의 value인 리스트만 추출
with open('./data/test_result.json', 'r') as f:
    all_books = json.load(f)['all_books']
    final_list = remove_dup_dicts(all_books)

final_dict = dict()
final_dict['all_books'] = final_list

# 3) json 객체로 변환 후 저장
final_json = json.dumps(final_dict, ensure_ascii=False, indent='\t')
with open('data/120000_2.json', 'w') as f:
    f.write(final_json)