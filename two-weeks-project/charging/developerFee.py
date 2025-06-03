import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 시스템에 기본 포함된 한글 가능한 폰트
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 깨짐 방지

# 기능 유형별 최소~최대 점수 범위 정의 (IFPUG 기준)
fp_score_range = {
    "입력(EI)": (3, 6),
    "출력(EO)": (4, 7),
    "조회(EQ)": (3, 6),
    "내부 논리 파일(ILF)": (7, 15),
    "외부 인터페이스 파일(EIF)": (5, 10)
}

# 데이터 분리
labels = list(fp_score_range.keys())
min_scores = [v[0] for v in fp_score_range.values()]
max_scores = [v[1] for v in fp_score_range.values()]

# 막대그래프
plt.figure(figsize=(10, 6))
plt.bar(labels, max_scores, color='lightgray', label='최대 점수')
plt.bar(labels, min_scores, color='steelblue', label='최소 점수')

# 텍스트 표시
for i in range(len(labels)):
    plt.text(i, min_scores[i]+0.3, f"{min_scores[i]}", ha='center', color='white', fontweight='bold')
    plt.text(i, max_scores[i]-1, f"{max_scores[i]}", ha='center', color='black')

plt.title("기능 유형별 최소~최대 기능점수 (IFPUG 기준)", fontsize=14)
plt.ylabel("점수 (FP)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
