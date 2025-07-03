import pandas as pd

file_path = "./auto_data(중간까지).csv"

df = pd.read_csv(file_path)

df.insert(0, 'model', 'LSTM')

output_path = "모델_학습결과2.csv"
df.to_csv(output_path, index=False)

output_path
