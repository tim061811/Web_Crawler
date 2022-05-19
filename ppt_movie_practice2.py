# 多頁爬取
import requests
from bs4 import BeautifulSoup

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


# 方法一
page = 2570

while page >= 2565:
    url = "https://www.ptt.cc/bbs/movie/index{}.html".format(page)

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.select('div[class="title"]')

    for title in titles:
        print(title.a.string)
        print("https://www.ptt.cc" + title.a["href"])
        print()

    page -= 1


# 方法二
for i in range(4):
    url = "https://www.ptt.cc/bbs/movie/index.html"

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.select('div[class="title"]')

    for title in titles:
        print(title.a.string)
        print("https://www.ptt.cc" + title.a["href"])
        print()

    next_page = soup.select('a[class="btn wide"]')[1]["href"]
    next_page = "https://www.ptt.cc" + next_page
    url = next_page