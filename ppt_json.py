import requests
import json
# 下載圖片模組
from urllib import request
import os

# 創建資料夾
pic_path = r'./dcard_photos'
if not os.path.exists(pic_path):
    os.mkdir(pic_path)

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }

url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=237962877"
response = requests.get(url, headers=headers)
json_str = response.text
json_data = json.loads(json_str)

# 取得最後一篇文章的id
# last_id = json_data[len(json_data)-1]["id"]

for titles in json_data:
    print(titles["title"])
    print("https://www.dcard.tw/f/photography/p/" + str(titles["id"]))

    # 將圖片網址取出並印出
    for n, img_url in enumerate(titles["mediaMeta"]):
        tmp_img_url = img_url["url"]
        location = os.path.join(pic_path + "/%s_%s.jpg"%(titles['title'].replace('/',''), n))
        print(('\t' + tmp_img_url), end = "")
        request.urlretrieve(tmp_img_url, location)
        print('\tDone.')
    print()

                                                                                # 將網址(id)更換成新的
# url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=%s"%(last_id)
