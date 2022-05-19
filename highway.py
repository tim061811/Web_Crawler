import requests
from bs4 import BeautifulSoup
import json

payload = {

"SearchType":"S",
"Lang":"TW",
"StartStation":"NanGang",
"EndStation":"ZuoYing",
"OutWardSearchDate":"2021/05/12",
"OutWardSearchTime":"15:00",
"ReturnSearchDate":"2021/05/12",
"ReturnSearchTime":"15:00",
"DiscountType":""
    
}


url = 'https://www.thsrc.com.tw/TimeTable/Search'
response = requests.post(url, data = payload)
#print(response.text)

result = json.loads(response.text)
#print(result['data']['DepartureTable']['TrainItem'])

for i in result['data']['DepartureTable']['TrainItem']:
    print('Train number: {}, Departure time: {}, Destination time: {}'.format(i['TrainNumber'], i['DepartureTime'], i['DestinationTime']))