import matplotlib.pyplot as plt
import pandas as pd
file_path = "./Cnn_dense_model_result.csv"

# 파일 읽기
df = pd.read_csv(file_path)

# LSTM 모델만 필터링
lstm_df = df[df['model'] == 'CNN']

# MAE 기준 정렬
# 하이퍼파라미터 조합을 문자열로 생성해서 새로운 컬럼으로 추가
lstm_df['config'] = lstm_df.apply(
    lambda row: f"lb={row['look_back']},u={row['units']},b={row['batch_size']},e={row['epochs']},d={row['dropout']},{row['optimizer']},l={row['layers']}",
    axis=1
)


top30_lstm = lstm_df.nsmallest(30, 'MAE')

print(top30_lstm)

# 시각화
plt.figure(figsize=(14, 6))
plt.plot(top30_lstm['config'], top30_lstm['MAE'], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title('CNN 성능 비교 (MAE 기준 상위 30개)')
plt.xlabel('하이퍼파라미터 구성')
plt.ylabel('MAE')
plt.grid(True)
plt.tight_layout()
plt.show()
