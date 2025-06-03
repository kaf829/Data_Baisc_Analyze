import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 및 마이너스 깨짐 방지 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 광고 시청자 수 시나리오
viewer_counts = [100000, 1000000, 10000000]

# 광고 단가 (1뷰당 비용)
cpi = 3.425  # 원

# 전환율 (CVR)
cvr = 0.038  # 3.8%

# 전환 1건당 광고주가 얻는 수익 시나리오
conversion_values = [1000, 3000, 5000, 7000, 10000]

# 결과 저장 리스트
results = []

# 수익 계산 반복
for viewers in viewer_counts:
    total_ad_cost = viewers * cpi  # 총 광고비
    expected_conversions = viewers * cvr  # 예상 전환 수
    for value in conversion_values:
        total_revenue = expected_conversions * value  # 총 수익
        profit = total_revenue - total_ad_cost  # 순이익
        results.append([
            viewers,
            value,
            round(expected_conversions),
            round(total_revenue),
            round(total_ad_cost),
            round(profit),
            "수익 O" if profit > 0 else "손해 X"
        ])

# 데이터프레임 생성
df_bulk_views = pd.DataFrame(results, columns=[
    "광고 시청자 수", "전환가치(₩)", "예상 전환수", "총 수익(₩)", "광고비(₩)", "순이익(₩)", "결과"
])

# 1. 콘솔에 출력
print(df_bulk_views)

# 2. CSV 저장
df_bulk_views.to_csv("광고수익_시뮬레이션.csv", index=False, encoding="utf-8-sig")

# 3. 시각화
pivot_df = df_bulk_views.pivot(index="전환가치(₩)", columns="광고 시청자 수", values="순이익(₩)")

pivot_df.plot(kind='bar', figsize=(12, 6), colormap='viridis')
plt.title("전환가치별 순이익 비교 (광고 시청자 수 기준)")
plt.ylabel("순이익 (₩)")
plt.xlabel("전환가치 (₩)")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


pivot_df.plot(kind='line', marker='o', figsize=(12, 6), logy=True)
plt.title("제품 가격별 매출 변화 그래프")
plt.ylabel("매출 변화 ")
plt.xlabel("제품 가격 (₩)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# '총 수익' 기준 그래프 만들기
pivot_revenue = df_bulk_views.pivot(index="전환가치(₩)", columns="광고 시청자 수", values="총 수익(₩)")

pivot_revenue.plot(kind='line', marker='o', figsize=(12, 6), logy=True)
plt.ylabel("총 수익 (₩)")
plt.xlabel("전환가치 (₩)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
