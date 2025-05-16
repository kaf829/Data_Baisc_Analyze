import pandas as pd

import matplotlib.pyplot as plt


# 1. CSV 파일 불러오기
file_path = "cctv_grouped.csv"  # 파일 경로를 필요에 맞게 수정하세요
df = pd.read_csv(file_path)

# 2. cctvCount 기준으로 내림차순 정렬 및 순위 매기기
df_sorted = df.sort_values(by='cctvCount', ascending=False).reset_index(drop=True)
df_sorted['rank'] = df_sorted.index + 1  # 순위 1부터 시작

# 3. 정렬된 결과에서 필요한 컬럼만 선택
df_ranked = df_sorted[['rank', 'cctvUid', 'cctvNm', 'cctvCount', 'lat', 'lon']]

# 4. 결과 확인 또는 저장
print(df_ranked.head(10))  # 상위 10개 출력
df_ranked.to_csv("cctv_grouped_ranked.csv", index=False)  # 새 파일로 저장




# 상위 10개만 추출
top10 = df_ranked.head(10)


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지
# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.barh(top10['cctvNm'], top10['cctvCount'])
plt.gca().invert_yaxis()
plt.xlabel('유동인구 카운트')
plt.title('유동인구가 많은 지역 TOP 10')
plt.tight_layout()
plt.show()

