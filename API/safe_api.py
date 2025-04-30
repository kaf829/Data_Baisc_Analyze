import requests
import pandas as pd
import time

# API 엔드포인트 (HTTP 사용하여 SSL 오류 방지)
url = "http://apis.data.go.kr/3450000/safeRestDesigStatService_new/getSafeRestDesigStat_v2"

# 서비스키 (이미지에 표시된 키 - 필요시 본인 키로 교체)
service_key = "blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"

# 결과를 저장할 리스트
all_data = []

# 페이지 번호 및 페이지당 데이터 수
current_page = 1
per_page = 100  # 한 페이지당 100건씩 조회 (최대치 설정)

# 에러 방지를 위한 최대 시도 횟수
max_tries = 3

print("대구 북구 안심식당 데이터 수집을 시작합니다...")

while True:
    retry_count = 0
    success = False

    while not success and retry_count < max_tries:
        try:
            # URL에 서비스키 직접 포함 (인코딩 문제 해결)
            full_url = f"{url}?serviceKey={service_key}&currentPage={current_page}&perPage={per_page}"

            # 요청 및 응답 확인
            print(f"페이지 {current_page} 데이터 요청 중...")
            response = requests.get(full_url, timeout=10)

            # 응답 확인
            print(f"HTTP 상태 코드: {response.status_code}")

            # 응답이 비어있는지 확인
            if not response.text.strip():
                print("비어있는 응답을 받았습니다. 다시 시도합니다.")
                retry_count += 1
                time.sleep(2)
                continue

            # JSON 파싱 시도
            try:
                data = response.json()

                # API 오류 메시지 확인
                result_code = data.get('header', {}).get('resultCode')
                result_msg = data.get('header', {}).get('resultMsg')

                if result_code != "00" or result_msg != "NORMAL SERVICE":
                    print(f"API 오류: {result_msg} (코드: {result_code})")
                    retry_count += 1
                    time.sleep(2)
                    continue

                # 데이터 추출
                items = data.get('body', {}).get('items', {}).get('item', [])

                if not items:
                    print(f"더 이상 데이터가 없습니다. 총 {len(all_data)}건 수집 완료.")
                    break

                # 데이터 수집
                all_data.extend(items)

                print(f"페이지 {current_page}: {len(items)}건 수집 완료 (누적: {len(all_data)}건)")

                # 다음 페이지로
                current_page += 1
                success = True

                # 수집된 데이터가 요청한 개수보다 적으면 마지막 페이지
                if len(items) < per_page:
                    break

            except ValueError as e:
                print(f"JSON 파싱 오류: {e}")
                print(f"응답 내용 일부: {response.text[:200]}")
                retry_count += 1
                time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"요청 오류: {e}")
            retry_count += 1
            time.sleep(2)

    # 성공 또는 최대 시도 횟수 초과 시 루프 종료
    if not success or (items and len(items) < per_page):
        break

# 데이터가 수집되었으면 DataFrame으로 변환하여 CSV 저장
if all_data:
    try:
        df = pd.DataFrame(all_data)
        csv_filename = "대구북구_안심식당_현황.csv"
        df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
        print(f"\n수집 완료! CSV 파일 저장 완료: {csv_filename}")
        print(f"총 {len(df)}건의 데이터가 저장되었습니다.")

        # 수집된 데이터 상위 5개 항목 미리보기
        print("\n데이터 미리보기:")
        print(df.head(5))

    except Exception as e:
        print(f"CSV 저장 중 오류 발생: {e}")
else:
    print("\n수집된 데이터가 없습니다.")
    print("서비스키와 API 주소를 확인하고 다시 시도하세요.")
