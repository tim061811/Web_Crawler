import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    # "cookie" : "over18=1"
    }

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

# 使用session連線設定cookies
ss = requests.session()
ss.cookies["over18"] = "1"

# response = requests.get(url, headers=headers)
response = ss.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select('div[class="title"]')

for title in titles:
    # print(title.a.text)
    # print("https://www.ptt.cc" + title.a["href"])
    # print()

    # 文章網址
    article_url = "https://www.ptt.cc" + title.a["href"]

    # 請求文章內容
    article_res = ss.get(article_url, headers=headers)
    article_soup = BeautifulSoup(article_res.text, "html.parser")
    article_content = article_soup.select('div[id="main-content"]')[0].text
    
    push_up = 0
    push_down = 0
    
    
    print(article_content)