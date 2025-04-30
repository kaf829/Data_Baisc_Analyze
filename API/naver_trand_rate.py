import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('korea_naver_trand.csv')

# 음식별 검색트렌드 표준편차 계산
std_df = df.groupby('food_name')['ratio'].std().reset_index()
std_df = std_df.rename(columns={'ratio': 'std_ratio'})

# 표준편차 기준 오름차순 정렬 후 상위 30개 추출
std_df = std_df.sort_values(by='std_ratio', ascending=True).head(30)

# 순위 컬럼 추가
std_df['rank'] = range(1, len(std_df) + 1)

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 색상 지정
custom_colors = ['#55676E', '#2CA3D0']
bar_colors = [custom_colors[i % 2] for i in range(len(std_df))]

# 그래프 그리기
plt.figure(figsize=(12, 10))
ax = sns.barplot(x='std_ratio', y='food_name', data=std_df, palette=bar_colors)
plt.title('한식 메뉴별 검색트렌드 표준편차 (낮은 순)', fontsize=16)
plt.xlabel('검색트렌드 표준편차')
plt.ylabel('음식명')
# 그리드: 세로선만 표시
ax.xaxis.grid(True)   # 세로선 표시
ax.yaxis.grid(False)  # 가로선 제거
# 막대에 순위 표시
for i, (value, name) in enumerate(zip(std_df['std_ratio'], std_df['food_name'])):
    ax.text(value + 0.05, i, f'{std_df["rank"].iloc[i]}위', va='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()
