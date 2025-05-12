import requests
from bs4 import BeautifulSoup
import pandas as pd


def bugs_rank(date = "20250511"):
    result = []
    url = f'https://music.bugs.co.kr/chart/track/day/total?chartdate={date}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    # print(tbody)
    if not tbody:
        print(f"해당일에 tbody를 찾지 못함")

    for tr in tbody.find_all('tr'):

        rank_t = tr.find('div', class_='ranking')
        title_t = tr.find('p', class_='title')
        artist_t = tr.find('p', class_='artist')

        rank = rank_t.find('strong').text.strip() if rank_t.find('strong') else ''
        title = title_t.find('a').text.strip() if title_t.find('a') else ''
        artist = artist_t.find('a').text.strip() if artist_t.find('a') else ''

        # print(date, rank, title, artist)
        result.append([date, rank, title, artist])

    return result


if __name__ == "__main__":
    date = input("순위 검색할 날짜를 8자리 입력하세요(ex: 20060922~20250511)")
    bugs_rank = bugs_rank(date)

    columns = ['날짜','순위', '곡제목', '아티스트']
    bugs_df = pd.DataFrame(bugs_rank, columns=columns)
    csv_name= f"bugs_chart_{date}.csv"
    bugs_df.to_csv(csv_name, encoding='utf8', mode= 'w', index = False)



