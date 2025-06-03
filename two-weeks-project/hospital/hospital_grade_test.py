import requests

# 공통 설정
ykiho = " "
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": f"https://www.hira.or.kr/ra/hosp/hospInfoAjax.do?ykiho={ykiho}",
    "Origin": "https://www.hira.or.kr"
}
data = {
    "ykiho": ykiho
}

# 1. care level 정보 추출
care_url = "https://www.hira.or.kr/ra/hosp/hospCareLevelAjax.do"
care_resp = requests.post(care_url, headers=headers, data=data)
care_grades = []

try:
    care_json = care_resp.json()
    careGrd06 = care_json['data']['grade'].get('careGrd06')
    careGrd05 = care_json['data']['grade'].get('careGrd05')
    care_grades.append([careGrd06, careGrd05])
    print("careGrd06 / careGrd05:", careGrd06, careGrd05)
except Exception as e:
    print("Care grade 데이터 파싱 실패:", e)

# 2. 장비 정보 중 oftCntD201 추출
equip_url = "https://www.hira.or.kr/ra/hosp/hospEquipmentAjax.do"
equip_resp = requests.post(equip_url, headers=headers, data=data)

try:
    equip_json = equip_resp.json()
    incubator = equip_json['data']['equipment'].get('oftCntD201')
    ultrasonic_cnt = equip_json['data']['equipment'].get('oftCntB302')

    print("인큐베이터 수:", incubator)
    print("초음파기계 수",ultrasonic_cnt)
except Exception as e:
    print("oftCntD201 데이터 파싱 실패:", e)
