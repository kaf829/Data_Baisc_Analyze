import requests
import xml.etree.ElementTree as ET
import pandas as pd

# ✅ 인코딩된 키 사용
service_key = "blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"

# ✅ API URL
url = (
    f"http://apis.data.go.kr/3460000/suseongfpa/viewdaypopudetail"
    f"?serviceKey={service_key}"
    f"&startYear=2023"
    f"&startBungi=4"
    f"&resultType=xml"
    f"&size=100"
    f"&Page=1"
)

# ✅ 요청
response = requests.get(url)

# ✅ 응답 상태 확인
print("✅ 상태코드:", response.status_code)

if response.status_code == 200:
    root = ET.fromstring(response.content)

    # ✅ <items> 태그 여러 개 추출
    items = root.findall(".//items")

    data = []
    for elem in items:
        data.append({
            "cctvUid": elem.findtext("cctvUid"),
            "cctvNm": elem.findtext("cctvNm"),
            "lat": elem.findtext("lat"),
            "lon": elem.findtext("lon"),
            "cctvCount": elem.findtext("cctvCount")
        })

    if data:
        df = pd.DataFrame(data)
        df.to_csv("cctv_result.csv", index=False, encoding="utf-8-sig")
        print("📁 CSV 저장 완료: cctv_result.csv")
    else:
        print("⚠️ <items> 태그는 있었지만 데이터 파싱 실패")
else:
    print("❌ 요청 실패:", response.status_code)
