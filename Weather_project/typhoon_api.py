import requests
import pandas as pd
import time
import json


def get_typhoon_data():
    auth_key = "u2lyb3TXTD6pcm9014w-wQ"
    base_url = "https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getTyphoonList"
    all_typhoons = []

    for year in range(2014, 2025):
        print(f"🔄 {year}년 데이터 수집 중...")
        page_no = 1
        year_typhoons = []

        while True:
            params = {
                "pageNo": page_no,
                "numOfRows": 100,
                "dataType": "JSON",
                "year": year,
                "authKey": auth_key
            }

            try:
                response = requests.get(base_url, params=params)
                print(f"   페이지 {page_no}: 상태 코드 {response.status_code}")

                if response.status_code == 200:
                    data = response.json()

                    # 응답 구조 디버깅
                    print(f"   응답 구조 확인: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}...")

                    # API 응답 구조 확인
                    response_body = data.get("response", {})
                    header = response_body.get("header", {})
                    body = response_body.get("body", {})

                    # 결과 코드 확인
                    result_code = header.get("resultCode", "")
                    result_msg = header.get("resultMsg", "")

                    if result_code != "00":
                        print(f"   ⚠️ API 오류: {result_code} - {result_msg}")
                        break

                    # 총 개수 및 페이지 정보 확인
                    total_count = body.get("totalCount", 0)
                    num_of_rows = body.get("numOfRows", 0)
                    current_page = body.get("pageNo", 1)

                    print(f"   총 개수: {total_count}, 현재 페이지: {current_page}, 페이지당 개수: {num_of_rows}")

                    # 아이템 추출
                    items_container = body.get("items", {})

                    if items_container:
                        # items가 리스트인 경우와 딕셔너리인 경우 모두 처리
                        if isinstance(items_container, list):
                            items = items_container
                        elif isinstance(items_container, dict):
                            items = items_container.get("item", [])
                        else:
                            items = []

                        # 단일 아이템이 딕셔너리로 온 경우 리스트로 변환
                        if isinstance(items, dict):
                            items = [items]

                        if items:
                            for item in items:
                                # 연도 정보 추가
                                item["year"] = year

                                # 필수 필드 기본값 설정
                                typhoon_data = {
                                    "year": year,
                                    "typ_seq": item.get("typ_seq", ""),
                                    "typ_name": item.get("typ_name", ""),
                                    "typ_en": item.get("typ_en", ""),
                                    "tm_st": item.get("tm_st", ""),
                                    "tm_ed": item.get("tm_ed", ""),
                                    "typ_ps": item.get("typ_ps", ""),
                                    "typ_ws": item.get("typ_ws", ""),
                                    "eff": item.get("eff", "")
                                }
                                year_typhoons.append(typhoon_data)

                            print(f"   ✅ {len(items)}개 태풍 데이터 수집")
                        else:
                            print(f"   ℹ️ 이 페이지에 데이터 없음")
                    else:
                        print(f"   ℹ️ items 컨테이너 없음")

                    # 페이징 처리: 더 이상 데이터가 없으면 종료
                    if not items or len(items) < num_of_rows or total_count <= (page_no * num_of_rows):
                        break

                    page_no += 1
                    time.sleep(0.1)  # API 호출 간격 조정

                else:
                    print(f"   ❌ HTTP 오류: {response.status_code}")
                    print(f"   응답 내용: {response.text[:200]}...")
                    break

            except requests.exceptions.RequestException as e:
                print(f"   ❌ 네트워크 오류: {e}")
                break
            except json.JSONDecodeError as e:
                print(f"   ❌ JSON 파싱 오류: {e}")
                print(f"   응답 내용: {response.text[:200]}...")
                break
            except Exception as e:
                print(f"   ❌ 예상치 못한 오류: {e}")
                break

        print(f"📊 {year}년 총 수집된 태풍: {len(year_typhoons)}개")
        all_typhoons.extend(year_typhoons)

        # 년도별 처리 간격
        time.sleep(0.5)

    return all_typhoons


def save_to_csv(typhoons_data):
    """태풍 데이터를 CSV로 저장"""
    if not typhoons_data:
        print("❌ 저장할 데이터가 없습니다.")
        return False

    df = pd.DataFrame(typhoons_data)

    # 컬럼 순서 정리
    columns_order = ['year', 'typ_seq', 'typ_name', 'typ_en', 'tm_st', 'tm_ed', 'typ_ps', 'typ_ws', 'eff']
    df = df[columns_order]

    # 중복 제거 (같은 년도, 태풍번호)
    df = df.drop_duplicates(subset=['year', 'typ_seq'], keep='first')

    # CSV 저장
    filename = "typhoon_2014_2024_improved.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')

    print(f"✅ CSV 저장 완료: {filename}")
    print(f"📈 총 저장된 태풍 수: {len(df)}개")
    print(f"📅 수집 기간: {df['year'].min()}년 ~ {df['year'].max()}년")

    # 연도별 통계
    year_stats = df.groupby('year').size()
    print("\n📊 연도별 태풍 발생 현황:")
    for year, count in year_stats.items():
        print(f"   {year}년: {count}개")

    return True


def main():
    print("🌀 기상청 태풍 데이터 수집 시작")
    print("=" * 50)

    # 데이터 수집
    typhoons = get_typhoon_data()

    print("\n" + "=" * 50)
    print(f"🎯 전체 수집 완료: 총 {len(typhoons)}개 태풍 데이터")

    # CSV 저장
    if typhoons:
        save_to_csv(typhoons)
    else:
        print("❌ 수집된 데이터가 없어 파일을 생성하지 않습니다.")
        print("🔍 가능한 원인:")
        print("   - API 인증키가 유효하지 않음")
        print("   - API 서버 문제")
        print("   - 네트워크 연결 문제")
        print("   - API 응답 구조 변경")


if __name__ == "__main__":
    main()
