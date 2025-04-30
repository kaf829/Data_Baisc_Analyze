import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('korea_naver_trand.csv')

# 음식별 전체 검색지수 합산
total_search = df.groupby('food_name')['ratio'].sum().reset_index()

# 검색지수 기준 내림차순 정렬 후 상위 30개 추출
top30_foods = total_search.sort_values(by='ratio', ascending=False).head(30)

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 커스텀 색상 리스트 생성
custom_colors = ['#55676E', '#2CA3D0']
bar_colors = [custom_colors[i % 2] for i in range(len(top30_foods))]

# Seaborn 스타일 설정 (흰색 배경 + 그리드)
sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(14, 8))
ax = sns.barplot(x='ratio', y='food_name', data=top30_foods, palette=bar_colors)

# 그리드 설정: 세로선만 표시
ax.xaxis.grid(True)   # X축(세로) 그리드 표시
ax.yaxis.grid(False)  # Y축(가로) 그리드 제거

plt.title('Top 30 한식 메뉴 검색량 합계')
plt.xlabel('검색량 합계')
plt.ylabel('음식명')
plt.tight_layout()
plt.show()
