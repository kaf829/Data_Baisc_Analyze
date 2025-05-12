import urllib.request
import json
import datetime

# 인코딩된 상태 그대로 사용
ServiceKey = "blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"


def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("연결 성공:", datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(" 요청 실패:", e)
        print("시간:", datetime.datetime.now())
        print("URL:", url)
        return None


def getForeignTouristStats(ym, nat_cd, sex_cd, age_cd, tra_purp_cd, port_cd):
    base_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getForeignTuristStatsList"
    params = f"?_type=json&serviceKey={ServiceKey}"
    params += f"&YM={ym}&NAT_CD={nat_cd}&SEX_CD={sex_cd}&AGE_CD={age_cd}&TRA_PURP_CD={tra_purp_cd}&PORT_CD={port_cd}"

    url = base_url + params
    print(f"요청 URL: {url}")

    response_data = getRequestUrl(url)
    if response_data is None:
        return None

    try:
        return json.loads(response_data)
    except json.JSONDecodeError:
        print("⚠️ JSON 파싱 실패")
        return None


# 테스트 호출
if __name__ == "__main__":
    ym = "200808"
    nat_cd = "112"
    sex_cd = "F"
    age_cd = "20"
    tra_purp_cd = "02"
    port_cd = "KJ"

    result = getForeignTouristStats(ym, nat_cd, sex_cd, age_cd, tra_purp_cd, port_cd)

    if result:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("에러")
