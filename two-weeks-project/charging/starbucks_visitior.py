import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 폰트 설정 (맑은 고딕이 없는 경우 경고 발생 가능)
mpl.rcParams['font.family'] = 'Malgun Gothic'
mpl.rcParams['axes.unicode_minus'] = False

# 매출 데이터 (단위: 억 원)
sales_by_year = {
    2020: 19248,
    2021: 23856,
    2022: 25939,
    2023: 29292,
    2024: 31001
}

# 기준값: 2021년 매출 대비 방문객 수
base_year = 2021
base_sales = sales_by_year[base_year]
base_visitors = 800000  # 하루 방문객 수

# 각 연도의 방문객 수 추정 (매출 비례 기준)
estimated_visitors = {
    year: (sales / base_sales) * base_visitors
    for year, sales in sales_by_year.items()
}

# 연도와 방문객 수 리스트로 변환
years = list(estimated_visitors.keys())
visitors = list(estimated_visitors.values())

# 숫자 포맷 함수 (만 단위)
def format_number(num):
    return f"{int(num / 10000):,}만 명"

# 초록색 계열 컬러맵
colors = plt.cm.Greens(np.linspace(0.5, 1, len(years)))

# 그래프 그리기
plt.figure(figsize=(10, 6))
for i in range(len(years) - 1):
    plt.plot(years[i:i+2], visitors[i:i+2], color=colors[i], linewidth=3)
plt.scatter(years, visitors, color=colors, s=100, zorder=5)

# 방문객 수 라벨
for year, visitor, color in zip(years, visitors, colors):
    plt.text(year, visitor + 10000, format_number(visitor), ha='center', fontsize=10, color='green')

# 기준선 및 텍스트 (그래프 내부에 박스 표시)
plt.axhline(y=800000, color='gray', linestyle='--', linewidth=1)
plt.text(2022.2, 815000, "2021년 기준: 하루 80만 명", va='bottom', ha='left',
         fontsize=10, color='black', bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.3'))

# 축과 제목 설정
plt.title("스타벅스 연도별 추정 하루 방문객 수", fontsize=16)
plt.xlabel("연도", fontsize=12)
plt.ylabel("하루 방문객 수 (명)", fontsize=12)
plt.grid(True)
plt.xticks(years)
plt.tight_layout()
plt.show()
