import requests

serviceKey = 'blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D'

url = "http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInRadius"
params = {
    'ServiceKey': serviceKey,
    'pageNo': 1,
    'numOfRows': 100,
    'radius': 100,
    'cx': 126.977962,
    'cy': 37.566535,
}

response = requests.get(url, params=params)
print(response.text)


response = requests.get(url, params=params, verify=False)
print(f'Status Code: {response.status_code}')
print(response.text)
