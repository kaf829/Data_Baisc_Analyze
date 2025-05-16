import pandas as pd
import folium
from folium.plugins import MarkerCluster
import re
import webbrowser

# CSV 불러오기
df = pd.read_csv("land_sale_data_full.csv")

# 평수 계산 함수
def convert_size_to_pyeong_safe(size_str):
    try:
        number_str = re.findall(r'\d+(?:\.\d+)?', str(size_str).replace(',', ''))[0]
        sqm = float(number_str)
        return round(sqm / 3.3, 2)
    except:
        return None

# 가격 변환 함수
def convert_price_to_won_safe(price_str):
    try:
        cleaned = str(price_str).replace('억', '').replace(',', '').replace(' ', '')
        return float(cleaned) * 100000000
    except:
        return None

# 도로 키워드
# road_keywords = ['대로', '도로', '접한', '도로변', '대료변', '코너', '사거리']

# 변환 적용
df['size_pyeong'] = df['size'].apply(convert_size_to_pyeong_safe)
df['price_won'] = df['price'].apply(convert_price_to_won_safe)
df['price_per_pyeong'] = df['price_won'] / df['size_pyeong']

# 위도/경도 숫자형 변환
df[['lat', 'lon']] = df[['lat', 'lon']].apply(pd.to_numeric, errors='coerce')

# 유효한 데이터만 추출
map_df = df[['address', 'lat', 'lon', 'price_per_pyeong']].dropna()
map_df = map_df.groupby(['address', 'lat', 'lon'])['price_per_pyeong'].mean().reset_index()

# 지도 생성 (대구 중심)
m = folium.Map(location=[35.8714, 128.6014], zoom_start=12)
marker_cluster = MarkerCluster().add_to(m)

# 마커 추가
for idx, row in map_df.iterrows():
    folium.CircleMarker(
        location=(row['lat'], row['lon']),
        radius=7,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=(f"<b>주소:</b> {row['address']}<br>"
               f"<b>평당 가격:</b> {int(row['price_per_pyeong']):,}원")
    ).add_to(marker_cluster)

# HTML로 저장도 가능
m.save("parking_site_price_map.html")

webbrowser.open("parking_site_price_map.html")
# 지도 표시

