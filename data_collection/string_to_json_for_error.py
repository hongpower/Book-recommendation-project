## 기존 json 파일의 문제점:
# {'all_books' : [] ... }{'all_books' : []} 이렇게 저장돼있어서 json으로 파싱이 안돼있었음
# 여기서는 해당 파일을 모두 문자열로 바꾼 후에, all_books를 기준으로 split한 후에 최종적으로 all_books의 하나의 값으로 나오게끔 변경한 것임

import json

with open('./data/test.json', 'r') as f:

    # readlines는 리스트로 반환
    temp = f.readlines()[0]

    # 첫번째로 나오는 all_books는 {" 로 시작하기 때문에 아래 조건에 해당되지 않음
    temp = list(temp.split(']}{"all_books": ['))

    # temp가 어떻게 split됐는지 확인하기 :
    print(temp[0][-30:],'/', temp[1][-30:], '/', temp[2][-30:], '/', temp[-1][-30:])
    print(len(temp[0]), len(temp[1]))

    new = list()
    final = ''

    # 마지막에 빈 []가 있어서 그거 제외하고 문자열로 변환 :
    for t in temp[:-1]:
        new.append(t)

    # temp안에 요소들은 문자열로 넣으면 ","가 없어져서 추가
    for n in new:
        final += n
        final += ','

    # 마지막 ','는 삭제:
    final = final[:-1]

    # 마지막에는 "]}"를 추가함으로써 dictionary와 list 닫아주기 :
    final += ']}'

    # 확인 :
    print(final[:500])
    print(final[-500:])
    print(final.count("item_id"))
    print(final[8920670:8920700])

# 문자열 -> 딕셔너리로 변환 :
final_json = json.loads(final)
print(type(final_json))

# 딕셔너리 -> json 객체로 변환 :
final_json = json.dumps(final_json, ensure_ascii=False)
with open('./data/test_result.json', 'w') as f:
    f.write(final_json)