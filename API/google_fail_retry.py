import pandas as pd
from pytrends.request import TrendReq
import time
import os
from tenacity import retry, stop_after_attempt, wait_exponential

retry_food_list = [
    '간장게장', '돼지고기 구이', '탕', '제육볶음', '참치찌개',
    '해산물요리', '김치찌개', '국', '두루치기', '회', '불고기'
]

output_csv = "food_google_trends_retry.csv"
file_exists = os.path.exists(output_csv)

pytrends = TrendReq(hl='ko', tz=540)

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=5, min=5, max=60))
def fetch_trends(chunk):
    pytrends.build_payload(chunk, timeframe='2024-01-01 2024-12-31', geo='KR')
    return pytrends.interest_over_time()

all_data = []

for i in range(0, len(retry_food_list), 5):
    chunk = retry_food_list[i:i + 5]
    try:
        data = fetch_trends(chunk)
        if not data.empty:
            df_chunk = data.drop(columns=['isPartial'])
            df_chunk = df_chunk.reset_index().melt(id_vars='date', var_name='food_name', value_name='trend')
            all_data.append(df_chunk)
            print(f"{chunk} 데이터 저장 완료")
        else:
            # 검색량이 0인 경우
            dates = pd.date_range('2024-01-01', '2024-04-30', freq='MS')
            df_chunk = pd.DataFrame([
                {'date': date, 'food_name': food, 'trend': 0}
                for food in chunk
                for date in dates
            ])
            all_data.append(df_chunk)
            print(f"{chunk} 데이터 없음(0으로 저장)")
    except Exception as e:
        print(f"{chunk} 처리 실패: {str(e)}")
    time.sleep(30)  # API 요청 간격

# 결과를 CSV에 저장
if all_data:
    result_df = pd.concat(all_data, ignore_index=True)
    result_df.to_csv(output_csv, mode='w', header=True, index=False, encoding='utf-8-sig')

print("데이터 저장 다 함!")
