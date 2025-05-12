from bs4 import BeautifulSoup
import urllib.request as MYURL

# 로컬 XML 파일 열기
jURL = "file:./joins.xml"
response = MYURL.urlopen(jURL)
soup = BeautifulSoup(response, "html.parser")

# "item"으로 수정
for item in soup.find_all("item"):
   #title = item.find("title")
   # description = item.find("description")

    print("title:", item.title.string if item.title else "None")
    print("description:", item.description.string if item.description else "None")
