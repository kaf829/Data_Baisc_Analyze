import requests
import pandas as pd

url = "https://www.starbucks.co.kr/store/getStore.do"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://www.starbucks.co.kr/store/store_map.do",
    "Origin": "https://www.starbucks.co.kr",
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest"
}

payload = "in_biz_cds=0&in_scodes=0&ins_lat=37.56682&ins_lng=126.97865&search_text=&p_sido_cd=01&p_gugun_cd=0110&in_distance=0&in_biz_cd=&isError=true&iend=100&searchType=C&set_date=&all_store=0&T03=0&T01=0&T27=0&T12=0&T09=0&T30=0&T05=0&T22=0&T21=0&T36=0&T43=0&Z9999=0&T64=0&T66=0&P02=0&P10=0&P50=0&P20=0&P60=0&P30=0&P70=0&P40=0&P80=0&whcroad_yn=0&P90=0&P01=0&new_bool=0&rndCod=T7R629535I"

response = requests.post(url, headers=headers, data=payload)

store_list = []
if response.status_code == 200:
    data = response.json().get("list", [])
    for store in data:
        store_list.append({
            "지점명": store.get("s_name"),
            "도로명주소": store.get("doro_address")
        })

df = pd.DataFrame(store_list)
csv_path = "data1.csv"
df.to_csv(csv_path, index=False, encoding="utf8")

