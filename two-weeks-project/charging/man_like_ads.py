import pandas as pd

# 📥 파일 불러오기
file_path = "품목별_광고관심도.xlsx"
df = pd.read_excel(file_path)

# 🔧 전처리: 공백 제거
df['Unnamed: 0'] = df['Unnamed: 0'].astype(str).str.strip()
df['Unnamed: 1'] = df['Unnamed: 1'].astype(str).str.strip()

# 📌 광고 항목명 추출 (1행)
ad_categories = df.iloc[0, 3:].values

# 👨‍💼 남성 전체 추출 및 비율 계산
male_total = df[(df['Unnamed: 0'] == '성별') & (df['Unnamed: 1'] == '남')]
male_interest = male_total.iloc[:, 3:]
male_interest.columns = ad_categories
male_interest = male_interest.astype(float)
male_ratio = male_interest.div(male_interest.sum(axis=1), axis=0)

# 👩‍🦰 여성 연령대 추출 (행 4~8)
female_age_df = df.iloc[4:9].copy()
female_age_df['Unnamed: 0'] = female_age_df['Unnamed: 0'].astype(str).str.strip()

female_interest = female_age_df.iloc[:, 3:]
female_interest.columns = ad_categories
female_interest.insert(0, '연령대', female_age_df['Unnamed: 1'].values)

female_ratio = female_interest.copy()
female_ratio.iloc[:, 1:] = female_ratio.iloc[:, 1:].div(female_ratio.iloc[:, 1:].sum(axis=1), axis=0)

# 📈 남성 연령대 추산: 여성 분포 × 남성 전체 평균
estimated_male_ratio = female_ratio.copy()
for col in ad_categories:
    estimated_male_ratio[col] = female_ratio[col] * float(male_ratio[col].iloc[0])  # ✅ 수정됨

# 🏆 연령대별 광고 TOP5 추출
estimated_male_top5 = {}
for index, row in estimated_male_ratio.iterrows():
    age_group = row['연령대']
    top5 = row.drop('연령대').sort_values(ascending=False).head(5)
    estimated_male_top5[age_group] = [f"{ad} ({row[ad] * 100:.4f}%)" for ad in top5.index]

# 📊 DataFrame 변환
estimated_male_top5_df = pd.DataFrame(estimated_male_top5).T
estimated_male_top5_df.columns = [f'선호{rank+1}' for rank in range(5)]

# 💾 CSV 저장
estimated_male_top5_df.to_csv("남성_연령대별_광고_선호_TOP5_추정.csv", encoding='utf-8-sig', index_label='연령대')

print("✅ 남성 연령대별 광고 선호 TOP5 (추정치)가 '남성_연령대별_광고_선호_TOP5_추정.csv' 로 저장되었습니다.")
