import pandas as pd

file1 = "./모델_학습결과_1.csv"
file2 = "./모델_학습결과2.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

df2 = df2[df1.columns]

merged_df = pd.concat([df1, df2], ignore_index=True)

merged_path = "./모델_학습결과3.csv"
merged_df.to_csv(merged_path, index=False)

