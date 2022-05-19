'''

from urllib import request

url = "http://httpbin.org/get"

res = request.urlopen(url)
# print("res.read() :", res.read())

print(res.read().decode("utf8"))

'''
'''

import requests

url = "http://httpbin.org/get"
res = requests.get(url)

print(res.text)

'''
'''
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)
# print(res.read().decode("utf8"))
soup = BeautifulSoup(res, "html.parser")

action = soup.findAll("div", id = "action-bar-container")

# print(action)

tmp_div = action[0].find("div")
print(tmp_div)
tmp_a = action[0].find("a")
print(tmp_a)

tmp_texe_in_a = tmp_a.text
print("Text in <a> tag: ")
print(tmp_texe_in_a)


tmp_url = tmp_a["href"]
print("url: ")
print(tmp_url)
'''
######

import pandas as pd

df = pd.DataFrame(columns=["name","age","sex"])
# print(df)

df.loc[0] = ["tim","26", "m"]
df.loc[1] = ["mumu", "26", "f"]
# print(df)

df["high"] =["160", "180"]
# print(df)

# df = df.drop(1)
# print(df)

df["name"][1] = "joslyn"
# print(df)

columns = ["coloer", "somthing"]
data = [
    ["red", "nothing"],
    ["biue", "something"]  
]

new_df = pd.DataFrame(columns=columns, data=data)
# print(new_df)

df = df.append(new_df)
# print(df)

# df = df.reset_index()
# print(df)

df = df.reset_index(drop=True)
print(df)

df.to_csv(r"./test.csv", index=0, encoding="utf-8")