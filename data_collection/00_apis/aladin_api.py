import requests

# 설명주소 : https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit
# 설명주소2 : https://blog.aladin.co.kr/openapi/5353304

key = "ttbnweda1120001"
#key = "ttbjisu37021357001"
#item_type에는 ItemId, ISBN13
item_type = "ISBN13"

#ISBN13 :
item_id = "9788930106481"

options = "FullDescription,FullDescription2,categoryIdList,Toc,ebookList,packing,Story,authors,phraseList"
url = "https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey="+key+"&itemIdType="+item_type+"&ItemId="+item_id+"&output=xml&" + "Version=20131101&OptResult=" + options
resp = requests.get(url)
print(resp.text)
