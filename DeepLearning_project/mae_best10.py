import pandas as pd


file_path = "./모델_학습결과3.csv"

# CSV 파일 읽기
df = pd.read_csv(file_path)

# 모델별로 MAE가 낮은 상위 10개씩 추출
top10_by_model = df.sort_values(by='MAE').groupby('model').head(10)

# 저장
output_path = "./top10_lowest_mae_by_model.csv"
top10_by_model.to_csv(output_path, index=False)

print(top10_by_model)