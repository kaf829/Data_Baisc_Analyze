import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import os

# 📁 결과 저장 폴더 생성
os.makedirs("graphs", exist_ok=True)

# 📌 데이터 불러오기 및 날짜 분해
df = pd.read_csv("weather_all_data_cleaned.csv", encoding='euc-kr')
df['일시'] = pd.to_datetime(df['일시'])
df['연'] = df['일시'].dt.year
df['월'] = df['일시'].dt.month
df['일'] = df['일시'].dt.day

# 📌 지점 및 예측 연도 지정
station_name = '서울'
target_year = 2023

# 📌 제외 컬럼 정의
excluded_cols = ['평균 상대습도(%)', '평균 이슬점온도(°C)', '평균 해면기압(hPa)', '지점', '지점명', '일시', '연', '월', '일']
target_cols = [col for col in df.columns if col not in excluded_cols]

# 📌 해당 지점 필터링
df_station = df[df['지점명'] == station_name]

# 📌 학습용, 테스트용 분리
train_df = df_station[df_station['연'] != target_year]
test_df = df_station[df_station['연'] == target_year]

# 📌 반복하여 예측 및 그래프 저장
for target_col in target_cols:
    train_temp = train_df.dropna(subset=[target_col])
    test_temp = test_df.dropna(subset=[target_col])

    if len(test_temp) == 0:
        continue

    X_train = train_temp[['연', '월', '일']]
    y_train = train_temp[target_col]

    X_test = test_temp[['연', '월', '일']]
    y_test = test_temp[target_col]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # 그래프 저장
    plt.figure(figsize=(14, 5))
    plt.plot(test_temp['일시'], y_test.values, label='실제값', linewidth=2)
    plt.plot(test_temp['일시'], y_pred, label='예측값', linewidth=2, linestyle='--')
    plt.title(f"{station_name} - {target_year}년 [{target_col}] 실제 vs 예측")
    plt.xlabel("날짜")
    plt.ylabel(target_col)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"graphs/{station_name}_{target_col}_2023.png")
    plt.close()

