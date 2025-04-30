from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://map.naver.com/p/search/한식")  # 예시: '한식' 카테고리

time.sleep(2)  # 페이지 로딩 대기

# iframe 전환 (네이버 지도/플레이스는 상세정보가 iframe에 있음)
driver.switch_to.frame('entryIframe')

# 메뉴명 추출 (class 이름은 실제 페이지 구조에 맞게 확인 필요)
menu_elements = driver.find_elements(By.CLASS_NAME, 'menu_name')  # 예시 클래스명

menu_names = [el.text for el in menu_elements if el.text]

print(menu_names)
driver.quit()
