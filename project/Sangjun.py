import requests
import pandas as pd


url = (
    "https://api.odcloud.kr/api/15050942/v1/uddi:e551c0e3-6f2f-4ef6-83c9-a5ab144d8ef4"
    "?page=1&perPage=1000&serviceKey=blQn7CpDK9qt6ZR%2B%2FlEbAt5Yb%2F0gE4k0zZpvonWxX0XWZv6MuS5TwFy%2BzmkDk0ZvFunmtNIN5sFnLqIlJWabrg%3D%3D"
)

response = requests.get(url)
print("Status Code:", response.status_code)


data = response.json()

rows = data.get("data", [])

df = pd.DataFrame(rows)

df.to_csv("bus_stop_info_1000.csv", index=False, encoding="utf-8")


