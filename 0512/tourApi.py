import datetime
import json
import urllib.request
import pandas as pd

# 공공데이터포털 서비스키
ServiceKey = "blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"

def getRequestUrl(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("연결 성공:", datetime.datetime.now(), url)
            return response.read().decode('utf-8')
    except Exception as e:
        print("에러 발생:", e)
        print("실패:", datetime.datetime.now(), url)
        return None

def getTourismStatesItem(yyymm, national_code, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&YM=" + yyymm
    parameters += "&NAT_CD=" + national_code
    parameters += "&ED_CD=" + ed_cd
    url = service_url + parameters
    print("요청 URL:", url)

    responseDecode = getRequestUrl(url)
    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)

def getTourismStatesServices(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []
    natName = ''
    dataEND = '{0}{1:0>2}'.format(str(nEndYear), str(12))
    isDataEnd = False
    ed = ''

    for year in range(nStartYear, nEndYear + 1):
        for month in range(1, 13):
            if isDataEnd:
                break

            yyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getTourismStatesItem(yyymm, nat_cd, ed_cd)

            if jsonData is None:
                continue

            if jsonData['response']['header']['resultMsg'] == 'OK':
                items = jsonData['response']['body']['items']
                if 'item' not in items:
                    isDataEnd = True
                    #if(month-1) ==0:
                    #    year = year-1
                      #  month = 13
                    print(f"📭 데이터 없음: {year}년 {month}월, 국가 코드: {nat_cd}, ed_cd: {ed_cd}")
                    print(f"데이터 없음: {year}년 {month}월")
                    break

                item = items['item']
                natName = item["natKorNm"].replace(" ", "")
                num = item["num"]
                ed = item["ed"]

                print(f"{natName} {yyymm} {num}")
                print("-" * 70)

                jsonResult.append({'nat_name': natName, 'nat_cd': nat_cd, 'yyymm': yyymm, 'visit_cnt': num})
                result.append([natName, nat_cd, yyymm, num])

    return jsonResult, result, natName, ed, dataEND

def main():
    print("국내 입국한 외국인의 통계 데이터를 수집합니다.")
    nat_cd = input("국가 코드를 입력하세요 (중국: 112 / 일본: 130 / 미국: 275): ").strip()
    if not nat_cd.isdigit():
        print("❗ 국가 코드는 숫자만 입력하세요.")
        return

    try:
        nStartYear = int(input("데이터 수집 시작 연도 (예: 2020): "))
        nEndYear = int(input("데이터 수집 종료 연도 (예: 2024): "))
    except ValueError:
        print("❗ 연도는 숫자만 입력해야 합니다.")
        return

    ed_cd = "E"  # 외래 관광객 기준
    jsonResult, result, natName, ed, dataEND = getTourismStatesServices(nat_cd, ed_cd, nStartYear, nEndYear)

    if natName == "":
        print("⛔ 데이터가 전달되지 않았습니다. 공공포털 API 확인 바랍니다.")
    else:
        filename = f"{natName}_{ed}_{nStartYear}_{dataEND}"

        # JSON 저장
        with open(f"./{filename}.json", 'w', encoding='utf-8') as outfile:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(jsonFile)

        # CSV 저장
        columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
        result_df = pd.DataFrame(result, columns=columns)
        result_df.to_csv(f"./{filename}.csv", index=False, encoding='utf-8-sig')  # 한글 깨짐 방지

        print(f"\n✅ 저장 완료: {filename}.json, {filename}.csv")

if __name__ == "__main__":
    main()
