import pandas as pd
from pytrends.request import TrendReq
import time
import os
from tenacity import retry, stop_after_attempt, wait_exponential

# 저장할 CSV 파일명
output_csv = "food_google_trends.csv"
file_exists = os.path.exists(output_csv)

# food_list 직접 정의
food_list = [
    "돼지고기 구이", "국수", "칼국수", "수제비", "소고기",
    "된장찌개", "청국장", "곱창", "막창", "내장부위",
    "제육볶음", "두루치기", "불고기", "해산물요리", "회",
    "계란찜", "계란말이", "죽", "육회", "고추장찌개",
    "돼지찌개", "전", "빈대떡", "부침개", "비빔밥",
    "물냉면", "돼지갈비", "주물럭", "양념갈비", "새우구이",
    "김치찌개", "참치찌개", "국", "탕", "간장게장",
    "양념게장", "수육", "매운탕", "해물탕", "생선구이",
    "닭갈비", "해장국", "보쌈", "비빔냉면", "설렁탕",
    "곰탕", "정식"
]

# pytrends 초기화
pytrends = TrendReq(hl='ko', tz=540)

# 429 오류 등 발생 시 재시도 로직
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=4, min=4, max=30))
def fetch_trends(chunk):
    pytrends.build_payload(chunk, timeframe='2024-01-01 2024-04-30', geo='KR')
    return pytrends.interest_over_time()

# 5개씩 묶어서 처리
for i in range(0, len(food_list), 5):
    chunk = food_list[i:i + 5]
    try:
        data = fetch_trends(chunk)
        if not data.empty:
            df_chunk = data.drop(columns=['isPartial'])
            df_chunk = df_chunk.reset_index().melt(id_vars='date', var_name='food_name', value_name='trend')
            print(f"{chunk} 데이터 저장 완료")
        else:
            # 검색량이 0인 경우
            dates = pd.date_range('2024-01-01', '2024-12-31', freq='MS')
            df_chunk = pd.DataFrame([
                {'date': date, 'food_name': food, 'trend': 0}
                for food in chunk
                for date in dates
            ])
            print(f"{chunk} 데이터 없음(0으로 저장)")

        # 결과를 CSV에 즉시 저장 (헤더는 최초 1회만)
        df_chunk.to_csv(
            output_csv,
            mode='a',
            header=not file_exists,
            index=False,
            encoding='utf-8-sig'
        )
        if not file_exists:
            file_exists = True

    except Exception as e:
        print(f"{chunk} 처리 실패: {str(e)}")

    time.sleep(60)  # API 요청 간격

print("모든 데이터 저장 완료!")
