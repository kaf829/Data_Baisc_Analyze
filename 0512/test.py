import requests

url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getForeignTuristStatsList'

encoded_service_key = 'IfJN7A3cBBPttYf%2FFcFWC8pNDT3mi3SRSsDJmyAXQAUOlqvkQhP4ggZkHzhacIhEEJzcswWo8fraVeUBAOxQng%3D%3D'

params = {
    'serviceKey': encoded_service_key,  # 디코딩하지 않은 키 사용
    'YM': '201201',
    'NAT_CD': '155',
    'SEX_CD': 'F',
    'AGE_CD': '40',
    'TRA_PURP_CD': '02',
    'PORT_CD': 'IA',
    '_type': 'json'
}

response = requests.get(url, params=params)
print(response.content.decode('utf-8'))
