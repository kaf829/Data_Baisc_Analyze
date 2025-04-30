import pandas as pd

# 두 파일 불러오기
df1 = pd.read_csv('food_google_trends.csv')
df2 = pd.read_csv('food_google_trends_retry.csv')

# 데이터 합치기
combined = pd.concat([df1, df2], ignore_index=True)

# 완전히 동일한 행 중복 제거
combined_unique = combined.drop_duplicates()

# 결과 저장
combined_unique.to_csv('combined_unique_food_google_trends.csv', index=False)
