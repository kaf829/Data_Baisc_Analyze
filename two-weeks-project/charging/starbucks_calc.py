import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# ▶ 한글 폰트 및 마이너스 깨짐 방지 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# ▶ 광고 단가 설정 (1뷰당 CPI 기준)
cpi = 3.625  # 원


# ▶ 시청자 수 시나리오 (1천명, 1만명, 10만명)
viewer_counts = [2000000, 4000000, 6000000, 8000000, 10000000, 1]

# ▶ 계산 결과 저장용 리스트
results = []

for viewers in viewer_counts:
    total_cost = viewers * cpi
    results.append([viewers, float(total_cost)])

# ▶ DataFrame 생성
df = pd.DataFrame(results, columns=["광고 시청자 수", "광고비용 (₩)"])

# ▶ 출력
print(df)

# ▶ CSV 저장
df.to_csv("광고비_노출기준.csv", index=False, encoding="utf-8-sig")

# ▶ 시각화 (그래프)
plt.figure(figsize=(8, 5))
plt.bar(df["광고 시청자 수"].astype(str), df["광고비용 (₩)"], color='green')
plt.title("광고 시청자 수에 따른 광고 선전 수익 계산")
plt.xlabel("광고 시청자 수")
plt.ylabel("광고수익 (₩)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
