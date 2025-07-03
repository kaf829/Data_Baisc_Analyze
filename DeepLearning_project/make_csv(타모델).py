import re
import pandas as pd


file_path = "타모델.txt"

with open(file_path, "r", encoding="utf-8") as file:
    log_text = file.read()

pattern = (
    r"Training (\w+): look_back=(\d+), units=(\d+), batch=(\d+), epochs=(\d+), "
    r"dropout=([\d.]+), opt=([\w]+), layers=(\d+).*?MAE: ([\d.]+)"
)

matches = re.findall(pattern, log_text, re.DOTALL)


columns = ['model', 'look_back', 'units', 'batch_size', 'epochs', 'dropout', 'optimizer', 'layers', 'MAE']
df = pd.DataFrame(matches, columns=columns)


df[['look_back', 'units', 'batch_size', 'epochs', 'layers']] = df[['look_back', 'units', 'batch_size', 'epochs', 'layers']].astype(int)
df[['dropout', 'MAE']] = df[['dropout', 'MAE']].astype(float)


output_path = "모델_학습결과_1.csv"
df.to_csv(output_path, index=False)

print(f"✅ 저장 완료 → {output_path}")
