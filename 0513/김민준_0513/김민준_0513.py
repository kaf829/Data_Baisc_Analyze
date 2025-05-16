from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()
    wd.get(CoffeeBean_URL)
    time.sleep(1)
    wd.execute_script("storeLocal2('서울')")
    time.sleep(1)
    html = wd.page_source
    soupCB = BeautifulSoup(html, "html.parser")

    for i in range(10):  # 406부터 401까지
        try:
            print("i:", i)

            store_name_tag = soupCB.select("div.store_txt > p.name > span")
            store_name = store_name_tag[i].text.strip() if store_name_tag else "정보 없음"

            store_address_tag = soupCB.select("div.store_txt > p.address > span")
            store_address = store_address_tag[i].text.strip() if store_address_tag else "정보 없음"

            store_phone_tag = soupCB.select("div.store_txt > p.tel > span")
            store_phone = store_phone_tag[i].text.strip() if store_phone_tag else "정보 없음"

            print("store_name:", store_name)
            print("store_address:", store_address)
            print("store_phone:", store_phone)

            result.append([store_name, store_address, store_phone])

        except Exception as e:
            print(f"{i} 에러 발생:", e)
            continue

    wd.quit()

def main():
    result = []
    CoffeeBean_store(result)

    columns = ['store', 'address', 'phone']
    coffee_df = pd.DataFrame(result, columns=columns)
    coffee_df.to_csv("coffeeBean_Newstore.csv", encoding='utf-8-sig', mode='w', index=False)

main()
