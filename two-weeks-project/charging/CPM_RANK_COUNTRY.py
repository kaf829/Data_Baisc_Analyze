import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 및 마이너스 깨짐 방지 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 데이터 수동 구성
data = {
    '국가': ['아랍에미리트','오스트리아','호주','방글라데시','벨기에','불가리아','브라질','캐나다','스위스','체코',
             '독일','덴마크','이집트','스페인','핀란드','프랑스','영국','그리스','홍콩','크로아티아',
             '헝가리','인도네시아','아일랜드','이스라엘','인도','이탈리아','일본','대한민국','스리랑카','멕시코',
             '말레이시아','네덜란드','노르웨이','네팔','뉴질랜드','필리핀','파키스탄','폴란드','포르투갈','루마니아',
             '세르비아','사우디 아라비아','스웨덴','싱가포르','태국','터키','대만','미국','베트남','남아프리카'],
    'CPM 중간값(EUR)': [2.603,4.25,7.667,0.444,5.6,1.5,1.143,5.713,6.889,2.75,
                    5.526,6.381,0.455,2.692,4.095,3.903,6.526,2,2.846,1.667,
                    1.8,0.744,3.688,2.5,0.826,3.087,2.929,2.5,0.545,1.412,
                    1.125,5.535,7.027,0.5,5.769,1.048,0.357,2.524,2.385,1.667,
                    1.095,1.875,5.414,3.108,1.045,0.75,1.786,10.263,0.7,1.455]
}

df = pd.DataFrame(data)

# 유로 → 원화 환산 (가정 환율 1유로 = 1,450원)
df["CPM 중간값(₩)"] = df["CPM 중간값(EUR)"] * 1369.30

# 상위 10개국 시각화
top10 = df.sort_values("CPM 중간값(₩)", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top10["국가"], top10["CPM 중간값(₩)"], color='skyblue')
plt.title("국가별 CPM 중간값 상위 10개국 (₩ 기준)")
plt.ylabel("CPM 중간값 (₩)")
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



# 상위 10개국 + 한국 포함
top10_plus_korea = df.sort_values("CPM 중간값(₩)", ascending=False).head(10)
korea_row = df[df["국가"] == "대한민국"]
japan_row = df[df['국가'] == "일본"]
china_row = df[df["국가"] == "중국"]

# 한국이 이미 포함되어 있지 않다면 추가
if korea_row.index[0] not in top10_plus_korea.index:
    top10_plus_korea = pd.concat([top10_plus_korea, korea_row, japan_row, china_row])

# 시각화
plt.figure(figsize=(12, 6))
plt.bar(top10_plus_korea["국가"], top10_plus_korea["CPM 중간값(₩)"], color='green')
plt.title("국가별 CPM 중간값 (₩ 기준) - 상위 10개국 + 대한민국")
plt.ylabel("CPM 중간값 (₩)")
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
print(korea_row)
