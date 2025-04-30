import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정 (윈도우 기준)


# 데이터 불러오기
df = pd.read_csv('combine_trend.csv')
sns.set_style('whitegrid')
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# 카테고리 추출 (MENU_CODE에서 대분류 추출)
df['CATEGORY'] = df['MENU_CODE'].apply(lambda x: x.split('_')[0])

# 메뉴별, 카테고리별 평균 언급수 계산
grouped = df.groupby(['CATEGORY', 'MENU_NM'])['NTT_PER_AVRG_MENTN_CNT'].mean().reset_index()

# 컬러 리스트
custom_colors = ['#55676E', '#2CA3D0']

# 카테고리별 Top30 메뉴 추출 및 시각화
for cat in grouped['CATEGORY'].unique():
    top30 = grouped[grouped['CATEGORY'] == cat].sort_values('NTT_PER_AVRG_MENTN_CNT', ascending=False).head(30)

    plt.figure(figsize=(10, 8))
    # 색상을 메뉴 개수만큼 반복
    colors = [custom_colors[i % 2] for i in range(len(top30))]
    sns.barplot(
        data=top30,
        y='MENU_NM',
        x='NTT_PER_AVRG_MENTN_CNT',
        palette=colors
    )
    plt.title(f'{cat} 카테고리별 언급 많은 메뉴 Top30')
    plt.xlabel('게시물당 평균 언급수')
    plt.ylabel('메뉴명')
    plt.tight_layout()
    plt.show()
