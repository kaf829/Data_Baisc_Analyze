import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def hollys_store():
    result = []
    for page in range(1, 52):
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            tbody = soup.find('tbody')
            if not tbody:
                print(f"[경고] page {page}에서 tbody를 찾지 못함")
                continue

            for store in tbody.find_all('tr'):
                print(store)
                tds = store.find_all('td')
                if len(tds) < 6:
                    continue

                store_name = tds[1].text.strip()
                store_sido = tds[0].text.strip()
                store_gugun = tds[2].text.strip()
                store_address = tds[3].text.strip()
                store_phone = tds[5].text.strip()

                result.append([store_name, store_sido, store_gugun, store_address, store_phone])

        except Exception as e:
            print(f"[에러] page {page}: {e}")
            continue
    return result

# 실행
hollys_result = hollys_store()

# 데이터프레임으로 변환
columns = ['매장명', '시도', '구군', '주소', '전화번호']
hollys_df = pd.DataFrame(hollys_result, columns=columns)
hollys_df.to_csv('hollys.csv', encoding='utf8', mode= 'w', index = False)

# 결과 출력
print(hollys_df)
