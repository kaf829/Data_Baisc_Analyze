import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time

# 지역코드가 들어있는 .xls 파일 읽기 (xlrd 필요)
df = pd.read_excel("./region_data.xls",engine="xlrd")

# 지역코드 컬럼명 예시로 '지역코드'라고 가정
sggu_codes = df["코드"].dropna().unique()

all_data = []

for code in sggu_codes:
    url = "http://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList"
    params = {
        "ServiceKey": "blQn7CpDK9qt6ZR+/lEbAt5Yb/0gE4k0zZpvonWxX0XWZv6MuS5TwFy+zmkDk0ZvFunmtNIN5sFnLqIlJWabrg==",
        "sgguCd": str(code),
        "dgsbjtCd": "10",      # 산부인과 진료과목 코드
        "numOfRows": 100,
        "pageNo": 1
    }

    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)
    items = root.findall(".//item")

    for item in items:
        row = {
            "지역코드": code,
            "병원명": item.findtext("yadmNm"),
            "주소": item.findtext("addr"),
            "전화번호": item.findtext("telno"),
            "요양기관번호": item.findtext("ykiho")
        }
        all_data.append(row)

    time.sleep(0.3)  # 과도한 요청 방지

# 최종 결과 저장
df_result = pd.DataFrame(all_data)
df_result.to_csv("산부인과_병원목록_통합.csv", index=False, encoding="utf-8-sig")
