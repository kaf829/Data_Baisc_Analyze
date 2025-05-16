import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt

# 1. CSV 파일 불러오기
df = pd.read_csv("cctv_grouped_ranked.csv")

# 2. 분석 대상 위치 정의
target_locations = {
    "신매동 10-37": (35.837456, 128.695321),
    "신매동 170-5": (35.839872, 128.698754),
    "신매동 234-11": (35.841210, 128.700567),
    "신매동 233-1": (35.840789, 128.699432)
}

# 3. 반경 100~150m 내 CCTV 유동인구 합산
results_100_150m = []

for name, coord in target_locations.items():
    # 거리 계산
    df['distance'] = df.apply(lambda row: geodesic(coord, (row['lat'], row['lon'])).meters, axis=1)
    # 100m 초과 ~ 150m 이하 필터링
    nearby = df[(df['distance'] > 100) & (df['distance'] <= 150)]
    # 유동인구 합계 계산
    total_flow = nearby['cctvCount'].sum()
    # 결과 저장
    results_100_150m.append((name, coord, total_flow))

# 4. 결과 정리
plot_df = pd.DataFrame(results_100_150m, columns=['주소', '위도,경도', '유동인구합계_100~150m'])
plot_df = plot_df.sort_values(by='유동인구합계_100~150m')


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


# 5. 시각화: 수평 막대 그래프
plt.figure(figsize=(10, 6))
plt.barh(plot_df['주소'], plot_df['유동인구합계_100~150m'])
plt.xlabel('유동인구 합계 (100~150m)')
plt.title('신매동 주요 지점별 유동인구 (100~150m 반경)')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
