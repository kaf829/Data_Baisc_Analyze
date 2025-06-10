import requests
from bs4 import BeautifulSoup
import csv
import re

def convert_alt_to_date_refined(alt_text):
    match = re.search(r"(\d{4})년\s*(\d{1,3})월\s*(\d{1,3})일", alt_text)
    if not match:
        return None
    year, month_str, day_str = match.groups()
    year = int(year)
    month = int(month_str[-2:]) if len(month_str) >= 2 else int(month_str)
    day = int(day_str[-2:]) if len(day_str) >= 2 else int(day_str)
    return f"{year:04d}-{month:02d}-{day:02d}"

filename = '제주.csv'
write_header = True
years = range(2015, 2025)

for year in years:
    url = f'https://www.weather.go.kr/w/dust/dust-obs-days.do?type=2&stnId=184&year={year}'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table-col')

    date_list = []
    if table:
        for row in table.find('tbody').find_all('tr'):
            for td in row.find_all('td'):
                img = td.find('img')
                if img and 'alt' in img.attrs:
                    date_str = convert_alt_to_date_refined(img['alt'])
                    if date_str:
                        date_list.append([date_str])

    with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['Date'])
            write_header = False
        writer.writerows(date_list)

    print(f"{year}년 데이터 CSV에 저장 완료: {filename}")
    print(f"총 저장된 날짜 수: {len(date_list)}")
