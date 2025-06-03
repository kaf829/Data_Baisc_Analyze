import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# 병원 식별자
# ykiho = "37100017"
ykiho = "JDQ4MTYyMiM4MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": f"https://www.hira.or.kr/ra/hosp/hospInfoAjax.do?ykiho={ykiho}",
    "Origin": "https://www.hira.or.kr"
}
data = {"ykiho": ykiho}

care_resp = requests.post("https://www.hira.or.kr/ra/hosp/hospCareLevelAjax.do", headers=headers, data=data)
care_grades = []
try:
    care_json = care_resp.json()
    careGrd06 = care_json['data']['grade'].get('careGrd06')
    careGrd05 = care_json['data']['grade'].get('careGrd05')
    care_grades.append([careGrd06, careGrd05])
    print("careGrd06 / careGrd05:", careGrd06, careGrd05)
except Exception as e:
    print("Care grade 파싱 오류:", e)

# 장비 정보 요청
equip_resp = requests.post("https://www.hira.or.kr/ra/hosp/hospEquipmentAjax.do", headers=headers, data=data)
try:
    equip_json = equip_resp.json()
    incubator = equip_json['data']['equipment'].get('oftCntD201')
    ultrasonic_cnt = equip_json['data']['equipment'].get('oftCntB302')

    print("인큐베이터 수:", incubator)
    print("초음파기계 수", ultrasonic_cnt)
except Exception as e:
    print("기계 데이터 파싱 오류:", e)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
try:
    url = f"https://www.hira.or.kr/ra/hosp/hospInfoAjax.do?ykiho={ykiho}"
    driver.get(url)
    time.sleep(2)

    ul_xpath = "/html/body/div/form/div[2]/div/div[2]/div[1]/div[2]/div[1]/table[5]/tbody/tr[3]/td/ul"
    li_elements = driver.find_elements(By.XPATH, f"{ul_xpath}/li")

    #산부인과 전공의 위치가 항상 같지가 않았음
    sanbu_number = None
    for li in li_elements:
        text = li.text
        if "산부인과" in text:
            print(text)
            match = re.search(r'\((\d+)\)', text)
            if match:
                sanbu_number = int(match.group(1))
            break

    print("산부인과 전공의 수:", sanbu_number)

    xpath_new_baby = '//*[@id="c"]/div/div[2]/div[1]/div[2]/div[1]/table[4]/tbody/tr/td[1]'
    new_baby_element = driver.find_element(By.XPATH, xpath_new_baby)
    extra_text = new_baby_element.text.strip()
    print("신생아실 수:", extra_text)


except Exception as e:
    print("전공의, 신생아실 크롤링 오류:", e)

finally:
    driver.quit()
