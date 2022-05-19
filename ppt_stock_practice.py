import requests
from bs4 import BeautifulSoup

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

url = "https://www.ptt.cc/bbs/Stock/index.html"

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

titles = soup.select('div[class="title"]')

for title in titles:
    try:
        print(title.a.string)
        print("https://www.ptt.cc" + title.a["href"])
    except AttributeError as e:
        pass
    print()