import requests
from bs4 import BeautifulSoup

url = "https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance"

# 字串轉換成字典
headers_str = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-CN;q=0.5
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 429
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=0000C7fHhSMtmqZ5hVI9DNwrgby:14iier93p; cookiesession1=627EFD003N3DGQEHFVOP20L0APPN4546
Host: web.pcc.gov.tw
Origin: https://web.pcc.gov.tw
Referer: https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'''

headers = {}
                    # 以換行切割
for row in headers_str.split("\n"):
                    # 以冒號切割                
    headers[row.split(": ")[0]] = row.split(": ")[1]


post_data_str = '''method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 111/01/25
awardAnnounceEndDate: 111/01/25
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢'''

post_data = {}
for row in post_data_str.split("\n"):
    post_data[row.split(": ")[0]] = row.split(": ")[1]

res = requests.post(url, headers = headers, data = post_data)
soup = BeautifulSoup(res.text, "html.parser")

titles = soup.select('td[align = "left"]')

# print(titles)

for title in titles:
    try:
        print(title.u.text)
        print("https://web.pcc.gov.tw/tps/" + title.a["href"])
    except AttributeError:
        pass