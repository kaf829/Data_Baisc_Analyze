import pandas as pd

# 파일 경로
file_path = '../food.csv'

# CSV 파일을 euc-kr 인코딩으로 읽기
df = pd.read_csv(file_path, encoding='euc-kr')

# 식품명만 추출
food_names = df[['식품명']]

# 결과를 CSV로 저장
output_file = 'food.csv'
food_names.to_csv(output_file, index=False, encoding='utf-8')
