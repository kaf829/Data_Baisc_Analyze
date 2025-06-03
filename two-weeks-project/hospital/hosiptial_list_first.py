from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
# 크롬 드라이버 설정
options = webdriver.ChromeOptions()

driver = webdriver.Chrome()

# 접속할 URL
url = "https://www.hira.or.kr/ra/hosp/hospInfoAjax.do?ykiho=JDQ4MTYyMiM4MSMkMSMkMCMkODkkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNzEjJDEjJDgjJDgz"
driver.get(url)


# 페이지가 로딩될 때까지 대기
time.sleep(2)

# XPath로 요소 추출
try:
    # XPath로 특정 li 태그의 텍스트 추출
    xpath = "/html/body/div/form/div[2]/div/div[2]/div[1]/div[2]/div[1]/table[5]/tbody/tr[3]/td/ul/li[10]"
    element = driver.find_element(By.XPATH, xpath)
    text_data = element.text
    print("1번 추출된 텍스트:", text_data)
    numbers = re.findall(r'\((\d+)\)', text_data)
    numbers = [int(n) for n in numbers]
    print(numbers)
    result_list = [numbers]
    print("리스트:", result_list)
except Exception as e:
    print("에러 발생:", e)

# 종료
driver.quit()
