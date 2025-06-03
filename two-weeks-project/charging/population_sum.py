import requests

def population_calc(group_ids):
    url = "https://data.ulsan.go.kr/bigdata/dataAnalysis/searchData.do"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Cookie": (
            "JSESSIONID=865C87402251C96D7BDE7A3E27ED107C; "
            "storyCmsLogVerification-SID_000001=data.ulsan.go.kr|155.230.84.146|20250520; "
            "JSESSIONID=HzLuXU9yy0DBrk1Ou8fUzSbLW1dVSymiWyCiB01OVPoqJMkilEyNem1Io5gyNhS6.UFVTR...; "  # 생략된 부분 채우기
            "_ga=GA1.1.1240760778.1747703595; "
            "_ga_6SMVZHXXRT=GS2.1.1747784484.84.1.1747784487.0.0.0"
        )
    }


    payload = {
        "tab": "유동인구",
        "year": "2025",
        "month": "03",
        "otherGugun": 1100000000,
        "otherGugunText": "서울특별시",
        "dong": None,
        "dongText": None,
        "endDay": "31",
        "endMonth": "05",
        "endYear": "2024",
        "groupIds": group_ids,
        "gugun": 31000,
        "gugunText": "울산시 전체",
        "road": None,
        "roadText": None,
        "startDay": "01",
        "startMonth": "05",
        "startYear": "2024"
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        data = response.json()
        teenager = sum(float(item.get("m10", 0)) for item in data)
        twenties = sum(float(item.get("m20", 0)) for item in data)
        thirties = sum(float(item.get("m30", 0)) for item in data)
        forties = sum(float(item.get("m40", 0)) for item in data)
        fifties = sum(float(item.get("m50", 0)) for item in data)
        sixties = sum(float(item.get("m60", 0)) for item in data)
        seventies = sum(float(item.get("m70", 0)) for item in data)
        total = sum(float(item.get("totalCnt", 0)) for item in data)

        print("데이터 출력:", data)

        print("10대:", teenager)
        print("20대:", twenties)
        print("30대:", thirties)
        print("40대:", forties)
        print("50대:", fifties)
        print("60대:", sixties)
        print("70대:", seventies)

        print("총 유동인구:", total)
    except Exception:
        print("응답 본문:", response.text)


def generate_neighbors(center):
    # 중심 좌표 분리 (예: "5205_3270" → x=5205, y=3270)
    x, y = map(int, center.split("_"))

    neighbors = []
    # -1, 0, 1 만큼 좌우/상하 이동해서 총 9개 좌표 생성
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            neighbors.append(f"{x + dx}_{y + dy}")

    return neighbors


if __name__ == "__main__":
    center_coord = "5204_3270" # 여기에 기준점 수정하면 됨
    group_ids = generate_neighbors(center_coord)
    population_calc(group_ids)

