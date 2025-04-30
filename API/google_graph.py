import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
file_path = 'combined_unique_food_google_trends.csv'
df = pd.read_csv(file_path)

# 음식별 평균 트렌드 점수 계산
mean_trend = df.groupby('food_name')['trend'].mean().reset_index()

# 평균 트렌드 점수를 기준으로 내림차순 정렬
mean_trend_sorted = mean_trend.sort_values(by='trend', ascending=False)

# 상위 30개 음식 추출
top30 = mean_trend_sorted.head(30)

# 색상 설정
custom_colors = ['#55676E', '#2CA3D0']
bar_colors = [custom_colors[i % 2] for i in range(len(top30))]  # 여기 수정

# 한글 폰트 설정 (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 그래프 그리기
plt.figure(figsize=(12, 10))
sns.barplot(data=top30, x='trend', y='food_name', palette=bar_colors)  # 여기 수정
plt.grid(axis='y', visible=False)  # 가로선(grid) 끄기
plt.grid(axis='x', visible=True)
plt.title('음식별 상대적 관심도 Top 30')
plt.xlabel('평균 관심도 (트렌드 점수)')
plt.ylabel('음식명')
plt.tight_layout()
plt.show()
