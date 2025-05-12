from config import *
import urllib.request
import json
import pandas as pd

client_id = client_id
client_secret = client_secret
snode = 'news'

query = "여행"
encText = urllib.parse.quote(query)

base = "https://openapi.naver.com/v1/search"
node = f"/{snode}.json"
parameters = f"?query={encText}&start=1&display=100"
url = base + node + parameters

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    data = json.loads(response_body.decode('utf-8'))

    items = data['items']
    print(items)

    news_list = []
    for item in items:
        news_list.append({
            'title': item['title'],
            'link': item['link'],
            'description': item['description'],
            'pubDate': item['pubDate']
        })

    df = pd.DataFrame(news_list)
    df.to_csv("여행_naver_news.csv", index=False, encoding='utf8')
    print("CSV 파일로 저장 완료!")
else:
    print("Error Code:", rescode)
