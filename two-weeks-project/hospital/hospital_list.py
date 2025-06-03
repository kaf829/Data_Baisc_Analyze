import requests

url = "https://www.hira.or.kr/ra/dtlCndHospSrch/dtlCndHospSrchAjax.do"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://www.hira.or.kr/ra/dtlCndHospSrch/dtlCndHospSrch.do?pgmid=HIRA050200000000&WT.tgbn=...%EA%B4%91%EC%95%99%EB%8F%84",  # 실제 referer 복사
    "Origin": "https://www.hira.or.kr",
    "Cookie": (
        "WHATAP=z6lqpvqyaoiao3; "
        "SCOUTER=x4p3di2apeg1tu; "
        "SESSION=MDRlZjY4Mzk1YjA1MS000OTVlLWExZDEtNTVmN2Q0NDIwYjNh; "
        "JSESSIONID=B2D247D10AB45DB1A1F03CE575630E05; "
        "WT_FPC=id=206b4ff48976778240b1747370168042; "
        "ss=1747552644337; "
        "ss2=1747551726069"
    )
}

data = {
    "ykiho": "",
    "isDown": "N",
    "pageIndex": "1",
    "clCd": "01",
    "hospSbjCd": "10",
    "srchCd": "",
    "oftFmtNomCd": "",
    "etcSrchCd": "",
    "sidoCd": "210000",
    "sgguCd": "",
    "clCds": "상급종합병원",
    "gubun": "6315",
    "gubun2": "on",
    "yadmNm": ""
}

response = requests.post(url, headers=headers, data=data)

# 결과 출력
print("Status Code:", response.status_code)
try:
    print(response.json())
except Exception as e:
    print("JSON 파싱 실패:", e)
    print(response.text[:1000])
