import pandas as pd
import requests
import json
import time
import os

# 네이버 API 인증 정보
client_id = "QbeZZ9QIHOY708Bij3tW"
client_secret = "qkG1DbxTky"
url = "https://openapi.naver.com/v1/datalab/search"
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
    "Content-Type": "application/json"
}

# 저장할 CSV 파일 준비
output_csv = "korea_naver_trand.csv"
if not os.path.exists(output_csv):
    pd.DataFrame(columns=['food_name', 'period', 'ratio']).to_csv(output_csv, index=False, encoding='utf-8-sig')

# 한식 메뉴 리스트 직접 입력
food_list = [
    "돼지고기 구이", "국수", "칼국수", "수제비", "소고기",
    "된장찌개", "청국장", "곱창", "막창", "내장부위",
    "제육볶음", "두루치기", "불고기", "해산물요리", "회",
    "계란찜", "계란말이", "죽", "육회", "고추장찌개",
    "돼지찌개", "전", "빈대떡", "부침개", "비빔밥",
    "물냉면", "돼지갈비", "주물럭", "양념갈비", "새우구이",
    "김치찌개", "참치찌개", "국", "탕", "간장게장",
    "양념게장", "수육", "매운탕", "해물탕", "생선구이",
    "닭갈비", "해장국", "보쌈", "비빔냉면", "설렁탕",
    "곰탕", "정식"
]

# 5개씩 나누어 API 요청
for i in range(0, len(food_list), 5):
    chunk = food_list[i:i+5]
    keyword_groups = [{"groupName": name, "keywords": [name]} for name in chunk]
    body = {
        "startDate": "2024-01-01",
        "endDate": "2024-12-31",
        "timeUnit": "month",
        "keywordGroups": keyword_groups,
        "device": "mo",
        "ages": [],
        "gender": ""
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code == 200:
        result = response.json()
        temp_data = []
        for group in result['results']:
            food_name = group['title']
            for data_point in group['data']:
                temp_data.append({
                    'food_name': food_name,
                    'period': data_point['period'],
                    'ratio': data_point['ratio']
                })
        pd.DataFrame(temp_data).to_csv(output_csv, mode='a', header=False, index=False, encoding='utf-8-sig')
        print(f"Batch {i//5 + 1} 완료: {len(temp_data)}개 데이터 저장")
        if len(temp_data) == 0:
            print("데이터 없음:", chunk)
    else:
        print(f"Batch {i//5 + 1} 실패: {response.text}")
    time.sleep(1)  # API 호출 제한 준수

print("모든 작업이 완료되었습니다.")
