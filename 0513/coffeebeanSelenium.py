from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()

    for i in range(406, 400, -1):  # 406부터 401까지
        wd.get(CoffeeBean_URL)
        time.sleep(1)

        try:
            print("i:", i)
            wd.execute_script(f"storePop2({i})")
            time.sleep(1)

            html = wd.page_source
            soupCB = BeautifulSoup(html, "html.parser")

            # 매장명
            store_name_tag = soupCB.select("div.store_txt > h2")
            store_name = store_name_tag[0].text.strip() if store_name_tag else "정보 없음"

            # 주소 및 전화번호
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address = store_info[2].text.strip() if len(store_info) > 2 else "주소 없음"
            store_phone = store_info[3].text.strip() if len(store_info) > 3 else "전화번호 없음"

            print("store_name:", store_name)
            print("store_address:", store_address)
            print("store_phone:", store_phone)

            # 결과 저장
            result.append([store_name, store_address, store_phone])

        except Exception as e:
            print(f"{i} 에러 발생:", e)
            continue

    wd.quit()

def main():
    result = []
    CoffeeBean_store(result)

    # DataFrame으로 저장
    columns = ['store', 'address', 'phone']
    coffee_df = pd.DataFrame(result, columns=columns)

    # CSV 저장
    coffee_df.to_csv("coffeeBean.csv", encoding='utf-8-sig', mode='w', index=False)

main()
