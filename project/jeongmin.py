import requests
import xml.etree.ElementTree as ET
import pandas as pd

# ▶ 본인의 인증키 입력
service_key = "blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"

# ▶ API URL 구성
url = f"http://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList?ServiceKey={service_key}&numOfRows=100&pageNo=1&dgsbjtCd=10"

# ▶ API 호출
response = requests.get(url)
if response.status_code == 200:
    root = ET.fromstring(response.content)

    hospitals = []
    for item in root.iter("item"):
        name = item.find("yadmNm").text if item.find("yadmNm") is not None else ""
        addr = item.find("addr").text if item.find("addr") is not None else ""
        tel = item.find("telno").text if item.find("telno") is not None else ""
        hosp_url = item.find("hospUrl").text if item.find("hospUrl") is not None else ""
        pnurs_cnt = item.find("pnursCnt").text if item.find("pnursCnt") is not None else ""
        dr_tot_cnt = item.find("drTotCnt").text if item.find("drTotCnt") is not None else ""
        hospitals.append([name, addr, tel, hosp_url, pnurs_cnt, dr_tot_cnt])

    df = pd.DataFrame(hospitals, columns=["병원명", "주소", "전화번호", "홈페이지","조산사수","암호요양기호"])
    df.to_csv("병원기본목록.csv", index=False, encoding='utf-8-sig')
    print("✅ 병원 목록 저장 완료: 병원기본목록.csv")
else:
    print("❌ API 요청 실패. 상태코드:", response.status_code)
