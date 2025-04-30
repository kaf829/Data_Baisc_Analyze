import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytrends.request import TrendReq

# 크롬 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 화면을 띄우지 않음
driver = webdriver.Chrome(options=options)

# 네이버 플레이스 검색 URL
search_url = "https://map.naver.com/v5/search/대구%20맛집"
driver.get(search_url)
time.sleep(5)

# 페이지를 계속 스크롤하여 여러 음식점 정보 확보
for _ in range(3):  # 스크롤 횟수 조정
    driver.execute_script("window.scrollBy(0, 1000);")  # 1000px만큼 스크롤
    time.sleep(2)

# 음식점 이름과 업종 추출
places = driver.find_elements(By.CLASS_NAME, 'place_bluelink')
restaurants = [place.text for place in places]
driver.quit()

# 음식점 데이터프레임화
df = pd.DataFrame(restaurants, columns=['음식점'])

# 중복 제거 (음식점 이름 기준)
df_unique = df.drop_duplicates(subset=['음식점'])

# 메뉴 빈도수 분석
menu_counts = df['음식점'].value_counts()

# 구글 트렌드 요청
pytrends = TrendReq(hl='ko', tz=540)
kw_list = ["고기싸롱", "출근길생고기", "찬앤찬막창", "초밥뷔페", "막창"]

# 트렌드 데이터를 요청하기 전에 잠시 대기
time.sleep(5)

# 키워드에 대한 트렌드 요청
pytrends.build_payload(kw_list, geo='KR', timeframe='today 3-m')

# 요청에 대한 응답을 받아오는 부분
try:
    trend_data = pytrends.interest_over_time()
    print(trend_data)
except Exception as e:
    print(f"Error: {e}")
    print("잠시 대기 후 재시도...")
    time.sleep(60)  # 60초 기다린 후 재시도
    trend_data = pytrends.interest_over_time()

# 트렌드 데이터 시각화
trend_data.plot(kind='line', title='구글 트렌드: 인기 음식점/메뉴')
plt.xlabel('날짜')
plt.ylabel('검색량')
plt.show()

# 인기 음식점/메뉴 상위 5개 출력
# print("\n[인기 음식점/메뉴 Top 5]")
# print(menu_counts.head(5))
#
# # 평점 및 리뷰 수 기준으로 인기 음식점 추출 (예시로 평점 > 4.7 및 리뷰 100개 이상)
# example_data = {
#     '음식점': ['고기싸롱', '고기싸롱', '출근길생고기', '찬앤찬막창', '고기싸롱'],
#     '평점': [4.7, 4.8, 4.5, 4.6, 4.9],
#     '리뷰수': [150, 200, 50, 80, 120]
# }
# df_ratings = pd.DataFrame(example_data)
#
# # 평점 > 4.7 및 리뷰수 100 이상 추출
# top_rated = df_ratings[(df_ratings['평점'] >= 4.7) & (df_ratings['리뷰수'] >= 100)]
# print("\n[평점 & 리뷰수 기준 인기 음식점]")
# print(top_rated)
#
# # 인기 음식점 및 메뉴 시각화
# menu_counts.plot(kind='bar', title='트렌드한 음식점 빈도수', color='skyblue')
# plt.xlabel('음식점')
# plt.ylabel('빈도수')
# plt.show()
