from bs4 import BeautifulSoup  # HTML 파싱을 위한 라이브러리
import pandas as pd  # 데이터프레임을 사용하기 위한 라이브러리
from selenium import webdriver  # 브라우저 자동화 도구
import time  # 대기 시간 설정용 모듈


# 각 위치별 매물 정보 수집 함수 정의
def land_sale_data(result, x, y, idx, address):
    land_URL = f"https://new.land.naver.com/offices?ms={x},{y},16&a=TJ&b=A1&e=RETAIL"

    wd = webdriver.Chrome()  # Chrome 브라우저 실행
    wd.get(land_URL)  # 해당 URL 접속
    time.sleep(2)  # 로딩 대기 (최소 2초 권장)

    html = wd.page_source  # 페이지 전체 HTML 소스 추출
    soupCB = BeautifulSoup(html, "html.parser")  # BeautifulSoup을 이용한 파싱

    # ▼ 매물에서 추출할 요소들
    price_data = soupCB.select("a.item_link > div.price_line > span.price")  # 가격
    land_type_data = soupCB.select("a.item_link > div.info_area > p.line > strong.type")  # 부동산 유형
    size_data = soupCB.select("a.item_link > div.info_area > p.line > span.spec")  # 면적
    land_info_data = soupCB.select("a.item_link > div.info_area > p.line > span.spec")  # 상세정보

    # ▼ 각 매물에 대해 반복 처리
    for i in range(len(price_data)):
        try:
            price = price_data[i].text.strip() if price_data[i] else "정보 없음"  # 가격 정보
            land_type = land_type_data[i].text.strip() if i < len(land_type_data) else "부동산 유형 없음"
            size = size_data[i].text.strip() if i < len(size_data) else "크기 정보 없음"
            land_info = land_info_data[i].text.strip() if i < len(land_info_data) else '땅 정보 없음'

            # 수집된 매물 정보 저장
            result.append([idx, address, price, land_type, size, land_info, x, y])

        except Exception as e:
            print(f"{idx}-{i} 에러 발생:", e)  # 개별 매물 오류 출력
            continue

    wd.quit()  # 크롬 드라이버 종료


# 불법주정차 주소 목록 엑셀 파일 불러오기
df = pd.read_excel("./crackdown_parking.xlsx")  # 주소, 위도, 경도 포함

# 전체 결과 저장용 리스트 초기화
result = []

# ▼ 각 행에 대해 반복하며 매물 크롤링
for idx, row in df.iterrows():
    address = row['주소']  # 주소 추출
    x = row['위도']  # 위도 추출
    y = row['경도']  # 경도 추출
    land_sale_data(result, x, y, idx, address)  # 매물 정보 수집 수행

#수집 결과를 데이터프레임으로 변환
columns = ['no', 'address', 'price', 'land_type', 'size', 'land_info', 'lat', 'lon']
land_sale_df = pd.DataFrame(result, columns=columns)

#CSV 파일로 저장
land_sale_df.to_csv("./land_sale_data.csv", encoding='utf-8', index=False)
