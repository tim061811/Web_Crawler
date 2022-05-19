import requests
from bs4 import BeautifulSoup
import os

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

# 創建資料夾存放文字檔
resource_path = r'./res'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)



for i in range(1):
    url = "https://www.ptt.cc/bbs/movie/index.html"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.select('div[class="title"]')

    for title in titles:
        try:
            print(title.a.string)
            print("https://www.ptt.cc" + title.a["href"])

            # 文章網址
            article_url = "https://www.ptt.cc" + title.a["href"]
            article_title = title.a.text
            # 對文章網址提出請求
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, "html.parser")
            # 宣告一個違章內容字串的變數
            article_content = article_soup.select('div[id="main-content"]')[0].text.split("--")[0]
            # 印出文章看看
            # print(article_content)

            # 將文字檔與該篇文章標題命名並存於資料夾內
            with open(r'%s/%s.txt'%(resource_path, article_title), "w", encoding="utf-8") as w:
                w.write(article_content)
            print()
        except FileNotFoundError as e:
            pass
        except OSError as e:
            pass

    next_page = soup.select('a[class="btn wide"]')[1]["href"]
    next_page = "https://www.ptt.cc" + next_page
    url = next_page