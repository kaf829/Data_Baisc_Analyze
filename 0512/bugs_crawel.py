import requests
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)  # headers 추가 필요할 수 있음
html = response.text

soup = BeautifulSoup(html, 'html.parser')
print()
for link in soup.find_all('a', 'title'):
    print(link)