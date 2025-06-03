import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# 한글 및 마이너스 깨짐 방지 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 대체 폰트 사용
matplotlib.rcParams['axes.unicode_minus'] = False

# CSV 불러오기
df = pd.read_csv("gallup_csv/smartphone_usage_trend_2012_2021.csv")

# 날짜 컬럼을 datetime으로 변환하고 정렬
df["년월"] = pd.to_datetime(df["년월"])
df = df.sort_values("년월")

# 그래프 그리기
plt.figure(figsize=(14, 6))
sns.lineplot(x="년월", y="전체", data=df, label="전체", marker="o")
sns.lineplot(x="년월", y="남성", data=df, label="남성", marker="s")
sns.lineplot(x="년월", y="여성", data=df, label="여성", marker="^")
plt.title("스마트폰 사용률 그래프 (전체 / 남성 / 여성)")
plt.xlabel("조사 년도")
plt.ylabel("스마트폰 사용률 (%)")
plt.ylim(0, 105)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
