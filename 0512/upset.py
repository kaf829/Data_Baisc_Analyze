
import requests

url = 'http://apis.data.go.kr/6270000/dgMwData/getTopKeyword'
params ={'serviceKey' : 'blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D', 'type' : 'xml', 'gbn' : 't', 'startDt' : '20191001', 'endDt' : '20191031', 'gugun' : '중구', 'cnl' : 'dud' }

response = requests.get(url, params=params)
print(response.content)

