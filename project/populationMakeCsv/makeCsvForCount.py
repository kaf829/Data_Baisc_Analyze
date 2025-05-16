import pandas as pd
import glob
import os

# 1. 파일 경로 설정 및 불러오기
file_pattern = "./bungi*.csv"
file_paths = glob.glob(file_pattern)

# 2. 모든 CSV 파일 읽기
dfs = [pd.read_csv(file) for file in file_paths]

# 3. DataFrame 병합
merged_df = pd.concat(dfs, ignore_index=True)

# 4. cctvCount 컬럼 숫자형 변환 (오류는 NaN 처리)
merged_df['cctvCount'] = pd.to_numeric(merged_df['cctvCount'], errors='coerce')

# 5. 그룹화 후 합계 계산
grouped_df = merged_df.groupby(['cctvUid', 'cctvNm', 'lat', 'lon'], as_index=False)['cctvCount'].sum()

# 6. 결과 저장
output_path = "cctv_grouped.csv"
grouped_df.to_csv(output_path, index=False)

# 7. 결과 출력
# import ace_tools as tools; tools.display_dataframe_to_user(name="Grouped CCTV Data", dataframe=grouped_df)
