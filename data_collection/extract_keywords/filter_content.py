import json
import csv

genre_lst = ['novel', 'document', 'essay']
cnt = 1
col = []

for genre in genre_lst:
    print(cnt)
    temp_lst = []

    with open('../kyobo_image_crawling/' + genre + '/isbn13.json') as f:
        isbn13 = json.load(f)['isbn13']

    with open("all_desc.csv", "r") as f:
        desc = csv.reader(f)
        for row in desc:
            if cnt == 1:
                col = [d for d in row]
                cnt += 1
            if row[0] in isbn13:
                temp_lst.append(row)
                cnt += 1

    with open('./desc&content_' +genre+'.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(col)
        write.writerows(temp_lst)

print(cnt)
