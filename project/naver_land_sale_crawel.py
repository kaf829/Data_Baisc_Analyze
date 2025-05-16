from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
#y가 경도 x가 위도
def CoffeeBean_store(result):
    CoffeeBean_URL = f"https://new.land.naver.com/offices?ms=35.840321,128.705216,16&a=TJ&b=A1&e=RETAIL"
    wd = webdriver.Chrome()

    for i in range(7):  # 406부터 401까지
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        html = wd.page_source
        soupCB = BeautifulSoup(html, "html.parser")

        price_data = soupCB.select("a.item_link > div.price_line > span.price")
        land_type_data = soupCB.select("a.item_link >div.info_area >p.line > strong.type")  # 부동산 유형
        size_data = soupCB.select("a.item_link >div.info_area >p.line > span.spec")  # 땅 크기
        land_info_data = soupCB.select("a.item_link>div.info_area > p.line> span.spec")  # 땅 정보

        try:
            print("i:", i)
            price = price_data[i].text.strip() if price_data[i] else "정보 없음" # 가격
            land_type = land_type_data[i].text.strip() if land_type_data[i] else "부동산 유형 없음"
            size = size_data[i].text.strip() if size_data[i] else "부동산 유형 없음"
            land_info = land_info_data[i].text.strip() if land_info_data[i] else '땅 정보 없음'

            print("가격:", price)
            print("부동산 유형:", land_type)
            print("땅 크기:", size)
            print("땅 정보:", land_info)

            # 결과 저장
            result.append([i, price, land_type, size, land_info])

        except Exception as e:
            print(f"{i} 에러 발생:", e)
            continue

    wd.quit()

def main():
    result = []
    CoffeeBean_store(result)

    # DataFrame으로 저장
    columns = ['no', 'price', 'land_type', 'size', 'land_info']
    land_sale_data = pd.DataFrame(result, columns=columns)

    # CSV 저장
    land_sale_data.to_csv("land_sale_data.csv", encoding='utf-8', mode='w', index=False)

main()
