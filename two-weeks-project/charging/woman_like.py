import pandas as pd

# 📥 엑셀 파일 경로
file_path = "품목별_광고관심도.xlsx"
df = pd.read_excel(file_path)

# 🔧 전처리: 공백 제거
df['Unnamed: 0'] = df['Unnamed: 0'].astype(str).str.strip()
df['Unnamed: 1'] = df['Unnamed: 1'].astype(str).str.strip()

# 📌 광고 항목명
ad_categories = df.iloc[0, 3:].values

# 👩‍🦰 여성 연령대 추출 (행 4~8)
female_age_df = df.iloc[4:9].copy()
female_interest = female_age_df.iloc[:, 3:]
female_interest.columns = ad_categories
female_interest.insert(0, '연령대', female_age_df['Unnamed: 1'].values)

# 📊 비율 계산
female_ratio = female_interest.copy()
female_ratio.iloc[:, 1:] = female_ratio.iloc[:, 1:].div(female_ratio.iloc[:, 1:].sum(axis=1), axis=0)

# 🏆 연령대별 광고 TOP5 추출
female_top5 = {}
for index, row in female_ratio.iterrows():
    age_group = row['연령대']
    top5 = row.drop('연령대').sort_values(ascending=False).head(5)
    female_top5[age_group] = [f"{ad} ({row[ad] * 100:.4f}%)" for ad in top5.index]

# 📊 DataFrame 변환
female_top5_df = pd.DataFrame(female_top5).T
female_top5_df.columns = [f'선호{rank+1}' for rank in range(5)]

# 💾 CSV 저장
female_top5_df.to_csv("여성_연령대별_광고_선호_TOP5.csv", encoding='utf-8-sig', index_label='연령대')

print("✅ 여성 연령대별 광고 선호 TOP5가 '여성_연령대별_광고_선호_TOP5.csv' 로 저장되었습니다.")
