from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# 크롬 드라이버 실행
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 창 안 띄우는 옵션 (디버깅 시 제거해도 됨)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# 페이지 열기
url = "https://www.coffeebeankorea.com/store/store.asp"
driver.get(url)
time.sleep(2)

# "서울" 클릭 (storeLocal2('서울') 호출하는 a 태그 클릭)
seoul_button = driver.find_element(By.XPATH, "//a[contains(text(), '서울')]")
seoul_button.click()
time.sleep(2)  # JavaScript 로 매장 리스트가 채워질 시간 기다림

# 매장 리스트 수집
stores = driver.find_elements(By.CSS_SELECTOR, "#storeListUL > li")

result = []
for store in stores:
    name = store.get_attribute("data-name")
    addr = store.get_attribute("data-addr")
    tel = store.get_attribute("data-tel")
    lat = store.get_attribute("data-lat")
    lng = store.get_attribute("data-lng")
    result.append([name, addr, tel, lat, lng])

# 종료
driver.quit()

# 데이터프레임으로 보기
df = pd.DataFrame(result, columns=["매장명", "주소", "전화번호", "위도", "경도"])
print(df)
