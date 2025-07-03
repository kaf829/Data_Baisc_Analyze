import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 불러오기
df = pd.read_csv("prophet_result_data.csv")

# 2. MAE 기준 상위 10개 선택
top10 = df.sort_values(by='MAE').head(10).reset_index(drop=True)

print(top10)

# 3. 조합명을 문자열로 생성
top10['param_combo'] = top10.apply(
    lambda row: f"cps:{row['changepoint_prior_scale']}, sps:{row['seasonality_prior_scale']}, {row['seasonality_mode']}, Y:{row['yearly']}, W:{row['weekly']}, D:{row['daily']}",
    axis=1
)
pd.set_option('display.max_colwidth', None)
print(top10['param_combo'].head(5))

# 4. 라인 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(top10['param_combo'], top10['MAE'], marker='o', linestyle='-')
plt.xticks(rotation=45, ha='right')
plt.xlabel('하이퍼파라미터 조합')
plt.ylabel('MAE')
plt.title('Prophet Top 10 조합 (MAE 기준)')
plt.grid(True)
plt.tight_layout()
plt.show()
